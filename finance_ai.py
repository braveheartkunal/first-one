import numpy as np
from sklearn.linear_model import LinearRegression

class FinanceAI:
    def __init__(self):
        # Mock NLP Categorization rules
        self.categories = {
            "food": ["starbucks", "mcdonalds", "grocery", "restaurant", "pizza"],
            "transport": ["uber", "lyft", "gas", "shell", "metro"],
            "utilities": ["rent", "electric", "water", "internet", "netflix"],
            "shopping": ["amazon", "walmart", "target", "nike"]
        }

    def auto_categorize(self, description):

        desc = description.lower()
        for category, keywords in self.categories.items():
            if any(key in desc for key in keywords):
                return category.capitalize()
        return "Other"

    def predict_next_month(self, historical_data):
        """Uses Linear Regression to predict next month's total spending."""
        if len(historical_data) < 2:
            return "Need at least 2 months of data for AI prediction."

        X = np.array(range(len(historical_data))).reshape(-1, 1)
        y = np.array(historical_data)

        model = LinearRegression()
        model.fit(X, y)
        next_month = np.array([[len(historical_data)]])
        prediction = model.predict(next_month)
        return f"rupee  {prediction[0]:.2f}"
    # Initialize your AI
ai = FinanceAI()

# 1. Test Input for Categorization (A String)
transaction = "Uber ride to university"
category = ai.auto_categorize(transaction)
print(f"Transaction: {transaction} | Category: {category}")

# 2. Test Input for Prediction (A List of numbers)
# Input at least 2 months of historical spending
spending_history = [1200, 1500, 1800, 2100]
prediction = ai.predict_next_month(spending_history)
print(f"Historical Data: {spending_history}")
print(f"Predicted spending for next month: {prediction}")

