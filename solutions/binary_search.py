from builtins import len


def doSearch(array, targetValue):
    min = 0
    max = len(array) - 1

    if max < min:
        return -1

    while True:
        guess_index = (max + min) // 2
        guess = array[guess_index]

        if guess > targetValue:
            max = guess_index - 1
        elif guess < targetValue:
            min = guess_index + 1
        else:
            return guess_index


print (doSearch([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], 73))