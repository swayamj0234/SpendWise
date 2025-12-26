def main():
    print("🚀Welcome to the Expense Tracker!")
    
    add_expense()

    save_expenses_to_file()

    summarize_expenses()


def add_expense():   #function to add an expense
    print(f"adding expense..")
    
def save_expenses_to_file():  #function to save expenses to a file
    print(f"saving expenses to file..")

def summarize_expenses():  #function to summarize expenses
    print(f"summarizing expenses..")

if __name__ == "__main__":  #only runs when this file is executed directly
    main()