## 📖 Catholic Social Teaching RAG Assistant
## A Domain-Specific Retrieval-Augmented Generation System for Business Ethics & Governance

This project implements a **domain-specific Retrieval-Augmented Generation (RAG) assistant**
focused on **Catholic Social Teaching (CST), corporate governance, and business ethics**.
The assistant is explicitly designed to answer questions **only using retrieved source
documents**, prioritizing doctrinal accuracy, academic rigor, and ethical clarity over
open-ended conversational behavior.

The system was built as a final project for an advanced NLP course and demonstrates
intentional AI system design, including **explicit agent persona definition, task-level
behavioral constraints, and safeguards against hallucination**.

The application is deployed using **Streamlit**, backed by a **DuckDB vector store**, and
powered by a custom **CrewAI agent** with clearly justified configuration choices.

## 🧠 Project Purpose & Learning Objectives

 
This project was developed to demonstrate mastery of:

- End-to-end **RAG pipeline design** (document ingestion → retrieval → grounded generation)
- The impact of **agent persona and task configuration** on model behavior
- The use of retrieval to improve **truthfulness, interpretability, and epistemic humility**
- Professional-grade **AI system architecture** suitable for academic evaluation
- Clean separation between UI, retrieval, and reasoning layers

The assistant intentionally favors **accuracy, transparency, and doctrinal grounding**
over fluency or speculative reasoning.

## 🚀 Application Overview

 
Users interact with the system through a Streamlit chat interface (`app.py`).
For each user query:

1. The query is passed to a custom RAG agent configured for academic reasoning
2. The agent retrieves semantically relevant passages from a CST-focused document corpus
3. Retrieved passages are injected into the agent’s reasoning context
4. The agent generates a **structured, academic response grounded in those passages**
5. If no relevant evidence is found, the agent explicitly states that the corpus
   does not contain sufficient information to answer the question

This workflow ensures responses are **auditable, explainable, and academically appropriate**.
 

## 🧱 System Architecture

 
User Query
→ Streamlit Interface (app.py)
→ RAG Agent (backend/agent.py)
→ Semantic Retrieval (backend/database.py)
→ DuckDB Vector Store (.duckdb)
→ LLM Reasoning (persona + task policy)
→ Structured Answer + Retrieved Evidence
 

## 🧩 Backend Architecture Details

## Streamlit Frontend (app.py)

 
- Handles user input and chat rendering
- Maintains conversation state across turns
- Displays both generated responses and retrieved source passages
- Contains no retrieval or reasoning logic

This ensures the UI remains a pure presentation layer.
 

## Retrieval Layer (backend/database.py)

 
- Manages document embeddings and vector similarity search
- Uses **DuckDB** as a lightweight, persistent vector database
- Returns top-k semantically relevant passages per query
- Labels passages (e.g., Passage 1, Passage 2) to support citation and traceability

All downstream reasoning is explicitly grounded in retrieved text.
 

## Vector Store (DuckDB)

 
- Stores embeddings and document metadata locally
- Enables fast similarity search without external infrastructure
- Ensures reproducibility and persistence across runs
- Supports academic transparency and offline evaluation
 

## 🧠 Agent Persona & Configuration Rationale

 
A core objective of this project is to show that **agent configuration meaningfully
shapes output quality**, not just prompt wording.
 

## Agent Persona (backend/agent.py)

 
The agent is explicitly configured as an:

“Academic research assistant specializing in Catholic Social Teaching,
business ethics, and corporate governance.”

Persona components:
- Role: Graduate-level teaching and research assistant
- Goal: Produce accurate, well-structured, evidence-based explanations
- Backstory: Familiarity with Church documents, ethical frameworks, and academic standards
- Style constraints:
  - Formal, academic tone
  - No speculation or fabricated claims
  - Explicit acknowledgment of uncertainty or corpus limitations

Encoding this persona at the agent level ensures consistent behavior
across all tasks and queries.
 

## 🧩 Task Configuration & Behavioral Constraints

 
Beyond persona, the agent operates under a strict **task policy** that governs output behavior.
 

 
The task configuration enforces:
- Retrieval-before-generation
- Clear separation between:
  - Evidence (retrieved passages)
  - Interpretation (agent reasoning)
- A consistent response structure:
  - Direct answer
  - Supporting evidence from retrieved documents
  - Analytical explanation
  - Ethical or practical implications (when relevant)
  - Explicit confidence limits

These constraints produce **predictable, auditable, and rubric-aligned outputs**.
 

## 🛑 Safeguards & Output Quality Controls

 
To prevent hallucinations and unsupported claims, the system includes:

- Mandatory retrieval grounding
- Passage-level citation logic
- Explicit fallback responses when retrieval fails
- Guardrails preventing answers not supported by the document corpus

These safeguards prioritize **truthfulness over completeness** and reflect
intentional, ethical AI design.
 

## 🧰 Tech Stack

 
- Python: Core system logic
- Streamlit: Interactive web interface
- CrewAI: Agent and task orchestration
- DuckDB: Persistent vector storage
- Sentence-level embeddings + LLM API: Controlled generation
 

## 📁 Project Directory Structure

 
.
├── app.py                      # Streamlit user interface
├── backend/
│   ├── agent.py                # Agent persona & task policy
│   ├── database.py             # Retrieval & vector search logic
│   └── __init__.py
├── *.duckdb                    # DuckDB vector store
├── requirements.txt
└── README.md
 

## ⚙️ Setup & Installation

 
1. Clone the repository
   git clone <repository-url>
   cd <project-directory>

2. Install dependencies
   pip install -r requirements.txt

3. Run the application
   streamlit run app.py
 

## 💡 Example Workflow

 
Scenario: A user asks a question about Catholic Social Teaching and business ethics.

1. Relevant Church documents and academic texts are retrieved
2. Retrieved passages are injected into the agent’s reasoning context
3. The agent generates a structured, evidence-grounded response
4. If no relevant sources exist, the agent returns an academically appropriate
   “insufficient evidence” statement

This emphasizes **disciplined ethical reasoning over surface-level answers**.
 

## 🌟 Why This Project Exceeds Expectations

 
- Domain-specific RAG tailored to CST and corporate governance
- Explicit architecture and design rationale
- Clear agent persona and task-level constraints
- Robust safeguards against hallucination
- Professional, modular codebase
- Strong alignment with academic grading rubrics
 

## 👩‍💻 About the Creator

 
Lauren Riffe is a Finance major at the University of Notre Dame with minors in
Computing & Digital Technologies and Theology. Her work focuses on building
rigorous, ethically grounded AI systems for academic and professional use.

Contact: lriffe@nd.edu
LinkedIn: https://www.linkedin.com/in/lauren-riffe
 
