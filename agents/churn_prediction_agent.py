from crewai import Agent
from ML_model import clf, feature_names  # Import model and feature names dynamically

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
        Assign churn probability scores to customer profiles.

        Args:
            customer_profiles (list): List of customer dictionaries.

        Returns:
            list: Customer profiles with added 'churn_score'.
        """
        features = [self._extract_features(p) for p in customer_profiles]
        scores = clf.predict_proba(features)[:, 1]
        for p, score in zip(customer_profiles, scores):
            p['churn_score'] = float(score)
        return customer_profiles

    def _extract_features(self, profile):
        """
        Convert a customer profile dict to a feature vector dynamically
        based on the feature_names list from ML_model.py.

        Args:
            profile (dict): Customer profile.

        Returns:
            list: Feature vector for ML model.
        """
        return [profile.get(feat, 0) for feat in feature_names]
