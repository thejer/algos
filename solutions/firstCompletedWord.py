def firstRepeatedWord():
    sentence = "He had,had;quite enough of- this:nonsense."
    sentence = sentence.replace(",", " ")
    sentence = sentence.replace(":", " ")
    sentence = sentence.replace(";", " ")
    sentence = sentence.replace("-", " ")
    sentence = sentence.replace(".", " ")
    arr = sentence.split(" ")
    wordset= set()
    for word in arr:
        leng = len(wordset)
        if word.strip() != "":
            wordset.add(word)
            if leng == len(wordset):
                return word

print(firstRepeatedWord())