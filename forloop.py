#list1 = ['a','b','c','d','e']
#for i in list1:
 #   print(i)
#name = 'python'
#for i in name:
 #   print(i)
 
 #nested loop
numbers = []
for i in range(1,101):
    numbers.append(i)
print(numbers)
even = []
for j in numbers:
    if j % 2 == 0:
        even.append(j)
print(even)