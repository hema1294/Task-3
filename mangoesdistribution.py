#Python program given a list of N integers  which represents the number of Mangoes in a bag. Each bag has a variable number of Mangoes. There are M students in a Guvi class,
# task is distribute the Mangoes in such a way that each student gets one bag. The difference between the number of Mangoes in a bag with maximum Mangoes and bag with minimum Mangoes given to the student is minimum

def distribute_mangoes(mangoes, students):
    mangoes.sort()  # Sort the list of mangoes
    bags_per_student = len(mangoes) // students  # Calculate bags per student
    remaining_bags = len(mangoes) % students  # Calculate remaining bags

    distribution = [[] for _ in range(students)]  # Initialize distribution list for each student
    bag_index = 0

    # Distribute mangoes to students
    for student in range(students):
        for _ in range(bags_per_student):
            distribution[student].append(mangoes[bag_index])
            bag_index += 1

        # Distribute remaining bags evenly
        if remaining_bags > 0:
            distribution[student].append(mangoes[bag_index])
            bag_index += 1
            remaining_bags -= 1

    return distribution

# Example usage
mangoes = [3, 7, 2, 8, 4, 5]
students = 3
distribution = distribute_mangoes(mangoes, students)
print("Distribution of mangoes:")
for i, bags in enumerate(distribution):
    print(f"Student {i+1}: {bags}")