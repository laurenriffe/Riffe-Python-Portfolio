 ## 📖 Catholic Social Teaching RAG Assistant  
 ## A Domain-Specific Retrieval-Augmented Generation System for Business Ethics and Finance  
   
 ## Project Description  
 This project implements a domain-specific Retrieval-Augmented Generation (RAG) assistant designed to apply Catholic Social Teaching (CST) principles to business and financial questions.  
 The system prioritizes doctrinal accuracy  academic rigor  and transparency by grounding all substantive claims in retrieved source documents rather than model intuition.  
 It was built as a capstone NLP project and intentionally mirrors how CST-based case analysis is conducted in an academic setting.  
   
 ## Domain Overview & Problem Statement  
 ### Domain  
 - Catholic Social Teaching as applied to business ethics  corporate governance  and finance  
 - Focus on labor dignity  solidarity  subsidiarity  shareholder vs. stakeholder theory  executive compensation  and environmental responsibility  
   
 ### Problem  
 - Ethical analysis in business often conflates personal moral intuition with formal CST principles.  
 - CST sources are authoritative but dense  making consistent application difficult and time-intensive.  
 - Generic chatbots tend to produce confident but ungrounded ethical claims.  
   
 ### Solution  
 This assistant streamlines CST-based reasoning by retrieving authoritative course-aligned texts first and then applying CST principles objectively and consistently.  
   
 ## System Architecture & Pipeline Explanation  
 The system follows a standard but intentionally constrained RAG architecture:  
   
 User Question  
 → Streamlit Interface (app.py)  
 → RAG Agent with CST Persona (backend/agent.py)  
 → Semantic Retrieval (Sentence Embeddings)  
 → DuckDB Vector Store (document corpus)  
 → Evidence-Grounded LLM Response  
   
 ### Pipeline Walkthrough  
 - The user submits a question through the Streamlit UI.  
 - app.py handles input/output and passes the query to the backend.  
 - The RAG agent determines how to answer the question and when retrieval is required.  
 - The query is embedded using all-MiniLM-L6-v2 and compared to pre-embedded document vectors stored in DuckDB.  
 - The top-K most relevant passages are retrieved based on similarity scores.  
 - The LLM generates a structured academic response grounded in the retrieved passages.  
 - If insufficient evidence is found  the system explicitly states this rather than speculating.  
   
 ## Document Collection Summary  
 The DuckDB vector database contains a curated set of approximately forty domain-specific documents  including:  
   
 - Papal social encyclicals (e.g.  Rerum Novarum  Quadragesimo Anno  Centesimus Annus  Caritas in Veritate  Laudato Si’)  
 - Scholarly work on corporate governance and business ethics  
 - Course-aligned readings and case studies (e.g.  shareholder primacy  stakeholder theory  labor ethics  hostile takeovers)  
   
 ### Why These Documents  
 - They represent authoritative CST sources and rigorous business scholarship.  
 - They reflect the exact materials used in academic CST-based case analysis.  
 - A bounded corpus ensures transparency  auditability  and reduced hallucination risk.  
   
 ## Agent Configuration & Rationale  
 ### Agent Role  
 - Academic research assistant specializing in Catholic Social Teaching  business ethics  and corporate governance  
   
 ### Agent Goal  
 - Provide accurate  evidence-grounded answers using retrieved passages as primary support.  
 - Translate CST doctrine into clear  structured analysis suitable for academic evaluation.  
   
 ### Agent Backstory  
 - Trained on Church social encyclicals and modern business ethics frameworks.  
 - Designed to synthesize theological principles with real-world business decision-making.  
   
 ### Why This Configuration  
 - A domain-specific persona constrains tone  vocabulary  and reasoning style.  
 - Explicit task rules enforce retrieval-first behavior and citation discipline.  
 - Separating evidence from interpretation mirrors academic ethics methodology.  
 - A no-evidence fallback ensures epistemic humility and responsible AI behavior.  
   
 ## Installation & Setup Instructions  
 ### Prerequisites  
 - Python 3.9+  
 - pip  
   
 ### Local Setup  
 1) Clone the repository:  
    git clone <your-repo-url>  
    cd RIFFE_LPP_RAG  
   
 2) Install dependencies:  
    pip install -r requirements.txt  
   
 3) Run the Streamlit app:  
    streamlit run app.py  
   
 ### Notes  
 - Ensure the DuckDB file is committed and referenced via a valid relative path.  
 - For deployment stability  compute database paths relative to config.py.  
   
 ## Streamlit Deployment  
 The application is deployed on Streamlit Cloud:  
 https://riffe-python-portfolio-xbjappotxgl2ee9wrexfxma.streamlit.app/ 
   
 ## Professional Summary  
 This project demonstrates how thoughtful agent configuration  curated document selection  and retrieval-first design can produce reliable  transparent  and academically grounded AI systems.  
 It highlights that effective RAG systems are not about larger models  but about better sources  stronger guardrails  and domain-aligned design decisions.  
