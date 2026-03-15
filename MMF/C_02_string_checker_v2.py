def string_checker(question, valid_ans=('yes', 'no'), num_letters=1):
    while True:
        response = input(question).lower()
        for item in valid_ans:
            if response == item:
                return item
            elif response == item[:num_letters]:
                return item
        print(f"Please choose an option from {valid_ans}")
pay_ans = ['cash', 'credit']
want_instructions = string_checker("do you want to see the instructions? ")
print(f"you chose {want_instructions}")
pay_meth = string_checker("payement method: ", pay_ans, 2)
print(f"you chose {pay_meth}")
