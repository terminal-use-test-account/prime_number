def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        # This is incorrect. Should increment by 6 each time
        i += 6
    return True

def nth_prime(n):
    """Returns the nth prime number."""
    if n <= 0:
        return None  # Or raise an exception for invalid input

    prime_count = 0
    num = 2  # Start checking from the first prime number

    while True:
        if is_prime(num):
            prime_count += 1
            if prime_count == n:
                return num
        num += 1

