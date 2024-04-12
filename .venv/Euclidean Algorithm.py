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
