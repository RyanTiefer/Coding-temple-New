# Snippet 1
#print("The answer is: " + 42)
#Error will be a TypeError
print(f"The answer is: {42}") #fix added the print to an f-string 


# Snippet 2
#favorite = input("Favorite number: ")
#result = favorite + 10
#print(result)
#Error will be a TypeError
favorite = input("Favorite number: ")
result = int(favorite) + 10
print(result)# fix is to add int in the result variable and wrap the favorite variable so it runs first. 

# Snippet 3
#print("Hello World)
#Error will be a SyntaxError      
print("Hello World") #fix is to add " at the end to parse the code.

# Snippet 4
#age = int("twenty-five")
#Error will be a ValueError
try:
    age = int("twenty-five")
except ValueError:
    print("Could not convert that to a number. Please try again.") # Fix is to use Try/Except to revert to user back and put the number not the text.
    
    # Snippet 5
#print(username)
#Error is a NameError
user_name = "Ryan"
print(user_name) # Fix is to make username a variable and print the variable could also use input to ask user for name and print that with try/except involved

