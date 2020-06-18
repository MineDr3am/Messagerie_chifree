import sys
import time
import socket
import threading
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


class Recv(threading.Thread):
    socket = None
    cipher  = None
    data = ''

    def __init__(self, canal, cipher):
        self.socket = canal
        self.cipher = cipher
        threading.Thread.__init__(self)
        self.setDaemon = True
        self.start()

    def run(self):
        while True:
            self.data = self.data + self.socket.recv(1).decode('utf-8')
            if "\r\n" in self.data:
                if "[AES]" in self.data:
                    data2 = self.data
                    pseudo = self.data.split(">")[0]
                    self.data = self.data.split("'")[1]
                    self.data =  pseudo + "> " + self.cipher.decrypt(self.data)

                    if self.data == pseudo + "> ":
                        self.data = data2

                print(self.data)
                self.data = ''
            time.sleep(0.001)

class Send(threading.Thread):
    socket = None
    cipher = None

    def __init__(self, canal, pseudo, cipher):
        self.socket = canal
        self.cipher = cipher
        threading.Thread.__init__(self)
        self.setDaemon = True
        self.start()
        self.socket.sendall(bytes("#pseudo=" + pseudo + "\r\n", 'utf-8'))

    def run(self):
        while True:
            saisie = self.cipher.encrypt(input(""))
            self.socket.sendall(bytes("[AES]" + str(saisie) + "\r\n", 'utf-8'))
            time.sleep(0.001)
def tcp(user):
    print(user["adresse"])
    port = 666

    cipher = AESCipher(user["key"])
    canal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    canal.connect((user["adresse"], port))

    Send(canal, user["pseudo"], cipher)
    Recv(canal, cipher)



def getArg():
    if len(sys.argv) >= 3:
        try:
            adresse = sys.argv[1]
        except:
            print("Une erreur est survenue pour récupérer l'adresse ")
        try:
            pseudo = sys.argv[2]
        except UnboundLocalError:
            print("Une erreur est survenue pour récupérer le pseudo")
        try:
            key = sys.argv[3]
        except UnboundLocalError:
            print("Une erreur est survenue pour récupérer le pseudo")

        return [adresse, pseudo, key]
    else:
        return -1


class AESCipher(object):

    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

infoUser = {}
if not getArg() == -1:
    infoUser = {
        "adresse": getArg()[0],
        "pseudo": getArg()[1],
        "key": getArg()[2]
    }
if infoUser:
    print("pseudo: {}, adresse: {}".format(infoUser["adresse"],infoUser["pseudo"]))

    tcp(infoUser)
