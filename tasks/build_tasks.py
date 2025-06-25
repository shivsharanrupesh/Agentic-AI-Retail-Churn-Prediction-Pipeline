from crewai import Task

def build_tasks(data_agent, churn_agent, persona_agent, offer_agent, engagement_agent, feedback_agent, file_path):
    """
    Build the CrewAI pipeline tasks, specifying dependencies and outputs.

    Returns:
        list of Task: Task definitions for the CrewAI workflow.
    """
    return [
        Task(
            agent=data_agent,
            name="Aggregate Data",
            description="Collect all customer data into a clean profile set.",
            expected_output="A list of customer profile dictionaries.",
            input_keys=["file_path"],
            output_key="customer_profiles",
            allow_parallel=False,
        ),
        Task(
            agent=churn_agent,
            name="Predict Churn",
            description="Predict churn risk using ML for each profile.",
            expected_output="Profiles labeled with churn_score.",
            input_keys=["customer_profiles"],
            output_key="scored_profiles",
        ),
        Task(
            agent=persona_agent,
            name="Build Personas",
            description="Cluster customers into marketing personas.",
            expected_output="Profiles labeled with persona.",
            input_keys=["scored_profiles"],
            output_key="persona_profiles",
        ),
        Task(
            agent=offer_agent,
            name="Optimize Offers",
            description="Pick the best offer for each persona.",
            expected_output="Profiles labeled with offer.",
            input_keys=["persona_profiles"],
            output_key="offer_profiles",
        ),
        Task(
            agent=engagement_agent,
            name="Engage Customers",
            description="Send personalized message via right channel.",
            expected_output="Profiles with message and channel.",
            input_keys=["offer_profiles"],
            output_key="engaged_profiles",
        ),
        Task(
            agent=feedback_agent,
            name="Feedback Loop",
            description="Track who responded and return final profiles.",
            expected_output="Final annotated customer profiles.",
            input_keys=["engaged_profiles"],
            output_key="final_profiles",
        ),
    ]
