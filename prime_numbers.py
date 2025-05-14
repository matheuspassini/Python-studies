# Script to verify and generate prime numbers using Python generators

def prime_generator(n):
    count = 0
    num = 2
    
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1
      
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input())
prime_gen = prime_generator(n)

for prime_number in prime_gen:
    print(prime_number)