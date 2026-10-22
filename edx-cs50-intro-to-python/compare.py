x=int(input("What's x? "))
y=int(input("What's y? "))

#bad design
# if x < y:
#     print("x is less than y")
# if x > y:
#     print("x is greater than y")
# if x == y:
#     print("x is equal to y")
    
#better design elif-else
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
    
#good design
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
    
#best design
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")