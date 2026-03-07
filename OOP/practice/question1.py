class programmer:
    company = "Microsoft"
    def __init__(self, name , salary , pin):
        self.name = name
        self.salary = salary 
        

p= programmer("Rabail", 100000, 1234)
print(p.name)
print(p.salary)
print(p.company)