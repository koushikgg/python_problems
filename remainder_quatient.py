# 6. Program to Compute Quotient and Remainder

def quotient_remainder(number, divisor):
    if (divisor == 0):
        return "Error: divisor cannot be 0 please enter valid divisor"
    remainder = number % divisor
    quotient = number // divisor
    return remainder, quotient 

if __name__ == "__main__":
    number = int(input("Enter the number: "))
    divisor = int(input("Enter the divisor: "))
    remainder,quotient =quotient_remainder(number, divisor)
    print(f'the number {number} remainder is {remainder} and divisor is {quotient}')