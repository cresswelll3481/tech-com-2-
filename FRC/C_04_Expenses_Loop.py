def not_blank(question):

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. please try again. \n")
def num_check(question, num_type="float", exit_code=None):

    if num_type == "integer":
        error = "Please enter a integer more than zero"
        change_to = int
    else:
        error = "Please enter a number more than zero"
        change_to = float
    while True:
        response = input(question).lower()
        if response == exit_code:
            return response
        try:
            response = change_to(response)
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

def get_expenses(exp_type):
    all_items = []
    while True:
        item_name = not_blank("item name:")
        if (exp_type == "variable" and
            item_name =="xxx") and len(all_items) == 0:
            print("you have not entered anything. "
                  "you need at least one item.")
            continue
        elif item_name == "xxx":
            break
        all_items.append(item_name)
    return all_items
            

print("getting variable costs...")
variable_expenses = get_expenses("variable")
num_variable = len(variable_expenses)
print(f"you entered {num_variable} items")
print()

print("Getting Fixed Costs...")
fixed_expenses = get_expenses("fixed")
num_fixed = len(fixed_expenses)
print(f"You have entered {num_fixed} items")