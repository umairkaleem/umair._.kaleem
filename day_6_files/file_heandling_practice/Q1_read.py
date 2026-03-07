'''
a = open("poem.txt")
poem= a.read()
print(poem)
a.close()

b = "written by: John Doe"

a = open("poem.txt", "a")
a.write("\n"+ b)
a.close()

a = open("poem.txt")
print (a.read())
'''

# with open("poem.txt") as a:
#     poem = a.readlines()

#     poem = poem[:-1]
# with open("poem.txt") as b:
#     b.writelines(poem)


with open("poem.txt") as a:
    poem = a.readlines()

poem = poem[:-1]  # remove last line

with open("poem.txt", "w") as b:
    b.writelines(poem)  # correctly write trimmed lines
with open("poem.txt") as b:
    print(b.read())  # print the updated content

