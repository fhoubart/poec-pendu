import random
print("Bienvenue dans le Jeu du Pendu 💀")

#Correction en bas

mots = ["chat", "chien", "maison", "voiture", "ordinateur", "banane", "orange", "table", "chaise", "livre", "téléphone", "poche", "porte", "chaise"]

motAtrouver = random.choice(mots)
nombreEssais = 0
motTrouvé = ""
nombreEssaisMax = 6 
lettresDevinées = []
lettresFausses = []


while nombreEssais < nombreEssaisMax and motAtrouver != motTrouvé:
    motAffiché = ""
    print(f"Il reste {nombreEssaisMax - nombreEssais} essai(s)")


    for lettre in motAtrouver:
        if lettre in lettresDevinées:
            motAffiché += lettre + ""
        else:
            motAffiché += "_"
    print(motAffiché)
    lettreProposée = input("Choisissez une lettre : ")


    if lettreProposée in motAtrouver:
        lettresDevinées.append(lettreProposée)
        print(f"✅ {lettreProposée}")
        motTrouvé = "".join(lettre if lettre in lettresDevinées else "_" for lettre in motAtrouver)
    else:
        nombreEssais += 1
        lettresFausses.append(lettreProposée)
        print(f"❌ {lettreProposée}")

if motAtrouver == motTrouvé:
    print(f"Félicitations ! Vous avez deviné {motAtrouver}")
else:
    print("Désolé, vous avez épuisé tous les essais. Le mot à trouver était :", motAtrouver)




#Correction 
mot = input('Choisis un mot: ')

nombreEssais = 5
bonnesLettres = []
mauvaisesLettres = []

#Ajout de la 1ère et dernière lettre aux lettres trouvées 
bonnesLettres.append(mot[0])
bonnesLettres.append(mot (len(mot) - 1))

def leMotEstDevine(mot, bonnesLettres):
    for lettre in mot: 
        if not lettre in bonnesLettres: 
            return False 
    return True

while nombreEssais > 0 and not leMotEstDevine(mot, bonnesLettres): 

    #Affichage d'une lettre si elle a été devinée et sinon d'un _
    for lettre in mot: 
        if lettre in bonnesLettres: 
            print(lettre, end = " ")
        else:
            print("_", end = " ")
    
    tentativeLettre = input("Saisissez une lettre: ")
    if tentativeLettre in mot: 
        bonnesLettres.append(tentativeLettre)
    else: 
        nombreEssais -= 1
        mauvaisesLettres.append(tentativeLettre)
    
    print("Vos mauvaises lettres: " + str(mauvaisesLettres))
    print("Il vous reste " + str(nombreEssais) + " essais")

if leMotEstDevine(mot, bonnesLettres):
    print("Félicitations, vous avez gagné!")
else: 
    print("Vous avez perdu")