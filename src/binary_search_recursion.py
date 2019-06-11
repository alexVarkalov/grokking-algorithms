from typing import Any, Optional


def binary_search_recursion(array: list, element: Any, left: int=0, right: int=None) -> Optional[int]:
    """
    TODO

    Parameters
    ----------
    array: list
        pre-sorted list.
    element: typing.Any
        the element could be any object which has the 
        overloaded magic methods for comparison
    left: int
        left boarder
    right: int
        right boarder
    Returns
    -------
    Optional[int]
        if the searched element is on the array - index of 
        the found element will be returned, otherwise - None.
    """
    if not right:
        right = len(array) - 1
    if left >= right:
        return None

    mid = (right + left) // 2
    guess = array[mid]
    if guess < element:
        left = mid + 1
    elif guess > element:
        right = mid - 1
    else:
        return mid
    return binary_search_recursion(array, element, left, right)


if __name__ == '__main__':
    from random import randint

    my_array = sorted([randint(0, 99) for _ in range(100)])
    print(my_array)
    result = binary_search_recursion(my_array, 8)
    print(result)
