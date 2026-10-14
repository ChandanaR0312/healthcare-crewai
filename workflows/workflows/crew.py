from crewai import Crew

def run_crew(agents, tasks):

    crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()
    return result