
import heapq


def min_after_removals(bag, m):
    index = {}
    for i in bag:
        if i in index:
            index[i] += 1
        else:
            index[i] = 1
    q = MinHeap()
    for item, count in index.items():
        q.push((count, str(item)))

    for i in range(m) :
        count, item = q.pop()
        if count > 1:
            q.push((count - 1, str(item)))

    return q.size()


class MinHeap:
    def __init__(self):
        self.data = []

    def top(self):
        return self.data[0]

    def push(self, val):
        heapq.heappush(self.data, val)

    def pop(self):
        return heapq.heappop(self.data)

    def size(self):
        return len(self.data)


print(min_after_removals([1, 2, 3, 1, 2, 2, 1], 3))