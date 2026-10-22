def main():
    # print_column(3)
    # print_row(4)
    print_square(2,12)

# def print_column(heigt):
#     for _ in range(heigt):
#         print("#")

# def print_column(heigt):
#     print("#\n" * heigt, end="")

# def print_row(width):
#     print("?" * width)

# def print_square(heigth,width):
#     for i in range(heigth):       # For each row in square
#         for j in range(width):   # For each brick(colonne) in row
#             print("#", end="")
#         print()
        
def print_square(heigth,width):
    for i in range(heigth):
        print_row(width) # print ("#" * width)
            
def print_row(width):
    print("#" * width)

main()

