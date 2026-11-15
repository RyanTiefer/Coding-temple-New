# My First Python Program
# This Prints a personal introduction

first_name = "Maria"
last_name = "Garcia"
age = 28
city = "Denver"
favorite_language = "Python"


print("=" * 40) # Prints a line of 40 equal signs
print("Personal Introduction")
print("=" * 40)

# output for user info
print("\nName:", first_name, last_name)

print("Age:", age)

print("City:", city)

print("Favorite Language:", favorite_language)

print("=" * 40)

# Maria Garcia is 28 years old and lives in Denver

# F strings let you embed variables directly in text
print(f"{first_name} {last_name} is {age} years old and lives in {city}")


