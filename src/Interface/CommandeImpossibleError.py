
class CommandeImpossibleError(Exception) :
    """
    Classe CommandeImpossibleError

    Exception qui est lancée quand la commande dépasse le stock disponible
    """
    
    def __init__(self, value):
        """Constructeur"""
        self.value = value

    def __str__(self):
        """Utilisé par la fonction print"""
        return (repr(self.value))


