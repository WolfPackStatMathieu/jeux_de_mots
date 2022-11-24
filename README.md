### Kata 

Kata is a game based on the well-known game Wordle: the player has a limited number of attempts to guess a 5 or 6-letters word. Each attempt is compared to the world to guess. The colour of each proposition’s letter is coloured in green (if the letter is well placed), yellow (if the letter is in the word but misplaced) or grey (the letter is not in the word). If the player succeeds to guess the world in 6 or less attempts then he wins. 

Kata operates in the same way but allows the player to select various difficulties (number of attempts, word length, time per attempt) and to play with customized lists.
To play a user must have an account. A non-already existing pseudo is required to create an account.
Once he is logged in, he cans visualize the top 10 scores, play a game, visualize his own lists or create a new list. When he is playing, he can pause. The game is automatically saved and the player cans play again the same game later on.
At the end of a game, if he has succeeded to guess the word, a score is calculated depending on the difficulties chosen. 

### INSTALLATION

There are a few steps to follow to operate the application. 

### Git repositories
The application is separated into two git repositories. Make sure you have download both. 
Jeux_de_mots: ‘https://github.com/WolfPackStatMathieu/jeux_de_mots.git’
Client_kata: ‘https://github.com/apollineguerineau/client_kata.git’
You have to open the two folders in separate windows.


### Database installation

The application needs a storage for the accounts, the games paused, the best scores and the personal lists. All of them are stored in a database. Therefore, you have to import the structure of the database. We use "PostgreSQL" system. 

You will find the code to be entered in the system in the "init_db.sql" file. 
Open "PostgreSQL" and copy the code in the system.

### Python packages requirements

Then, you have some Python packages to install to have all the necessary modules. 
Write this line of code in the terminal for the two windows : 

pip install -r requirements.txt

### Configuration

Finally you have to create a ".env" file in the root of the first folder with the following information : 

PASSWORD=XXXX
HOST=sgbd-eleves.domensai.ecole
PORT=5432
DATABASE=XXXX
USER=XXXX

### Usage

You first have to run the api.py file in the jeux_de_mots file. Then you just have to run the “main.py”. You will have to create an account if you want to play.

### Credits

Apolline GUERINEAU, Mathis DAVID-QUILLOT, Linh-Da DINH, Oussama MARHFOUL, Mathieu THOMASSIN  - ENSAI-2022