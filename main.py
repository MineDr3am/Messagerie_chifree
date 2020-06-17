import sys
import time
import socket
import threading
from Crypto.PublicKey import RSA

class Recv(threading.Thread):
    socket = None
    data = ''

    def __init__(self, canal):
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

    def __init__(self, canal, pseudo):
        self.socket = canal
        threading.Thread.__init__(self)
        self.setDaemon = True
        self.start()
        self.socket.sendall(bytes("#pseudo=" + pseudo + "\r\n", 'utf-8'))

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

    Send(canal, pseudo)
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


def FunctionRSA():
    #creation d´un couple de clés
    key = RSA.generate(1024)

    #chiffrage
    public_key = key.publickey()
    enc_data = public_key.encrypt(b"""bonjour c'est un message secret""", 32)

    #dechiffrage
    x = key.decrypt(enc_data)
    x = x.decode('utf-8')

    #afficher ses clés:
    k = key.exportKey('PEM')
    p = key.publickey().exportKey('PEM')

    #sauvegarder ses clés dans des fichiers:
    with open('private.pem','w') as kf:
	    kf.write(k.decode())
	    kf.close()

    with open('public.pem','w') as pf:
	    pf.write(p.decode())
	    pf.close()

    #importer des clés à partir d'un fichier
    with open('private.pem','r') as fk:
	priv = fk.read()
	fk.close()

    with open('public.pem','r') as fp:
	    pub = fp.read()
	    fp.close()

    privat = RSA.importKey(priv)
    public = RSA.importKey(pub)




infoUser = {}
if not getArg() == -1:
    infoUser = {
        "addresse": getArg()[0],
        "pseudo": getArg()[1]
    }
if infoUser:
    print("pseudo: {}, addresse: {}".format(infoUser["addresse"],infoUser["pseudo"]))

    connection(infoUser["addresse"], infoUser["pseudo"])


