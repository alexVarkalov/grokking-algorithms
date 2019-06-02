def selection_sort(array: list) -> None:
    """
    A sorting array via the selection algorithm. Finds the minimum
    element in the whole array and swaps the minimum element with
    the first element. Then finds the minimum element in the subarray
    that is the whole array without the first element and swaps
    found element with the second. And so on till the end of the array.

    Parameters
    ----------
    array: list
        the list whose elements could be compared with each other.
    """
    array_length = len(array)
    for i in range(array_length):
        smallest_index = i
        for j in range(i, array_length):
            if array[j] < array[smallest_index]:
                smallest_index = j
        tmp = array[i]
        array[i] = array[smallest_index]
        array[smallest_index] = tmp


if __name__ == '__main__':
    from random import randint
    my_array = [randint(0, 9) for _ in range(20)]
    print(my_array)
    selection_sort(my_array)
    print(my_array)
