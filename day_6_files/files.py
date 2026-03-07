'''
f = open("data.txt")
data= f.readline()
print(data,type(data))
print (" IT will print all data in the file a written")
f = open("data.txt")
data= f.read()
print(data,type(data))

f.close()


print (" \nIT will print all data in the file and show it form\n")
f = open("data.txt")
data= f.readlines()
print(data,type(data))

f.close()

print ("\n IT will print only one by one line depend on how many times we run the program:\n")
f = open("data.txt")
data= f.readline()
print(data,type(data))
f.close()
'''

'''
f = open("data.txt")
line1= f.readline()
print(line1)
# f.close()


# f = open("data.txt")
line2= f.readline()
print(line2)
# f.close()


# f = open("data.txt")
line3= f.readline()
print(line3)
# f.close()


# f = open("data.txt")
line4= f.readline()
print(line4,type(line4))
f.close()

'''
f = open("data.txt")
line= f.readline()
print(line)
while ( line!=""):
      print(line)
      line= f.readline()
f.close()