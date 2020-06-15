import socket
import sys

def connection (hote, pseudo):

    hote = ""
    port = 666

    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_serveur.connect((infoUser["addresse"], port))

    connexion_avec_serveur.send(infoUser["pseudo"])
    print("Connexion établie avec le serveur sur le port {}".format(port))



    print("Fermeture de la connexion")
    connexion_avec_serveur.close()



def getArg():
    addresse = sys.argv[1]
    pseudo = sys.argv[2]

    return [addresse, pseudo]

infoUser = {
    "addresse": getArg()[0],
    "pseudo": getArg()[1]
}

print("pseudo: {}, addresse: {}".format(infoUser["addresse"],infoUser["pseudo"]))

connection(infoUser["addresse"], infoUser["pseudo"])
