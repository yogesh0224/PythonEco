# balance = 5000
# amount = int(input("enter the amount:"))

# if amount<0:
#     print("invalid amount")
# elif amount>balance:
#     print("insufficinent funds")
# else:
#     balance = balance -amount
#     print("withdrawal successfull")
#     print(f"the remaining balance is {balance}")

num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
num3 = float(input("enter third number:"))


if (num1>=num2) and(num1>=num3):
    largest =num1
elif(num2>=num1) and (num2>=num3):
    largest=num2
else:
    largest =num3

print(f"the largest amongst three number is:{largest}")
 