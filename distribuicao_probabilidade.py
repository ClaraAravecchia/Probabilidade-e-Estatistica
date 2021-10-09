import math as m
import matplotlib.pyplot as plt

def combinacao(N, P):
	c = ( m.factorial(N) ) / ( m.factorial(N-P) * m.factorial(P) )
	return c


def p_binomial(N, P, Q, K):
	binomial = 0
	for i in K:
		binomial += combinacao(N, i) * ( P**i ) * ( Q ** (N-i) )
	return binomial


def graph(x, px):
        plt.figure(figsize=(8, 6))
        #plt.title("[Media  %.2f]   [VAR  %.2f]   [DP  %.2f]" %(media, var, dp))
        plt.xlabel("X")
        plt.ylabel("P(x)")
        plt.grid(True)

        plt.plot(x, px, C = 'purple', ls='-', lw='1', marker='o')
        
        plt.legend()
        plt.show()


# k precisa estar dentro da lista
k = [1, 2, 3]
b = p_binomial(4, .07, .93, k)

#graph([1, 3, 5, 7, 9], [.1, .2, .4, .2, .1])
#b = (1 - b) * 100
b = (b) * 100
print("%.f%%" %b)
