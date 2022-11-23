from numpy import union1d


dict1 = {1:12,2:34,4:33}
dict2 = {1:3,3:30,4:21}

dict4 = {x: dict1.get(x,0) + dict2.get(x,0) for x in set(dict1).union(dict2)}
dict3 = {x:dict1.get(x,0)+dict2.get(x,0) for x in set(dict2).union(dict1)}
print(dict3)
print(dict4)