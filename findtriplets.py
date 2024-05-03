#Python program to find the triplet in the list whose sum is equal to the given value with given list [10, 20, 30, 9] and given value = 59

def find_triplets(nums, target):
    triplets = []
    nums.sort()  # Sort the list to simplify the search
    
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target:
                triplets.append((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return triplets

# Example usage with given list and value
nums = [10, 20, 30, 9]
target = 59
triplets = find_triplets(nums, target)

if triplets:
    print("Triplets with sum equal to", target, ":", triplets)
else:
    print("No triplets found with sum equal to", target)