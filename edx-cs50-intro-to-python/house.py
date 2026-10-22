name = input("What's your name? ").strip().capitalize()

#first design 
# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermione":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who ?")

# better
# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who ?")
    
# the best match
# match name: 
#     case "Harry":
#         print("Gryffindor")
#     case "Hermione":
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")
        
 # amélioration match
match name: 
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

    
        
    