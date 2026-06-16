import random
devine = random.randint(1, 100)
tentatives = 0

while True:
    choix = int(input("Choisissez un nombre entre 1 et 100 : "))
    tentatives += 1
    if choix == devine:
        print(f"Félicitations ! Vous avez trouvé le nombre en {tentatives} tentatives.")
        break

    