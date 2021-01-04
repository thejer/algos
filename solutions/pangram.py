def pangram_solution1(s):
    s = s.lower()

    alpha_dict = {"a": 0,
                  "b": 0,
                  "c": 0,
                  "d": 0,
                  "e": 0,
                  "f": 0,
                  "g": 0,
                  "h": 0,
                  "i": 0,
                  "j": 0,
                  "k": 0,
                  "l": 0,
                  "m": 0,
                  "n": 0,
                  "o": 0,
                  "p": 0,
                  "q": 0,
                  "r": 0,
                  "s": 0,
                  "t": 0,
                  "u": 0,
                  "v": 0,
                  "w": 0,
                  "x": 0,
                  "y": 0,
                  "z": 0,
                  }
    for a in s:
        if a in alpha_dict:
            alpha_dict[a] = 1
    if sum(alpha_dict.values()) == 26:
        return "pangram"
    else:
        return "not pangram"


def pangram_solution2(s):
    s = s.lower()
    alpha_set = set()
    for i in s:
        if str(i).isalpha():
            alpha_set.add(i)
            if len(alpha_set) == 26:
                return "pangram"
    return "not pangram"


print(pangram_solution2("We promptly judgedx %antique ivory buckles for the net prize"))
