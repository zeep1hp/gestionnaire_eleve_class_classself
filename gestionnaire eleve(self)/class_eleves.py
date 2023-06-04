class Eleve:
    
    def __init__(self):
        self.nom= input("Entre le nom de l'eleve\n=>")
        self.classe= input("En quel classe est-il ?\n=>")
        self.note_math=[]
        self.note_svt=[]
        self.note_francais=[]
        self.note_histoire=[]
        self.note_geographie=[]
        self.note_sport=[]
        self.note_anglais=[]
        
        
        
    def r_eleve(self):
        nom= self.nom
        classe= self.classe
        note_math= self.note_math
        note_svt= self.note_svt
        note_francais= self.note_francais
        note_histoire= self.note_histoire
        note_geographie= self.note_geographie
        note_sport= self.note_sport
        note_anglais= self.note_anglais
        
    
        dico_eleve={
            "nom": nom,
            "classe": classe,
            "math": note_math,
            "svt": note_svt,
            "francais": note_francais,
            "histoire": note_histoire,
            "geographie": note_geographie,
            "sport": note_sport,
            "anglais": note_anglais
               
        }
        return dico_eleve



