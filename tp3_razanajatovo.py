#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


# Classe principale (racine de tous les heritages)
class Medium:
    def __init__(self, titre, auteur, date_parution):
        self.__titre = titre
        self.__auteur = auteur
        self.__date_parution = date_parution
        self.__emprunteur = None

    def emprunter(self, emprunteur):
        self.__emprunteur = emprunteur
    
    # Getters
    # Ici, il suffit d'appeler les getters comme des attributs de la classe medium : "medium.titre"
    # Et les setters, il suffit d'y assigner une valeur : medium.titre = "titre saisie"
    @property
    def titre(self):
        return self.__titre

    @property
    def auteur(self):
        return self.__auteur

    @property
    def date_parution(self):
        return self.__date_parution

    @property
    def emprunteur(self):
        return self.__emprunteur

class Livre(Medium):
    def __init__(self, titre, auteur, date_parution, nombre_pages, editeur):
        super().__init__(titre, auteur, date_parution)
        # Caracteristiques propres aux "Livres"
        self.__nombre_pages = nombre_pages
        self.__editeur = editeur

    @property
    def nombre_pages(self):
        return self.__nombre_pages
    
    @property
    def editeur(self):
        return self.__editeur
        
# Getter et Setter si necessaire, dans le meme format que precedemment

class CD(Medium):
    def __init__(self, titre, auteur, date_parution, duree, nombre_morceaux):
        super().__init__(titre, auteur, date_parution)
        # Caracteristiques propres aux "CDs"
        self.__duree = duree
        self.__nombre_morceaux = nombre_morceaux

    @property
    def duree(self):
        return self.__duree
    
    @property
    def nombre_morceaux(self):
        return self.__nombre_morceaux

class DVD(Medium):
    def __init__(self, titre, auteur, date_parution, duree):
        super().__init__(titre, auteur, date_parution)
        # Caracteristique propre aux "DvDs"
        self.duree = duree

# 3) Extension du logiciel
class ArticleMagazine(Medium):
    def __init__(self, titre, auteur, date_parution, nom_magazine, numero_magazine, intervalle_pages):
        super().__init__(titre, auteur, date_parution)
        self.__nom_magazine = nom_magazine
        self.__numero_magazine = numero_magazine
        self.__intervalle_pages = intervalle_pages

    @property
    def nom_magazine(self):
        return self.__nom_magazine
    
    @property
    def numero_magazine(self):
        return self.__numero_magazine
    
    @property
    def intervalle_pages(self):
        return self.__intervalle_pages


class Mediatheque:
    def __init__(self):
        # Liste contenant tous les medias (que ce soit un CD, ou un Livre, ou un DVD)
        self.__collection = []

    # Ajout d'un media a une liste de mediums
    def ajouter_medium(self, medium):
        self.__collection.append(medium)

    def lister_par_auteur(self, auteur):
        # On retourne les mediums dans la liste correspondant a un auteur
        return [medium for medium in self.__collection if medium.auteur == auteur]

    # Suppression de media en fonction du titre et de l'auteur
    def supprimer_medium(self, titre, auteur):
        self.__collection = [medium for medium in self.__collection if not (medium.titre == titre and medium.auteur == auteur)]

    # Suppression de medias dans la liste en fonction de l'auteur
    def supprimer_par_auteur(self, auteur):
        self.__collection = [medium for medium in self.__collection if medium.auteur != auteur]

    # Emprunt d'un media par l'"emprunteur" en question
    # en faisant appel a la methode emprunter
    def emprunter_medium(self, titre, auteur, emprunteur):
        for medium in self.__collection:
            if medium.titre == titre and medium.auteur == auteur:
                medium.emprunter(emprunteur)
                break
    
    # Compteur pour determiner le nombre de medias empruntes
    def compter_empruntes(self):
        return sum(1 for medium in self.__collection if medium.emprunteur is not None)
    

    # Pour vérifier si les medias sont bien rajoutés
    def afficher_medias(self):
        for medium in self.__collection:
            print("-----")
            print(f"Titre: {medium.titre}, Auteur: {medium.auteur}, Date de parution (année): {medium.date_parution}")
            # Savoir si le medium a cet attribut (caracteristique)
            if hasattr(medium, 'nombre_pages'):  # Si c'est un livre
                print(f"Nombre de pages: {medium.nombre_pages}, Éditeur: {medium.editeur}")
            if hasattr(medium, 'duree'):  # Si c'est un CD ou un DVD
                print(f"Durée (en minutes): {medium.duree}")
            if hasattr(medium, 'nom_magazine'):  # Si c'est un article de magazine
                print(f"Magazine: {medium.nom_magazine}, Numéro: {medium.numero_magazine}, Pages: {medium.intervalle_pages}")
            print("-----")
    
    @property
    def collection(self):
        return self.__collection

