####################################################################################
#   Fichier     :   main.py
#   Auteur      :   EyaTom Augustin SANGAM & AbdelRahman Mohammed Bassiouni 
#                       & Nicolas Verbaere
#   Date        :   17 Novembre 2019
#   Projet      :   Automate : Filtres de recherches
####################################################################################



from Etat                               import Etat
from Automate                           import Automate
from Panier                             import Panier
from Interface.CommandeImpossibleError  import CommandeImpossibleError



def testAutomate1() :

    print("Recherche de '', '', ''")

    automate = Automate()
    
    print('\nAvant le retrait')

    etat = Etat('', '', '')

    choixPossibles = automate.obtenirChoixPossibles(etat)

    print("Le nombre total d'éléments correspondant à la recherche est : ", choixPossibles[0])

    for element in choixPossibles[1] :
        print(element.obtenirChaine())




def testAutomate2() :

    print("Recherche de 'av', 'B', ''")

    automate = Automate()
    
    print('\nAvant le retrait')

    etat = Etat('av', 'B', '')

    for element in automate[etat] :
        print(element.obtenirChaine())


    print('\nAprès le retrait de avion B16A49 A')
    automate -= Etat('avion', 'B16A49', 'A')

    etat = Etat('av', 'B', '')

    for element in automate[etat] :
        print(element.obtenirChaine())

    


def testPanier1() :

    panier = Panier()
    
    panier += Etat('avion', 'B16A49', 'A')
    panier += Etat('avion', 'B26A49', 'B')
    panier += Etat('ami', '111111', 'B')
    panier += Etat('amie', '123ABC' , 'C');

    print('Les éléments du panier sont : ')

    for element in panier :
        print(element.obtenirChaine())
    print('Poids total :', panier.poids)

    print("\nOn retire 'avion B26A49 B'")
    panier -= Etat('avion', 'B26A49', 'B')

    print('Les éléments du panier sont : ')

    for element in panier :
        print(element.obtenirChaine())
    print('Poids total :', panier.poids)

    print("\nOn vide le panier")
    panier.vider()

    print('Les éléments du panier sont : ')

    for element in panier :
        print(element.obtenirChaine())
    print('Poids total :', panier.poids)




def testPanier2() :

    panier = Panier()
    
    panier += Etat('avion', 'B16A49', 'A')
    panier += Etat('avion', 'B26A49', 'B')
    panier += Etat('ami', '111111', 'B')
    panier += Etat('amies', '123ABC' , 'C');   # Créé au hasard. Pas d'importance
    panier += Etat('amies', '123ABD' , 'C');   # Créé au hasard. Pas d'importance
    panier += Etat('amiess', '123ABE' , 'C');  # Créé au hasard. Pas d'importance
    try :
        panier += Etat('amiesss', '123ABF' , 'C'); # Créé au hasard. Pas d'importance
    except CommandeImpossibleError :
        print('Le test passe. On ne peut pas inserer plus de 25 kg dans le panier.')
    



if __name__ == "__main__" :
    print ('*'*70)
    testAutomate1()

    print()
    print ('*'*70)
    testAutomate2()

    print()
    print('\n\n')
    print ('*'*70)
    testPanier1()

    print()
    print('\n\n')
    print ('*'*70)
    testPanier2()

    print()
    print()
    print()