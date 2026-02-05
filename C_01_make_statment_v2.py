def make_statment(statment, decoration, lines):

    middle = (f"{decoration * 3} {statment} {decoration * 3}")
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)
    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)

make_statment("hello whats one plus one ", "!", 3)
print()
make_statment("two","=",2)
print()
make_statment(" hahahah", "#", 1)