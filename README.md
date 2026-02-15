# 🧠 AI Customer Support Assistant (RAG + LangGraph)

An AI-powered customer support assistant that answers user questions from uploaded documents using Retrieval-Augmented Generation (RAG). The system intelligently handles ambiguous queries, asks clarifying questions, and produces document-grounded answers using a LangGraph-based reasoning flow.

An end-to-end AI-powered customer support assistant built using **React**, **FastAPI**, **LangChain**, **LangGraph**, and **local LLMs (Ollama)**.

The system supports **document upload**, **retrieval-augmented generation (RAG)**, **clarification-aware reasoning**, and **multi-document querying**.

---

## ✨ Features

- 📄 **PDF Upload from UI** (Knowledge Ingestion)
- 🔍 **Retrieval-Augmented Generation (RAG)** using Chroma DB
- 🧠 **LangGraph-based control flow**
- ❓ Clarifies ambiguous user queries
- 🚫 Prevents hallucinations
- 🤖 Local LLM support via **Ollama (Mistral)**
- 💬 ChatGPT-style React UI
- 📚 Multi-document support
- ⚡ FastAPI backend with OpenAPI docs

---

## 🏗️ Architecture Overview

### 🔷 High-Level Flow

User (React UI)  
&nbsp;&nbsp;↓  
1. Upload PDF / Ask Question via FastAPI Backend  
&nbsp;&nbsp;├── **/upload** → PDF ingestion & vectorization  
&nbsp;&nbsp;└── **/chat** → LangGraph execution  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
LangGraph Orchestration  
&nbsp;&nbsp;├── Intent / Clarity Check  
&nbsp;&nbsp;├── Clarifying Question (if needed)  
&nbsp;&nbsp;├── RAG Node (Vector Retrieval via ChromaDB)  
&nbsp;&nbsp;└── LLM Reasoning (Mistral via Ollama)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
Final response returned to the UI

---

### 🔷 LangGraph Control Flow

User Question  
&nbsp;&nbsp;↓  
Router Node (Is the question clear?)  
&nbsp;&nbsp;├── ❌ No → Ask Clarifying Question  
&nbsp;&nbsp;└── ✅ Yes  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
Retrieve Relevant Documents (ChromaDB)  
&nbsp;&nbsp;↓  
LLM Reasoning (Mistral via Ollama)  
&nbsp;&nbsp;↓  
Final Answer

---

### ✅ This Ensures

- Ambiguous questions don’t trigger hallucinations
- Answers are grounded in uploaded documents
- Multi-document contexts are handled correctly

---

## 🧠 Retrieval-Augmented Generation (RAG)

- PDFs are split into chunks
- Chunks are embedded using sentence-transformers
- Stored in **Chroma Vector DB**
- Relevant chunks retrieved per query
- LLM answers only using retrieved context

If relevant information is missing, the assistant responds with:

> “I don’t have enough information to answer that.”

---

## 🖥️ Tech Stack

### Frontend

- React (Vite)
- Fetch API
- Chat-style UI (Flexbox)

### Backend

- FastAPI(Python)
- LangChain
- LangGraph
- ChromaDB
- Ollama (Mistral LLM)
- HuggingFace Embeddings

---

## 📸 Screenshots
- Chat UI Screenshot
<img width="1155" height="881" alt="image" src="https://github.com/user-attachments/assets/f9628cb4-174e-4df9-aaa7-7c2b9107eb20" />

- PDF Upload Screenshot
<img width="1154" height="884" alt="image" src="https://github.com/user-attachments/assets/3c2048ed-3525-4efe-80d0-12fab334d403" />

- RAG
<img width="911" height="816" alt="image" src="https://github.com/user-attachments/assets/9c6fdb4b-cda1-41eb-acae-3a8eaa21ee7f" />
<img width="919" height="764" alt="image" src="https://github.com/user-attachments/assets/319b6294-2232-4355-80e9-8f004fb97a3b" />

- Out-of-Scope (Hallucination Test)
<img width="904" height="777" alt="image" src="https://github.com/user-attachments/assets/d91628f3-dd1c-4c55-8b09-44bcde22f083" />
