text = input("enter a string(enter 'q' for quit): \n")

point = 0
count = 0

while True:

    if text == "q":
        print(" --- EXIT --- ")
        break

    while point < len(text):
        point += 1
        if text[point] == " ":
            count += 1
    else:
        print(point)
        print(count)
        point = 0
        count = 0 

    text = input("enter a string(enter 'q' for quit): \n")

