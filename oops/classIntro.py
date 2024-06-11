"""
Topics covered :
1.Class
2.Object
3.two methods of initialising object
4.__init__ method - constructor
5.self and cls variable (class and instance variable)
6.comparing two object attributes
7.decorators - @class and @staticmethod


Size of object depends on the number of variables in class
Constructor allocates the memory to object


"""

class Doctor:
# variables defined in side class are class variables
    occupation="Role - doctor"
    def __init__ (self):
        # variables defined inside init are instance variables
        self.name="kyra"
        print("this is default constructor")
    

    def config(self):
        print("Doctor")


    def compare(self,other):
        if self.name==other.name:
            return True
        else:
            return False
    
    # pass - it is used to leave the class empty and avoid error for empty class

        """Use cls while working with class variables and use decorator classmethod """
    @classmethod
    def getOccupation(cls):
        return cls.occupation
    
    @staticmethod
    def getInfo():
        print("Got the job")


d = Doctor()
# 2ways of calling the Doctor class  
Doctor.config(d)
d.config()
d.name="kyra"
print(d.name)
# address of object d
print(id(d))

# creating second object
d2=Doctor()
d2.config()


# comparing two objects
if d.compare(d2):
    print("They are same")
else:
    print("not same")

# we can access the class variables using the class name itself no object needed
print(Doctor.occupation)
#  by default object gets the class variable access too
print(d2.occupation)

