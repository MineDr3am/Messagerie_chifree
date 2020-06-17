from Crypto.PublicKey import RSA


#creation d un couple de cles
key = RSA.generate(1024)

#chiffrage
public_key = key.publickey()
enc_data = public_key.encrypt(b"""bonjour c'est un message secret""", 32)

#dechiffrage
x = key.decrypt(enc_data)
x = x.decode('utf-8')

#afficher ses cles:
k = key.exportKey('PEM')
p = key.publickey().exportKey('PEM')

#sauvegarder ses cles dans des fichiers:
with open('private.priv','w') as kf:
	kf.write(k.decode())
	kf.close()

with open('public.pub','w') as pf:
	pf.write(p.decode())
	pf.close()

#importer des cles a partir d'un fichier
with open('private.priv','r') as fk:
	priv = fk.read()
	fk.close()

with open('public.pub','r') as fp:
	pub = fp.read()
	fp.close()

privat = RSA.importKey(priv)
public = RSA.importKey(pub)
