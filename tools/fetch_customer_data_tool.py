from crewai.tools import tool
from utils.data_utils import fetch_customer_data

@tool("FetchCustomerData")
def fetch_customer_data_tool(file_path: str):
    """
    Loads customer data from a CSV file.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        list: Customer profiles as dictionaries.
    """
    return fetch_customer_data(file_path)
