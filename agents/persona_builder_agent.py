from crewai import Agent
from sklearn.cluster import KMeans
import pandas as pd

class PersonaBuilderAgent(Agent):
    """
    CrewAI Agent for clustering customers into personas using KMeans.
    
    This agent segments customers into actionable personas based on
    features like churn risk, demographics, purchase behavior, etc.
    """
    n_clusters: int  # Pydantic field for number of clusters

    def __init__(self, llm, n_clusters=4):
        super().__init__(
            name="Persona Builder Agent",
            description="Clusters customers for segmentation.",
            goal="Generate actionable persona clusters.",
            role="Segmentation specialist",
            backstory="Expert at unsupervised learning for retail personas.",
            verbose=True,
            llm=llm,
            allow_delegation=True,
            n_clusters=n_clusters
        )

    def run(self, customer_profiles):
        """
        Runs KMeans clustering on customer profiles to assign personas.

        Args:
            customer_profiles (list of dict): Customer data with features.

        Returns:
            list of dict: Customer data with added 'persona' field.
        """
        import numpy as np

        # Convert list of dict to DataFrame for clustering
        df = pd.DataFrame(customer_profiles)

        # Select features dynamically: churn_score, visit_freq, avg_basket, reward_points etc.
        # Use only numeric columns and drop missing
        feature_cols = []
        for col in ['churn_score', 'visit_freq', 'avg_basket', 'reward_points']:
            if col in df.columns:
                feature_cols.append(col)

        if not feature_cols:
            raise ValueError("No valid features found for clustering.")

        X = df[feature_cols].apply(pd.to_numeric, errors='coerce').fillna(0)

        kmeans = KMeans(n_clusters=self.n_clusters, n_init=10, random_state=42)
        df['persona'] = kmeans.fit_predict(X)

        # Map numeric personas to string labels optionally
        persona_labels = {i: f"Persona_{i+1}" for i in range(self.n_clusters)}
        df['persona_label'] = df['persona'].map(persona_labels)

        # Convert back to list of dict
        enriched_profiles = df.to_dict(orient='records')
        return enriched_profiles
