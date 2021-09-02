list = []
indexTotal = int(input("How many numbers? "))
for i in range(indexTotal):
    element = int(input("Enter " + str(indexTotal-len(list)) + " more integers: "))
    list.append(element)
print(list)
listSum = sum(list)
average = listSum/indexTotal
print("Average of " + str(list) + " is " + str(average))