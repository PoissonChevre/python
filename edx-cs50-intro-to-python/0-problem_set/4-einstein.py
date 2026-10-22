#!/usr/bin/env python3

# EINSTEIN
# E=mc²
# In a file called einstein.py, implement a program in Python that prompts the user 
# for mass as an integer (in kilograms) and then outputs the equivalent number of Joules
# as an integer. Assume that the user will input an integer.
# HINTS
# Recall that input returns a str, per docs.python.org/3/library/functions.html#input

m=int(input("Enter mass in kg: "))
c=int(3e8)
E=int(m*c**2)
print(f"Equivalent number of Joules: {E}")