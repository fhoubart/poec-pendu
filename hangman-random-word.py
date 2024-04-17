# Definition des variables ( Mot, nombre d'essais... )

from random_word import RandomWords
generateur = RandomWords()
Essais = 11

# Return a single random word
MotSecret = generateur.get_random_word()

LettresBonnes = []
LettresMauvaises = []

# Définir une fonction qui détermine si le mot est deviné ou non
def leMotEstDevine(mot, lettresBonnes):
    for lettre in mot:
        if not lettre in lettresBonnes:
            return False
        
    return True

# Boucle
while Essais > 0 and not leMotEstDevine(MotSecret, LettresBonnes):
    # afficher les mauvaises lettres
    print("Mauvaises lettres : " + str(LettresMauvaises))
    affichage = ""
    for lettre in MotSecret:
        affichage += "_" + " "
    print(affichage)
    
    # Demander une lettre
    proposition = input("Proposez une lettre : ")

    # Vérifier la lettre :
        # Si elle est bonne l'ajouter dans la liste 'LettresBonnes'
        # Sinon, l'ajouer dans 'lettresMauvaises' et ajouter l'essai à 'Essais' 
    if proposition in MotSecret:
        LettresBonnes.append(proposition)
    else:
        LettresMauvaises.append(proposition) 
        Essais -= 1

# Mettre une ligne vide
    print()

if Essais == 0:
    print("Vous avez perdu. Le nombre d'essais maximum est atteint.")
else:
    print("Bravo! Vous avez trouvé le mot.")
    
