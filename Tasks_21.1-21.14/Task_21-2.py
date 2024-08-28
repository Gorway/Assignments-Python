# Write a generator function prime_generator(n) that yields prime numbers up to n. Use this generator to print all prime numbers less than 100.

def prime_generator(n):
  for num in range(2, n):
    isPrime = True
    for i in range(2,int(num ** 0.5) + 1):
      if num % i == 0:
        isPrime = False
        break
    if isPrime:
      yield num

prime_nums = [num for num in prime_generator(100)]
print(prime_nums)