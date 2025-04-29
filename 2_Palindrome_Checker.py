def check_alph(lower_txt):
    new_text = ""
    for i in lower_txt:
        if i.isalnum():
            new_text += i
    return new_text

def check_palindrome(lower_txt):
    duplicate_text = check_alph(lower_txt)
    return duplicate_text == duplicate_text[::-1]


text = input("Enter to check if it's palindrome: ")
lower_txt = text.lower()

if check_palindrome(lower_txt):
    print("Yes, it's palindrome")
else:
    print("Sorry, it's not palindrome")