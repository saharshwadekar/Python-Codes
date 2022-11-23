def subMarsks(sub):
    return int(input(f"Enter {sub} Marks out of 35 :"))
subjects = ['EC&ES','EP-II','CS-II','AM-II','PSP']
result = {x:subMarsks(x) for x in subjects}
for m in result.keys():
    if result[m] > 18:
        print(f"{m} - Pass")
    else:
        print(f"{m} - Fail")
