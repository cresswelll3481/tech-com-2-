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

max_tickets = 5
tickets_sold = 0

pay_ans = ('cash', 'credit')
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

    if age < 12:
        print(f"sorry {name} you are too young to watch this movie")
        continue
    elif age > 120:
        print(f"{name} is too old ")
        continue
    else:
        pass
    pay_meth = string_checker("payment method: ", pay_ans, 2)
    print(f"{name} has brought a ticket using {pay_meth}")
    tickets_sold += 1


if tickets_sold == max_tickets:
    print("you have sold all of the tickets")
else:
    print(f"you have sold {tickets_sold} out of {max_tickets} tickets")