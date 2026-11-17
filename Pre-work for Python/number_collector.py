try:
    Number_1 = int(input(f"Enter first number: \n"))
except ValueError:
    print("Invalid input. Using 0 as placeholder")
    Number_1 = 0


try:
    Number_2 = int(input(f"\nEnter second number: "))
except ValueError:
    print("Invalid input. Using 0 as placeholder")
    Number_2 = 0


try:
    Number_3 = int(input(f"\nEnter third number: "))
except ValueError:
    print("Invalid input. Using 0 as placeholder")
    Number_3 = 0


numbers = Number_1, Number_2, Number_3
numbers_sum = Number_1 + Number_2 + Number_3
numbers_avg = numbers_sum / 3



print(f"\nYour numbers are: {numbers}")
print(f"Sum: {numbers_sum}")
print(f"Average: {numbers_avg:.2f}")