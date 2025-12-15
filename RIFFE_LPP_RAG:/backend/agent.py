# =============================================================================
# Agent module for RAG Assistant
# =============================================================================
# This file creates an AI agent that can DECIDE when to search the database.
# Instead of always retrieving passages, the LLM chooses when retrieval helps.
# =============================================================================

from crewai import Agent, Task, Crew, LLM
from crewai.tools import tool
from backend.database import RAGDatabase
# =============================================================================
# Agent Persona + Task Policy (Rubric: persona + configuration + quality)
# =============================================================================

AGENT_PERSONA = """
You are an advanced academic research assistant specializing in Catholic Social Teaching (CST),
business ethics, and corporate governance.

ROLE
- Graduate-level teaching + research assistant for an ethics-in-business course.
- Interpret CST principles and apply them to business/finance cases with conceptual rigor.

GOAL
- Provide accurate, evidence-grounded answers using retrieved passages as primary support.
- Translate complex theology/ethics into clear, structured academic writing suitable for grading.

BACKSTORY
- Trained on Church social encyclicals and modern business ethics frameworks.
- Experienced in synthesizing doctrine (e.g., Rerum Novarum, Quadragesimo Anno, Laudato Si’,
  Centesimus Annus, Caritas in Veritate, Fratelli Tutti) with corporate governance concepts
  (stakeholders, fiduciary duty, short-termism, labor ethics, capital allocation).

STYLE
- Formal, precise, and academically neutral.
- Prefer clarity + structure over verbosity.
- No emojis, no slang, no invented citations.
"""

TASK_POLICY = """
NON-NEGOTIABLE RULES (Quality & Truthfulness)
1) Base domain-specific factual claims on retrieved passages when available.
2) If the retrieved passages are insufficient, explicitly say so and explain what is missing.
3) Never fabricate quotations, Church document references, or source material.
4) Separate evidence from interpretation:
   - Evidence: what the passage(s) say
   - Interpretation: your ethical analysis
5) Use this structure whenever possible:

RESPONSE TEMPLATE
- Direct Answer (2–6 sentences)
- Evidence from Sources (bullets; cite Passage numbers)
- Ethical Analysis (connect CST principles explicitly)
- Practical Implications (for managers/investors/boards)
- Confidence & Limits (1–2 sentences)

CITATION FORMAT
- Cite retrieved content as: [Passage 1], [Passage 2], etc.
- If no passages were used: state “No supporting passages were retrieved.”
"""

FALLBACK_NO_EVIDENCE = (
    "Based on the currently retrieved passages, there is insufficient textual evidence in the "
    "document collection to provide a well-supported answer. "
    "To answer rigorously, I would need additional authoritative material (e.g., relevant CST documents "
    "or course readings) added to the corpus."
)

class RAGAgent:
    def __init__(self, db: RAGDatabase, model_name: str, max_iter: int):
        self.db = db
        self.model_name = model_name
        self.max_iter = max_iter
        self.last_sources = []  # We'll store retrieved passages here for the UI

    def create_tool(self):
        # ---------------------------------------------------------------------
        # The @tool decorator transforms this function into something the
        # LLM can call. The docstring is CRUCIAL—it's what the LLM reads
        # to decide whether and how to use this tool.
        # ---------------------------------------------------------------------
        @tool("Query RAG Database")
        def query_rag_db(query: str) -> str:
            """Search the vector database containing customized texts.
            
            Args:
                query: Search query about topic.
                
            Returns:
                Relevant passages from the database
            """
            try:
                results = self.db.query(query)
                
                if results:
                    # Store sources for UI display
                    self.last_sources.extend(results)
                    
                    # Format passages for the LLM to read
                    passages = []
                    for i, row in enumerate(results, start=1):
                        text = row.get("text", "")
                        source = row.get("source", row.get("metadata", ""))
                        header = f"Passage {i} (source={source}):" if source else f"Passage {i}:"
                        passages.append(f"{header}\n{text}".strip())
                    return "\n\n---\n\n".join(passages)
                
                else:
                    return "No relevant passages found."
                    
            except Exception as e:
                return f"Error querying database: {str(e)}"
        
        return query_rag_db

    # TO DO: Update the ask() function
    def ask(self, question: str) -> dict:
        """
        Ask a question to the agent.
        
        Returns:
            Dictionary with 'answer' and 'sources'.
        """
        # Reset sources for this query
        self.last_sources = []
        
        # TO DO: Create the LLM instance
        llm = LLM(model=self.model_name)

        # TO DO: Call the database tool (e.g. the function above)
        query_tool = self.create_tool()
        

        agent = Agent(
            role="CST & Business Ethics Research Assistant",
            goal=(
                "Provide academically rigorous, evidence-grounded answers about Catholic Social Teaching, "
                "business ethics, and corporate governance using retrieved passages as primary support."
            ),
            backstory=AGENT_PERSONA.strip(),
            tools=[query_tool],
            llm=llm,
            verbose=True,
            allow_delegation=False,
            max_iter=self.max_iter
        )

        
        # TO DO: Create the task
        task = Task(
            description=(
                f"{TASK_POLICY.strip()}\n\n"
                f"USER QUESTION:\n{question}\n\n"
                "INSTRUCTIONS:\n"
                "- Retrieve relevant passages before answering.\n"
                "- Follow the RESPONSE STRUCTURE.\n"
                "- Cite passages explicitly as [Passage N].\n"
                "- If evidence is insufficient, state this clearly.\n"
            ),
            agent=agent,
            expected_output=(
                "A structured academic response with explicit passage citations "
                "and a brief confidence/limits statement."
            )
        )
        # TO DO: Create the Crew and run it
        crew = Crew(agents = [agent],
                    tasks = [task],
                    verbose = True,
                    max_rpm= 20)
        
        result = crew.kickoff()
        if not self.last_sources:
            return {
                "answer": FALLBACK_NO_EVIDENCE,
                "sources": []
            }

        
        # Returns the answer and sources
        return {
            "answer": str(result),
            "sources": self.last_sources.copy()
        }
