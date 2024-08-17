"""
@File    :   binary_search_variants.py
@Time    :   2024/8/16 9:55
@Author  :   LinLi6
@Desc    :   

@usage   :
    
"""
from typing import List


def binary_search_left(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if low < len(nums) and nums[low] == target:
        return low
    else:
        return -1


def binary_search_right(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    if high >= 0 and nums[high] == target:
        return high
    else:
        return -1


def binary_search_left_not_less(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    if high >= 0 and nums[high] <= target:
        return high
    else:
        return -1


def binary_search_right_not_greater(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    if high >= 0 and nums[high] <= target:
        return high
    else:
        return -1


if __name__ == "__main__":
    a = [1, 1, 2, 3, 4, 6, 7, 7, 7, 7, 10, 22]

    print(binary_search_left(a, 0) == -1)
    print(binary_search_left(a, 7) == 6)
    print(binary_search_left(a, 30) == -1)

    print(binary_search_right(a, 0) == -1)
    print(binary_search_right(a, 7) == 9)
    print(binary_search_right(a, 30) == -1)

    print(binary_search_left_not_less(a, 0) == 0)
    print(binary_search_left_not_less(a, 5) == 5)
    print(binary_search_left_not_less(a, 30) == -1)

    print(binary_search_right_not_greater(a, 0) == -1)
    print(binary_search_right_not_greater(a, 6) == 5)
    print(binary_search_right_not_greater(a, 30) == 11)
