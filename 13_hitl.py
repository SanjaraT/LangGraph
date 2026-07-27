from typing import TypedDict, Annotated

from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.types import interrupt, Command

load_dotenv()

# LLM
llm = ChatGroq(model="llama-3.3-70b-versatile")

# Tools
@tool
def get_stock_price(symbol: str) -> dict:
    """Return a fake stock price for the given symbol (e.g. 'AAPL')."""
    # Mocked so the demo runs with zero external API keys/calls.
    fake_price = 123.45
    return {"symbol": symbol, "price": fake_price}


@tool
def purchase_stock(symbol: str, quantity: int) -> dict:
    """
    Simulate buying `quantity` shares of `symbol`.
    """
    decision = interrupt(f"Approve buying {quantity} shares of {symbol}? (yes/no)")

    if isinstance(decision, str) and decision.strip().lower() == "yes":
        return {"status": "approved", "symbol": symbol, "quantity": quantity}
    return {"status": "declined", "symbol": symbol, "quantity": quantity}


tools = [get_stock_price, purchase_stock]
llm_with_tools = llm.bind_tools(tools)

# Graph state
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# Nodes
def chat_node(state: ChatState):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}

tool_node = ToolNode(tools)

# Build the graph
memory = MemorySaver()  # in-memory checkpointer, required for interrupt()/resume

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_node("tools", tool_node)

graph.add_edge(START, "chat_node")
graph.add_conditional_edges("chat_node", tools_condition)  # -> "tools" or END
graph.add_edge("tools", "chat_node")

chatbot = graph.compile(checkpointer=memory)

# CLI loop
if __name__ == "__main__":
    thread_id = "demo-thread" 

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in {"exit", "quit","bye"}:
            print("Goodbye!")
            break

        config = {"configurable": {"thread_id": thread_id}}
        result = chatbot.invoke({"messages": [HumanMessage(content=user_input)]}, config=config)

       # If a tool called interrupt(), it shows up here
        interrupts = result.get("__interrupt__", [])
        if interrupts:
            prompt_to_human = interrupts[0].value
            print(f"HITL: {prompt_to_human}")
            decision = input("Your decision (yes/no): ").strip().lower()
 
            if decision == "yes":
                result = chatbot.invoke(Command(resume=decision), config=config)
            else:
                print("Bot: Okay, purchase cancelled.\n")
                continue
 
        print(f"Bot: {result['messages'][-1].content}\n")
 