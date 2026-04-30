
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no.\n")

def profit_goals(total_costs):
    error = "please enter a valid profit goal"
    valid = False
    while True:
        response = input("what is your profit goal (eg $500 or 50%): ")
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
                continue
                return None
                return None
        except ValueError:
            print(error)
            continue
            return None
            return None
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

while True:
    total_expenses = 200
    target = profit_goals(total_expenses)
    sales_target = total_expenses + target
    print(f"Profit Goal: ${target:.2f}")
    print(f"sales target: ${sales_target:.2f}")
    print()