class TestMedium(unittest.TestCase):
    def setUp(self):
        self.medium = Medium("Titre", "Auteur", "Date")

    def test_emprunter(self):
        self.assertIsNone(self.medium.emprunteur)
        self.medium.emprunter("Emprunteur")
        self.assertEqual(self.medium.emprunteur, "Emprunteur")

class TestLivre(unittest.TestCase):
    def setUp(self):
        self.livre = Livre("Titre", "Auteur", "Date", 123, "Editeur")

    def test_init(self):
        self.assertEqual(self.livre.nombre_pages, 123)
        self.assertEqual(self.livre.editeur, "Editeur")

class TestCD(unittest.TestCase):
    def setUp(self):
        self.cd = CD("Titre", "Auteur", "Date", 60, 12)

    def test_init(self):
        self.assertEqual(self.cd.duree, 60)
        self.assertEqual(self.cd.nombre_morceaux, 12)

class TestDVD(unittest.TestCase):
    def setUp(self):
        self.dvd = DVD("Titre", "Auteur", "Date", 120)

    def test_init(self):
        self.assertEqual(self.dvd.duree, 120)

class TestArticleMagazine(unittest.TestCase):
    def setUp(self):
        self.article = ArticleMagazine("Titre", "Auteur", "Date", "Magazine", 5, "10-20")

    def test_init(self):
        self.assertEqual(self.article.nom_magazine, "Magazine")
        self.assertEqual(self.article.numero_magazine, 5)
        self.assertEqual(self.article.intervalle_pages, "10-20")

class TestMediatheque(unittest.TestCase):
    def setUp(self):
        self.mediatheque = Mediatheque()
        self.livre = Livre("Livre", "Auteur", "Date", 123, "Editeur")
        self.cd = CD("CD", "Auteur", "Date", 60, 12)

    def test_ajouter_medium(self):
        self.mediatheque.ajouter_medium(self.livre)
        self.assertIn(self.livre, self.mediatheque.collection)

    def test_lister_par_auteur(self):
        self.mediatheque.ajouter_medium(self.livre)
        self.mediatheque.ajouter_medium(self.cd)
        result = self.mediatheque.lister_par_auteur("Auteur")
        self.assertEqual(len(result), 2)

    def test_supprimer_medium(self):
        self.mediatheque.ajouter_medium(self.livre)
        self.mediatheque.supprimer_medium("Livre", "Auteur")
        self.assertNotIn(self.livre, self.mediatheque.collection)

    def test_emprunter_medium(self):
        self.mediatheque.ajouter_medium(self.livre)
        self.mediatheque.emprunter_medium("Livre", "Auteur", "Emprunteur")
        self.assertEqual(self.livre.emprunteur, "Emprunteur")

    def test_compter_empruntes(self):
        self.mediatheque.ajouter_medium(self.livre)
        self.mediatheque.emprunter_medium("Livre", "Auteur", "Emprunteur")
        count = self.mediatheque.compter_empruntes()
        self.assertEqual(count, 1)


# Interface utilisateur

def Test_liste_par_auteur(bibliotheque):
# Test sur le fonctionnement de "liste_par_auteur"
    rep = input("Voulez-vous découvrir les medias associes à un auteur ?")
    if rep.lower() == 'oui':
        auteur_ref = input("Entrez le nom de l'auteur pour lister ses médias : ").strip()
        # Appel de la méthode lister_par_auteur
        medias_auteur = bibliotheque.lister_par_auteur(auteur_ref)
        if medias_auteur:
            print(f"\nMédias de l'auteur {auteur_ref}:")
            for medium in medias_auteur:
                print("-----")
                print(f"    Titre: {medium.titre}, Auteur: {medium.auteur}, Date de parution (JJ/MM/AA): {medium.date_parution}")
                if hasattr(medium, 'nombre_pages'):
                    print(f"    Nombre de pages: {medium.nombre_pages}, Éditeur: {medium.editeur}")
                if hasattr(medium, 'duree'):
                    print(f"    Durée (en minutes): {medium.duree}")
                if hasattr(medium, 'nom_magazine'):
                    print(f"    Magazine: {medium.nom_magazine}, Numéro: {medium.numero_magazine}, Pages: {medium.intervalle_pages}")
                print("-----\n")
        else:
            print(f"Aucun média trouvé pour l'auteur {auteur_ref}.")

