#write a program to find the maximum of two numbers
def max_of_two_numbers(a, b):
    if a > b:
        return a
    else:
        return b
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

maximum = max_of_two_numbers(num1, num2)
print(f"The maximum of {num1} and {num2} is {maximum}.")
