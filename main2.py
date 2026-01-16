#  main = input('Введите что нибудь: ')

#  print (main)

#  print(type(5))
# troub = 1

# print(dir(__builtins__))


# entered_num = input('enter number: ')

# x = int(float(entered_num))

# print (x + 2)
# print (type(x))

# num = bool(None)

# print(num)

# text = float('25.45')

# print(text)

# x = 5

# num = 2 < x + 4 < 10

# print(num)

# x = 2

# if x == 0:
#     print ('wrong number!')
#     x = 1

# print(100/x)


# value = float(input('Value: '))
# part = float(input('How many?: '))

# if value <= 0 or part < 0:
#     print('value cant be 0 or less than 0')

# else:
#     precent = part / value * 100
#     print(round(precent, 2), '%')

# x = 5
# y = 7

# if x >= 0 and y >= 0:
#     print(x * y)

# name = "Alex"
# if name and len(name) > 2:
#     print("Имя непустое и длиннее двух символов")
# x = 5
# if x > 0 and x < 10: # 
#     print("x в диапазоне 1..9")
# a = 10
# b = 0
# if b != 0 and a / b > 1:   # правая часть НЕ выполнится!
#     print("Не будет деления на ноль")

username = ""
user = username or "Гость"   # если пустая строка > "Гость"
print(user)