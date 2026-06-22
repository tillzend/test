
while True:

    index = 0
    count = 0

    text = input("enter a string(enter 'q' for quit): \n")

    if text == "q":
        print(" --- EXIT --- ")
        break

    while index < len(text):

        current_symbol = text[index]

        if current_symbol == " ":
            count += 1

        index += 1

    count_wrd = count + 1
    print("words : ", count_wrd )


    