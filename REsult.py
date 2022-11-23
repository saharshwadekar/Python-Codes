english_Marks = int(input("Enter English Marks :"))
maths_Marks = int(input("Enter Maths Marks :"))
physics_Marks = int(input("Enter Physics Marks :"))
chemistry_Marks = int(input("Enter Chemistry Marks :"))
biology_Marks = int(input("Enter Biology Marks :"))

list_sub = [english_Marks,maths_Marks,physics_Marks,chemistry_Marks,biology_Marks]
sub = ["English","Maths","Physics","Chemistry","Biology"]
print("Result: ")
for i in range(len(list_sub)):
    if list_sub[i] < 35:
        print(f"{sub[i]} - Fail")
    else:
        print(f"{sub[i]} - Pass")