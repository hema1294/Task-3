#Python program to find the first non-repeating element in a given list of integers

def first_non_repeating_element(nums):
    # Create a dictionary to store the count of each element
    count_dict = {}
    
    # Iterate through the list and update the count of each element
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Iterate through the list again to find the first non-repeating element
    for num in nums:
        if count_dict[num] == 1:
            return num
    
    # If no non-repeating element found, return None
    return None

# Example usage:
nums = [1, 2, 3, 4, 5, 6, 1, 3]
result = first_non_repeating_element(nums)
if result is not None:
    print("First non-repeating element:", result)
else:
    print("No non-repeating element found.")