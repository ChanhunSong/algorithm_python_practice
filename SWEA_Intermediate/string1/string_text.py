num = 10000
with open("text_input.txt", "w") as file:
    file.write("1\n")
    file.write("10000 10\n")
    for i in range(num):
        file.write("{}\n".format("A"*num))
    #file.write("World!")
