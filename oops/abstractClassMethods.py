"""
An abstract class can never be instantiated
    
"""
# library used to make class abstract
from abc import ABC , abstractmethod
class Hospital(ABC):
    @abstractmethod
    def hideMethod(self):
        pass
    
class Doctor(Hospital):
    # implement all the abstract method present in parent class 
    def hideMethod(self):
        print("Concept of abstract classes")
    

d=Doctor()
d.hideMethod()


