import random


def binary_search(array, target):
    low = 0
    mid = 0
    high = len(array) - 1
    while low <= high:
        mid = (high+low) // 2
        # If target is greater, ignore left half
        if array[mid] < target:
            low = mid + 1
        # If target is smaller, ignore right half
        elif array[mid] > target:
            high = mid - 1
        # means x is present at mid
        else:
            return mid
    # If we reach here, then the element was not present
    return -1
# Test array
array = [93, 15, 36, 63, 65, 90, 79, 53, 55, 68, 61, 16, 43, 79, 60, 50, 55, 42, 47, 36, 67, 82, 41, 33, 51, 62, 92, 8, 20, 51, 65, 13, 56, 59, 91, 45, 43, 15, 2, 81, 22, 38, 29, 26, 83, 97, 37, 36, 13, 33, 72, 50, 3, 43, 67, 68, 93, 11, 31, 77, 89, 71, 4, 34, 66, 5, 20, 87, 1, 48, 83, 68, 7, 4, 63, 3, 87, 41, 77, 86, 87, 76, 16, 9, 1, 34, 55, 53, 4, 92, 75, 86, 42, 44, 54, 70, 5, 23, 81, 65]
target = random.randint(1,100)
# Function call
result = binary_search(array, target)
if result != -1:
    print(f"Element '{target}' is present at index {result}")
else:
    print(f"Element '{target}' is not present in array")