x = int (input("What's x? ").strip())
y = float(input("What's y? ").strip())
#z = int(x) + int(y) # if not int() print like a string 53 ??? !!! concatanation +
z=round(x+y)

print(x+y) # float l'emporte sur int
print(z)   # round
print(f"{z}")
print(f"{z:,}") # us notation 1,000
print(f"{z:,.3f}") # us notation 1,000
y = 7
z = round(x / y, 2)
print(z)

z = x / y
print(f"{z:.3f}") # float .00