# prime_number_checker.py

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Sample usage
num = int(input("Enter a number: "))
print(f"{num} is a prime number." if is_prime(num) else f"{num} is not a prime number.")
