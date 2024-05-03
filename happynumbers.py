#Python program to identify how many numbers are there in the given python list which are happy numbers and the given python list is [10,501,22,37,100,999,87,351]

# Function to check if a number is a happy number
def is_happy(num):
    seen = set()
    while num != 1:
        num = sum(int(digit) ** 2 for digit in str(num))
        if num in seen:
            return False
        seen.add(num)
    return True

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Initialize variable to count happy numbers
happy_count = 0

# Iterate through the list
for num in numbers:
    if is_happy(num):
        happy_count += 1

# Print the count of happy numbers
print("Total happy numbers:", happy_count)