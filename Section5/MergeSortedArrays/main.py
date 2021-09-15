# Merge sorted arrays


def merge_sorted_arrays(left_array, right_array):
    left_index = 0
    right_index = 0
    merged_array = []
    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            merged_array.append(left_array[left_index])
            left_index += 1
        else:
            merged_array.append(right_array[right_index])
            right_index += 1
    while left_index < len(left_array):
        merged_array.append(left_array[left_index])
        left_index += 1
    while right_index < len(right_array):
        merged_array.append(right_array[right_index])
        right_index += 1
    return merged_array


left = input("Enter the first sorted array with elements separated by space ")
right = input("Enter the second sorted array with elements separated by space ")
if len(left) > 0 and len(right) > 0:
    first_array = left.split(" ")
    second_array = right.split(" ")
    print(merge_sorted_arrays([int(i) for i in first_array], [int(i) for i in second_array]))
elif len(left) == 0 and len(right) > 0:
    print(right.split(" "))
elif len(right) == 0 and len(left) > 0:
    print(left.split(" "))
