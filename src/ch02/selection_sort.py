def find_smallest(array):
    smallest = array[0]
    smallest_index = 0
    for index, elem in enumerate(array):
        if elem < smallest:
            smallest = elem
            smallest_index = index
    return smallest_index


def selection_sort(array):
    new_array = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        new_array.append(array.pop(smallest))
    return new_array


if __name__ == '__main__':
    from random import randint
    my_array = [randint(0, 9) for _ in range(10)]
    print(my_array)
    result = selection_sort(my_array)
    print(result)
