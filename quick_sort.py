def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)


def partition(array, l, r):
    key = array[r]
    i = l
    for j in range(l, r):
        if array[j] <= key:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[r] = array[r], array[i]
    return i


if __name__ == "__main__":
    a = [1, 21, 3, 4, 5, 21, 7, 8]
    quick_sort(a, 0, len(a) - 1)
    print(a)
