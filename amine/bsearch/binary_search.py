"""
@File    :   binary_search.py
@Time    :   2024/8/15 16:28
@Author  :   LinLi6
@Desc    :   

@usage   :
    
"""
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursion(nums: List[int], target: int) -> int:
    return _binary_search_recursion(nums, 0, len(nums) - 1, target)


def _binary_search_recursion(nums: List[int], low: int, high: int, target: int) -> int:
    if low > high:
        return -1

    mid = low + int((high - low) >> 2)
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return _binary_search_recursion(nums, mid + 1, high, target)
    else:
        return _binary_search_recursion(nums, low, mid - 1, target)
