def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
           return  "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no.\n")


