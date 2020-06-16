import socket
import sys
import time
import socket
import threading

class Recv(threading.Thread):
    socket = None
    data = ""

    def __int__(self, canal):
        self.socket = canal
        threading.Thread.__init__(self)
        self.setDaemon = True
        self.start()

    def run(self):
        while True:
            self.data = self.data + self.socket.recv(1).decode('utf-8')
            if "\r\n" in self.data:
                print(self.data)
                self.data = ''
            time.sleep(0.001)

class Send(threading.Thread):
    socket = None

    def __init__(self, canal):
        self.socket = canal
        threading.Thread.__init__(self)
        self.setDaemon = True
        self.start()

    def run(self):
        while True:
            saisie = input("")
            self.socket.sendall(bytes(saisie + "\r\n", 'utf-8'))
            time.sleep(0.001)




def connection(hote, pseudo):
    print(hote)
    port = 666

    canal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    canal.connect((hote, port))

    Send(canal)
    Recv(canal)


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
