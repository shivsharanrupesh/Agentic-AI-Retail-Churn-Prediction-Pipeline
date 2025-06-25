from crewai import Agent
import random

class FeedbackLoopAgent(Agent):
    """
    CrewAI Agent for simulating engagement feedback and learning.
    """
    def __init__(self, llm):
        super().__init__(
            name="Feedback Loop Agent",
            description="Monitors engagement response and signals continuous learning.",
            goal="Make every outreach cycle smarter for the next one.",
            role="The operations optimizer and feedback analyst.",
            backstory="You connect campaign performance to real business impact.",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def run(self, customer_profiles, **kwargs):
        """
        Simulate and assign feedback (response) to each customer.

        Args:
            customer_profiles (list): Profiles with engagement info.

        Returns:
            list: Profiles with response feedback.
        """
        for p in customer_profiles:
            p['responded'] = bool(random.getrandbits(1))
        return customer_profiles
