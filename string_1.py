
string = input("Enter the string: ")
counter = {}
#store letter occurances
for i in string:
    if not i in counter:
        counter[i] = 1
    else:
        counter[i] = counter[i]+1
print(counter)
#find the most occuring letter:
mostoccuring = ""
maxsofar = 0
for i in counter:
    if counter[i] > maxsofar:
        mostoccuring = i
        maxsofar = counter[i]   
print("most occuring letter is:",mostoccuring)

print("count of the most occurring letter is",maxsofar)
    