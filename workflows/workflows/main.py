from agents.analyzer import get_analyzer_agent
from agents.researcher import get_researcher_agent
from agents.recommender import get_recommender_agent
from agents.reporter import get_reporter_agent

from workflows.tasks import create_tasks
from workflows.crew import run_crew

# Sample input (later replace with PDF)
input_text = """
Hemoglobin: 9.5 g/dL (Low)
WBC: 11000 (High)
Platelets: 150000 (Normal)
"""

# Initialize agents
analyzer = get_analyzer_agent()
researcher = get_researcher_agent()
recommender = get_recommender_agent()
reporter = get_reporter_agent()

agents = [analyzer, researcher, recommender, reporter]

# Create tasks
tasks = create_tasks(analyzer, researcher, recommender, reporter, input_text)

# Run CrewAI system
result = run_crew(agents, tasks)

print("\n===== FINAL MEDICAL REPORT =====\n")
print(result)