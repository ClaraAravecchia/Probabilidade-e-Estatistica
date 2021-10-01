import math
import matplotlib.pyplot as plt


def XPx(x,px):
	soma = 0
	sum = 0
	for i in range(len(x)):
		soma += x[i] * px[i]
		sum += px[i]
	print("Soma de P(x) = %.2f" %sum)
	return soma


def VAR(media, x, px):
	var = 0
	for i in range(len(x)):
		sigma = ((media - x[i])**2) * px[i]
		var += sigma 
	return var

def DP(var):
	return math.sqrt(var)

def desvio(media, dp):
	min = media - dp
	max = media + dp

	min2 = media - (2*dp)
	max2 = media + (2*dp)

	min3 = media - (3*dp)
	max3 = media + (3*dp)
	print("\n")
	print("Desvio 1 - 68%%   - Min %.2f Max %.2f" %(min, max))
	print("Desvio 2 - 95%%   - Min %.2f Max %.2f" %(min2, max2))
	print("Desvio 3 - 99.7%% - Min %.2f Max %.2f" %(min3, max3))
	return (min, max, min2, max2, min3, max3)

def graph(x, px, media, var, dp, desvio):
	plt.figure(figsize=(8, 6))
	plt.title("[Media  %.2f]   [VAR  %.2f]   [DP  %.2f]" %(media, var, dp))
	plt.xlabel("X")
	plt.ylabel("P(x)")
	plt.grid(True)

	plt.plot(x, px, C = 'purple', ls='-', lw='1', marker='o')
	m = sum(px) / float(len(px))
 
	plt.plot(desvio[0:2], [m+(m/2), m+(m/2)], ls='--', color = '#10A0DF', label="68%% Min %.2f Max %.2f"%(desvio[0], desvio[1]))
	plt.plot(desvio[2:4], [m, m], ls='--', color = 'red',  label="95%% Min %.2f Max %.2f"%(desvio[2], desvio[3]))
	plt.plot(desvio[4:6], [m/2, m/2], ls='--', color = '#FFB31D', label="99.7%% Min %.2f Max %.2f"%(desvio[4], desvio[5]))
	plt.legend()
	plt.show()


x = [10, 20, 30, 40, 50, 60]
px = [.05, .2, .3, .25, .1, .1]

media = XPx(x, px)
var = VAR(media, x, px)
dp = DP(var)
print("Media - %.2f" %media)
print("VAR - %.2f" %var)
print("DP - %.2f" %dp)

d = desvio(media, dp)
# Descomentar para visualizar o grafico
graph(x, px, media, var, dp, d)
