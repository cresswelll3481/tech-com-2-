import math

def rounding_up(amount, round_val):
    return int(math.ceil(amount / round_val) * round_val)

while True:
    quantity = int(input(" num of items: "))
    expenses = float(input("expenses: "))
    target = float(input("profit goal: "))
    round_to = int(input("Rounding to: "))

    selling_price = (expenses + target) / quantity
    price_rec = rounding_up(selling_price, round_to)
    print(f"minimum price: ${selling_price:.2f}")
    print(f"suggested price: ${price_rec:.2f}")
    print()