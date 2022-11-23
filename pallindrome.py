
# method 1

# num = input("Enter the number :")
# print(f"{num} is pallindrome") if num == num[::-1] else print(f"{num} is not an pallindrom")

# method 2

# num = int(input("Enter the number : "))
# temp = num
# rev = 0
# while num > 0:
#     ld = num % 10
#     rev = rev*10 + ld
#     num //= 10
# print(f"{temp} is pallindrome") if temp == rev else print(f"{temp} is not an pallindrom")


def isPallindrome(n):
    return 1 if n == n[::-1] else 0

if isPallindrome(input("Enter a number : ")):
    print("yes ",end = "")
else:
    print("no",end = "")
