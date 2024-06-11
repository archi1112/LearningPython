#Super class (parent class)
class A:
    def __init__(self):
        print("In constructor of super class")
    def featureA1(self):
        print("feature a1")
        
    def featureA2(self):
        print("feature a2")

# Sub class(child class)
class B(A):
    def __init__(self):
        # to call the constructor of super class 
        super().__init__()
        print("In constructor of sub class")
    def featureB1(self):
        print("feature b1")
        
    def featureB2(self):
        print("feature b2")
        

class C(B):
    def __init__(self):
        super().__init__()
        print("Implementing multilevel inheritance , C is inherited from A and B ")
           
 
    #  constructor of parent class (A) gets invoked  
objA = A()

# constructor of sub class (B) gets invoked  
obj=B()

# using sub class object we can call method of parent class
# but we cannot invoke sub class method using the parent class object
obj.featureA1()

objC=C()



        


        