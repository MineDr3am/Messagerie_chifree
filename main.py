import sys


def getArg():
    addresse = sys.argv[1]
    pseudo = sys.argv[2]

    return [addresse, pseudo]

infoUser = {
    "addresse": getArg()[0],
    "pseudo": getArg()[1]
}

getArg();

print("pseudo: {}, addresse: {}".format(infoUser["addresse"],infoUser["pseudo"]))