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
        """Simple NLP: Matches keywords to categorize expenses."""
        desc = description.lower()
        for category, keywords in self.categories.items():
            if any(key in desc for key in keywords):
                return category.capitalize()
        return "Other"

    def predict_next_month(self, historical_data):
        """Uses Linear Regression to predict next month's total spending."""
        if len(historical_data) < 2:
            return "Need at least 2 months of data for AI prediction."

        # X = month numbers [1, 2, 3...], Y = total spent
        X = np.array(range(len(historical_data))).reshape(-1, 1)
        y = np.array(historical_data)

        model = LinearRegression()
        model.fit(X, y)

        # Predict for the next index (next month)
        next_month = np.array([[len(historical_data)]])
        prediction = model.predict(next_month)
        print("done mama")
        return f"${prediction[0]:.2f}"
