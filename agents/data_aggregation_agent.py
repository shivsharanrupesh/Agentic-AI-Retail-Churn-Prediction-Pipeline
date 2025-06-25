from crewai import Agent
import pandas as pd

class DataAggregationAgent(Agent):
    file_path: str  # Declare as Pydantic field

    def __init__(self, file_path, llm):
        super().__init__(
            name="Data Aggregation Agent",
            description="Orchestrates and cleans customer data.",
            goal="Provide structured customer data for downstream agents.",
            role="Data orchestrator",
            backstory="Expert at collecting and normalizing retail customer data.",
            verbose=True,
            llm=llm,
            allow_delegation=True,
            file_path=file_path  # <-- Pass as argument!
        )
        # No need to set self.file_path manually

    def run(self, *args, **kwargs):
        print(f"[DataAggregationAgent] Loading customer data from: {self.file_path}")
        df = pd.read_csv(self.file_path)
        df.dropna(how='all', inplace=True)
        df.fillna('', inplace=True)
        df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
        print(f"[DataAggregationAgent] Loaded {len(df)} customer records.")
        return df
