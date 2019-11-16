####################################################################################
#   Fichier     :   Entrepot.py
#   Auteur      :   EyaTom Augustin SANGAM & AbdelRahman Mohammed Bassiouni 
#                       & Nicolas Verbaere
#   Date        :   2 Novembre 2019
#   Projet      :   Itinéraire rapide - Drone collecteur
####################################################################################

from Noeud import Noeud    

class Entrepot(object):
    """

    Classe Entrepot

    Classe qui modélise un entrepôt
    Un entrepôt n'est rien d'autre qu'une liste de noeuds reliés dans un graphe

    """


    instance = None       # Attribut statique de classe
   

    def __new__(cls): 
        """
        Méthode de construction standard en Python
        Elle suit l'implémentation d'une classe Singleton comme défini ici :
        https://fr.wikipedia.org/wiki/Singleton_(patron_de_conception)#Python
        """

        if cls.instance is None:
            cls.instance        = object.__new__(cls)
            cls.instance.noeuds = []            # La liste des noeuds du grape
            cls.instance.graphe = None          # Le graphe asscocié à l'entrepôt. Il s'agit d'un graphe valué
                                                # Il est censé être une map<Noeud, set<NoueudIncident, Distance>>
            cls.instance.lireFichier("../data/entrepot.txt")

        return cls.instance


    def lireFichier(self, nomFichier) :
        """
        Méthode lireFichier(nomFichier)
        Permet de lire le fichier et de remplir les deux attributs de la classe

        param nomFichier    : Le chemin vers le fichier contenant les données
        """
        # On ouvre le fichier et on lit tous les lignes du fichier
        with open (nomFichier, 'r') as fichier :
            lignes = fichier.readlines()
    

        # On va trouver l'index de rupture dans le fichier
        # Il s'agit de la ligne de séparation entre les noeuds et
        # les relations entre les noeuds
        for i, ligne in enumerate(lignes) :
            if ligne.strip() == '' :  # strip() pour enlever les espaces inutiles
                indexRupture = i
                break

        self.lireNoeuds(lignes[:indexRupture])          # On lit les noeuds
        self.lireGraphe(lignes[indexRupture + 1:])      # On lit les relations entre les noeuds
                                                        # (le graphe)

       

    def lireNoeuds(self, lignes) :
        """
        Méthode lireNoeuds(lignes)

        Permet de lire la première partie du fichier contenant les 
        détails sur les noeuds. Elle remplit automatiquement l'attribut noeuds

        param lignes : les lignes correspondantes à la première partie du fichier

        """
        for ligne in lignes :
            ligne = ligne.strip()
            # Noeud : (id, nA, nB, nC)
            self.noeuds.append(Noeud(*(list(map(int, ligne.strip().split(',')))))) 



    def lireGraphe(self, lignes) :
        """
        Méthode lireGraphe(lignes)

        Permet de lire la deuxième partie du fichier contenant les détails sur les
        relations entre les noeuds. Elle remplit automatiquement l'attribut graphe


        param lignes : les lignes correspondantes à la deuxième partie du fichier

        """
        # graphe :  map<Noeud, set<NoueudIncident, Distance>>
        self.graphe = {noeud : set() for noeud in self.noeuds}
        for ligne in lignes :
            idNoeud1, idNoeud2, distance = map(int, ligne.strip().split(','))
            self.graphe[self.noeuds[idNoeud1]].add((self.noeuds[idNoeud2], distance))
            self.graphe[self.noeuds[idNoeud2]].add((self.noeuds[idNoeud1], distance))



    def distanceEntre(self, noeud1, noeud2) :
        """
        Méthode distanceEntre(noeud1, noeud2)

        Permet de trouver la distance entre deux noeuds.
        Elle est programmée pour ne marcher que sur des noeuds adjacents

        param   noeud1  :   Un noeud
        param   noued2  :   L'autre noeud

        Renvoie une exception de type "NotAdjancedNodeException" si les noeuds ne sont
        pas adjencents.
        """

        if noeud1 == noeud2 :
            return 0

        for noeud, distance in self.graphe[noeud1] :
            if noeud == noeud2 :
                return distance

        raise Exception("NoeudsPasAdjacentsException")


    
    def enleverRecolte(self, recolte) :
        """
        Méthode enleverRecolte(recolte)

        Met à jour l' entrepôt après une commande

        recolte         :       La recolte efectuée
        """

        for ceuillete in recolte.ceuilletes :
            ceuillete.noeud.nA -= ceuillete.nA 
            ceuillete.noeud.nB -= ceuillete.nB
            ceuillete.noeud.nC -= ceuillete.nC


    def afficher(self) :
        """
        Méthode afficherEntreprot()

        Permet d'afficher l'entrepôt selon la méthode demandée par l'ennoncé du TP
        """

        listeTexte = []
        for noeud in self.noeuds:
            texteNoeud = '(Noeud {:>2}, {:>2}, {:>2}, {:>2}, ('.format(noeud.id, noeud.nA, noeud.nB, noeud.nC)
            noeudsIncidents = ''
            for noeudIncident, distance in self.graphe[noeud]:
                noeudsIncidents += '(Noeud {:>2}, {:>2}) , '.format(noeudIncident.id, distance)
            texteNoeud += noeudsIncidents[:-3] + ')'
            texteNoeud.replace(" ", "  ")
            listeTexte.append(texteNoeud)

        return listeTexte





