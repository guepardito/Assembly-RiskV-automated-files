import sys
import random


args = sys.argv #arg introduced in console:    aleatorio.py {hexadecimal numbers in .byte}
n = int(args[1]) #arg parsed to int

name = input("Give the name of the file to create: ") #input the file name
file_name = name + ".txt"
file = open(file_name, "w") #create the file or rewrite it

arr = [] #array with random hexadecimals on it
count = 0 #counter in while
j = 1 #iterator 



#create the hex number
while count < n:
    ran = random.randrange(10**80)
    hex = "%064x" % ran

    #limit string to 8 characters
    hex = hex[:8]
    arr.append("0x" + hex)

    count += 1

#write the body
file.write(".text\n\n\n\n.data\n.byte ")

#append the hex nums
for i in arr:
    if j == len(arr):
        file.write(i)
    else:
        file.write(i + ", ")
    j += 1
