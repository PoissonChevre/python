#!/usr/bin/env python3

chaine = "Ceci est une Chaine de CARACTERES"
resultat = ""

for caractere in chaine:
    if caractere.isupper():
        resultat += caractere

print(resultat)