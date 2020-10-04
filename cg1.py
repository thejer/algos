message = input()

leng = len(message)

if leng % 2 == 0:
    print("Error")
else:
    for i in range(int(leng / 2)):
        message = message.replace(message[i], " ")
        message = message.replace(message[-(i+1)], " ")
        print(message)
