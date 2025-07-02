from crewai import Agent
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Placeholder for ML model - assume imported from ml_model.py or injected
X = np.random.rand(100, 4)
y = np.random.randint(0, 2, 100)
clf = RandomForestClassifier()
clf.fit(X, y)

class ChurnPredictionAgent(Agent):
    """
    CrewAI Agent for predicting customer churn risk.
    """
    def __init__(self, llm):
        super().__init__(
            name="Churn Prediction Agent",
            description="Predicts churn risk for every profile using ML.",
            goal="Label every customer with a data-driven churn score.",
            role="The business analyst who won't let a loyal customer slip away.",
            backstory="A loyalty analytics specialist who trusts numbers and patterns.",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def run(self, customer_profiles, **kwargs):
        """
        Assign churn probability scores and risk levels to customer profiles.

        Args:
            customer_profiles (list): List of customer dictionaries.

        Returns:
            list: Customer profiles with added 'churn_score' and 'risk_level'.
        """
        features = [self._extract_features(p) for p in customer_profiles]
        scores = clf.predict_proba(features)[:, 1]

        for p, score in zip(customer_profiles, scores):
            p['churn_score'] = float(score)
            p['risk_level'] = self._assign_risk_level(score)

        return customer_profiles

    def _assign_risk_level(self, score):
        """
        Convert churn probability into risk categories.

        Args:
            score (float): Churn probability score between 0 and 1.

        Returns:
            str: Risk category - 'high', 'medium', or 'low'.
        """
        if score >= 0.7:
            return 'high'
        elif score >= 0.4:
            return 'medium'
        else:
            return 'low'

    def _extract_features(self, profile):
        """
        Convert a customer profile dict to a feature vector.

        Args:
            profile (dict): Customer profile.

        Returns:
            list: Feature vector for ML model.
        """
        return [
            profile.get('visit_freq', 0),
            profile.get('avg_basket', 0),
            profile.get('last_coupon_days', 99),
            profile.get('reward_points', 0),
        ]
