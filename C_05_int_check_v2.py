def num_check(question,low,high):
    error = f"Please enter a integer between {low} and {high}"

    while True:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)
while True:
    print()
    my_int= num_check("please enter an integer more than zero: ", 1, 10)
    print(f" You choose {my_int}")
