# # # write a program to take an input of number 
# # # and print if it is even or odd.

# # num = int(input("enter a number:"))

# # if num % 2 == 0:
# #     print("even")
# # else:
# #     print("odd")


# a = int (input("enter marks 1:"))
# b = int (input("enter marks 2:"))
# c = int (input("enter marks 3:"))

# total = a+b+c
# percentage = (total/300)*100

# print(f"total marks:{total}")
# print(f"percentage:{percentage}")

# if total>200 and percentage>75:
#     print("pass")
# else:
#     print("fail")

# write a program that takes input of two numbers from user 
# and classify if their sum is 50 or not.

a = int(input("take first number:"))
b = int(input("take second number:"))

sum = a+b

if  49<sum<51:
    print("yes the sum is 50")
else:
    print("no the sum is not 50")