def Test_supression(bibliotheque):
# Test pour la suppression d'un media
    sup = input("Voulez-vous supprimer un media dans cette collection ?")
    if sup.lower() == 'oui':
        titre_sup = input("Entrez le titre : ").strip()
        auteur_sup = input("Entrez le nom de l'auteur : ").strip()
        # Appel de la méthode supprimer_medium
        bibliotheque.supprimer_medium(titre_sup,auteur_sup)
        print("\nAprès suppression, on a :")
        bibliotheque.afficher_medias()

    # Test pour la suppression en fonction de l'auteur
    sup_list = input("Voulez-vous supprimer un media par auteur ?")
    if sup_list.lower() == 'oui':
        auteur_sup_list = input("Entrez le nom de l'auteur : ").strip()
        # Appel de la méthode supprimer_medium
        bibliotheque.supprimer_par_auteur(auteur_sup_list)
        print("\nAprès suppression, on a :")
        bibliotheque.afficher_medias()

def Test_emprunt(bibliotheque):
# Test pour l'emprunt d'un medium
    borrow = input("Veux tu emprunter un media ?")
    if borrow.lower() == 'oui':
        nom_emprunteur = input("Entrez le nom de l'emprunteur :").strip()
        titre_borrow = input("Entrez le titre du media à emprunter :")
        auteur_borrow = input("Entrez le nom de l'auteur du media :")
        bibliotheque.emprunter_medium(titre_borrow, auteur_borrow, nom_emprunteur)
        nb_media_borrow = bibliotheque.compter_empruntes()
        print(nom_emprunteur," a emprunté le media dont le titre est ",titre_borrow," et l'auteur est ",auteur_borrow,"\n")
        if (nb_media_borrow == 1):
            print(nb_media_borrow," media a été emprunté !")
        else:
            print(nb_media_borrow," medias ont été empruntés !")

def main():
    bibliotheque = Mediatheque()
    while True:
        type_medium = input("Entrez le type de médium (Livre, CD, DVD, ArticleMagazine) ou 'quitter' pour sortir: ").strip()
        if type_medium.lower() == 'quitter':
            break
        
        # Ici strip() permet d'enlever les espaces au debut et a la fin d'une chaine de caracteres
        titre = input("Titre: ").strip()
        auteur = input("Auteur: ").strip()
        date_parution = input("Date de parution (JJ/MM/AA): ").strip()

        # Conditions pour les differents types de medium selectionne par l'utilisateur
        if type_medium.lower() == 'livre':
            nombre_pages = int(input("Nombre de pages: ").strip())
            editeur = input("Éditeur: ").strip()
            medium = Livre(titre, auteur, date_parution, nombre_pages, editeur)
        elif type_medium.lower() == 'cd':
            duree = float(input("Durée (en minutes): ").strip())
            nombre_morceaux = int(input("Nombre de morceaux: ").strip())
            medium = CD(titre, auteur, date_parution, duree, nombre_morceaux)
        elif type_medium.lower() == 'dvd':
            duree = float(input("Durée (en minutes): ").strip())
            medium = DVD(titre, auteur, date_parution, duree)
        elif type_medium.lower() == 'articlemagazine':
            nom_magazine = input("Nom du magazine: ").strip()
            numero_magazine = input("Numéro du magazine: ").strip()
            intervalle_pages = input("Intervalle des pages: ").strip()
            medium = ArticleMagazine(titre, auteur, date_parution, nom_magazine, numero_magazine, intervalle_pages)
        else:
            print("Type de médium inconnu.")
            continue

        bibliotheque.ajouter_medium(medium)
        print(f"{type_medium} ajouté avec succès.\n")
        bibliotheque.afficher_medias()

        Test_liste_par_auteur(bibliotheque)
        Test_supression(bibliotheque)
        Test_emprunt(bibliotheque)

if __name__ == "__main__":
    main()
    unittest.main()
