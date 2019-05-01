newDict = {} #create a dictionary (map) that has a unique key and corresponds to a value
while True:
    key = input("What is the name of the customer? ")
    if len(key) > 0: #if string is entered
        value = int(input("enter amount: "))
        if key not in newDict:#check if key exists (does not exist in this case)
            valueList = [value] #set variable = list of values
            newDict[key] = valueList #pair key to value
            print(newDict)
    
        else:#if key already exists
           newDict[key].append(value) #append value to the valueList for key that already exists
           print(newDict)
    else:#breaks out of the loop
        break
            
for key in newDict:#prints out pairing
    print(key," spent ", sum(newDict[key])) #sum() adds the elements of the valueList
