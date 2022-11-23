def isArmStrongNumber(x):
    return x if x == 0 else isArmStrongNumber(x//10) + ((x%10)**i)

num = int(input("Enter the number :"))
i = len(str(num))
if isArmStrongNumber(num) == num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is not an Armstrong Number")