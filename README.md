# jeux_de_mots
projet informatique de 2A

## problème d’import en python.
Depuis VS code faites ctrl+, cela va ouvrir la panneau de config, puis cliquez sur le bouteau en haut à droite qui ressemble à une feuille en train d’être retournée (il y a une flèche). Dans le fichier json copier ce texte (avec la virgule, et restant à l’intérieur de l'accolade finale):
 
```
"python.analysis.extraPaths": ["./*"],
,"terminal.integrated.env.osx": {
    	"PYTHONPATH": "${workspaceFolder}",
	},
	"terminal.integrated.env.linux": {
    	"PYTHONPATH": "${workspaceFolder}",
	},
	"terminal.integrated.env.windows": {
    	"PYTHONPATH": "${workspaceFolder}",
	}, 
	"python.languageServer": "Jedi",
    "python.linting.pylintArgs": ["--disable=E0401"]
```

**Faire ensuite dans un terminal:**
pip install jedi-language-server
pip install inquirer
pip3 install InquirerPy   (ou peut-être ‘pip’ au lieu de ‘pip3’)
