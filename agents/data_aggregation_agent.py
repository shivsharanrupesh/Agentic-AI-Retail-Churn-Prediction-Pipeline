from crewai import Agent
import pandas as pd

class DataAggregationAgent(Agent):
    """
    CrewAI Agent to aggregate and clean customer data from CSV.
    """

    def __init__(self, llm):
        super().__init__(
            name="Data Aggregation Agent",
            description="Aggregates customer data from source files.",
            goal="Produce a clean customer profile list.",
            role="Data orchestrator",
            backstory="Expert in data ingestion and normalization.",
            verbose=True,
            llm=llm,
            allow_delegation=False
        )

    def run(self, file_path, **kwargs):
        """
        Read CSV file and return list of customer profiles.

        Args:
            file_path (str): Path to input CSV file.

        Returns:
            list: List of dicts with customer data.
        """
        df = pd.read_csv(file_path)
        df = df.fillna(0)  # Basic cleaning, extend as needed
        return df.to_dict(orient='records')
