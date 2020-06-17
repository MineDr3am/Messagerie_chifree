from Crypto.PublicKey import RSA

key = RSA.generate(1024)

k = key.exportKey('PEM')

p = key.publickey().exportKey('PEM')

with open('private.pem','w') as kf:
	kf.write(k.decode())
	kf.close()

with open('public.pem','w') as pf:
	pf.write(p.decode())
	pf.close()