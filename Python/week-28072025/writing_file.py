with open("data/test_write","w") as file:
    new_file = file.write("This is what i wrote in this file")
    print(new_file)  # prints 0, because write() returns 0