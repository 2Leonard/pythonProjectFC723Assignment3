class EuclideanAlgorithm:
    def __init__(self, a, b):
        # Initialize the EuclideanAlgorithm with two positive integers a and b
        self.a = a
        self.b = b

    def gcd_compute(self):
        # Compute the greatest common divisor of two integers using the Euclidean algorithm
        while self.b != 0:  # Consist running until b becomes 0
            temp = self.b  # Create a temporary variable to hold the value of b
            self.b = self.a % self.b  # Update b to the remainder of a divided by b
            self.a = temp  # Update a to the former value of b
        return self.a  # Return a as gcd when b is 0

def get_input():
    # Get two positive integers from the users
    try:
        # Validates if the inputs are positive integers
        a = int(input("Enter the first positive integer: "))
        b = int(input("Enter the second positive integer: "))
        # Raise an error if entered negative number
        if a <= 0 or b <= 0:
            raise ValueError("Please enter a positive integer")
        # Return tuple containing two integers (a, b) if valid
        return a, b
    except ValueError as e:
        print(f"Invalid input: {e}")
        # Return tuple (None, None) if entered invalid
        return None, None


# Main execution part to calculate the gcd
a, b = get_input()
if a and b:
    gcd = EuclideanAlgorithm(a, b)
    print(f"GCD is {gcd.gcd_compute()}")
