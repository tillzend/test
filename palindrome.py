word = input("enter word: \n")

is_palindrome = bool

if len(word) == "" or len(word) < 3:
    print("empty string or too short word! ")
else:
    is_palindrome = word == word[::-1]

print(is_palindrome)