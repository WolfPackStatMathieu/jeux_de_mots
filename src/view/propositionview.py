from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.view.abstractview import AbstractView
from src.view.session import Session

import signal
ASK_PROPOSITION =inquirer.text(message = 'Quel mot veux tu proposer?')
def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")



class PropositionView(AbstractView) :
    
    def display_info(self):
        pass

    def make_choice(self):
        proposition = ASK_PROPOSITION.execute()
        # Set the signal handler and a 5-second alarm
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(5)
        print(proposition)



        
        