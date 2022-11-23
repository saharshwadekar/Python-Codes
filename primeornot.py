# num = int(input("Enter the number :"))

# for i in range(2,num):
#     if num%i == 0:
#         flag = 0
#         break
#     else:
#         flag = 1
# if flag :
#     print("Prime number")
# else:
#     print("Not an Prime number")

def primeno(num,i):
    if i <= 1:
        return 1
    elif num%i == 0:
        return 0
    else:
        primeno(num,i-1)
    
num = int(input("Enter a number :"))
if primeno(num,num//2):
    print("yes")
else:
    print("no")