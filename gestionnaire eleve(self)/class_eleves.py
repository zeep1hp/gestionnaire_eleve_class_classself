class Eleve:
    def __init__(self):
        self.nom = input("Entre un nom\n=>")
        self.classe = input("Entre une classe\n=>")
        self.note_math = []
        self.note_svt = []
        self.note_francais= []
        self.note_histoire= []
        self.note_geographie= []
        self.note_anglais= []


        
    def moyenne_math(self):    
        self.moyenne_math = 0
        if len(self.note_math) > 0:
            self.moyenne_math= sum(self.note_math)/len(self.note_math)
        return self.moyenne_math
        
        
        
    def moyenne_svt(self):
        self.moyenne_svt = 0
        if len(self.note_svt) > 0:
            self.moyenne_svt = sum(self.note_svt)/len(self.note_svt)
        return self.moyenne_svt

        
    def moyenne_francais(self):
        self.moyenne_francais = 0
        if len(self.note_francais) > 0:
            self.moyenne_francais = sum(self.note_francais)/len(self.note_francais)
        return self.moyenne_francais
        
    def moyenne_histoire(self):
        self.moyenne_histoire = 0
        if len(self.note_histoire) > 0:
            self.moyenne_histoire = sum(self.note_histoire)/len(self.note_histoire)
        return self.moyenne_histoire
        
        
    def moyenne_geographie(self):
        self.moyenne_geographie = 0
        if len(self.note_geographie) > 0:
            self.moyenne_geographie = sum(self.note_geographie)/len(self.note_geographie)
        return self.moyenne_geographie
        
        
    def moyenne_anglais(self):
        self.moyenne_anglais = 0
        if len(self.note_anglais) > 0:
            self.moyenne_anglais = sum(self.note_anglais)/len(self.note_anglais)
        return self.moyenne_anglais
    

        #moyenne general
    def moyenne_general(self):
        self.moyenne_g=[self.moyenne_math, self.moyenne_svt, self.moyenne_francais, self.moyenne_histoire, self.moyenne_geographie, self.moyenne_anglais]
        self.moyenne_general = sum(self.moyenne_g)/len(self.moyenne_g)

    def maj_moyenne(self):
        self.moyenne_math()
        self.moyenne_svt()
        self.moyenne_francais()
        self.moyenne_histoire()
        self.moyenne_geographie()
        self.moyenne_anglais()
        self.moyenne_general()
   


