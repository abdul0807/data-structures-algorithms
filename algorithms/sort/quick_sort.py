# ********************************************
# Created by Mohammed Abdul Qavi on 19/06/22
# ********************************************


def partition(array, l, r):
    while l < r:
        if array[r] < array[l]:
            array[l], array[r], array[r - 1] = array[r - 1], array[l], array[r]
            r -= 1
        else:
            l += 1
    return r


def quick_sort(array, l, r):
    if l < r:
        m = partition(array, l, r)
        quick_sort(array, l, m - 1)
        quick_sort(array, m + 1, r)


if __name__ == "__main__":
    import random
    random.seed(0)

    # creating a random array
    arr = sorted(range(1000))
    random.shuffle(arr)
    print(arr[:10])

    # quick sorting
    quick_sort(arr, 0, len(arr) - 1)
    print(arr[:10])

"""
Output

[439, 621, 160, 549, 237, 389, 658, 507, 124, 290]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
