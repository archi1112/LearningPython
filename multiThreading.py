from threading import Thread
from time import sleep

class Doctor(Thread):
    def run(self):
        for i in range(5):
            print("Doctor treats" , end=" ")
            sleep(1)
        

class Patient(Thread):
    def run(self):
        for i in range(5):
            print("Patient",end="\n")
            sleep(1)
        

d=Doctor()
p=Patient()
d.start()
sleep(0.2)
p.start()

# let d and p get joined/completed then execute next thread
d.join()
p.join()

print("Patients get recovered")