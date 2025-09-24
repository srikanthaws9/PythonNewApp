"""
   This function checks if a number is even or odd.
"""
def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even number"
    else:
        return "Odd number"

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = is_even_or_odd(num)
    print(f"The number {num} is {result}.")