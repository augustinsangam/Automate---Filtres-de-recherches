
class PasDeRobotsPossiblesError(Exception):
    """
    Classe PasDeRobotsPossiblesError

    Exception qui est levée quand aucun robot ne satisfait la commande
    (charges trop lourdes)
    """


    def __init__(self, value):
        """Contructeur"""
        self.value = value

    def __str__(self):
        """Utilisé par la fonction print"""
        return (repr(self.value))


