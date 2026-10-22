
# SOURCE https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@744dad66fcce478a92fb1073b3d373fa/block-v1:HarvardX+CS50P+Python+type@vertical+block@50897469e09545f29c4535c6ffb2c704

# demande à l'utilisateur son nom
name=input("What's your name? ")
# demande à l'utilisateur son âge
age=input("What's your age? ")
#say hello to the user
print(f"hello, {name} {age} ans") # print hello, world
print()
print("Hello")
print(name)
print(age+" ans") 
print()
print("hello, " + name + " " + age + " ans") # concatenation
print()
print("hello,",name,age,"ans")
print()
print("type name",type(name))
print()
#print{f"type age {type(age)})
################################
# Ask user for their name
name=input("What's your name?")

print("hello,",end="???") # default value end=\n
print(name)
################################

print('hello, "friend"')
print("hello, \"friend\"")
print(f"hello, {name}, {age} ans")

################################

# Remove whitespace from str
name = name.strip()

#Capitalize user's name , first letter
name = name.capitalize()
print(f"hello, {name}, {age} ans")

#Capitalize user's name 
name = name.title()
print(f"hello, {name}, {age} ans")

# Remove whitespace and Capitalize user's name 
name = name.strip().title()
print(f"hello, {name}, {age} ans")

# Ask user for their name + remove whitspace+ capitalization
name=input("What's your name?").strip().title()
print(f"hello, {name}, {age} ans")

# Ask user for their name + remove whitspace+ capitalization + separate last name first name
name=input("What's your name? ").strip().title()

#Split user's name into first name and last name
first, last = name.split(" ")
print(f"hello, {last}, {age} ans")




