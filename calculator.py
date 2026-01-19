#Task claculator


print("K.A.L.K.U.L.A.T.O.R")

user_value_first = float(input("enter first value: "))
user_value_second = float(input("enter second value: "))

answer = float

if user_value_first == 0 and user_value_second == 0 :
    print("ERROR: value cannot be alphabetic!")

user_option = input("choose option: (+), (-), (*), (/), (//), (%) ")

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

round_option = input("Do you want to round the value? (yes/no) ")

round_number = 0

if round_option == "yes":
    round_number = int(input("Round to how many decimal places? "))
    print("Result: ", round(answer, round_number))
else:
    print("Result: ", answer)