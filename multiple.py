num= int(input(" enter a number:"))

if num %2 == 0 and num % 3 == 0:
    print(f"{num}the number is mulitple of both 2 and 3")
elif num%2 ==0:
    print(f"{num}the number is mulitple of  by 2")
elif num %3 == 0:
    print(f"{num}the number is mulitple of  by 3")
else:
    print(f"{num} is not mulitple of any 2 or 3")