def find_palindromes(string, i, j, palindromes_set):
    while i >= 0 and j < len(string) and string[i] == string[j]:
        palindrome = string[i: j + 1]
        if len(palindrome) >= 3:
            palindromes_set.append(palindrome)
        i -= 1
        j += 1


def threatDetector(textMessages):
    for textMessage in textMessages:
        palindromes_set = []
        symbol = textMessage[-3:]
        message = textMessage[:-3]
        if not message.isalnum():
            print(symbol, "Ignore")
        else:
            for pivot in range(len(message)):
                find_palindromes(textMessage, pivot, pivot, palindromes_set)
                find_palindromes(textMessage, pivot, pivot + 1, palindromes_set)

            if len(palindromes_set) < 2:
                print(symbol, "Ignore")
            else:
                score = 0
                for palindrome in palindromes_set:
                    score += len(palindrome)
                if score in range(1, 11):
                    print(symbol, "Possible")
                elif score in range(11, 41):
                    print(symbol, "Probable")
                elif score in range(41, 151):
                    print(symbol, "Escalate")
                else:
                    print(symbol, "Ignore")


threatDetector("xxxxxxbzzzzzzIVV")