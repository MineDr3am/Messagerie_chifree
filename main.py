#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import sys
import time
import socket
import threading
from Crypto.PublicKey import RSA
from pprint import pprint
import re

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
            #On saisit le texte
            saisie = input("")    
            #on appelle un fonction cryptage pour chiffrer le message.
            # Affecté dans la variable de Texte avec [RSA|Destination]MessageChiffré  
            texte = crypt(saisie ,infoUser["pseudoContact"], infoUser["pseudo"])
            # On délimite les caractère afin de récupérer le nom de l'auteur
            Auteur = find_between( texte, "{RSA|", "}" )
            #On délimite les caractère afin de récupérer le message chiffré 
            Message = find_between( texte, "{RSA|"+infoUser["pseudoContact"]+"}", "Fin" )
            #on appelle la fonction déchiffrage pour déchiffrer le message. 
            Messagedecrypt = decrypt(Auteur, Message , infoUser["pseudoContact"] , infoUser["pseudo"])
            #On affiche le message
            self.socket.sendall(bytes(Messagedecrypt + "\r\n", 'utf-8'))
            time.sleep(0.001)

def connection(hote, pseudo ):
    print(hote)
    port = 666

    canal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    canal.connect((hote, port))

    Send(canal, pseudo)
    Recv(canal)

# La fonction pour déchiffrer le message
def decrypt (Destination, MessageCHiffrement , pseudoContact , pseudo):
    if pseudoContact == "steve" and pseudo == "hugue":
        if(Destination == pseudoContact ):

            with open('/home/steve-evian74/.ssh/steve.priv','r') as fp:
                priv = fp.read()
                fp.close()
            
            privat = RSA.importKey(priv)
            x = privat.decrypt(MessageCHiffrement)
            x = x.decode('utf-8')
            return x


    if pseudoContact == "hugue" and pseudo == "steve":
        if(Destination == pseudoContact ):
            with open('/home/steve-evian74/.ssh/hugue.priv','r') as fp:
                priv = fp.read()
                fp.close()
            
            privat = RSA.importKey(priv)
            x = privat.decrypt(str(MessageCHiffrement))
            x = x.decode('utf-8')
            return x

# La fonction pour chiffrer le message
def crypt(saisie , pseudoContact , pseudo):

    if pseudoContact == "steve" and pseudo == "hugue":

        
        with open('/home/steve-evian74/.ssh/steve.pub','r') as fp:
            pub = fp.read()
            fp.close()
        
        public = RSA.importKey(pub)

        public_key = public.publickey()
        my_str_as_bytes = str.encode(saisie)
        enc_data = public_key.encrypt(my_str_as_bytes, 32)[0]
        #RsaToSend = "[RSA |"+ pseudo +"]"+ str(enc_data)

        NameCrypto =  "RSA"
        Destination = pseudoContact
        MessageCrypt = enc_data
        return "{" + NameCrypto + "|" + Destination + "}" + MessageCrypt +" Fin"
        
        

    if pseudoContact == "hugue" and pseudo == "steve":
    

        with open('/home/steve-evian74/.ssh/hugue.pub','r') as fp:
            pub = fp.read()
            fp.close()
        
        public = RSA.importKey(pub)

        public_key = public.publickey()
        my_str_as_bytes = str.encode(saisie)
        enc_data = public_key.encrypt(my_str_as_bytes, 32)[0]

        #RsaToSend = "[RSA |"+ pseudo +"]"+ str(enc_data)
        NameCrypto =  "RSA"
        Destination = pseudoContact
        MessageCrypt =  str(enc_data)
        
        return "{" + NameCrypto + "|" + Destination + "}" + MessageCrypt + " Fin"

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

        try:
            pseudoContact = sys.argv[3]
        except UnboundLocalError:
            print("Une erreur est survenue pour récupérer le pseudo 'contact' ")

        return [addresse, pseudo , pseudoContact]
    else:
        return -1



def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""





NameCrypto =  ""
Destination = ""
MessageCrypt =  ""

infoUser = {}
MessageRsaSend = {}
if not getArg() == -1:
    infoUser = {
        "addresse": getArg()[0],
        "pseudo": getArg()[1],
        "pseudoContact": getArg()[2]
    }
if infoUser:

    print( "addresse: {}, pseudo: {} , pseudoContact: {} ".format(infoUser["addresse"],infoUser["pseudo"],infoUser["pseudoContact"]))

    connection(infoUser["addresse"], infoUser["pseudo"])
    

