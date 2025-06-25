# agents/offer_optimization_agent.py

from crewai import Agent

class OfferOptimizationAgent(Agent):
    """
    CrewAI Agent for optimizing retention offers based on persona mapping.
    """
    offer_map: dict  # Pydantic field

    def __init__(self, offer_map, llm):
        """
        Args:
            offer_map (dict): Mapping of persona types to offers.
            llm (str): The name of the LLM model to use.
        """
        super().__init__(
            name="Offer Optimization Agent",
            description="Recommends optimal retention offers per customer persona.",
            goal="Increase retention with targeted, data-driven offers.",
            role="Offer engine",
            backstory="Marketing optimizer with a deep understanding of customer motivation.",
            verbose=True,
            llm=llm,
            allow_delegation=True,
            offer_map=offer_map  # Set as Pydantic field!
        )

    def run(self, customer_df):
        """
        Assigns retention offers to customers based on their persona.

        Args:
            customer_df (pd.DataFrame): The DataFrame with a 'persona' column.

        Returns:
            pd.DataFrame: DataFrame with new 'offer' column assigned.
        """
        print(f"[OfferOptimizationAgent] Assigning offers based on persona mapping.")
        if 'persona' not in customer_df.columns:
            raise ValueError("No 'persona' column found in input data.")

        customer_df['offer'] = customer_df['persona'].map(self.offer_map).fillna("DEFAULT_OFFER")
        print(f"[OfferOptimizationAgent] Offers assigned.")
        return customer_df
