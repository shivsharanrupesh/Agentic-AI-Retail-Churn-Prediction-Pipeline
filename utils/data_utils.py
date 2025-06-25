import pandas as pd

def fetch_customer_data(file_path):
    """
    Load customer profiles from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list of dict: List of customer profile dictionaries.
    """
    df = pd.read_csv(file_path)
    sample_data = []
    for _, row in df.iterrows():
        profile = {
            "customer_id": row["customer_id"],
            "visit_freq": int(row["visit_freq"]),
            "avg_basket": float(row["avg_basket"]),
            "last_coupon_days": int(row["last_coupon_days"]),
            "reward_points": int(row["reward_points"]),
        }
        sample_data.append(profile)
    return sample_data
