from crewai import Crew, Process
from agents import researcher, writer, proof_reader
from tasks import research_task, write_task, proof_read_task

topic = input("Enter Topic: ")

crew = Crew(
    agents=[researcher, writer, proof_reader],
    tasks=[research_task, write_task, proof_read_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff(
    inputs={"topic": topic}
)

print("\n" + "="*80)
print("FINAL NEWSLETTER")
print("="*80)
print(result)

print("\nNewsletter saved to newsletter.md")