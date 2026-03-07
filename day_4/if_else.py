'''
marks =int(input(f"enter your marks: "))
if (marks >= 90):
 print ("grade = A ")
elif (marks >= 80): 
    print("grade = B")
elif (marks >= 70):
    print("grade = C")
elif (marks >= 60):
    print("grade = D")
elif (marks >= 50):
    print("grade = E")
else:
    print("grade = F")
      
      '''


n1 = int(input ("enter number one : "))
n2 = int (input ("enter number two :"))
n3 = int (input ("enter number three :"))
n4 = int(input ("enter number four :"))
if (n1 > n2)and (n1 > n3) and (n1 > n4):        
    print(f"n1 is greater",n1)
elif (n2 > n1) and (n2 > n3) and (n2 > n4):
    print("n2 is greater"+ n2)
elif (n3 > n1) and (n3 > n2) and (n3 > n4):
    print("n3 is greater" +n4)
elif (n4 > n1) and (n4 > n2) and (n4 > n3):
    print("n4 is greater"+ n4)
else:
    print("all numbers are equal or invalid input")    


