from typing import List


def bubble_sort(a: List[int]):
    """
    Bubble sort algorithm.
    :param a:
    :return:
    """
    length = len(a)
    if length <= 1:
        return
    for i in range(length):
        swapped = False
        for j in range(length - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break


def bubble_sort_without_optimization(a: List[int]):
    """
    Bubble sort without optimization
    :param a:
    :return:
    """
    length = len(a)
    if length <= 1:
        return
    for i in range(length):
        for j in range(length - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return


def selection_sort(a: List[int]):
    """
    Selection sort algorithm.
    :param a:
    :return:
    """
    length = len(a)
    if length <= 1:
        return

    for i in range(length):
        min_index = i
        min_value = a[i]
        for j in range(i, length):
            if a[j] < min_value:
                min_index = j
                min_value = a[j]
        a[i], a[min_index] = a[min_index], a[i]


def insertion_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return

    for i in range(1, length):
        value = a[i]
        j = i - 1
        while j >= 0 and value < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value


def merge_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return


def _merge_sort(a: List[int], low: int, high: int):
    if high < low:
        mid = low + (high - low) // 2
        _merge_sort(a, low, mid)
        _merge_sort(a, mid + 1, high)
        _merge(a, low, mid, high)


def _merge(a, low, mid, high):
    i, j = low, mid + 1
    tem = []
    while i <= mid and j <= high:
        if a[i] < a[j]:
            tem.append(a[i])
            i += 1
        else:
            tem.append(a[j])
            j += 1
    start = i if i <= mid else low
    end = j if j <= mid else high
    tem.extend(a[start:end + 1])
    a[low:high + 1] = tem


def test_bubble_sort():
    test_aay = [1, 1, 1, 1]
    bubble_sort(test_aay)
    assert test_aay == [1, 1, 1, 1]
    test_aay = [4, 1, 2, 3]
    bubble_sort(test_aay)
    assert test_aay == [1, 2, 3, 4]
    test_aay = [4, 3, 2, 1]
    bubble_sort(test_aay)
    assert test_aay == [1, 2, 3, 4]


def test_insertion_sort():
    test_aay = [1, 1, 1, 1]
    insertion_sort(test_aay)
    assert test_aay == [1, 1, 1, 1]
    test_aay = [4, 1, 2, 3]
    insertion_sort(test_aay)
    assert test_aay == [1, 2, 3, 4]
    test_aay = [4, 3, 2, 1]
    insertion_sort(test_aay)
    assert test_aay == [1, 2, 3, 4]


def test_selection_sort():
    test_aay = [1, 1, 1, 1]
    selection_sort(test_aay)
    assert test_aay == [1, 1, 1, 1]
    test_aay = [4, 1, 2, 3]
    selection_sort(test_aay)
    assert test_aay == [1, 2, 3, 4]
    test_aay = [4, 3, 2, 1]
    selection_sort(test_aay)
    assert test_aay == [1, 2, 3, 4]


if __name__ == "__main__":
    aay = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    bubble_sort(aay)
    print(aay)

    aay = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    insertion_sort(aay)
    print(aay)

    aay = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    selection_sort(aay)
    print(aay)

    test_bubble_sort()
    test_selection_sort()
    test_insertion_sort()
