students ={
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

for student in students: # iterate the keys
    print(student)
    
for student in students: # iterate all
    print(student, students[student], sep=",")
    