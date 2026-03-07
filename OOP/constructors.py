class employee():
    section= "ooo"
    salary = 1000
    def department(self):
        print (f"My department is {self.section}")
    def __init__(self,section,salary):
        self.section = section
        self.salary = salary
        # print (f"Ali,s salaty is {self.salary}")
        # print (f"Ali,s salaty is {self.section}")
        print ("my name is umair kaleem")




# main
umair = employee("IT", 1000)
umair.department()
print (umair.salary,umair.section)