
def checkMagazine(magazine, note):
    mag_dict = {}
    for i in magazine:
        if i in mag_dict:
            mag_dict[i] += 1
        else:
            mag_dict[i] = 1

    for word in note:
        if word not in mag_dict or mag_dict[word] == 0:
            print("No")
            return
        else:
            mag_dict[word] -= 1
    print("Yes")


checkMagazine("give me one night".split(" "), "give one grand today".split(" "))