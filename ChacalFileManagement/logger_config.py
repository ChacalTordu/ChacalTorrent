import logging
import os

def setup_logger():
    """
    Configure le système de journalisation.
    """
    # Obtenez le chemin absolu du répertoire parent du répertoire actuel
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), './'))

    # Construisez le chemin complet du fichier de log dans le répertoire parent
    log_file_path = os.path.join(parent_dir, 'fileManagement.log')

    # Assurez-vous que le répertoire parent existe, sinon créez-le
    os.makedirs(parent_dir, exist_ok=True)

    logging.basicConfig(filename=log_file_path, level=logging.INFO, encoding='utf-8')

# Appeler la fonction de configuration du logger dès l'importation du module
setup_logger()

# Créer et exporter le logger configuré pour être utilisé dans d'autres fichiers
logger = logging.getLogger(__name__)
