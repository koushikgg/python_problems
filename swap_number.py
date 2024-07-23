def swap(a, b):
    a,b = b,a
    return a, b

if __name__ == '__main__':
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    
    num1, num2 = swap(num1, num2)
    print(f' first number = {num1} & second number = {num2}')
