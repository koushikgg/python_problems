def power_of_two(num):
    if(0<= num <31):
        for i in range (num+1):
            print (f'2**{i} = {2**i}')
    else:
        print("enter value b/w 0-31")
    
if __name__ == '__main__':
    power = int(input("Enter the power value: "))
    power_of_two(power)