class car():
    color="red"
    mode="automatic"
    def farari(a):
        color ="blue"
        print(f"This is a {color} with {a.mode}  car class.")
class bugati(car):
    def fun(self):
        print ("i'm second class ")
obj1 = car()
obj1.farari()
obj2 = bugati()
obj2.fun()
obj2.farari()