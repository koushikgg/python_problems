def perfect_number(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum == num :
        print("it is perfect number")
    else:
        print("it is not perfect number")

number= 28

perfect_number(number)