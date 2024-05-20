#write a program to find if the given number is prime no or not
ddef is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
number = int(input("Enter a number to check if it's prime: "))
if is_prime(number):
    print(f"The number {number} is prime.")
else:
    print(f"The number {number} is not prime.")
