# Road trip planner
# Input variables with data types
road_trip = input("\nWhat is your destination?\n")
total_distance = float(input("Total miles of trip?\n"))
car_mpg = float(input("What is your vehicles mpg?\n"))
gas_price = float(input("What is the current price of gas?\n"))
nights_stayed = int(input("How many night will you be staying?\n"))
hotel_avg_cost = float(input("How much is the hotel per night?\n"))
food_budget = float(input("What is you daily food budget?\n"))

# Calculation of data for output
gas_needed = total_distance / car_mpg
gas_cost = gas_needed * gas_price
hotel_cost = nights_stayed * hotel_avg_cost
food_cost = (nights_stayed + 1) * food_budget
days_stayed = nights_stayed + 1 
grand_total = gas_cost + hotel_cost + food_cost

#output of given data
print("=" * 3, "Road Trip Budget Planner", "=" * 3)
print(f"\nDestination: {road_trip}")
print(f"Distance: {total_distance} miles\n")

print("-" * 3, "Cost Breakdown", "-" * 3)
# output of calculated data
print(f"Gas ({gas_needed:.2f} @ ${gas_price:.2f}): ${gas_cost:.2f}")
print(f"Hotel ({nights_stayed} nights @ ${hotel_avg_cost:.2f}): ${hotel_cost:.2f}")
print(f"Food ({days_stayed} days @ ${food_budget:.2f}): ${food_cost:.2f}")
# Grand total of trip
print("-" * 40)
print(f"Estimated Total: ${grand_total:.2f}")
