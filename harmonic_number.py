def harmonic_number(n):
    result = 0
    if(n==0):
        return "Enter a valid positive integer"
    for i in range(1, n + 1):
        result += 1 / i
    return f"{result:.2f}"

if __name__ == '__main__':
    num = int(input("Enter the harmonic value: "))
    print(harmonic_number(num))