#coding: utf-8
# Script criado para fins de estudos...
alpha_lower = [x for x in "abcdefghijklmnopqrstuvwxyz"] # Alfabeto de letrar minusculas ['a','b','c',...,'z']
alpha_upper = [x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"] # Alfabeto de letras maiusculas ['A','B','C',...,'Z']
msg_enc = raw_input("Digite a mensagem cifrada: ") # Recebe a mensagem cifrada
for key in range(0,26): # Para cada chave possivel
	result = "" # Resultado final
	for x in msg_enc: # Para cada letra da mensagem cifrada
		if x.isupper(): # se a letra estiver em maiuscula
			result += alpha_upper[alpha_upper.index(x)-key] # adicione ao resultado a letra que estiver na posição da letra atual - a chave
		else: # se não
			if x in alpha_lower: # se a letra estiver em minuscula
				result += alpha_lower[alpha_lower.index(x)-key] # adicione ao resultado a letra que estiver na posição da letra atual - a chave
			else: # caso seja outro tipo de caracter
				result += x # adicione o caracter, sem nenhuma mudança
	if key < 9: # só p embelezar o output
		print "Tentativa %s  = " %(key+1),result # só p embelezar o output
	else:  # s p embelezar o output
		print "Tentativa %s = " %(key+1),result # só p embelezar o output
print "\nBrute force finalizado\n" # FIM
