def avgTempOfWeekend(dict):
    sum = 0
    for value in dict.values():
        sum += value
    return sum/len(dict)

dict = {"sun":30,"mon":30,"tue":30,"wed":30,"thus":30,"fri":30,"sat":30}
print("Average of temperature of This weekend is ",avgTempOfWeekend(dict))