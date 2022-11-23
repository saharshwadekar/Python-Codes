# i = 1
# sum = 0 
# while i <= 5: 
#     sum += int(input(f"Enter {i} number :"))
#     i += 1
# print("Averge = ",sum/5)


sum = 0
for i in range(1,6):
    sum += int(input(f"Enter {i} number :"))
print(f"Average is {sum/5}")
