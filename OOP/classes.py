class car():
    def message(a):
        
        print("This is a car class.")
    @staticmethod
    def salam():
        print("Hello from the car class!")


obj1 = car()
obj1.message()
obj1.salam()
obj2 = obj1
obj2.message()
