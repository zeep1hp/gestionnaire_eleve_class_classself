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


def ajouter_eleves():
    new_eleves = Eleve()
    ne= new_eleves.r_eleve()
    liste_eleves.append(ne)
    sauvegarde()

def supprimer_eleves():
    x= input("Entre le nom de l'eleve que tu souhaite supprimer:\n=>")
    for element in liste_eleves:
        if x==element['nom']:
            liste_eleves.remove(element)
            print(f"l'eleve {x} a bien était supprimer!")
            sauvegarde()

def info_eleves():
    x= input("Entre le nom de l'eleve que tu souhaite consulter :\n=>")
    for element in liste_eleves:
        if x==element["nom"]:
            moyenne_math=0
            if len(element['math'])>0:
                moyenne_math=sum(element['math'])/len(element['math'])
            moyenne_svt=0
            if len(element['svt'])>0:
                moyenne_svt=sum(element['svt'])/len(element['svt'])
            print(f"Nom: {element['nom']}\nClasse: {element['classe']}\nNotes de maths: {element['math']}\nmoyenne math: {moyenne_math}/20\nNotes de svt: {element['svt']}\nmoyenne svt: {moyenne_svt}/20")
            #print("inscrit")
            break

def ajouter_une_notes():
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
                
def moyenne_general():
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
            moyenne_ge= sum(moyenne_g)/len(moyenne_g)
            print(f"{x} en classe de {element['classe']}ème:\nMoyenne général: {moyenne_ge}/20")