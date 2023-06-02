from class_eleves import Eleve
import json


def lecture():
    with open('eleves.json', 'r') as f:
        data = json.load(f)
        return data
def sauvegarde():
    with open('eleves.json', 'w') as f:
        json.dump(e1, f)

class Etablisement:

    def __init__(self):
        self.liste_eleves = []


    def ajouter_eleves(self):
        ne= Eleve()
        self.liste_eleves.append(ne)
    
    def afficher_liste_eleves(self):
        for i in self.liste_eleves:
            print(f"{i.nom} en classe de {i.classe}")
    
    def afficher_un_eleve(self):
        x=input("Entre le nom de l'élève que tu souhaite consulter\n=>")
        for i in self.liste_eleves:
            if x == i.nom:
                print(f"nom: {i.nom}\nclasse: {i.classe}\nnotes math : {i.note_math}\nmoyenne math : {i.moyenne_math}/20\nnote svt : {i.note_svt}\nmoyenne svt : {i.moyenne_svt}/20\nnotes français : {i.note_francais}\nmoyenne français : {i.moyenne_francais}/20\nnote histoire : {i.note_histoire}\nmoyenne histoire : {i.moyenne_histoire}/20\nnote geographie : {i.note_geographie}\nmoyenne geographie : {i.moyenne_geographie}/20\nnotes anglais : {i.note_anglais}/20\nmoyenne anglais : {i.moyenne_anglais}\nmoyenne général : {i.moyenne_general}/20")
                break
            else:
                print(f"l'élève {x} n'est pas inscrit .")

    def ajouter_une_note(self):
        x=input("Entre le nom de l'élève au quel tu souhaite ajouter une note\n=>")
        y=input("Entre le nom de la matiere\n=>")
        if y == "math":
            for i in self.liste_eleves:
                if x == i.nom:
                    nn=int(input("Entre une note:\n=>"))
                    i.note_math.append(nn)
                    i.maj_moyenne()
                    #sauvegarde()
        
        elif y == "svt":
            for i in self.liste_eleves:
                if x == i.nom:
                    nn=int(input("Entre une note:\n=>"))
                    i.note_svt.append(nn)
                    i.maj_moyenne()
                    #sauvegarde()

        elif y == "francais":
            for i in self.liste_eleves:
                if x == i.nom:
                    nn=int(input("Entre une note:\n=>"))
                    i.note_francais.append(nn)
                    i.maj_moyenne()
                    #sauvegarde()
        
        elif y == "histoire":
            for i in self.liste_eleves:
                if x == i.nom:
                    nn=int(input("Entre une note:\n=>"))
                    i.note_histoire.append(nn)
                    i.maj_moyenne()
                    #sauvegarde()

        elif y == "geographie":
            for i in self.liste_eleves:
                if x == i.nom:
                    nn=int(input("Entre une note:\n=>"))
                    i.note_geographie.append(nn)
                    i.maj_moyenne()
                    #sauvegarde()
        
        elif y == "anglais":
            for i in self.liste_eleves:
                if x == i.nom:
                    nn=int(input("Entre une note:\n=>"))
                    i.note_anglais.append(nn)
                    i.maj_moyenne()
                    #sauvegarde()


e1= Etablisement()
e1.ajouter_eleves()
sauvegarde()
e1.ajouter_une_note()
#e1.afficher_liste_eleves()
e1.afficher_un_eleve()