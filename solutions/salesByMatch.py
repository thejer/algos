
def sockMerchant(n, ar):
    matches = {}
    count = 0
    for i in ar:
        if i not in matches or matches[i] == 2:
            matches[i] = 1
        elif matches[i] == 1:
            matches[i] = 2
            count += 1
    return count


sockMerchant(9, [10, 20, 20 ,10 ,10 ,30 ,50 ,10,20])