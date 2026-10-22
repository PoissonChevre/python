# fct declaration
def hello():
    name = input("What's your name? ").strip().title() # Ask user for their name
    print(f"hello, {name}") # Say hello to user

hello()

##########################
# autre méthode
def hello2(to):
    print("hello,",to)

name2 = input("What's your name? ")

hello2(name2)

##########################
# autre méthode
def hello3(to="world"):
    print("hello,",to)
hello3()
name3 = input("What's your name? ")
hello3(name3)