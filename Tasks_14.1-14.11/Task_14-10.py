def isPalindome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return isPalindome(string[1:-1])

    return False

user_input = input("Еnter a word to check if it is a palindrome: ")

if isPalindome(user_input):
    print(f"{user_input} is palindrome.")
else:
    print(f"{user_input} is not polindrome.")

