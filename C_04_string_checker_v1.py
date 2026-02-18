def string_checker(question, valid_ans_list):
    while True:
        response = input(question).lower()
        for item in valid_ans_list:
            if response == item:
                return item
            elif response == item[0]:
                return item
        print(f"Please choose an option from {valid_ans_list}")


question = string_checker("what day is it", ['mon', 'tue'])

