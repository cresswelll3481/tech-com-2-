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
            elif response == item:
                return item
        print(f"Please choose an option from {valid_ans}")
def instructions():
    make_statement("Instructions", "^")
    print('''
    For each ticket holder enter:
    -Name
    -Age
    -Payment (cash or credit

    this program will record the ticket sale and calculate the ticket cost

    once you have either sold all of the tickets or entered all of the 
    exit code "xxx" the program will display the ticket sales info and write it to a text file 

    it will also choose one lucky ticket holder who wins the draw their ticket is free
    ''')

pay_ans = ['cash', 'credit']
want_instructions = string_checker("do you want to see the instructions? ")
print(f"you chose {want_instructions}")
if want_instructions == "yes":
    instructions()
pay_meth = string_checker("payement method: ", pay_ans, 2)
print(f"you chose {pay_meth}")
