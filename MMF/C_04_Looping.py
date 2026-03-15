max_tickets = 5
tickets_sold = 0

while tickets_sold < max_tickets:
    name = input("Name: ")
    if name == "xxx":
        break
    tickets_sold += 1
if tickets_sold == max_tickets:
    print("you have sold all of the tickets")
else:
    print(f"you have sold {tickets_sold} out of {max_tickets} tickets")