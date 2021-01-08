def minimumSwaps(arr):
    dict_elements = dict(enumerate(arr, 1))
    dict_indices = {v: k for k, v in dict_elements.items()}
    count = 0
    for i in dict_elements:
        a = dict_elements[i]
        if a != i:
            b = dict_indices[i]
            dict_elements[b] = a
            dict_indices[a] = b
            count += 1
    return count


smol = [4,3,1,2]

print(minimumSwaps(smol))
