def main():
    print("🚀Welcome to the Expense Tracker!")
    
    add_expense()

    #save_expenses_to_file()

    #summarize_expenses()


def add_expense():   #function to add an expense
    print(f"adding expense..")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print(f"You've entered : {expense_name}, {expense_amount: .2f} €")

    expense_category = [
        "Food 🍔",
        "Transport 🚗",
        "Entertainment 🎮",
        "Home 🏠",
        "Miscellaneous 🧾",
    ]

    while True:
        print("Select expense category:")
        for i, category in enumerate(expense_category, 1): #enumerate to number the categories
            print(f"  {i}. {category}")

        value_range = f"[1 - {len(expense_category)}]"
        selected_category = int(input(f"Enter category number {value_range}: "))

        if selected_category in range(1, len(expense_category) + 1):
          break
        else:
            print(f"Invalid input. Please enter a number {value_range}.")
    print(f"Category selected: {expense_category[selected_category - 1]}")  #-1 to adjust for 0-based index
     
    
 
    
def save_expenses_to_file():  #function to save expenses to a file
    print(f"saving expenses to file..")

def summarize_expenses():  #function to summarize expenses
    print(f"summarizing expenses..")

if __name__ == "__main__":  #only runs when this file is executed directly
    main()