import requests
import pyautogui
import json
import fade
import ctypes
from colorama import *
from pystyle import *
import time
import os

ctypes.windll.kernel32.SetConsoleTitleW(f" DoxTool v1 - Saladefruit")


def clear_console():
    # Efface la console en fonction du système d'exploitation
    os.system('cls' if os.name == 'nt' else 'clear')

list_number = ["1", "2", "x"]

create_dox_intro = """
╦ ╦┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ╔╦╗┌─┐  ╔═╗┬─┐┌─┐┌─┐┌┬┐┌─┐  ╔╦╗┌─┐═╗ ╦
║║║├┤ │  │  │ ││││├┤    ║ │ │  ║  ├┬┘├┤ ├─┤ │ ├┤    ║║│ │╔╩╦╝
╚╩╝└─┘┴─┘└─┘└─┘┴ ┴└─┘   ╩ └─┘  ╚═╝┴└─└─┘┴ ┴ ┴ └─┘  ═╩╝└─┘╩ ╚═
"""

list_dox_intro = """
╦ ╦┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ╔╦╗┌─┐  ╦  ┬┌─┐┌┬┐  ╔╦╗┌─┐─┐ ┬
║║║├┤ │  │  │ ││││├┤    ║ │ │  ║  │└─┐ │    ║║│ │┌┴┬┘
╚╩╝└─┘┴─┘└─┘└─┘┴ ┴└─┘   ╩ └─┘  ╩═╝┴└─┘ ┴   ═╩╝└─┘┴ └─
"""

view_dox_intro = """
╦ ╦┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ╔╦╗┌─┐  ╦  ╦┬┌─┐┬ ┬  ╔╦╗┌─┐─┐ ┬
║║║├┤ │  │  │ ││││├┤    ║ │ │  ╚╗╔╝│├┤ │││   ║║│ │┌┴┬┘
╚╩╝└─┘┴─┘└─┘└─┘┴ ┴└─┘   ╩ └─┘   ╚╝ ┴└─┘└┴┘  ═╩╝└─┘┴ └─
"""

text = """
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\\
       ::::::;       ;          OOOOO \\
       ;:::::;       ;         OOOOOOOO\\              By saladefruit_
      ,;::::::;     ;'         / OOOOOOO\\
    ;:::::::::`. ,,,;.        /  / DOOOOOO\\                     
  .';:::::::::::::::::;,     /  /     DOOOO\               ▓█████▄  ▒█████  ▒██   ██▒
 ,::::::;::::::;;;;::::;,   /  /        DOOO\              ▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░
;`::::::`'::::::;;;::::: ,#/  /          DOOO\             ░██   █▌▒██░  ██▒░░  █   ░
:`:::::::`;::::::;;::: ;::#  /            DOOO|            ░▓█▄   ▌▒██   ██░ ░ █ █ ▒ 
::`:::::::`;:::::::: ;::::# /              DOO|            ░▒████▓ ░ ████▓▒░▒██▒ ▒██▒
`:`:::::::`;:::::: ;::::::#/               DOO|             ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
 :::`:::::::`;; ;:::::::::##                OO|             ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░
 ::::`:::::::`;::::::::;:::#                OO|             ░ ░  ░ ░ ░ ░ ▒   ░    ░  
 `:::::`::::::::::::;'`:;::#                O/                ░        ░ ░   ░    ░  
  `:::::`::::::::;' /  / `:#                                  ░                        
   ::::::`:::::;'  /  /   `#
"""

Anime.Fade(Center.Center(text), Colors.green_to_blue, Colorate.Vertical, interval=0.050, enter=True)


def main():
    dox_easy ="""
    
██████╗  ██████╗ ██╗  ██╗    ███████╗ █████╗ ███████╗██╗   ██╗
██╔══██╗██╔═══██╗╚██╗██╔╝    ██╔════╝██╔══██╗╚══███╔╝╚██╗ ██╔╝
██║  ██║██║   ██║ ╚███╔╝     █████╗  ███████║  ███╔╝  ╚████╔╝ 
██║  ██║██║   ██║ ██╔██╗     ██╔══╝  ██╔══██║ ███╔╝    ╚██╔╝  
██████╔╝╚██████╔╝██╔╝ ██╗    ███████╗██║  ██║███████╗   ██║   
╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   
                                                              
"""
    dox_easy = fade.greenblue(dox_easy)
    print(dox_easy)
    choix = input(Fore.LIGHTCYAN_EX + "\n\n                              1- Create Dox\n                              2- Look Dox\n                              3- List Dox\n\n                              x- Exit\n\n\nPlease Entrer a number :" + Fore.LIGHTBLACK_EX + " ")
    if choix == "1":
      create_dox()
    if choix == "2":
      look_dox()
    if choix == "3":
      list_dox()

    if choix == "x":
      os.system("exit")
    # number false
  

