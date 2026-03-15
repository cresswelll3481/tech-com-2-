
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
pay_ans = ('cash', 'credit')
while True:
    print()
    name = not_blank("Name: ")
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
    print(f"{name} has brought a ticket using {pay_meth}")