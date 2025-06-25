import os
from dotenv import load_dotenv
import sys
import json

from agents.data_aggregation_agent import DataAggregationAgent
from agents.churn_prediction_agent import ChurnPredictionAgent
from agents.persona_builder_agent import PersonaBuilderAgent
from agents.offer_optimization_agent import OfferOptimizationAgent
from agents.engagement_agent import EngagementAgent
from agents.feedback_loop_agent import FeedbackLoopAgent

def main():
    load_dotenv()
    if len(sys.argv) != 3:
        print("Usage: python main.py customer_data.csv offers.json")
        sys.exit(1)

    file_path = sys.argv[1]
    offers_path = sys.argv[2]
    llm = "gpt-3.5-turbo"  # or "gpt-4o" if you have access

    with open(offers_path, "r", encoding="utf-8-sig") as f:
        offer_map = json.load(f)

    # Pass only positional arguments to avoid double-value errors
    data_agent = DataAggregationAgent(file_path, llm)
    churn_agent = ChurnPredictionAgent(llm)
    persona_agent = PersonaBuilderAgent(llm, 4)
    offer_agent = OfferOptimizationAgent(offer_map, llm)
    engagement_agent = EngagementAgent(llm)
    feedback_agent = FeedbackLoopAgent(llm)

    from crewai import Crew, Task

    tasks = [
        Task(agent=data_agent, description="Aggregate customer data.", expected_output="Customer profiles"),
        Task(agent=churn_agent, description="Score customers for churn risk.", expected_output="Churn predictions"),
        Task(agent=persona_agent, description="Build customer personas.", expected_output="Persona segments"),
        Task(agent=offer_agent, description="Optimize retention offers.", expected_output="Offer assignments"),
        Task(agent=engagement_agent, description="Engage customers with offers.", expected_output="Engagement results"),
        Task(agent=feedback_agent, description="Collect and use feedback.", expected_output="Feedback insights"),
    ]

    crew = Crew(
        agents=[data_agent, churn_agent, persona_agent, offer_agent, engagement_agent, feedback_agent],
        tasks=tasks,
        verbose=True,
    )

    result = crew.kickoff()
    print("Pipeline result:", result)

if __name__ == "__main__":
    main()
