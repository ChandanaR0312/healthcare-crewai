from crewai import Task

def create_tasks(analyzer, researcher, recommender, reporter, input_text):

    task1 = Task(
        description=f"""
        Analyze this blood report carefully.

        Extract:
        - Hemoglobin
        - RBC, WBC, Platelets
        - Any abnormal values
        - Medical concerns

        Report:
        {input_text}
        """,
        agent=analyzer
    )

    task2 = Task(
        description="""
        Based on abnormal values, find medical explanations.
        Explain possible diseases, risks, and conditions.
        """,
        agent=researcher
    )

    task3 = Task(
        description="""
        Provide:
        - Diet recommendations
        - Lifestyle changes
        - Preventive health measures
        """,
        agent=recommender
    )

    task4 = Task(
        description="""
        Create final structured report:

        1. Summary
        2. Abnormal Findings
        3. Medical Insights
        4. Recommendations
        5. References
        """,
        agent=reporter
    )

    return [task1, task2, task3, task4]