def calculate_leap_year(year):
    
    if year>=1582:
            #checking the year is leap year or not
        if (year%400==0):
            print(f"The year {year} is a leap year")
        elif (year%4==0)and(year%100!=0):
            print(f"The year {year} is a leap year")
        else:
            print(f"The year {year} is not a leap year")
    else:
        print(f"Invalid year {year}  Please Enter year must be 1582 or later")
    
if __name__ == '__main__':
    year = int(input("Enter a year: "))
    calculate_leap_year(year)