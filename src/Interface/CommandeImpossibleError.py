
class CommandeImpossibleError(Exception) :
    """
    Classe CommandeImpossibleError

    Exception qui est lancée quand la commande dépasse le stock disponible
    """
    
    def __init__(self, message):
        """Constructeur"""
        super().__init__(message)



