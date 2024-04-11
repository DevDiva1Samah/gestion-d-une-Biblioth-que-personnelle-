import numpy as np #calcul inputs and outputs statistics

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
        self.livre = livre
        if livre not in self.stockage:
            print(f"the book  {livre} doesn't exist check later")
        if livre in self.stockage:
            reserved_book = self.stockage.get(livre)
            data = [name_user, date, reserved_book]
        return data 
    
    def supprimer_livre(self):
        if self.livre in self.stockage:
            self.stockage.pop(self.livre)

    def ajouter_livre(self, new_book):
        if not isinstance(new_book, list):
            raise TypeError
        self.stockage.update({"name": new_book[0]})
        self.stockage.update({"writer": new_book[1]})
        self.stockage.update({"publication": new_book[2]})
        self.stockage.update({"type": new_book[2]})
        return self.stockage
    

class Livre:

    def __init__(self, namee, typee, schreiber):
        self.namee = namee
        self.typee = typee
        self.schreiber = schreiber

    def book_description(self):
        f"{self.namee}-{self.typee}-{self.schreiber}"

#ajouter un fonction qui calcule des données statistiques 