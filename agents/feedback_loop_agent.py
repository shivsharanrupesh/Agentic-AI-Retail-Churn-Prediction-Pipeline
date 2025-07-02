from crewai import Agent

class FeedbackLoopAgent(Agent):
    """
    CrewAI Agent for collecting feedback on engagement and refining customer profiles.
    """

    def __init__(self, llm):
        super().__init__(
            name="Feedback Loop Agent",
            description="Collects engagement feedback and updates customer profiles accordingly.",
            goal="Improve future campaigns by learning from feedback.",
            role="The operations optimizer and feedback analyst.",
            backstory="Connects campaign performance to business impact.",
            verbose=True,
            llm=llm,
            allow_delegation=True,
        )

    def run(self, engaged_profiles, **kwargs):
        """
        Simulate or accept feedback and update customer profiles.

        Args:
            engaged_profiles (list): Customer profiles after engagement step.

        Returns:
            list: Profiles updated with feedback insights.
        """
        for p in engaged_profiles:
            # Simulated feedback; replace with actual input as needed
            if p.get("churn_risk") == "high":
                p["feedback"] = "neutral"
            else:
                p["feedback"] = "positive"

            # Optionally adjust churn risk or retention predictions here based on feedback

        return engaged_profiles
