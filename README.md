# 🛒 Agentic AI Retail Churn Prediction Pipeline

## Overview

This project implements an **Agentic AI pipeline** for retail churn prediction using CrewAI, Large Language Models (LLMs), and modular agents. It simulates a real-world, enterprise-grade scenario where multiple intelligent agents automate data aggregation, churn risk scoring, customer segmentation, offer optimization, and feedback analysis—delivering actionable business outcomes with minimal manual intervention.

---

## Problem Statement

**Retailers face high customer churn rates, impacting revenue and growth.**  
Predicting which customers are likely to churn, understanding their profiles, and proactively engaging them with personalized retention strategies is critical. Traditional approaches are manual, slow, and fail to deliver targeted action.

---

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

## Sample Output

*Below is an actual excerpt from the project output:*

