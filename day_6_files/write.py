info = input ("Enter your information: ")
f = open("write.txt","w")
# f.write(info)
# f.close()

# print(f.readlines())info = input("Enter your information: ")

# Write to the file
with open("write.txt", "w") as f:
    f.write(info)

# Read from the same file
with open("write.txt", "r") as f:
    print(f.readlines())