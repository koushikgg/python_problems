def check_odd_even(num):
    if num % 2 == 0:
        return f'{num} is even number'
    else: 
        return f'{num} is odd number'
    
if __name__ == '__main__':
    number = int(input("Enter the  number: "))
    print(check_odd_even(number))