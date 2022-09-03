import random

# Naive Search scan entire list and ask if its equal to the target
import time


def naive_search(l, target):
    # l = [1, 3, 5, 10]
    for i in range(len(l)):
        if l[i] == target:
            return i
        return -1


# Binary Search use divide and conquer
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    # l = [1, 3, 5, 10 ,15]
    midpt = (low + high) // 2  # 2

    if l[midpt] == target:
        return midpt
    elif l[midpt] > target:
        return binary_search(l, target, low, midpt - 1)
    else:  # l[midpt] < target
        return binary_search(l, target, midpt + 1, high)


length = 10000
sorted_list = set()
while len(sorted_list) < length:
    sorted_list.add(random.randint(-3 * length, 3 * length))
sorted_list = sorted(list(sorted_list))

start = time.time()
for target in sorted_list:
    naive_search(sorted_list, target)
end = time.time()
print(f'Naive search time: {(end - start) / length} seconds')  # each iteration on avg

start = time.time()
for target in sorted_list:
    binary_search(sorted_list, target)
end = time.time()
print(f'Binary search time: {(end - start) / length} seconds')  # each iteration on avg
