from crewai import Task
from agents import researcher, writer, proof_reader
from tools import google_search_tool

research_task = Task(
    description="""
    Research the topic: {topic}.

    Identify:
    - Current trends
    - Future opportunities
    - Risks and challenges
    - Real-world applications
    - Industry impact

    Provide fact-based insights from reliable sources.
    """,
    expected_output="""
    Detailed research report with:
    - Key findings
    - Market opportunities
    - Risks
    - Future outlook
    """,
    tools=[google_search_tool],
    agent=researcher
)

write_task = Task(
    description="""
    Using the research report, write a professional newsletter article.

    Requirements:
    - Catchy title
    - Executive summary
    - Latest trends
    - Industry impact
    - Future outlook
    - Conclusion

    Use markdown formatting.
    """,
    expected_output="""
    Professional newsletter article in markdown format.
    """,
    agent=writer,
    context=[research_task]
)

proof_read_task = Task(
    description="""
    Review and improve the newsletter.

    Check:
    - Grammar
    - Readability
    - Structure
    - Factual consistency

    Add:
    - Sources section
    - 3 further reading references

    Return final polished markdown newsletter.
    """,
    expected_output="""
    Final polished newsletter in markdown format.
    """,
    agent=proof_reader,
    context=[research_task, write_task],
    output_file="newsletter.md"
)