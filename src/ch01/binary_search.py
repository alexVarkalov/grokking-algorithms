def binary_search(array, elem):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (right + left) // 2
        guess = array[mid]
        if guess < elem:
            left = mid + 1
        elif guess > elem:
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


