from crewai import Agent
from ML_model import load_model  # Your ML model loader module

class ChurnPredictionAgent(Agent):
    """
    CrewAI Agent for predicting customer churn risk.
    """

    def __init__(self, llm):
        super().__init__(
            name="Churn Prediction Agent",
            description="Predicts churn risk for every profile using ML.",
            goal="Label every customer with a data-driven churn score and risk level.",
            role="The business analyst who won't let a loyal customer slip away.",
            backstory="A loyalty analytics specialist who trusts numbers and patterns.",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
        # Load the model and features dynamically from ML_model.py
        self.model, self.feature_cols = load_model()

    def run(self, customer_profiles, **kwargs):
        """
        Assign churn probability scores and risk levels to customer profiles.

        Args:
            customer_profiles (list): List of customer dictionaries.

        Returns:
            list: Customer profiles with added 'churn_score' and 'churn_risk'.
        """
        features = [self._extract_features(p) for p in customer_profiles]
        probs = self.model.predict_proba(features)[:, 1]

        for p, score in zip(customer_profiles, probs):
            p['churn_score'] = float(score)
            p['churn_risk'] = self._risk_level(score)
        return customer_profiles

    def _extract_features(self, profile):
        """
        Extract features dynamically based on model's expected columns.

        Args:
            profile (dict): Customer profile.

        Returns:
            list: Feature vector for ML model.
        """
        return [profile.get(col, 0) for col in self.feature_cols]

    def _risk_level(self, score):
        """
        Map churn probability to risk categories.

        Args:
            score (float): Churn probability score.

        Returns:
            str: Risk level label.
        """
        if score >= 0.7:
            return "high"
        elif score >= 0.4:
            return "medium"
        else:
            return "low"
