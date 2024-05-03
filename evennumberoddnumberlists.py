#Python program to create two list one with all the even numbers and the other with all odd numbers and the given python list is [10,501,22,37,100,999,87,351]

numbers = [10,501,22,37,100,999,87,351] #Given List

#Initialize empty lists for even and odd numbers
even_numbers = [] 
odd_numbers =[]

# Iterate through the list
for num in numbers:
    if num % 2 == 0:  #Check if the number is even
        even_numbers.append(num) #Add even number to the even_numbers list
    else:
        odd_numbers.append(num)  #Add odd number to the odd_numbers list

# Print the lists
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)