def solution(string):
    acount = 0
    nonacount = 0
    for i in range(len(string)):
        if 0 < i < len(string) - 2:
            if string[i] == 'a' and string[i - 1] == 'a' and string[i + 1] == 'a':
                return -1
        if string[i] == 'a':
            acount += 1
        else:
            nonacount += 1

    return 2 * nonacount + 2 - acount


print(solution('dog'))
