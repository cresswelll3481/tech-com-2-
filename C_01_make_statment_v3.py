def make_statement(statement, decoration, lines = 1):

    middle = (f"{decoration * 3} {statement} {decoration * 3}")
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

make_statement("hello whats one plus one ", "!", 3)
print()
make_statement("two","=",2)
print()
make_statement("hahahah", "#",)