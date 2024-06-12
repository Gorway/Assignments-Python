for number in range(1, 101):
    if number <= 1:
        continue
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
            break
    if isPrime:
        print(f"{number} is prime.")
