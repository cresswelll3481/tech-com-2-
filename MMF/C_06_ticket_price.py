def not_blank(question):

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. please try again. \n")
def int_check(question):
    error = f"Please enter a integer more than 0"

    while True:
        response = input(question).lower()
        try:
            response = int(response)
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)
def string_checker(question, valid_ans=('yes', 'no'), num_letters=1):
    while True:
        response = input(question).lower()
        for item in valid_ans:
            if response == item:
                return item
            elif response == item[:num_letters]:
                return item
        print(f"Please choose an option from {valid_ans}")


# intialise variables / constants

# ticket prices...
CHILD = 7.5
ADULT = 10.5
SENIOR = 6.5

# surcharge is 15% - use this to apply surcharge to credit payments
surcharge = 1.05

pay_ans = ('cash', 'credit')
while True:
    print()

    # check name is no blank, exit if users type 'xxx'
    name = not_blank("Name: ")

    if name == "xxx":
        break

    age = int_check("age: ")
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old ")
        continue
    else:
        pass

    pay_meth = string_checker("payment method: ", pay_ans, 2)

    # Work out ticket price based on age
    if age <= 16:
        ticket_price = CHILD
    elif age >= 65:
        ticket_price = SENIOR
    else:
        ticket_price = ADULT

    # Apply surcharge to credit payments
    if pay_meth == "credit":
        ticket_price = ticket_price * surcharge

    print(f"the ticket price is ${ticket_price:.2f}")
    print(f"{name} has brought a ticket using {pay_meth}")
    if pay_meth == "credit":
        print(f"the surcharge is 15% ")
    print(f"the total payable is ${ticket_price:.2f}")


