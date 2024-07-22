def prime_number(num):
    for i in range(2,num):
        if num%i==0:
            return f'{num} is not prime number'
    return f'{num} is prime number'

number = int((input('Enter the number: ')))
print(prime_number(number))