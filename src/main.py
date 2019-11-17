####################################################################################
#   Fichier     :   main.py
#   Auteur      :   EyaTom Augustin SANGAM & AbdelRahman Mohammed Bassiouni 
#                       & Nicolas Verbaere
#   Date        :   16 Novembre 2019
#   Projet      :   Itinéraire rapide - Drone collecteur
####################################################################################

from Automate   import Automate
from Etat       import Etat

if __name__ == "__main__" :
    
    print("Recherche de 'av', 'B', ''")

    automate = Automate()
    
    print('\nAvant le retrait')

    etat = Etat('av', 'B', '')

    for element in automate[etat] :
        print(element)


    print('\nAprès le retrait de avion B16A49 A')
    automate -= Etat('avion', 'B16A49', 'A')

    etat = Etat('av', 'B', '')

    for element in automate[etat] :
        print(element)


