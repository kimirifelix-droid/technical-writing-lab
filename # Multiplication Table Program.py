# Multiplication Table Program

try:
    # Ask the user to enter a whole number
    number = int(input("Enter a number: "))

    # Initialize the counter
    y = 1

    # Display the table heading
    print("\n" + "-" * 30)
    print(f"Multiplication Table of {number}")
    print("-" * 30)

    # Generate the multiplication table
    while y <= 12:
        result = y * number
        print(f"{y} × {number} = {result}")
        y += 1

    # Display the end of the table
    print("-" * 30)

# Handle invalid input
except ValueError:
    print("Error: Please enter a valid whole number.")

# Handle any other unexpected errors
except Exception as error:
    print("An unexpected error occurred:", error)