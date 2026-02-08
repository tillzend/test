word = "level"

is_palindrome = bool


if len(word) == "" or len(word) < 3:
    print("empty string or too short word! ")
else:
    if word[0] == word[4] and word[1] == word[3]:
        is_palindrome = True
    else:
        is_palindrome = False

print(is_palindrome)