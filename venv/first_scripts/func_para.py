from functools import reduce

# Recursive function to calculate factorial
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Using reduce to calculate factorial in a functional way
def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

# Function to get user input in a functional manner
def get_positive_integer():
    try:
        number = int(input("Enter a positive integer: "))
        if number < 0:
            raise ValueError("Please enter a non-negative integer.")
        return number
    except ValueError as e:
        print(e)
        return get_positive_integer()  # Recursively prompt again on invalid input

# Main function to calculate factorial and display it
def main():
    # Get user input
    number = get_positive_integer()

    # Calculate factorial using both approaches
    fact_recursive = factorial_recursive(number)
    fact_reduce = factorial_reduce(number)

    # Display results
    print(f"Factorial (recursive) of {number} is: {fact_recursive}")
    print(f"Factorial (reduce) of {number} is: {fact_reduce}")

# Entry point of the script
if __name__ == "__main__":
    main()

