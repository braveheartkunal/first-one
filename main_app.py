from data_manager import DataManager
from finance_ai import FinanceAI
from datetime import datetime

def main():
    db = DataManager()
    ai = FinanceAI()
    
    print("--- AI Personal Finance Manager (College Edition) ---")
    
    while True:
        print("\n1. Add Expense\n2. View Summary\n3. AI Budget Prediction\n4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            desc = input("Enter description (e.g., Starbucks Coffee): ")
            amt = float(input("Enter amount: "))
            date = datetime.now().strftime("%Y-%m-%d")
            
            # AI Step: Auto-categorize
            category = ai.auto_categorize(desc)
            print(f"AI categorized this as: {category}")
            
            db.add_expense(date, desc, category, amt)
            print("Expense saved!")

        elif choice == '2':
            print("\nRecent Expenses:")
            print(db.get_all_data())

        elif choice == '3':
            # Extract monthly totals for prediction
            df = db.get_all_data()
            if df.empty:
                print("No data available.")
                continue
            
            # Simple simulation: using the last few entries as monthly totals
            history = df['Amount'].tolist()
            prediction = ai.predict_next_month(history)
            print(f"\nAI Predicted Spending for next month: {prediction}")

        elif choice == '4':
            break

if __name__ == "__main__":
    main()