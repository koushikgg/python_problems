def largest_number(a, b, c):
    """finds the largest number among three numbers
    """
    if b < a > c:
        return f"{a} is largest"
    elif a < b > c:
        return f"{b} is largest"
    else: 
        return f"{c} is largest"

if __name__ == '__main__':
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    number3 = int(input("Enter third number: "))

    print(largest_number(number1, number2, number3))