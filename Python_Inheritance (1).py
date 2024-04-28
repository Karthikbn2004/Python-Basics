class Box:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

class student(Box):
    def __init__(self,name,roll,fees):
        self.fees = fees
        Box.__init__(self,"sreenivas",61)

obj = student("sreenivas",61,30000)
print(obj.name)
print(obj.roll)
print(obj.fees)

