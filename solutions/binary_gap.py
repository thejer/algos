def binary_gap(number):
    max_val = 0
    bin_number = int_to_bin(number).strip("0")
    val = 0
    for i in bin_number:
        if i == "0":
            val +=1
        elif val > max_val:
            max_val = val
            val = 0
        else:
            val = 0

    print(max_val)


def int_to_bin(i):
    if i == 0:
        return "0"
    bin = ""
    while i:
        if i & 1 == 1:
            bin = "1" + bin
        else:
            bin = "0" + bin
        i //= 2
        print("i", i)
    return bin


binary_gap(37)
