import pandas as pd
import os

class DataManager:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        if not os.path.exists(self.filename):
            df = pd.DataFrame(columns=["Date", "Description", "Category", "Amount"])
            df.to_csv(self.filename, index=False)

    def add_expense(self, date, desc, cat, amt):
        df = pd.read_csv(self.filename)
        new_row = {"Date": date, "Description": desc, "Category": cat, "Amount": amt}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(self.filename, index=False)

    def get_all_data(self):
        return pd.read_csv(self.filename)