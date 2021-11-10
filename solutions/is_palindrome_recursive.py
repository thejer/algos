
def isPalindrome(str):
    # base case #1
    if len(str) <= 1:
        return True
    # base case #2
    elif str[0] != str[-1]:
        return False
    elif str[0] == str[-1]:
        return isPalindrome(str[1:-1])
        # recursive case

print(isPalindrome("rotor"))