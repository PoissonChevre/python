students = [
    {"name":"Hermione", "house":"Gryffindor","patronous":"Otter" },
    {"name":"Harry", "house":"Gryffindor","patronous":"Stag" },
    {"name":"Ron", "house":"Gryffindor","patronous":"Jack Russel terrier" },
    {"name":"Draco", "house":"Slytherin","patronous": None },
]

for student in students:
    print(student["name"],student["house"],student["patronous"], sep=", ")
    
