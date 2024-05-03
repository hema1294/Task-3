#Python program to find if there is a sub list with sum equal to 0 with given list [4, 2, -3, 1, 6]

def has_sublist_with_zero_sum(nums):
    # Dictionary to store cumulative sum and its index
    cumulative_sum = {0: -1}
    current_sum = 0
    
    for index, num in enumerate(nums):
        current_sum += num
        
        # If current_sum is already in the dictionary, a sublist with sum 0 exists
        if current_sum in cumulative_sum:
            return True
        
        # Store the cumulative sum and its index
        cumulative_sum[current_sum] = index
    
    # If no sublist with sum 0 is found
    return False

# Example usage with given list
nums = [4, 2, -3, 1, 6]
if has_sublist_with_zero_sum(nums):
    print("Sublist with sum 0 exists.")
else:
    print("No sublist with sum 0 exists.")