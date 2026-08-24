# num1 = float(input("enter first number:"))
# num2 = float(input("enter second number:"))

# if num1>num2:
#     print(f"{num1} is greater than {num2}")
#     print(f"{num2} is smaller than {num1}")

# if num>num1:
#     print


# python program that takes a year as input and
# checks wheather it is a leap year or not.
#-----Rule-----
# 1. a years is a leap year if it is divisible by 4
# 2. but if the year is divisible by 100, it it not a leap ywear
# 3. however, if the year is also divisble by 400 then it is a le ap year

year =int(input("enter a year:"))

if (year%4 ==0 and year %100 !=0) or (year %400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")