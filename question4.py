#write a program to find the sum of digits of a given number'
def sum_of_digits(number):
    str_number = str(number)
    total = 0
    for char in str_number:
        total += int(char)
    return totalgit
number = int(input("Enter a number to find the sum of its digits: "))
print(f"The sum of the digits of {number} is {sum_of_digits(number)}.")
