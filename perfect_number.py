def perfect_number(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum == num :
        print("it is perfect number")
    else:
        print("it is not perfect number")

if __name__ == "__main__":

    number = int((input('Enter the number: ')))
    perfect_number(number)