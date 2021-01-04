
def countingValleys(steps, path):
    count = 0
    tracker = 0
    for i in path:
        if i == 'U':
            tracker += 1
            if tracker == 0:
                count += 1
        else:
            tracker -= 1
    return count
