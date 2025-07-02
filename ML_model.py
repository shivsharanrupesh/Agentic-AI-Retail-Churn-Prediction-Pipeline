import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Path to customer data CSV - adjust as needed or parameterize
CUSTOMER_DATA_CSV = "customer_data.csv"

# Load data dynamically from CSV
df = pd.read_csv(CUSTOMER_DATA_CSV)

# Target column name - change if different
target_column = 'churn'

# Extract feature columns dynamically (all except target)
feature_names = [col for col in df.columns if col != target_column]

# Prepare feature matrix X and target vector y
X = df[feature_names]
y = df[target_column]

# Optional: Preprocessing (fill missing, encode, scale, etc.)
X = X.fillna(0)  # Simple missing value handling example

# Split dataset for training and validation (optional)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Optional: Print test accuracy for your info
print(f"Test Accuracy: {clf.score(X_test, y_test):.4f}")
