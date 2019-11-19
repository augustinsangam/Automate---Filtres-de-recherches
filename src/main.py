
####################################################################################
#   Fichier     :   main.py
#   Auteur      :   EyaTom Augustin SANGAM & AbdelRahman Mohammed Bassiouni
#                       & Nicolas Verbaere
#   Date        :   16 Novembre 2019
#   Projet      :   Itinéraire rapide - Drone collecteur
####################################################################################

from Etat import Etat
from Automate import Automate
from Panier import Panier
from Interface.Interface import Interface
from tkinter import *

def testAutomate():
    print("Recherche de 'av', 'B', ''")

    automate = Automate()

    print('\nAvant le retrait')

    etat = Etat('av', 'B', '')

    for element in automate[etat]:
        print(element)

    print('\nAprès le retrait de avion B16A49 A')
    automate -= Etat('avion', 'B16A49', 'A')

    etat = Etat('av', 'B', '')

    for element in automate[etat]:
        print(element)


def testPanier():
    panier = Panier()

    panier.ajouter('avion B16A49 A')
    panier.ajouter('avion B26A49 B')
    panier.ajouter('ami 111111 B')
    panier.ajouter('amie 123ABC C')

    print('Les éléments du panier sont : ')

    for element in panier.objets:
        print(element)

    print("\nOn retire 'avion B26A49 B'")
    panier.retirer('avion B26A49 B')

    print('Les éléments du panier sont : ')

    for element in panier.objets:
        print(element)

    print("\nOn vide le panier")
    panier.vider()

    print('Les éléments du panier sont : ')

    for element in panier.objets:
        print(element)


if __name__ == "__main__":
    # print('*' * 70)
    # testAutomate()
    #
    # print('\n\n')
    # print('*' * 70)
    # testPanier()
    interface = Interface()
    interface.mainloop()