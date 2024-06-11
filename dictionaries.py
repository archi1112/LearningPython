students={
    "1":"a",
    "2":"b",
    "3":"c"
}

for student in students:
    print(student,students[student])


# printing element using the key 
print(students["1"])
print(students.get("1"))
# prints not found if key does not exists
print(students.get("9","not found"))

keys=[99,100,101]
values=["last second" , "last" , "first"]
new_dict=dict(zip(keys,values))
print(new_dict)