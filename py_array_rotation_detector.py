# Write a Python function that takes two lists (arrays) as parameters and determines 
# if the second list is a rotation of the first list (left or right).

# A rotation means that the elements are shifted circularly. 
# For example, shifting [1, 2, 3] to the right by one position results in [3, 1, 2].

# The function must return True if arr2 is a rotation of arr1, and False otherwise.
# If the arrays have different lengths, they cannot be rotations of each other.
# Two empty arrays are considered rotations of each other.

# EXAMPLES
# array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]) -> True

# array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]) -> True

# array_rotation_detector([1, 2, 3], [3, 2, 1]) -> False

# array_rotation_detector([1, 2], [1, 2, 3]) -> False

# array_rotation_detector([], []) -> True

def py_array_detector(arr1, arr2) -> bool:
    if len(arr1) != len(arr2):
        return False

    if  not arr1 and not arr2:
        return True

    value = arr1[0]

    for i in range(len(arr2)):
        if arr2[i] == value:
            rotation = arr2[i:] + arr2[:i]
            break
    
    if arr1 == rotation:
        return True

    return False


if __name__ == "__main__":
    result1 = py_array_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3])
    result2 = py_array_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4])
    result3 = py_array_detector([1, 2, 3], [3, 2, 1])
    result4 = py_array_detector([1, 2], [1, 2, 3])
    result5 = py_array_detector([], [])
    
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)