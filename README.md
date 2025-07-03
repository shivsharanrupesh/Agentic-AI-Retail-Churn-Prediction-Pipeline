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

# AI-Powered Customer Churn Prediction & Retention Pipeline

## Overview
This project is an AI-powered, modular pipeline designed to help retail clients predict customer churn, segment customers into actionable personas, optimize retention offers, engage customers, and use feedback for continuous improvement.

The architecture leverages **Agentic AI** concepts: multiple specialized agents perform focused tasks and collaborate asynchronously within a defined workflow.

## High-Level Workflow
1. **Data Aggregation** - Collect and unify customer data from multiple sources.
2. **Churn Prediction** - Predict customer churn risk using ML models.
3. **Persona Building** - Segment customers into distinct personas.
4. **Offer Optimization** - Recommend retention offers based on risk and persona.
5. **Customer Engagement** - Generate personalized messages and select optimal channels.
6. **Feedback Loop** - Collect and process feedback to refine future actions.

Each step is handled by a dedicated agent class, orchestrated through CrewAI's task pipeline.

## Detailed File Descriptions

### 1. `data_aggregation_agent.py`
- **Purpose**: Collects and unifies customer data from multiple sources (CSV files, databases, APIs).
- **Key Functions**:
  - Reads raw input customer and transaction data.
  - Cleans, normalizes, and formats data into consistent profiles.
  - Outputs a list of customer profile dictionaries.
- **Role**: *Data Orchestrator / Data Aggregator*

### 2. `ml_model.py`
- **Purpose**: Encapsulates the machine learning churn prediction model.
- **Key Details**:
  - Reads customer and transaction data CSVs.
  - Trains a classification model (e.g., `RandomForestClassifier`) dynamically.
  - Saves the trained model for use by the churn prediction agent.
- **Role**: *ML Model Trainer and Provider*

### 3. `churn_prediction_agent.py`
- **Purpose**: Loads the pre-trained ML model and predicts churn probability for each customer.
- **Key Features**:
  - Dynamically extracts features from customer profiles.
  - Predicts churn risk probability.
  - Categorizes customers into high, medium, or low risk.
- **Role**: *Churn Risk Scorer*

### 4. `persona_builder_agent.py`
- **Purpose**: Clusters customers into distinct personas based on churn risk and behavioral data.
- **Key Features**:
  - Uses `KMeans` clustering on dynamic feature sets.
  - Assigns persona labels to customers for targeted marketing.
- **Role**: *Customer Segmenter / Persona Generator*

### 5. `offer_optimization_agent.py`
- **Purpose**: Selects the best retention offer for each customer based on churn risk and persona.
- **Key Features**:
  - Uses churn risk categories to assign dynamic offers (e.g., discounts, bundles).
  - Logic can be extended to use persona or other profile info.
- **Role**: *Retention Offer Optimizer*

### 6. `engagement_agent.py`
- **Purpose**: Generates personalized communication messages and selects the optimal channel.
- **Key Features**:
  - Crafts tailored messages based on customer details.
  - Chooses channels dynamically (e.g., phone calls for high-risk, email for medium).
- **Role**: *Customer Engagement Specialist / Copywriter*

### 7. `feedback_loop_agent.py`
- **Purpose**: Collects and processes feedback from customer engagement efforts.
- **Key Features**:
  - Simulates or consumes real feedback on campaign success.
  - Updates customer profiles with feedback annotations.
- **Role**: *Campaign Performance Analyst*

### 8. `build_tasks.py`
- **Purpose**: Defines the CrewAI task pipeline linking all agents sequentially.
- **Key Details**:
  - Specifies execution order.
  - Declares expected outputs and input keys.
  - Sets parallelism or sequential execution flags.

### 9. `main.py`
- **Purpose**: Entry point to run the full pipeline.
- **Key Details**:
  - Instantiates agents with appropriate LLM or dependencies.
  - Loads input files (customer data, offers, etc.).
  - Constructs the pipeline using `build_tasks.py`.
  - Triggers execution and displays final results.

## Output Description
The final output is an annotated customer profile list, enriched with:
- `churn_score`: Probability (0-1) indicating churn risk.
- `churn_risk`: Categorized risk level (high, medium, low).
- `persona`: Cluster assignment for segmentation.
- `offer`: Recommended retention offer.
- `message` & `channel`: Personalized communication details.
- `feedback`: Engagement feedback for optimization.

## Benefits for Stakeholders
- **Proactive Churn Reduction**: Identify high-risk customers early.
- **Personalized Campaigns**: Tailor offers and messages based on risk and persona.
- **Efficient Resource Allocation**: Focus marketing efforts on high-impact segments.
- **Continuous Improvement**: Learn from feedback to refine future campaigns.

## Summary
**Goal**: Reduce customer churn and increase retention via AI-driven automation.  
**Approach**: Modular, reusable agents handle discrete tasks from data to feedback.  
**Result**: Significant reduction in churn risk, improved engagement, and optimized marketing spend.

## Evaluation Parameters & Tools

| Aspect                  | Metrics / Methods                          | Tools / Techniques                     |
|-------------------------|-------------------------------------------|----------------------------------------|
| **Data Quality**        | Completeness, correctness, anomaly detection | Data profiling tools, custom scripts  |
| **Model Accuracy**      | Precision, Recall, F1, ROC-AUC            | Scikit-learn, MLflow, custom tests    |
| **Clustering Validity** | Silhouette score, Davies-Bouldin          | Scikit-learn metrics                  |
| **Recommendation Quality** | Conversion rate, A/B test lift         | Experiment platforms, analytics       |
| **Engagement Metrics**  | Open rate, CTR, response rate            | Email/SMS analytics, CRM platforms    |
| **Feedback Integration**| KPI improvements after feedback          | Monitoring dashboards                 |
| **Business Impact**     | Churn reduction %, revenue uplift, cost savings | BI tools (Tableau, Power BI)       |
| **Pipeline Performance**| Latency, throughput, error rate          | Logging, monitoring (Prometheus, ELK) |


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

