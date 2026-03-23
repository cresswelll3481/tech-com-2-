import pandas
import random
def currency(x):
    return "${:.2f}".format(x)
def make_statement(statement, decoration, lines = 1):

    return f"{decoration * 3} {statement} {decoration * 3}"
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
    print(make_statement("Instructions", "^"))
    print('''
For each ticket holder enter:
-Name
-Age
-Payment (cash or credit)

This program will record the ticket sale and calculate the ticket cost

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
# print heading
print(make_statement("Mini Movie Fundraiser","$"))

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


ticket_won = mini_movie_frame.at[winner_index, "Total"]
profit_won = mini_movie_frame.at[winner_index, "Profit"]

#adds dollar sign
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)
#prints stats

mini_movie_string = mini_movie_frame.to_string(index=False)

total_paid_string = f"\ntotal paid: ${total_paid:.2f}"
total_profit_string = f"total profit: ${total_profit:.2f}"
#chose winner
winner = random.choice(names_list)
winner_index = names_list.index(winner)
#winnings
total_won = mini_movie_frame.at[winner_index, "Total"]
winner_string = (f"The lucky winner is {winner}."
                 f"Their ticket worth ${total_won} is free!")

final_total_paid = f"\nTotal paid is now ${total_paid - ticket_won:.2f}"
final_total_profit = f"\nTotal profit is now ${total_profit - profit_won:.2f}"
#tickets sold
if tickets_sold == max_tickets:
    num_sold_string = make_statement(f"you have sold all of the tickets "
                                     f"({max_tickets})", "-")
else:
    num_sold_string = make_statement(f"you have sold {tickets_sold} out of "
                                     f"{max_tickets} tickets","-")


heading_string = make_statement("mini movie fundraiser", "=")
ticket_headeing = make_statement("ticket details", "-")
raffle_headding = make_statement(" raffle winner", "-")
adjusted_sales_heading = make_statement("adjusted sales and profit", "#")
adjusted_explantion = make_statement(f"we have given away a ticket worth {total_won} which means"
                                     f"\nsales have decreased by {total_won} "
                                     f"\nand our profit decreased by {profit_won}", " ")

# list to output to user / write to file
to_write = [heading_string, "\n",
            ticket_headeing,
            mini_movie_string, "\n",
            total_paid_string,
            total_profit_string, "\n",
            raffle_headding,
            winner_string, "\n",
            adjusted_sales_heading,
            adjusted_explantion, "\n",
            final_total_paid,
            final_total_profit, "\n",
            num_sold_string]
print()
for item in to_write:
    print(item)

file_name = "mmf_ticket_details"
write_to = "{}.txt".format(file_name)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")