import pandas
import random

def currency(x):
    return "${:.2f}".format(x)
def make_statement(statement, decoration, lines = 1):

    middle = (f"{decoration * 3} {statement} {decoration * 3}")
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)
    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)
def string_checker(question, valid_ans=('yes', 'no'), num_letters=1):
    while True:
        response = input(question).lower()
        for item in valid_ans:
            if response == item:
                return item
            elif response == item[:num_letters]:
                return item
        print(f"Please choose an option from {valid_ans}")
def instructions():
    make_statement("Instructions", "^")
    inst = ('''
    For each ticket holder enter:
    -Name
    -Age
    -Payment (cash or credit

    this program will record the ticket sale and calculate the ticket cost

    once you have either sold all of the tickets or entered all of the 
    exit code "xxx" the program will display the ticket sales info and write it to a text file 

    it will also choose one lucky ticket holder who wins the draw their ticket is free
    ''')
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
def not_blank(question):

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. please try again. \n")

pay_ans = ('cash', 'credit')
max_tickets = 5
tickets_sold = 0

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

# surcharge is 5% - use this to apply surcharge to credit payments
surcharge = 0.05

make_statement("Mini Movie Fundraiser","$")
want_instructions = string_checker("do you want to see the instructions? ",)
print(f"you chose {want_instructions}")
if want_instructions == "yes":
   instructions()

while tickets_sold < max_tickets:
    print()
    name = not_blank("Name: ")
    if name == "xxx":
        break
    print()
    age = int_check("age: ")

    if age < 16:
        ticket_price = CHILD
    elif age >= 65:
        ticket_price = SENIOR
    else:
        ticket_price = ADULT

        # apply surcharge if paying by credit...

    pay_meth = string_checker("payment method: ", pay_ans, 2)
    if pay_meth == "credit":
        add_surcharge = ticket_price * surcharge
    else:
        add_surcharge = 0

    names_list.append(name)
    ticket_list.append(ticket_price)
    surcharge_list.append(add_surcharge)
    #adds one to total
    tickets_sold += 1


# outside loop - show panda
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()
#random winner
winner = random.choice(names_list)
winner_index = names_list.index(winner)
print("winner", winner, "list position", winner_index)

ticket_won = mini_movie_frame.at[winner_index, "Total"]
profit_won = mini_movie_frame.at[winner_index, "Profit"]

#adds dollar sign
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)
#prints stats

print(mini_movie_frame.to_string(index=False))
print()
print(f"total paid: ${total_paid:.2f}")
print(f"total profit: ${total_profit:.2f}")

winner = random.choice(names_list)
winner_index = names_list.index(winner)
print("winner", winner, "list position", winner_index)

total_won = mini_movie_frame.at[winner_index, "Total"]
print(f"The lucky winner is {winner}. Their ticket worth ${total_won:.2f} is free!")
print(f"Total paid is now ${total_paid - ticket_won:.2f}")
print(f"Total profit is now ${total_profit - profit_won:.2f}")
if tickets_sold == max_tickets:
    print("you have sold all of the tickets")
else:
    print(f"you have sold {tickets_sold} out of {max_tickets} tickets")
