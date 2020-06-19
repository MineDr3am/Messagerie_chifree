from Crypto.PublicKey import RSA


#creation d´un couple de clés
key = RSA.generate(1024)

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
with open('/home/steve-evian74/.ssh/steve.priv','r') as fk:
	priv = fk.read()
	fk.close()

with open('/home/steve-evian74/.ssh/steve.pub','r') as fp:
	pub = fp.read()
	fp.close()

privat = RSA.importKey(priv)
public = RSA.importKey(pub)


public_key = public.publickey()
enc_data = public_key.encrypt(b"""bonjour c'est un message secret""", 32)

x = privat.decrypt(enc_data)
x = x.decode('utf-8')

print(x)