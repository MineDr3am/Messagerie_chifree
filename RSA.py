from Crypto.PublicKey import RSA


#creation d´un couple de clés
#key = RSA.generate(1024)

#chiffrage
#public_key = key.publickey()
#enc_data = public_key.encrypt(b"""bonjour c'est un message secret""", 32)

# dechiffrage
# x = key.decrypt(enc_data)
# x = x.decode('utf-8')

# afficher ses clés:
# k = key.exportKey('PEM')
# p = key.publickey().exportKey('PEM')


#importer des clés à partir d'un fichier
with open('/home/steve-evian74/.ssh/hugue.priv','r') as fk:
	priv = fk.read()
	fk.close()

with open('/home/steve-evian74/.ssh/steve.pub','r') as fp:
	pub = fp.read()
	fp.close()

privat = RSA.importKey(priv)
public = RSA.importKey(pub)


# Je crypte le message avec la clé public de Steve. 
public_key = public.publickey()
enc_data = public_key.encrypt(b"""bonjour c'est un message secret""", 32)

RsaToSend = "[RSA|steve]" + str(enc_data)
print(RsaToSend) 
print(RsaToSend)
#Je decrypte le message avec la clé privé de steve 
print(type(enc_data))
x = privat.decrypt(enc_data)
x = x.decode('utf-8')

print(x)

