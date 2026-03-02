"""
Fibonacci Series Program
Author: Deep (Aspiring Data Analyst)
Description:
This program prints the Fibonacci series up to n terms using a loop.
It also explains the time complexity (Big-O).
"""

def fibonacci(n):
    """
    Function to generate Fibonacci series up to n terms
    """
    a, b = 0, 1
    series = []

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series


def main():
    print("Fibonacci Series Generator")
    print("---------------------------")

    n = int(input("Enter number of terms: "))

    if n <= 0:
        print("Please enter a positive number.")
        return

    result = fibonacci(n)

    print("\nFibonacci Series:")
    for num in result:
        print(num, end=" ")

    print("\n\nBig-O Complexity Analysis")
    print("Time Complexity: O(n)")
    print("Space Complexity: O(n)")


if __name__ == "__main__":
    main()