# string = 'a' * 10 
# stuing = 'a' * 9 + 'ы'

# print(string.__sizeof__())
# print(stuing.__sizeof__())

# name = "rahuk user"
# id = 1.2345

# # message = "wasap {n} , your id is : {r:.4f}".format(n=name , r=id)  # //////   OR

# message = f" wasap {name} , your id is : {id:.4f} " # current standart 

# # message = " wasap %s , your id is : %.2f " % (name , id) # OLD STYLE

# print (message)

# //////// EXAMPLE FOR USE .format ///////

# name = "rahuk user"
# id = 1.2345

# message = "wasap {n} , your id is : {r:.3f}"

# message = message.format(n=name , r=id)
# print(message)

'''
prior:
1 - f
2 - .format
'''

#TASK FOR STR #1 

#Условие: Пользователь вводит строку.  
# Если длина строки больше 10 символов — 
# выведите первый и последний символ, 
# иначе — выведите "Строка слишком короткая".

# text = input("Введите строку: \n")

# a = ""
# b = ""

# if len(text) > 10:
#     a = text[0]
#     b = text[10]
#     print(f"Строка длинее 10 символов: {a} {b}")
# else:
#     print('ales good')


#TASK FOR STR #2

#Условие: Пользователь вводит строку.  
# Если строка начинается с буквы "A" или "a" — выведите "Начинается с A", 
# иначе — "Начинается с другой буквы". Можно использовать методы строк.

# text = input("Введите строку: \n")

# if text[0] == "A" or text[0] == "a":
#     print(text)
# else:
#     text = text[1: ]
#     print(text)


#3+

#Условие: Пользователь вводит строку.  
# Если длина строки больше 6 символов и последний символ — "!" 
# выведите "Эмоциональное сообщение", иначе — "Обычное сообщение".


# text = input("Введите сообщение: \n")

# if len(text) > 6 and text.endswith("!") :
#     print ("emotional damage!!")
# else:
#     print('damage')


# text = 'i don\'t want vegetables , Mom!'

# path = 'C:\\Users\\name\\Desktop' # экранирование вин пути 
# при работе с файлами пишем обычный / 

# s = "\U0001F600"

# print(path)