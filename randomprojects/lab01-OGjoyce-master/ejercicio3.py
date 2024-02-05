import sys

'''MODIFIQUE ESTOS VALORES PARA ACOMODAR LOS $1000 EN LOS 10 SOBRES'''
ENV_1 = 1
ENV_2 = 2
ENV_3 = 4
ENV_4 = 8
ENV_5 = 16
ENV_6 = 32
ENV_7 = 64
ENV_8 = 132
ENV_9 = 256
ENV_10 = 512

'''NO TOCAR NADA A PARTIR DE ESTA LINEA'''
def getTotal():
	total = ENV_1+ENV_2+ENV_3+ENV_4+ENV_5
	total+= ENV_6+ENV_7+ENV_8+ENV_9+ENV_10
	return total == 1000

def isPossible(number):
	envelopes = list()
	envelopes.append(ENV_1)
	envelopes.append(ENV_2)
	envelopes.append(ENV_3)
	envelopes.append(ENV_4)
	envelopes.append(ENV_5)
	envelopes.append(ENV_6)
	envelopes.append(ENV_7)
	envelopes.append(ENV_8)
	envelopes.append(ENV_9)
	envelopes.append(ENV_10)
	envelopes.sort(reverse = True)
	for envelope in envelopes:
		if number >= envelope:
			number -= envelope
			if number == 0:
				return True
	return False

def check():
	total = 0
	for count in range(1,1001):
		if isPossible(count):
			total+=1
	print total

def main(n):
	if getTotal():
		if  (n > 0) and (n < 1001):
			if isPossible(n):
				print "Es posible combinar los sobres para un total de " + str(n)
			else:
				print "No es posible combilar los sobres para un total de " + str(n)
		else:
			print "Parametros invalidos"
	else:
		print "El total en los sobres no suma 1,000"


if __name__ == "__main__":
	if len(sys.argv) == 1:
		check()
	else:
		main(int(sys.argv[1]))
