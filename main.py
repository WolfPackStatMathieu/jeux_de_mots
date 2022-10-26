import dotenv
from src.vues.accueilkataview import AccueilKataView

# This script is the entry point of your application
dotenv.load_dotenv()

if __name__ == '__main__':
    # Lancer l'écran d'accueil
    current_view = AccueilKataView()

# while current_view is not none, the application is still running
    while current_view:

        # Display the info of the view
        current_view.display_info()
        # ask user for a choice
        current_view = current_view.make_choice()
