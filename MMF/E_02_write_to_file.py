file_name = "write_experiment"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

heading = "=== MMF TEST ===\n"
content = "random content"
more = "a bit more content"

to_write = [heading, content, more]

for item in to_write:
    print(item)

for item in to_write:
    text_file.write(item)
    text_file.write("\n")