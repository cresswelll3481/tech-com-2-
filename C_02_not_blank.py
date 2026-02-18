def not_blank(question):

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. please try again. \n")

name = not_blank("please enter your name: ")
print(f"Hello {name}")
