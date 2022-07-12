# ********************************************
# Created by Mohammed Abdul Qavi on 12/07/22
# ********************************************

# Cycle sort is an in-place sorting algorithm and optimal in terms of the total number of writes to the original array


def cycle_sort(nums):
    writes = 0
    N = len(nums)

    for cycle_start in range(N - 1):
        item = nums[cycle_start]

        pos = cycle_start
        for i in range(cycle_start + 1, N):
            if nums[i] < item:
                pos += 1

        if pos == cycle_start:
            continue

        while nums[pos] == item:
            pos += 1

        item, nums[pos] = nums[pos], item
        writes += 1

        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, N):
                if nums[i] < item:
                    pos += 1

            while nums[pos] == item:
                pos += 1

            item, nums[pos] = nums[pos], item
            writes += 1

    return writes


if __name__ == "__main__":
    nums = [5, 4, 3, 2, 1, 4]
    print("the total number of writes is {}".format(cycle_sort(nums)))
    print("the new array is {}".format(nums))

"""
Output

the total number of writes is 5
the new array is [1, 2, 3, 4, 4, 5]

"""