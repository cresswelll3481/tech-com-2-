def string_checker(question, valid_ans_list, num_letters):
    while True:
        response = input(question).lower()
        for item in valid_ans_list:
            if response == item:
                return item
            elif response == item[:num_letters]:
                return item
        print(f"Please choose an option from {valid_ans_list}")

day_list = ['monday', 'tuesday', 'wednesday']
date_list = ['1st', '2nd', '3rd']
question = string_checker("what day is it ", day_list, 9)
question_two = string_checker("whats the date ", date_list,3)
print(f"its {question} the {question_two}")

