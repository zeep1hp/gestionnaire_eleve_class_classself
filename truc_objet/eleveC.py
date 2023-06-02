class Eleve:
    
    def __init__(self):
        self.nom= input("Entre le nom de l'eleve\n=>")
        self.classe= input("En quel classe est-il ?\n=>")
        self.note_math=[]
        self.note_svt=[]
        
    def r_eleve(self):
        nom= self.nom
        classe= self.classe
        note_math= self.note_math
        note_svt= self.note_svt
    
        dico_eleve={
            "nom": nom,
            "classe": classe,
            "math": note_math,
            "svt": note_svt
        }
        return dico_eleve