from typing import Any, Optional


def binary_search(array: list, element: Any) -> Optional[int]:
    """
    Search the element in sorted list. If the element is in the array,
    the index of the found element will be returned, else - None.
    The algorithm takes the middle element from the array and compare
    it with the searched element. If the element is bigger than the
    middle element, for the reason that the array was sorted, the left
    half of the array is not the place where searched value could be.
    The left border index will be equal to the index of the middle
    element plus one. Otherwise, if the element is less than the middle
    element, the right half of the array is not the place where the
    searched value can be. The right border will be equal to the index
    of the middle element minus one. The comparison will continue until
    the searched element will be found, or the left border will be
    bigger or equal to the right border.

    Parameters
    ----------
    array: list
        pre-sorted list.
    element: typing.Any
        the element could be any object which has the 
        overloaded magic methods for comparison

    Returns
    -------
    Optional[int]
        if the searched element is on the array - index of 
        the found element will be returned, otherwise - None.
    """
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (right + left) // 2
        guess = array[mid]
        if guess < element:
            left = mid + 1
        elif guess > element:
            right = mid - 1
        else:
            return mid
    return None


if __name__ == '__main__':
    from random import randint

    my_array = sorted([randint(0, 99) for _ in range(100)])
    print(my_array)
    result = binary_search(my_array, 8)
    print(result)
