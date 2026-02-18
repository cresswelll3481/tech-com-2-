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
while True:
    print()
    my_int= int_check("please enter an integer more than zero: ")
    print(f" You choose {my_int}")


