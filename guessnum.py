import random
cache = random.randint(1, 1000)
essai = 0
print("listez le nombre entre 1 et 1000 ")
trouve = False

while not trouve:
    nombre = int(input("Entrez un nombre : "))
    essais += 1
    
if nombre < cache:
        print("Le nombre secret est plus grand.")
elif nombre > cache:
        print("Le nombre secret est plus petit.")
else:
        print("Bravo ! Vous avez trouvé le nombre.")
