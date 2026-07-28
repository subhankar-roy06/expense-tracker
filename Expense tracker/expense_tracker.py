from expense import Expense
import expense
def main():
    print(f"🎯Running Expense Tracker!")
    expense_file_path = "expense.csv"
    pass
    #------------------------------
    # get input for expense
    Expense = get_user_expense()
    print(Expense)
    # write there expense to their file
    save_expense_to_file(Expense,expense_file_path)
    # read file and summerize expense
    show_summery(expense_file_path)
    #------------------------------
def get_user_expense():
    print("🎯Getting User expense:")
    expense_name = input("Enter expense name:")
    expense_amount = float(input("Enter expense amount:"))
    expense_catagory = [
        "🍎Food",
        "🏠Home",
        "💼Work",
        "🎉Fun",
        "✨Misc"
    ]
    while True:
        print("Select a catagory -> ")
        for  i , catagory_name in enumerate(expense_catagory):
            print(f"  {i+1}. {catagory_name}")
        value_range = f"[1- {len(expense_catagory)}]"
        Selected_index = int(input(f"Enter a Catagory Number {value_range}: ")) - 1
        if Selected_index in range(len(expense_catagory)):
            selected_catagory = expense_catagory[Selected_index]
            try:
                amount_value = float(expense_amount)
            except ValueError:
                print("Skipping malformed line:", stripped_line)
                continue
            new_expense = Expense(
                name=expense_name,
                amount=amount_value,
                catagory=selected_catagory
            )
            return new_expense
        else:
            print("Invalid catagory,Please try again!")
        break


    print(f"You've Enterd {expense_name} -> {expense_amount} rupees")

def save_expense_to_file(expense,expense_file_path):
    print(f"🎯Saving file:{expense} to{expense_file_path}")
    with open(expense_file_path,"a") as f :
        f.write(f"{expense.name},{expense.amount},{expense.catagory}\n")



def show_summery(expense_file_path):
    print(f"🎯giving the summery")
    with open(expense_file_path,"r") as f:
        line = f.readlines()
        for lines in line:
            stripped_line = lines.strip()
            expense_name, expense_amount, expense_catagory = stripped_line.split(",", 2)
            print(expense_name, expense_amount, expense_catagory)
            try:
                amount_value = float(expense_amount)
            except ValueError:
                print("Skipping malformed line:", stripped_line)
                continue
            line_expense = Expense(
                name=expense_name,
                amount=amount_value,
                catagory=expense_catagory
            )
            print(expense_name, expense_amount, expense_catagory)
            expense.append(expense_file_path, line_expense)
if __name__ == "__main__":
    main()