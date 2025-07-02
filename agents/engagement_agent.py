from crewai import Agent

class EngagementAgent(Agent):
    """
    CrewAI Agent for engaging customers with personalized messages via appropriate channels.
    """

    def __init__(self, llm):
        super().__init__(
            name="Engagement Agent",
            description="Sends personalized messages through appropriate channels based on customer data.",
            goal="Maximize engagement and retention through tailored communication.",
            role="The copywriter who speaks each shopper's language.",
            backstory="Specialist in crafting high-converting messages across channels.",
            verbose=True,
            llm=llm,
            allow_delegation=True,
        )

    def run(self, customer_profiles, **kwargs):
        """
        Generate personalized messages and assign communication channels dynamically.

        Args:
            customer_profiles (list): List of customer dictionaries with offers and risk.

        Returns:
            list: Customer profiles annotated with 'message' and 'channel' fields.
        """
        for p in customer_profiles:
            offer = p.get("offer", "Standard Offer")
            risk = p.get("churn_risk", "low")
            name = p.get("name", "Customer")

            # Compose a personalized message
            message = f"Hi {name}, don't miss out on our {offer} just for you!"

            # Decide communication channel based on risk
            if risk == "high":
                channel = "phone_call"
            elif risk == "medium":
                channel = "email"
            else:
                channel = "sms"

            p["message"] = message
            p["channel"] = channel

        return customer_profiles
