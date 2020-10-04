def perm_missing_element(A):
    leng = len(A)
    if leng == 0:
        return 1
    return sum(range(leng+2)) - sum(A)

print(perm_missing_element([2,3,1,5]))