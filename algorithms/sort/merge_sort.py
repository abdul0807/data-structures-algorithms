# ********************************************
# Created by Mohammed Abdul Qavi on 18/06/22
# ********************************************


def merge(array, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = array[l + i]

    for i in range(n2):
        R[i] = array[m + i + 1]

    lid = 0
    rid = 0
    aid = l

    while lid < len(L) and rid < len(R):
        if L[lid] <= R[rid]:
            array[aid] = L[lid]
            lid += 1
        else:
            array[aid] = R[rid]
            rid += 1
        aid += 1

    while lid < n1:
        array[aid] = L[lid]
        lid += 1
        aid += 1

    while rid < n2:
        array[aid] = R[rid]
        rid += 1
        aid += 1


def merge_sort(array, l, r):
    if l < r:
        m = l + (r - l) // 2

        merge_sort(array, l, m)
        merge_sort(array, m + 1, r)
        merge(array, l, m, r)


if __name__ == "__main__":
    import random
    random.seed(0)

    # creating random array
    arr = sorted(range(1000))
    random.shuffle(arr)
    print(arr[:10])

    # merge sorting
    merge_sort(arr, 0, len(arr) - 1)
    print(arr[:10])

"""
Output

[439, 621, 160, 549, 237, 389, 658, 507, 124, 290]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
