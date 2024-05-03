#Python program to count all the prime numbers and create a new python list which will contain all the prime numbers in the list and the given python list is [10,501,22,37,100,999,87,351]

numbers = [10,501,22,37,100,999,87,351] #Given List

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Initialize variables to count prime numbers and create a list for prime numbers
prime_count = 0
prime_list = []

# Iterate through the list
for num in numbers:
    if is_prime(num):
        prime_count += 1
        prime_list.append(num)

# Print the count and the list of prime numbers
print("Total prime numbers:", prime_count)
print("List of prime numbers:", prime_list)