from crewai import Agent

class OfferOptimizationAgent(Agent):
    """
    CrewAI Agent for optimizing retention offers based on churn risk and personas.
    """

    def __init__(self, llm):
        super().__init__(
            name="Offer Optimization Agent",
            description="Selects the best retention offer for each customer persona or risk segment.",
            goal="Increase customer retention with tailored offers.",
            role="Offer engine",
            backstory="Marketing optimizer with deep understanding of customer motivation.",
            verbose=True,
            llm=llm,
            allow_delegation=True,
        )

    def run(self, customer_profiles, **kwargs):
        """
        Assign best offers dynamically based on churn risk or persona labels.

        Args:
            customer_profiles (list): List of customer dictionaries with churn risk and persona.

        Returns:
            list: Customer profiles annotated with an 'offer' field.
        """
        offer_map = {
            "high": "Exclusive Discount",
            "medium": "Special Bundle",
            "low": "Loyalty Rewards"
        }

        for p in customer_profiles:
            churn_score = p.get('churn_score', 0)
            # Categorize churn risk
            if churn_score >= 0.7:
                risk = "high"
            elif churn_score >= 0.4:
                risk = "medium"
            else:
                risk = "low"
            p['churn_risk'] = risk

            # Pick offer based on churn risk; optionally extend using persona
            p["offer"] = offer_map.get(risk, "Standard Offer")

        return customer_profiles
