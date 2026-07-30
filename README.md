# LangGraph

A hands-on collection of notebooks and scripts built while completing a **LangGraph** course , covering everything from basic graph workflows to persistence, tool calling, RAG, human-in-the-loop flows, and subgraphs.

Each file in this repo corresponds to a concept in the course, with commits documenting the progression from simple graphs to more advanced, production-style patterns.

## 📚 What's Inside

| # | File | Concept |
|---|------|---------|
| 1 | `1_bmi_calculator.ipynb` | A simple single-node graph (BMI calculator) |
| 2 | `2_simple_llm_workflow.ipynb` | Wiring an LLM call into a graph node |
| 3 | `3_prompt_chain.ipynb` | Chaining multiple prompts / nodes sequentially |
| 4 | `4_simple_parallel_workflow.ipynb` | Running independent nodes in parallel |
| 5 | `5_llm_parallel_workflow.ipynb` | Parallel workflow with multiple LLM calls |
| 6 | `6_simple_conditional_workflow.ipynb` | Conditional edges / branching logic |
| 7 | `7_llm_conditional_workflow.ipynb` | LLM-driven conditional routing |
| 8 | `8_iterative_workflow.ipynb` | Loops and iterative graph execution |
| 9 | `9_basic_chatbot.ipynb` | A basic conversational chatbot graph |
| 10 | `10_persistence.ipynb` | Checkpointing and persisting graph state |
| 11 | `11_tools.ipynb` | Tool calling / function calling within a graph |
| 12 | `12_RAG.ipynb` | Retrieval-Augmented Generation with LangGraph |
| 13 | `13_hitl.py` | Human-in-the-loop (HITL) interrupts and approvals |
| 14 | `14_subgraph_separate.ipynb` | Composing separate subgraphs |
| 15 | `15_subgraph_shared.ipynb` | Subgraphs with shared state |

## 🛠️ Tech Stack

- Python
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://github.com/langchain-ai/langchain)
- Groq — LLM inference
- Jupyter Notebook

## 📈 Learning Path

The notebooks are numbered to reflect the natural progression of the course:

**Fundamentals** (1–3) → **Parallelism** (4–5) → **Conditional Logic** (6–7) → **Loops & Chatbots** (8–9) → **State & Tools** (10–11) → **RAG** (12) → **Human-in-the-Loop** (13) → **Subgraphs** (14–15)

## 📌 Notes

This repository is a personal learning log from completing a LangGraph course. Each commit corresponds to a specific concept, making the commit history a useful reference for tracking how each pattern was built up incrementally.
