
import random
abc = 0

def heapify(arr, n, i):
    global abc
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        abc = abc + 1
        # Heapify the root.
        heapify(arr, n, largest)


def heapSort(arr):
    global abc
    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        abc += 1
        heapify(arr, i, 0)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    abc = 0
    arr = []
    # minA = []
    # maxA = []

    abc_arr = []
    for i in range(1, 300):
        arr = []
        abc = 0
        for j in range(1, 1000):
            arr.append(random.randrange(0, 1000))
        heapSort(arr)
        abc_arr.append(abc)

    print(sum(abc_arr)/len(abc_arr))
    print(min(abc_arr))
    print(max(abc_arr))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
