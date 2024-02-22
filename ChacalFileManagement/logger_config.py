import logging

def setup_logger():
    """
    Configure le système de journalisation.
    """
    logging.basicConfig(filename='fileManagement.log', level=logging.INFO, encoding='utf-8')

# Appeler la fonction de configuration du logger dès l'importation du module
setup_logger()

# Créer et exporter le logger configuré pour être utilisé dans d'autres fichiers
logger = logging.getLogger(__name__)
