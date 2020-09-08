print("f")
'''
1. Sort the array
2. Binary search through the array
 start half way through, check lower & higher and move up or down
 if 20 elements start at 20/2 = element 10 (9)
 if lower start at 10/2             TRUE
 if higher start at 20/2 + 10/2
  if lower start at 5/2 **round up
  if higher start at 10/2 + 5/2 **round down
  // the rounding tries to stick closest to the middle
'''

# ---Recursive Binary Search
# https://www.geeksforgeeks.org/python-program-for-binary-search/


# Returns index of x in arr if present, Else -1
def binary_search(arr, target, low=0, high=None):  # low & high are index locations
    if high is None:
        high = len(arr)

    # check index range is valid
    if high >= low:
        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == target:
            return mid

        # If element is smaller than mid, then it can only be present in left sub-array
        elif arr[mid] > target:
            return binary_search(arr, target, low, mid - 1)

        # Else *If element is larger than mid, then it can only be present in right sub-array
        else:
            return binary_search(arr, target, mid + 1, high)

    else:
        # Element is not present in the array
        return -1

# Test arrays
arr = [2, 3, 4, 10, 40]
x = 10

arr2 = ["amed", "diego", "abaa", "tim", "josh"]  # array is NOT sorted
arr2.sort()  # array IS sorted
x2 = "amed"

# Function calls
result = binary_search(arr, x, 0, len(arr) - 1)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

result2 = binary_search(arr2, x2, 0, len(arr) - 1)
if result2 != -1:
    print("Element is present at index", str(result2))
else:
    print("Element is not present in array")



print("amed" > "abaa")