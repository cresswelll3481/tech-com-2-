import pandas

def currency(x):
    return "${:.2f}".format(x)
def not_blank(question):
    """Checks that a response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. please try again. \n")

def int_check(question):
    """Checks for integers more than 0"""

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
    """ checks users enter a valid option from a given list, accepts first / first
     few letters and full word"""

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

names_list = []
ticket_list = []
surcharge_list = []

mini_movie_dict = {
    'Name': names_list,
    'Ticket Price': ticket_list,
    'Surcharge': surcharge_list
}

# surcharge is 15% - use this to apply surcharge to credit payments
surcharge = 0.15

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

    # get payment method (cash / credit)
    pay_meth = string_checker("payment method: ", pay_ans, 2)

    # Work out ticket price based on age
    if age < 16:
        ticket_price = CHILD
    elif age >= 65:
        ticket_price = SENIOR
    else:
        ticket_price = ADULT

    # apply surcharge if paying by credit...
    if pay_meth == "credit":
        add_surcharge = ticket_price * surcharge
    else:
        add_surcharge = 0

    names_list.append(name)
    ticket_list.append(ticket_price)
    surcharge_list.append(add_surcharge)

# outside loop - show panda
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()
#adds dollar sign
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

#print(mini_movie_frame)
print(mini_movie_frame.to_string(index=False))
print()
print(f"total paid: ${total_paid:.2f}")
print(f"total profit: ${total_profit:.2f}")
