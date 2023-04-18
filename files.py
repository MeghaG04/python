#FILES

file = open("numbers.txt",'r')
lines = file.readlines()
file_to_write = open("even.txt",'w')

for i in lines:
    if int(i)%2==0:
        print(i.strip())
        file_to_write.write(i.strip())
        file_to_write.write("\n")
        



#Context Manager

with open("numbers.txt",'r') as file:
    print(file.readlines())