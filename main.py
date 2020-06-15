import socket
import sys

def connection(hote, pseudo):

    port = 666

    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_serveur.connect((infoUser["addresse"], port))

    connexion_avec_serveur.send(infoUser["pseudo"])
    print("Connexion établie avec le serveur sur le port {}".format(port))



    print("Fermeture de la connexion")
    connexion_avec_serveur.close()



def getArg():
    if len(sys.argv) >= 3:
        try:
            addresse = sys.argv[1]
        except:
            print("Une erreur est survenue pour récupérer l'adresse ")
        try:
            pseudo = sys.argv[2]
        except UnboundLocalError:
            print("Une erreur est survenue pour récupérer le pseudo")

        return [addresse, pseudo]
    else:
        return -1

infoUser = {}
if not getArg() == -1:
    infoUser = {
        "addresse": getArg()[0],
        "pseudo": getArg()[1]
    }
if infoUser:
    print("pseudo: {}, addresse: {}".format(infoUser["addresse"],infoUser["pseudo"]))

    connection(infoUser["addresse"], infoUser["pseudo"])

