import math
def is_prime(x):
    two = 2;
    while two <= math.sqrt(x):
        if x % two == 0: return False
        else: two += 1
    return True

if __name__ == "__main__":
    primes = [result for result in range(1, 50) if is_prime(result)]
    print(primes)