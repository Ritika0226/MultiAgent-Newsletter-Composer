
import os
from dotenv import load_dotenv

from crewai import Agent, LLM
from tools import google_search_tool   # <-- make sure this is here

load_dotenv()

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

# Researcher
researcher = Agent(
    role="Technology Intelligence Specialist & Innovation Scout",
    goal="""
    1. Track emerging breakthroughs in {topic}
    2. Identify patterns and connections between developments
    3. Predict future technological inflection points
    4. Assess real-world impact potential and adoption barriers
    5. Validate findings through multiple authoritative sources
    """,
    backstory="""
    Former quantum computing researcher turned tech intelligence expert.
    Known for spotting emerging technology trends before they become mainstream.
    """,
    verbose=True,
    memory=False,
    llm=llm,
    tools=[google_search_tool],
    allow_delegation=True
)

# Writer
writer = Agent(
    role="Technology Storyteller & Innovation Chronicler",
    goal="""
    Transform complex technological concepts into compelling narratives.
    Bridge the gap between technical complexity and public understanding.
    """,
    backstory="""
    Former quantum physicist turned science communicator with extensive
    experience translating advanced technologies into engaging stories.
    """,
    verbose=True,
    memory=False,
    llm=llm,
    tools=[google_search_tool],
    allow_delegation=True
)

# Proof Reader
proof_reader = Agent(
    role="Principal Proofreader",
    goal="""
    Ensure reports are polished, accurate, and ready for stakeholder review.
    """,
    backstory="""
    Expert editor with strong attention to grammar, structure,
    readability, and factual accuracy.
    """,
    verbose=True,
    memory=False,
    llm=llm,
    tools=[google_search_tool],
    allow_delegation=True
)