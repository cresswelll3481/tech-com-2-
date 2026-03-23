import pandas
import random

all_names = ['a', 'b', 'c', 'd', 'e']
all_tickets = [7.50, 7.50, 10.50, 10.50, 6.50]
all_surcharges = [0, 0, 0.5, 0.53, 0]

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_tickets,
    'Surcharge': all_surcharges
}

mini_movie_frame = pandas.DataFrame(mini_movie_dict)

mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

#prints stats
print(mini_movie_frame.to_string(index=False))
winner = random.choice(all_names)
winner_index = all_names.index(winner)
print("winner", winner, "list position", winner_index)
winner_ticket_price = all_tickets[winner_index]
winner_surcharge = all_surcharges[winner_index]

total_won = winner_ticket_price + winner_surcharge
print(f"The lucky winner is {winner}. Their ticket worth ${total_won:.2f} is free!")