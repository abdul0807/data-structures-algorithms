# ********************************************
# Created by Mohammed Abdul Qavi on 18/06/22
# ********************************************


def bubble_sort(array):
    count = 0
    for j in range(1, len(array)):
        for i in range(1, len(array)):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
            count += 1

    return array


if __name__ == "__main__":
    import random
    random.seed(0)

    # creating random array
    arr = [i for i in range(1000)]
    random.shuffle(arr)
    print(arr[:10])

    # bubble sorting
    result = bubble_sort(arr)
    print(result[:10])

"""
Output

[342, 471, 929, 100, 543, 231, 154, 450, 721, 788]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