def create_dox():
  clear_console()
  print(Fore.LIGHTRED_EX + f"{create_dox_intro}")
  name_of_dox = input("Entrez le nom du dox : ")
  print(Fore.LIGHTMAGENTA_EX + "\n\n C'est Parti !! ( remarque : si vous ne possédez pas l'information demandé merci d'écrire : none )")
  time.sleep(1)
  prenom = input(Fore.LIGHTRED_EX + "\n\nPrenom : ")
  nom = input("\nNom : ")
  ip = input("\nAdresse Ip : ")
  numero = input("\nNumero de Tel : ")
  adresse = input("\nAdresse : ")
  autre = input("\nAutre Infos : \n\n[\n\n                        ")
  autre_suite = input("\n\n]\n\n Voulez-vous enregistrer ce dox (o/n) : ")
  if autre_suite == "o":
    dox_data = {
      "Principal" : {

        "Prenom": prenom,
        "Nom": nom,
        "Adresse IP": ip,
        "Numero de Tel": numero,
        "Adresse": adresse,
        
      },

      "Autres" : {
        "Autres Infos": autre
      }
    }
    
    # Créez un dossier "dox" s'il n'existe pas
    if not os.path.exists("dox"):
        os.makedirs("dox")
    
    # Obtenez le chemin absolu du fichier JSON
    json_file_path = os.path.join("dox", f"{name_of_dox}.json")
    
    # Enregistrez les réponses dans un fichier JSON avec le chemin absolu spécifié
    with open(json_file_path, "w") as file:
        json.dump(dox_data, file, indent=4)
    print(Fore.LIGHTGREEN_EX + f"Le Dox : {name_of_dox}, a bien été enregistré !")
    time.sleep(2)
    clear_console()
    main()

  if autre_suite != "o":
    clear_console()
    print("Le dox a été annulé !")
    time.sleep(2)
    clear_console()
    main()


def look_dox():
  clear_console()
  if not os.path.exists("dox"):
    print(Fore.LIGHTRED_EX + "Aucun dox n'a été enregistré !")
    time.sleep(2)
    clear_console()
    main()

  else:
      clear_console()
      print(Fore.LIGHTRED_EX + f"{view_dox_intro}")
      name_of_dox = input(Fore.LIGHTCYAN_EX + "\n\nEntrez le nom du dox : ")
      json_file_path = os.path.join("dox", f"{name_of_dox}.json")
      if not os.path.exists(json_file_path):
          print(Fore.RED + f"Le dox '{name_of_dox}' n'existe pas.")
          time.sleep(2)
          clear_console()
          main()
      else:
          with open(json_file_path, "r") as file:
              dox_data = json.load(file)
          
          json_output = {}
          for question, reponse in dox_data.items():
              json_output[question] = reponse
          print(Fore.LIGHTYELLOW_EX + "\n\n" + json.dumps(json_output, indent=4))
          input(Fore.RESET + "\n\nPress any key to continue ...")
          clear_console()
          main()
        



def list_dox():
  clear_console()
  if not os.path.exists("dox"):
    print(Fore.LIGHTRED_EX + "Aucun dox n'a été enregistré !")
    time.sleep(2)
    clear_console()
    main()
  else:
    # Liste tous les fichiers .json dans le dossier "dox"
    json_files = [os.path.splitext(f)[0] for f in os.listdir("dox") if f.endswith(".json")]
    
    if not json_files:
        print(Fore.LIGHTRED_EX + "Aucun dox n'a été enregistré !")
    else:
        clear_console()
        print(Fore.LIGHTRED_EX + f"{list_dox_intro}")
        print(Fore.LIGHTBLUE_EX + "Voici tous les dox enregistrés ! : \n\n")
        for json_file in json_files:
            print(Fore.LIGHTYELLOW_EX + json_file)
            input(Fore.RESET + "\n\nPress any key to continue ...")
            clear_console()
            main()





if __name__ == "__main__":
    main()
