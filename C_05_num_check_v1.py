
def num_check(question, num_type, exit_code=None):

    if num_type == "integer":
        error = "Please enter a integer more than zero"
        change_to = int
    else:
        error = "Please enter a number more than zero"
        change_to = float
    while True:
        response = input(question).lower()
        if response == exit_code:
            return response
        try:
            response = change_to(response)
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)
while True:
    print()
    my_float = num_check("please enter a number more than zero: ", "float")
    print(f" You choose {my_float}")
    print()
    my_int= num_check("please enter an integer more than zero: ", "integer", "")
    if my_int == "":
        print(f" You choose infinite mode")
    else:
        print(f" You choose {my_int}")
