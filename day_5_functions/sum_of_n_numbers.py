def add(n):
    if n==0:
        return 0
    else :
        return n+add(n-1)
n = int(input("Enter a number: "))
print("The sum of first", n, "numbers is:", add(n))