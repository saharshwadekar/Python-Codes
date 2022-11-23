temp = ("hello","goodmorning",12,"python","hello",12)
set = {x for x in temp if temp.count(x) > 1}
print(set)

repeatedItem = {item for item in temp if temp.count(item) > 1}
print(repeatedItem)