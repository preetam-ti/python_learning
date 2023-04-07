def selection_sort(nums):
    # This value of i corresponds to how many values were sorted
    for i in range(len(nums)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


# Verify it works
random_list_of_nums = [12, 8, 3, 20, 11]
selection_sort(random_list_of_nums)
print(random_list_of_nums)

"""
Time Complexity
We can easily get the time complexity by examining the for loops in the Selection Sort algorithm. For a list with n elements, the outer loop iterates n times.

The inner loop iterate n-1 when i is equal to 1, and then n-2 as i is equal to 2 and so forth.
The amount of comparisons are (n - 1) + (n - 2) + ... + 1, which gives Selection Sort a time complexity of O(n^2).

"""