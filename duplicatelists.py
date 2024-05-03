#Python program to find the duplicates in the three lists and the given python list are list1 [10,501,22,37,100,999,87,351], list2[23. 45, 37, 100, 999, 10, 49, 501] and lists3 [44, 100, 501, 33, 999, 37, 12]

def find_duplicates(list1, list2, list3):
    # Convert lists to sets for faster lookup
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    
    # Find common elements among the three sets
    common_elements = set1.intersection(set2, set3)
    
    return list(common_elements)

# Given lists
list1 = [10, 501, 22, 37, 100, 999, 87, 351]
list2 = [23, 45, 37, 100, 999, 10, 49, 501]
list3 = [44, 100, 501, 33, 999, 37, 12]

# Find duplicates
duplicates = find_duplicates(list1, list2, list3)
print("Duplicates:", duplicates)