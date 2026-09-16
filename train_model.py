import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
from sklearn.preprocessing import LabelEncoder

# Load CSV
data = pd.read_csv("adult 3.csv")

# Encode income column (if it's text like <=50K, >50K)
le = LabelEncoder()
data['income'] = le.fit_transform(data['income'])

# Features and target
X = data[['age', 'educational-num', 'hours-per-week']]
y = data['income']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, 'salary_model.pkl')
print("Model trained and saved successfully.")
