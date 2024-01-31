class A():  
     def __init__(self):  
         self.A=1  
         self.B=2  
obj=A()  
obj2 =A()
testdict = {}
testdict[len(testdict)+1] = obj.__dict__

for i in range(4):
     obj = A()
     testdict[len(testdict)+1] = obj.__dict__

for o in testdict.items():
     print(o)


print(type(testdict))