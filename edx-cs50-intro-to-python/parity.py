# x = int(input("What's x? "))

# #parite
# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
    
# parité dans une fonction
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
        
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    
# pythonesque
def is_even(n):
    # return True if n % 2 == 0 else False
    return n % 2 == 0

main()
    
    
    