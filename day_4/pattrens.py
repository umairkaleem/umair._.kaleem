# simpleprinting of stars + end=""use 

# for i in range (1,6):
#     print ("*"* (i+2) ,end="")

'''
# rectangle printing
n = int (input("enter rows to print rectangle: "))
for i in range (1,n+1):
    print ("&"* (n))  # Print rectangle pattern
    for j in range (1,n+1):
        print("]", end="")
    print("")
'''

'''
rows =int (input ("enter number of rows to print :"))
column =int (input ("enter number of column to print :"))
for i in range (rows):
    for j in range (column):
        print ("*",end="")
    print("")  # Print space after each star
'''



'''
# paramid printting

n = int (input("enter rows to print peramids: "))
for i in range (1,n+1):
   
    print (" " * (n-i) ,end="")
    print("*" * (2 * i - 1), end="")
    print("")

print(f"Pattern of {n} rows is printed above.")
 # print (" " * (n - i) + "*" * (2 * i - 1))  # Print spaces and stars for pyramid pattern
'''

# n = int (input("enter rows to print peramids: "))
# for i in range (1,n+1):
#     print (" " * ((n+1)/2)-i ,end="")
#     print("*" * (2 * i - 1), end="")
#     print("")

# n = int(input("Enter number of rows: "))
# n=9
# stars = 1
# for i in range(n):
#     spaces = ((2 * n + 3) - stars) // 2  # Adjust spacing to center the stars
#     print(" " * spaces + "*" * stars)
#     stars += 4


'''
33+1/2=17
17-1=16


'''
n = int(input("Enter number of rows: "))
stars = 1

for i in range(n):
    max_stars = 1 + (n - 1) * 4  # Largest number of stars in the last row
    spaces = (max_stars - stars) // 2
    print(" " * spaces + "*" * stars)
    stars += 4
