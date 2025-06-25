from crewai import Agent
import openai
import os
import random

CHANNELS = ['sms', 'email', 'app']  # Module-level default channels

class EngagementAgent(Agent):
    """
    CrewAI Agent for generating personalized messages for customer engagement.
    """
    def __init__(self, llm):
        super().__init__(
            name="Engagement Agent",
            description="Generates and personalizes outreach via LLM for each customer.",
            goal="Craft high-converting messages in the right channel.",
            role="The copywriter who speaks each shopper's language.",
            backstory="You live for loyalty and engagement metrics.",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def run(self, customer_profiles, **kwargs):
        """
        Generate and assign a personalized message for each customer.

        Args:
            customer_profiles (list): Profiles with offers.

        Returns:
            list: Profiles with engagement channel and message.
        """
        for p in customer_profiles:
            p['engagement_channel'] = random.choice(CHANNELS)
            p['message'] = self._generate_message(p)
        return customer_profiles

    def _generate_message(self, profile):
        """
        Use OpenAI to generate a personalized marketing message.

        Args:
            profile (dict): Single customer profile.

        Returns:
            str: Generated message.
        """
        prompt = (
            f"Create a Dollar General outreach message for a {profile['persona']} at risk of churn. "
            f"The offer is {profile['offer']}."
        )
        try:
            completion = openai.ChatCompletion.create(
                model="ggpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a creative retail marketing specialist."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=60
            )
            return completion.choices[0].message['content']
        except Exception as e:
            return f"DG offer for {profile['persona']}: {profile['offer']} (LLM error: {str(e)})"
