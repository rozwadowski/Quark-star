# -*- coding: utf-8 -*-
 
import numpy as np
import matplotlib.pyplot as plt

c = 29979245800. #[cm/s]
a = 0.2*c**2
b = 0.3*c**2
rho_0 = 1.e14 #[g/cm3]
rho_c = 8.e14
p = []

def P(rho):
	if rho<rho_0:
		return 0
	elif rho<rho_c:
		return a*(rho-rho_0)
	else:
		return a*(rho-rho_0)+b*(rho-rho_c)

rho = np.linspace(rho_0,50*rho_0,1000000)

for r in rho:
	p.append(P(r))

plt.xlabel("Density [gm/cm3]")
plt.ylabel("Pressure [b]")
plt.plot(rho,p)
plt.show()
