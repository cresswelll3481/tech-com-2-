import pandas


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

def get_expenses(exp_type, how_many=None):
    all_items = []
    all_amount = []
    all_dollar_per_item = []

    expenses_dict = {
        "Item": all_items,
        "Amount": all_amount,
        "$ / Item": all_dollar_per_item
    }
    amount = 1

    while True:
        item_name = not_blank("item name:")
        if (exp_type == "variable" and item_name =="xxx") and len(all_items) == 0:
            print("you have not entered anything. "
                  "you need at least one item.")
            continue
        elif item_name == "xxx":
            break

        amount = num_check(f"how many <enter for {how_many}>:", "integer", "")
        if amount == "":
            amount = how_many
        costs = num_check("price for one?  ", "float")

        all_items.append(item_name)
        all_amount.append(amount)
        all_dollar_per_item.append(costs)

    expenses_frame = pandas.DataFrame(expenses_dict)
    expenses_frame['Cost'] = expenses_frame['Amount'] * expenses_frame['$ / Item']
    subtotal = expenses_frame['Cost'].sum()
    return expenses_frame, subtotal
            
quantity_made = num_check("quantity being made: ",
                          "integer")
print()

print("getting variable costs...")
variable_expenses = get_expenses("variable", quantity_made)
print()
variable_panda = variable_expenses[0]
variable_subtotal = variable_expenses[1]
print(variable_panda)
print(variable_subtotal)