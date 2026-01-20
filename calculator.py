#Task claculator


print("K.A.L.K.U.L.A.T.O.R")

user_value_first = float(input("enter first value: "))        # request values
user_value_second = float(input("enter second value: "))


answer = 0 
round_number = 0
round_option = str


if user_value_first == 0 or user_value_second == 0 : # check if any value equal zero
    print("ERROR: value cannot be zero!")
else:
    user_option = input("choose option: (+), (-), (*), (/), (//), (%) ")
    round_option = input("Do you want to round the value? (yes/no) ")

    if user_option == "+":
        answer = user_value_first + user_value_second 

    elif user_option == "-":
        answer = user_value_first - user_value_second

    elif user_option == "*":
        answer = user_value_first * user_value_second

    elif user_option == "/":
        answer = user_value_first / user_value_second

    elif user_option == "//":
        answer = user_value_first // user_value_second

    elif user_option == "%":
       answer = user_value_first % user_value_second

    if round_option == "yes" or round_option == "y":
        round_number = int(input("Round to how many decimal places? "))
        print("Result: ", round(answer, round_number))
    else:

        print("Result: ", answer)
