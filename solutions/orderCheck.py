
def countStudents(height):
    right_order = sorted(height)
    count = 0
    for i in range(len(height)):
        if right_order[i] != height[i]:
            count += 1
    return count


print(countStudents([]))