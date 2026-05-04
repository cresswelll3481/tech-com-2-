import pandas
import math
from tabulate import tabulate
from datetime import date

def make_statement(statement, decoration, lines=1):
    return f"{decoration * 3} {statement} {decoration * 3}"

def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no.\n")

def instructions():
    print(make_statement("Instructions", "^"))
    print('''
enter your product name
enter the variable expenses
enter the fixed expenses if you have them
enter the profit goal
    ''')

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
        item_name = not_blank("item name: ")
        if (exp_type == "variable" and item_name == "xxx") and len(all_items) == 0:
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
    add_dollars = ['$ / Item', 'Cost', ]
    for var_item in add_dollars:
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

def profit_goals(total_costs):
    error = "please enter a valid profit goal"
    while True:
        response = not_blank("what is your profit goal (eg $500 or 50%): ")
        if response[0] == "$":
            profit_type = "$"
            amount = response[1:]
        elif response[-1:] == "%":
            profit_type = "%"
            amount =   response[:-1]
        else:
            profit_type = "unknown"
            amount = response
        try:
            amount = float(amount)
            if amount <= 0:
                print(error)
                return None
                continue


        except ValueError:
            print(error)
            return None
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no(f"Do you mean ${amount:.2f}. ie {amount:.2f} dollars?, y / n: ")
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"
        elif profit_type == "unknown" and amount < 100:
            precent_type = yes_no(f"Do you mean {amount:.2f}%, y / n: ")
            if precent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal

def rounding_up(amount, round_val):
    return int(math.ceil(amount / round_val) * round_val)



#main
spaces_string = make_statement("Fund raising calculator", "#")
underscores_string = spaces_string.replace(" ", "_")
print()
want_instructions = yes_no("do you want to see the instructions? ")
print()
if want_instructions == "yes":
    instructions()
print()
#getting information
product_name = not_blank("Product name: ")
quantity_made = num_check("quantity being made: ", "integer")
print()
print("getting variable costs...")
variable_expenses = get_expenses("variable", quantity_made)
print()

variable_panda, variable_subtotal, variable_string = variable_expenses

print("Getting fixed costs... ")

has_fixed = yes_no("Do you have the fixed costs? ")
if has_fixed == "yes":
    fixed_expenses = get_expenses("fixed")

    print()
    fixed_pandas, fixed_subtotal, fixed_string = fixed_expenses
    print()

else:
    fixed_pandas = ""
    fixed_string = ""
    fixed_subtotal = 0

#getting expenses
print("=== Variable Expenses ===")
print(variable_string)
print(f"variable subtotal: ${variable_subtotal:.2f}")
print()
print("=== Fixed Expenses ===")
print(fixed_string)
print(f"fixed subtotal: ${fixed_subtotal:.2f}")
print()
print("Getting total expenses... ")
total_expenses = variable_subtotal + fixed_subtotal
print(f"Total Expenses: ${total_expenses:.2f}")

target = profit_goals(total_expenses)
sales_target = total_expenses + target
selling_price = (total_expenses + target) / quantity_made
round_to = num_check("Round to: ", 'integer')
suggested_price = rounding_up(selling_price, round_to)

today = date.today()
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")
#making strings and headings
main_heading = make_statement(f" Fund Raising Calculator "
                              f"({product_name}, {day}/{month}/{year})", "=")
quantity_string = f"Quantity being made: {quantity_made}"
variable_string_heading = make_statement("variable expenses", "-")
variable_subtotal_heading = f"Variable Expenses Subtotal: ${variable_subtotal:.2f}"

if has_fixed == "yes":
    fixed_heading_string = make_statement("fixed expenses", "-")
    fixed_subtotal_string = f"Fixed Expenses Subtotal: {fixed_subtotal:.2f}"
else:
    fixed_heading_string = make_statement("You have no Fixed Expenses", "-")
    fixed_subtotal_string = "Fixed Expenses Subtotal: $0.00"

selling_price_heading = make_statement("Selling price calculations", "|")
profit_goals_string = f"Profit Goal: ${target:.2f}"
sales_target_string = f"\nTotal Sales Needed: ${sales_target:.2f}"
minimum_price_string = f"Minimum Selling Price: ${selling_price:.2f}"
suggested_price_string = make_statement(f"Suggested Selling Price: "
                                        f"${suggested_price:.2f}", "")

# fixed_pandas_string = f"{fixed_pandas}"
# variable_panda_string = f"{variable_panda}"
total_expenses_heading = make_statement("Total Expenses", "!")
total_expenses_string = f"Total Expenses: ${total_expenses:.2f}"

#writing to file
to_write = [main_heading, "\n", quantity_string,
            "\n", variable_string_heading, variable_string, variable_subtotal_heading,
            "\n", fixed_heading_string, fixed_string, fixed_subtotal_string,
            "\n", selling_price_heading, "\n", total_expenses_string, profit_goals_string,
            "\n", minimum_price_string, suggested_price_string]

print()
for item in to_write:
    print(item)

file_name = f"{product_name}_{year}_{month}_{day}"
write_to = "{}.txt".format(file_name)
text_file = open(write_to, "w+")
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
