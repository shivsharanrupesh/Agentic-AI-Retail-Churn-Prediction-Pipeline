from crewai import Agent
from sklearn.cluster import KMeans
import pandas as pd

class PersonaBuilderAgent(Agent):
    """
    CrewAI Agent for clustering customers into personas using KMeans.
    """

    n_clusters: int  # Pydantic field for number of personas

    def __init__(self, llm, n_clusters):
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

    def run(self, customer_profiles, **kwargs):
        """
        Cluster customers into personas using KMeans.

        Args:
            customer_profiles (list): List of customer dicts with churn_score and other features.

        Returns:
            list: Customer profiles with 'persona' label added.
        """
        # Convert list of dicts to DataFrame
        df = pd.DataFrame(customer_profiles)

        # Select numeric features relevant for clustering dynamically
        feature_cols = [col for col in df.columns if col in ['churn_score', 'visit_freq', 'avg_basket', 'reward_points']]
        if not feature_cols:
            raise ValueError("No valid features found for clustering.")

        X = df[feature_cols].fillna(0)

        kmeans = KMeans(n_clusters=self.n_clusters, n_init=10, random_state=42)
        df['persona'] = kmeans.fit_predict(X)

        # Convert back to list of dicts
        return df.to_dict(orient='records')
