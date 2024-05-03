#Python program to find the sum of the first and last digit of an integer

def sum_of_first_and_last_digit(number):
    # Convert the number to a string to access individual digits
    number_str = str(number)
    
    # Extract the first and last digits
    first_digit = int(number_str[0])
    last_digit = int(number_str[-1])
    
    # Calculate the sum of the first and last digits
    sum_digits = first_digit + last_digit
    
    return sum_digits

# Test the function with an example integer
integer = 123456789
result = sum_of_first_and_last_digit(integer)
print("Sum of first and last digit of", integer, "is:", result)