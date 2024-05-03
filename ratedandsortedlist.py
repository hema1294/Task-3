#Python program to find the minimum element in a rated and sorted list

def find_minimum(sorted_list):
    if not sorted_list:
        return None  # Return None if the list is empty
    else:
        return sorted_list[0]  # Return the first element

# Example usage:
sorted_list = [1, 2, 3, 4, 5]
min_element = find_minimum(sorted_list)
if min_element is not None:
    print("Minimum element:", min_element)
else:
    print("List is empty.")