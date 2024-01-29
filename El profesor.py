import random

Liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
l = int(input("Entrez une valeur pour l: "))

print("l*l=?")
if l * l == l + 1 or l * l == l - 1:
    while l * l != l * l:
        print("Presque")
elif l * l == l:
    print("Bravo! C'est bien ça!")
else:
    print("Faux")
