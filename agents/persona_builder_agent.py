# agents/persona_builder_agent.py

from crewai import Agent
from sklearn.cluster import KMeans
import pandas as pd

class PersonaBuilderAgent(Agent):
    """
    CrewAI Agent for clustering customers into personas using KMeans.
    
    This agent segments high-risk customers into actionable personas based on 
    demographics, purchase behavior, and other usage data.
    """
    n_clusters: int  # Declare as a Pydantic field

    def __init__(self, llm, n_clusters):
        """
        Args:
            llm (str): The name of the LLM model to use (e.g., 'gpt-3.5-turbo').
            n_clusters (int): Number of clusters/personas to generate.
        """
        super().__init__(
            name="Persona Builder Agent",
            description="Clusters customers for segmentation.",
            goal="Generate actionable persona clusters.",
            role="Segmentation specialist",
            backstory="Expert at unsupervised learning for retail personas.",
            verbose=True,
            llm=llm,
            allow_delegation=True,
            n_clusters=n_clusters   # Set as pydantic field!
        )

    def run(self, customer_df: pd.DataFrame):
        """
        Cluster customers using KMeans and assign persona labels.
        
        Args:
            customer_df (pd.DataFrame): The DataFrame of customer data.
        
        Returns:
            pd.DataFrame: Input DataFrame with added 'persona' column.
        """
        print(f"[PersonaBuilderAgent] Clustering {len(customer_df)} customers into {self.n_clusters} personas.")

        # Example: Cluster on selected numeric columns (customize as needed)
        # Assume columns: 'age', 'annual_spend', 'visit_count'
        feature_cols = [col for col in ['age', 'annual_spend', 'visit_count'] if col in customer_df.columns]
        if not feature_cols:
            raise ValueError("No valid clustering features found in the data.")

        X = customer_df[feature_cols].copy()
        # Handle missing/non-numeric gracefully
        X = X.apply(pd.to_numeric, errors='coerce').fillna(0)

        kmeans = KMeans(n_clusters=self.n_clusters, n_init=10, random_state=42)
        customer_df['persona'] = kmeans.fit_predict(X)

        print(f"[PersonaBuilderAgent] Assigned personas to customers.")
        return customer_df

    # If using CrewAI's LLM pattern for persona explanation, add methods here

