word = input("enter word : \n")

is_palindrome = bool

pal_size = len(word)
pal_size_t = int

if len(word) == "" or len(word) < 3:
    print("empty string or too short word! ")
else:
    if pal_size % 2 == 0:
        pal_size_t = pal_size / 2
        pal_size_partside = pal_size_t -1
    else:
        
