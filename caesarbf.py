# Script criado para fins de estudos...
alpha_lower = [x for x in "abcdefghijklmnopqrstuvwxyz"]
alpha_upper = [x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
msg_enc = raw_input("Digite a mensagem cifrada: ")
for key in range(0,26):
	result = ""
	for x in msg_enc:
		if x.isupper():
			if x in alpha_upper:
				result += alpha_upper[alpha_upper.index(x)-key]
		else:
			if x in alpha_lower:
				result += alpha_lower[alpha_lower.index(x)-key]
			else:
				result += x
	if key < 9:
		print "Tentativa %s  = " %(key+1),result
	else: 
		print "Tentativa %s = " %(key+1),result
print "\nBrute force finalizado\n"
