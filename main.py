#imports
try:
    import os
except:
    print("Impossible d'importer la librairie OS")

os.system("title BatEdit")
os.system("cls")
try:
    from pystyle import Colors, Colorate
except:
    os.system("pip install pystyle")
    from pystyle import Colors, Colorate
try:
    print(Colorate.Horizontal(Colors.blue_to_red, """╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                               ║                                                                      ║
║                                               ║   BatEdit est un outil qui vous permetteras de faire du              ║
║     ▄▄▄▄·  ▄▄▄· ▄▄▄▄▄▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄     ║   language batch sans coder                                          ║
║     ▐█ ▀█▪▐█ ▀█ •██  ▀▄.▀·██▪ ██ ██ •██       ║   Copyrigt NeverX#1724 Ne pas skid ce code sous peine                ║
║     ▐█▀▀█▄▄█▀▀█  ▐█.▪▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪     ║   de concequence                                                     ║
║     ██▄▪▐█▐█ ▪▐▌ ▐█▌·▐█▄▄▌██. ██ ▐█▌ ▐█▌·     ║   Toutes Copies de ce tool entrainera une concequence                ║
║     ·▀▀▀▀  ▀  ▀  ▀▀▀  ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀      ║   Toutes Revente de ce tool est interdite                            ║
║                                               ║                                                                      ║
║     ╔╗ ╦ ╦  ╔╗╔╔═╗╦  ╦╔═╗╦═╗═╗ ╦              ║                                                                      ║
║     ╠╩╗╚╦╝  ║║║║╣ ╚╗╔╝║╣ ╠╦╝╔╩╦╝              ║                                                                      ║
║     ╚═╝ ╩   ╝╚╝╚═╝ ╚╝ ╚═╝╩╚═╩ ╚═              ║                                                                      ║
║                                               ║                                                                      ║
║                                               ║                                                                      ║
║                                               ║                                                                      ║
╠═══════════════════════════════════════════════╩══════════════════════════════════════════════════════════════════════╣
║                                                                                                                      ║
║   [1] écrire un text                                                                                                 ║
║   [2] Changer le titre                                                                                               ║
║   [3] Changer les couleurs                                                                                           ║
║   [4] Envoi de requetes                                                                                              ║
║   [5] Effacer tous                                                                                                   ║
║   [6] Faire une pause                                                                                                ║
║   [7] Faire une pause sans rien afficher                                                                             ║
║   [8] Démarrer un fichier                                                                                            ║
║   [9] Créer une variable                                                                                             ║
║   [10] Commande personalisé                                                                                          ║
║                                                                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝""", 1))
except:
    print("Impossible d'afficher l'interface")
try:
    fonction = input(Colorate.Horizontal(Colors.green_to_red, "Ton Option >>>  ", 1))
except:
    print("impossible de demander l'option")

if fonction=='1':
    os.system("cls")
    print(Colorate.Horizontal(Colors.green_to_red, "[*] pour citer une variable, mettez le nom de la variable entre %", 1))
    text = input(Colorate.Horizontal(Colors.green_to_red, "Quel est le text à afficher? : ", 1))
    os.system("echo echo " + text + ">>fichier.bat")
    os.system("python main.py")

if fonction=='2':
    os.system("cls")
    print(Colorate.Horizontal(Colors.green_to_red, "[*] pour citer une variable, mettez le nom de la variable entre %", 1))
    title = input(Colorate.Horizontal(Colors.green_to_red, "Quel est le titre que tu veux attribuer à la fenêtre? : ", 1))
    os.system("echo  title " + title + ">>fichier.bat")
    os.system("python main.py")

if fonction=='3':
    os.system("cls")
    print(Colorate.Horizontal(Colors.green_to_red, "[*] pour citer une variable, mettez le nom de la variable entre %", 1))
    print("""voici les syntaxes : 
        le premier caractère que vous mettez désignera le text et le second l'arrière plan
        
        0 = Noir        8 = Gris
        1 = Bleu        9 = Bleu clair
        2 = Vert        A = Vert clair
        3 = Bleu-gris   B = Cyan
        4 = Rouge       C = Rouge clair
        5 = Violet      D = Violet clair
        6 = Jaune       E = Jaune clair
        7 = Blanc       F = Blanc brillant


        """)
    color = input(Colorate.Horizontal(Colors.green_to_red, "Quel sont les couleurs à afficher", 1))
    os.system("echo color " + color + ">>fichier.bat")
    os.system("python main.py")

if fonction=='4':
    os.system("cls")
    print(Colorate.Horizontal(Colors.green_to_red, "[*] pour citer une variable, mettez le nom de la variable entre %", 1))
    ping = input(Colorate.Horizontal(Colors.green_to_red, "Quel est l'adresse IP à la quelle faut-il envoyer une requête? : ", 1))
    os.system("echo ping " + ping + ">>fichier.bat")
    os.system("python main.py")

if fonction=='5':
    os.system("cls")
    os.system("echo cls>>fichier.bat")
    os.system("python main.py")

if fonction=='6':
    os.system("cls")
    os.system("echo pause>>fichier.bat")
    os.system("python main.py")

if fonction=='7':
    os.system("cls")
    os.system("echo pause>nul>>fichier.bat")
    os.system("python main.py")

if fonction=='8':
    os.system("cls")
    print(Colorate.Horizontal(Colors.green_to_red, "[*] pour citer une variable, mettez le nom de la variable entre %", 1))
    print("[!] Vous devez entrer un patch ou le nom d'un fichier qui est dans le même dossier que 'Programme batch.bat'")
    sfile = input(Colorate.Horizontal(Colors.green_to_red, "Quel est le fichier a démarrer? : ", 1))
    os.system("echo start" + sfile + ">>fichier.bat")
    os.system("python main.py")

if fonction=='9':
    os.system("cls")
    var = input(Colorate.Horizontal(Colors.green_to_red, "Quel est le nom de votre variable ? :   ", 1))
    varval = input(Colorate.Horizontal(Colors.green_to_red, "Quel est la valeur de la variable? : ", 1))
    os.system("echo set" + var + varval + ">>fichier.bat")
    os.system("python main.py")

if fonction=='10':
    os.system("cls")
    print(Colorate.Horizontal(Colors.green_to_red, "[*] pour citer une variable, mettez le nom de la variable entre %", 1))
    percom = input("Entre ta commande >>> " + """
    """)
    os.system("echo " + percom + ">>fichier.bat")
    os.system("python main.py")