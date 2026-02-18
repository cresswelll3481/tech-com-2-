def int_check(question):
    error = f"Please enter a integer"

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
    name = input("Name: ")
    print(f"Hello {name}")
    age = int_check("age: ")

    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} brought a ticket")