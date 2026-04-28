def not_blank(question):

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. please try again. \n")
def num_check(question, num_type="float", exit_code=None):

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


# noinspection PyUnreachableCode
while True:
    product_name = not_blank("Product Name: ")
    if product_name == "xxx":
        break
    else:
        continue
    quantity_made = num_check("quantity being made: ", "integer")
    print(f"you are making {quantity_made} {product_name}")
    print()