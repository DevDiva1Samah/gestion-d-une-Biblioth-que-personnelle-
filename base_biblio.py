import json

class Library:
    def __init__(self, livres):
        assert isinstance(livres, list) #LIST nom, auteur, publication, type de livre
        self.livres = livres
        self.stockage = {}

    def stocker_livres(self):
        self.stockage['name'] = self.livres[0]
        self.stockage['writer'] = self.livres[1]
        self.stockage['publication'] = self.livres[2]
        self.stockage['type'] = self.livres[3]
        return self.stockage
    
    def emprunter_user(self, name_user, livre, date):
        if livre not in self.stockage:
            print(f"the book  {livre} doesn't exist check later")
        if livre in self.stockage:
            reserved_book = self.stockage.get(livre)
        return f"<<user: {name_user} : {date} : {reserved_book}>>"
    
    def supprimer_livre(self):
        del_book = self.emprunter_user()
        
        



def ajout_livre(name, year, writer, type, publication):
   pass

def lister_livres(livres):
    print(livres)

def recherche_livre(titre, auteur, genre):
    pass

def supprimer_livre():
    pass