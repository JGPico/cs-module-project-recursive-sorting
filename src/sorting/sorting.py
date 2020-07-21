# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    aIndex, bIndex, = 0, 0
    while aIndex < len(arrA) and bIndex < len(arrB):
        if arrA[aIndex] <= arrB[bIndex]:
            merged_arr[aIndex + bIndex] = arrA[aIndex]
            aIndex += 1
        else:
            merged_arr[aIndex + bIndex] = arrB[bIndex]
            bIndex += 1

    while aIndex < len(arrA):
        merged_arr[aIndex + bIndex] = arrA[aIndex]
        aIndex += 1

    while bIndex < len(arrB):
        merged_arr[aIndex + bIndex] = arrB[bIndex]
        bIndex += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here

    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(left, right)
    else:
        return arr

    # split each element into partitions of size 1

    # recursively merge adjacent partitions

    # copy elements back to original array (use merge function)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
