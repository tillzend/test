
while True:

    index = 0
    count = 0   

    text = input("enter a string(enter 'q' for quit): \n")

    if text == "q":
        print(" --- EXIT --- ")
        break

    while index < len(text):
        
        if text[index] == " ":
            count += 1

        index += 1

    count_wrd = count + 1
    print("words : ", count_wrd )


# Вариант с методом .count

# while True:
#     text = input("enter a string(enter 'q' for quit): \n")

#     if text == "q":
#         print(" --- EXIT --- ")
#         break

#     spaces = text.count(" ")
    
#     count_wrd = spaces + 1
#     print("words : ", count_wrd)