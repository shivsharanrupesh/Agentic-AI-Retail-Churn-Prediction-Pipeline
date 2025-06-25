# 🛒 Agentic AI Retail Churn Prediction Pipeline

## Overview

This project implements an **Agentic AI pipeline** for retail churn prediction using CrewAI, Large Language Models (LLMs), and modular agents. It simulates a real-world, enterprise-grade scenario where multiple intelligent agents automate data aggregation, churn risk scoring, customer segmentation, offer optimization, and feedback analysis—delivering actionable business outcomes with minimal manual intervention.

---

## Problem Statement

**Retailers face high customer churn rates, impacting revenue and growth.**  
Predicting which customers are likely to churn, understanding their profiles, and proactively engaging them with personalized retention strategies is critical. Traditional approaches are manual, slow, and fail to deliver targeted action.

---
![Workflow Diagram](https://github.com/shivsharanrupesh/Agentic-AI-Retail-Churn-Prediction-Pipeline/blob/main/workflow%20Diagram.png)


## What This Project Does

1. **Aggregates customer data** from various sources.
2. **Scores each customer for churn risk** using ML/AI models.
3. **Segments customers into actionable personas** (e.g., high-risk, moderate, low-risk).
4. **Assigns optimal retention offers** to at-risk segments.
5. **Engages customers** with personalized messaging.
6. **Collects and analyzes feedback** to improve future outreach.

The entire pipeline operates autonomously, with agents passing results and insights to each other—mimicking a real “digital workforce”.

---

## How it Works (High-Level Flow)

1. **Data Orchestrator Agent**: Collects and cleans all customer data.
2. **Churn Analyst Agent**: Labels each customer with a churn risk score.
3. **Segmentation Specialist Agent**: Builds customer personas (segments) based on risk and behavior.
4. **Offer Engine Agent**: Decides which offers to give to which segment.
5. **Copywriter Agent**: Crafts personalized communication for each persona.
6. **Feedback Analyst Agent**: Monitors engagement, gathers feedback, and feeds results back for future improvement.

---

## Script/Module Descriptions

- `main.py`  
  Main entrypoint; orchestrates the pipeline and agents.

- `agents/data_aggregation_agent.py`  
  Aggregates, cleans, and normalizes customer data.

- `agents/churn_risk_agent.py`  
  Applies churn prediction logic or ML models; assigns churn scores.

- `agents/persona_builder_agent.py`  
  Segments customers into actionable personas (e.g., high-risk churners).

- `agents/offer_optimization_agent.py`  
  Matches retention offers to customer segments based on risk.

- `agents/copywriter_agent.py`  
  Crafts personalized communication for targeted engagement.

- `agents/feedback_agent.py`  
  Analyzes the impact of offers and collects feedback for future cycles.

- `customer_data.csv`, `offers.json`  
  Sample customer data and offer definitions.

---

##  Output

*Below is an actual excerpt from the project output:*

# Retail Customer Churn Prediction System

![Pipeline Visualization](https://via.placeholder.com/800x400?text=Retail+Churn+Prediction+Pipeline) 
*Example visualization of the multi-agent workflow*

## Overview

An automated pipeline that processes customer data through specialized AI agents to predict churn risk and optimize retention strategies. The system coordinates six specialized agents that each handle a specific stage of the churn prediction and prevention process.

## Key Features

- **Multi-Agent Architecture**: Coordinated team of specialized AI agents
- **End-to-End Processing**: From raw data to actionable retention strategies
- **Real-Time Analytics**: Continuous monitoring of customer churn signals
- **Personalized Interventions**: Tailored offers based on customer segments

## Pipeline Components

### 1. Data Orchestrator
- **Role**: Data aggregation and normalization
- **Input**: Raw customer data (CSV)
- **Output**: Structured customer profiles
- **Sample Output**:

Customer profiles with complete content


### 2. Business Analyst
- **Role**: Churn risk scoring
- **Method**: Machine learning models
- **Output**: Customer churn risk levels
- **Sample Output**:

Churn scores calculated based on purchase frequency,
spending patterns, and interaction history


### 3. Segmentation Specialist
- **Role**: Customer persona creation
- **Method**: Clustering algorithms
- **Output**: 3-tier customer segments
- **Sample Output**:


### 3. Segmentation Specialist
- **Role**: Customer persona creation
- **Method**: Clustering algorithms
- **Output**: 3-tier customer segments
- **Sample Output**:

High-risk Churners: Infrequent purchasers, low spending

Moderate-risk: Varied purchase frequency

Low-risk: Regular purchasers, high spending


### 4. Offer Engine
- **Role**: Retention offer optimization  
- **Output**: Targeted offers per segment
- **Sample Strategies**:
- Exclusive discounts for high-risk
- Loyalty rewards for low-risk
- Personalized communication for all

### 5. Copywriter
- **Role**: Engagement messaging
- **Output**: Tailored communication templates
- **Sample Output**:

Customized email templates addressing specific
churn risk factors for each segment


### 6. Operations Optimizer
- **Role**: Feedback analysis
- **Output**: Improvement insights
- **Sample Output**:

Campaign performance metrics and optimization suggestions


## Installation & Usage

```bash
# Set up environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run pipeline
python main.py customer_data.csv offers.json

Input Requirements
customer_data.csv:

Required fields: Customer ID, purchase history, interaction logs, feedback

Format: CSV with header row

offers.json:

Structure: JSON array of available offers with parameters

Example:

[
  {
    "offer_id": "discount_10",
    "type": "percentage_discount",
    "value": 10,
    "applicable_segments": ["high_risk"]
  }
]

Output Interpretation
The pipeline produces:

Structured customer profiles with churn scores

Defined customer segments

Recommended retention strategies

Engagement templates

Performance feedback

Final output appears as:

Pipeline result: [Summary of optimized retention strategy]

Troubleshooting
Common issues:

Data format errors: Verify CSV structure and JSON validity

API connectivity: Check network access to OpenAI endpoints

Permission issues: Ensure write access to output directories

License
MIT License - See LICENSE for details.

