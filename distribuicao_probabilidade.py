import math as m

def combinacao(N, P):
	c = ( m.factorial(N) ) / ( m.factorial(N-P) * m.factorial(P) )
	return c


def p_binomial(N, P, Q, K):
	binomial = 0
	for i in K:
		binomial += combinacao(N, i) * ( P**i ) * ( Q ** (N-i) )
	return binomial



# k precisa estar dentro da lista
k = [12, 13, 14, 15, 16]
b = p_binomial(16, 0.75, 0.25, k)


#b = (1 - b) * 100
b = (b) * 100
print("%.4f%%" %b)
