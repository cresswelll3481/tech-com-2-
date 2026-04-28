import pandas
from tabulate import tabulate

def not_blank(question):

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. please try again. \n")

def num_check(question, num_type="float", exit_code=None):

    if num_type == "float":
        error = "Please enter a number more than zero"
    else:
        error = "Please enter a integer more than zero"
    while True:
        response = input(question)
        if response == exit_code:
            return response
        try:
            if num_type == "float":
                response = float(response)
            else:
                response = int(response)
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

def get_expenses(exp_type, how_many=1):
    all_items = []
    all_amount = []
    all_dollar_per_item = []

    expenses_dict = {
        "Item": all_items,
        "Amount": all_amount,
        "$ / Item": all_dollar_per_item
    }
    Amount = how_many
    how_much_question = "how much? $"

    while True:
        item_name = not_blank("item name:")
        if (exp_type == "variable" and item_name =="xxx") and len(all_items) == 0:
            print("you have not entered anything. "
                  "you need at least one item.")
            continue
        elif item_name == "xxx":
            break
        if exp_type == "variable":
            Amount = num_check(f"how many <enter for {how_many}>:", "integer", "")
            if Amount == "":
                Amount = how_many
            how_much_question = "price for one? $"
        price_for_one = num_check(how_much_question, "float")

        all_items.append(item_name)
        all_amount.append(Amount)
        all_dollar_per_item.append(price_for_one)

    expenses_frame = pandas.DataFrame(expenses_dict)
    expenses_frame['Cost'] = expenses_frame['Amount'] * expenses_frame['$ / Item']
    subtotal = expenses_frame['Cost'].sum()
    add_dollars = ['Amount', '$ / Item', 'Cost']
    for var_item in  add_dollars:
        expenses_frame[var_item] = expenses_frame[var_item].apply(currency)
    if exp_type == "variable":
        expense_string = tabulate(expenses_frame, headers='keys',
                                  tablefmt='psql', showindex=False)
    else:
        expense_string = tabulate(expenses_frame[['Item', 'Cost']], headers='keys',
                                  tablefmt='psql', showindex=False)

    return expenses_frame, subtotal, expense_string
def currency(x):
    return "${:.2f}".format(x)


#main
quantity_made = num_check("quantity being made: ",
                          "integer")
print()
print("getting variable costs...")
variable_expenses = get_expenses("variable", quantity_made)
print()
variable_panda, variable_subtotal, variable_string = variable_expenses
print("Getting fixed costs... ")
fixed_expenses = get_expenses("fixed")
print()
fixed_pandas, fixed_subtotal, fixed_string = fixed_expenses
print("=== Variable Expenses ===")
print(variable_string)
print(f"variable subtotal: ${variable_subtotal:.2f}")
print("=== Fixed Expenses ===")
print(fixed_string)
print(f"fixed subtotal: ${fixed_subtotal:.2f}")
print()
print("Getting total expenses... ")
total_expenses = variable_subtotal + fixed_subtotal
print(f"Total Expenses: ${total_expenses:.2f}")
