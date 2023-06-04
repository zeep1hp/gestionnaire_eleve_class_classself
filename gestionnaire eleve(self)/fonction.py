import json
from class_eleves import Eleve

def lecture():
    with open("list_elev.json", "r") as f:
        data = json.load(f)
        return data

def sauvegarde():
    with open("list_elev.json", "w") as f:
        json.dump(liste_eleves, f)
        
liste_eleves = lecture()
def retour_menu():
    liste_choix= ["oui", "OUI", "non","NON"]
    x= input("\nVeut tu revenir au menu(oui|non)\n=>")
    while x not in liste_choix:
        x= input("\nVeut tu revenir au menu(oui|non)\n=>")
    if x == "oui" or x == "OUI":
        return True
    elif x == "non" or x == "NON":
        return False

def ajouter_eleves():
    new_eleves = Eleve()
    ne= new_eleves.r_eleve()
    liste_eleves.append(ne)
    print(f"{new_eleves.nom} a bien etait ajouter !")
    sauvegarde()
    z = retour_menu()
    return z

def supprimer_eleves():
    if len(liste_eleves)==0:
        print("la liste des eleves est vide...")
        return None
    x= input("Entre le nom de l'eleve que tu souhaite supprimer:\n=>")
    for element in liste_eleves:
        if x==element['nom']:
            liste_eleves.remove(element)
            print(f"l'eleve {x} a bien était supprimer!")
            sauvegarde()
    z = retour_menu()
    return z



def info_eleves():
    if len(liste_eleves)==0:
        print("la liste des eleves est vide...")
        return None
    x= input("Entre le nom de l'eleve que tu souhaite consulter :\n=>")
    for element in liste_eleves:
        if x==element["nom"]:
            moyenne_math=0
            if len(element['math'])>0:
                moyenne_math=sum(element['math'])/len(element['math'])
            moyenne_svt=0
            if len(element['svt'])>0:
                moyenne_svt=sum(element['svt'])/len(element['svt'])
            moyenne_francais=0
            if len(element['francais'])>0:
                moyenne_francais=sum(element['francais'])/len(element['francais'])
            moyenne_histoire=0
            if len(element['histoire'])>0:
                moyenne_histoire=sum(element['histoire'])/len(element['histoire'])
            moyenne_geographie=0
            if len(element['geographie'])>0:
                moyenne_geographie=sum(element['geographie'])/len(element['geographie'])
            moyenne_sport=0
            if len(element['sport'])>0:
                moyenne_sport=sum(element['sport'])/len(element['sport'])
            moyenne_anglais=0
            if len(element['anglais'])>0:
                moyenne_anglais=sum(element['anglais'])/len(element['anglais'])
            print(f"Nom: {element['nom']}\nClasse: {element['classe']}\nNotes de maths: {element['math']}\nmoyenne math: {moyenne_math}/20\nNotes de svt: {element['svt']}\nmoyenne svt: {moyenne_svt}/20\nNotes de français: {element['francais']}\nmoyenne français: {moyenne_francais}/20\nNotes d'histoire: {element['histoire']}\nmoyenne histoire: {moyenne_histoire}/20\nNotes de géographie: {element['geographie']}\nmoyenne géographie: {moyenne_geographie}/20\nNotes de sport: {element['sport']}\nmoyenne de sport: {moyenne_sport}/20\nNotes d'anglais: {element['anglais']}\nmoyenne anglais: {moyenne_anglais}/20")
            #print("inscrit")
            break
    z = retour_menu()
    return z

def ajouter_une_notes():
    if len(liste_eleves)==0:
        print("la liste des eleves est vide...")
        return None
    x= input("Entre le nom de l'eleve a qui tu souhaite ajouter une note :\n=>")
    for element in liste_eleves:
        if x==element["nom"]:
            y=input("Quel matière ?\n=>")
            if y in element.keys():
                note= input("Entre une note:\n=>")
                verif = note.isdigit()
                while verif is False:
                    note= input("Entre une note:\n=>")
                    verif = note.isdigit()
                note=int(note)
                element[y].append(note)
                print(f"la note de {note} a bien etait ajouté a l'eleve {x} pour le cours de {y}")

                sauvegarde()
    z = retour_menu()
    return z
                
def moyenne_general():
    if len(liste_eleves)==0:
        print("la liste des eleves est vide...")
        return None
    moyenne_g= []
    x= input("Entre le nom de l'eleve au quel tu souhaite consulter la moyenne géneral :\n=>")
    for element in liste_eleves:
        if x == element['nom']:
            moyenne_math=0
            if len(element['math'])>0:
                moyenne_math = sum(element['math'])/len(element['math'])
            moyenne_g.append(moyenne_math)
            moyenne_svt=0
            if len(element['svt'])>0:
                moyenne_svt = sum(element['svt'])/len(element['svt'])
            moyenne_g.append(moyenne_svt)
            moyenne_francais=0
            if len(element['francais'])>0:
                moyenne_francais = sum(element['francais'])/len(element['francais'])
            moyenne_g.append(moyenne_francais)
            moyenne_histoire=0
            if len(element['histoire'])>0:
                moyenne_histoire = sum(element['histoire'])/len(element['histoire'])
            moyenne_g.append(moyenne_histoire)
            moyenne_geographie=0
            if len(element['geographie'])>0:
                moyenne_geographie = sum(element['geographie'])/len(element['geographie'])
            moyenne_g.append(moyenne_geographie)
            moyenne_sport=0
            if len(element['sport'])>0:
                moyenne_sport = sum(element['sport'])/len(element['sport'])
            moyenne_g.append(moyenne_sport)
            moyenne_anglais=0
            if len(element['anglais'])>0:
                moyenne_anglais = sum(element['anglais'])/len(element['anglais'])
            moyenne_g.append(moyenne_anglais)
            moyenne_ge= sum(moyenne_g)/len(moyenne_g)
            print(f"{x} en classe de {element['classe']}ème:\nMoyenne général: {moyenne_ge}/20")
    z = retour_menu()
    return z

def supprimer_une_note():
    if len(liste_eleves)==0:
        print("liste d'élèves vide...")
        return None
    x=input("A quel élève souhaite tu supprimer une note ?\n=>")
    for element in liste_eleves:
        if x == element['nom']:
            y=input("Dans quel matière ?\n=>")
            print(element[y])
            note = input("Quel note souhaite tu supprimer?\n=>")
            verif = note.isdigit()
            while verif is False:
                note = input("Quel note souhaite tu supprimer?\n=>")
                verif = note.isdigit()
            note=int(note)
            element[y].remove(note)
            print(f"la note de {note} a bien était supprimer")
            sauvegarde()

def info_classe():
    x= input("\nQuel classe souhaite tu consulter:\n=>")
    for element in liste_eleves:
        if element['classe'] == x:
            print(f"{element['nom']}") 
        elif element['classe'] == x:
            print(f"{element['nom']}") 
        elif element['classe'] == x:
            print(f"{element['nom']}") 
        elif element['classe'] == x:
            print(f"{element['nom']}")
    z = retour_menu()
    return z
        