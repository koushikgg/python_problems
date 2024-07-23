def reverse_number(num):
    reverse = 0
    while (num>0):
        temp=num%10
        reverse= (reverse*10)+temp
        num= num//10
    print(reverse)
    
    
if __name__ == "__main__":
    number = int((input('Enter the number: ')))
    reverse_number(number)