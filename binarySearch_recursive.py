# Returns index of x in arr if present, else -1
def binary_search(arr, left, right, x):
    # Check base case
    if right >= left:

        mid = (right + left) // 2

        if arr[mid] == x:  # If element is present at the middle itself
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, left, mid - 1, x)

        else:  # Else the element can only be present in right subarray
            return binary_search(arr, mid + 1, right, x)

    else:
        # Element is not present in the array
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10


# Function call
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
