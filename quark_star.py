# -*- coding: utf-8 -*-
 
import numpy as np
import matplotlib.pyplot as plt

#CONST
c = 29979245800. #[cm/s]
a = 0.2*c**2
b = 0.3*c**2
rho_0 = 1.e14 #[g/cm3]
rho_c = 8.e14 #[g/cm3]
G = 6.67259e-8 #[cm3g-1s-2]
M_sun = 1.9891e33

def P(rho):
	if rho<rho_c:
		return a*(rho-rho_0)
	else:
		return a*(rho_c-rho_0)+b*(rho-rho_c)

def f_M(r,rho):
	return 4*np.pi*rho*r**2

def f_rho(r,rho):
	if rho<rho_c:
		return -G/a*M*rho/r/r* (1+P(rho)/rho/c/c)*(1+4*np.pi*r**3*P(rho)/M/c/c)*(1-2*G*M/r/c/c)**-1
	else:
		return -G/b*M*rho/r/r * (1+P(rho)/rho/c/c)*(1+4*np.pi*r**3*P(rho)/M/c/c)*(1-2*G*M/r/c/c)**-1

rho_tab = np.linspace(1000*rho_0,2000*rho_0,10)
#print rho_tab
for rho in rho_tab:
	print rho,
	M=0.00000001
	r=0.00000001
	dr=10
	while P(rho)>0.:

		k1 = dr*f_rho(r,rho)
		k2 = dr*f_rho(r+dr/2,rho+0.5*k1)
		k3 = dr*f_rho(r+dr/2,rho+0.5*k2)
		k4 = dr*f_rho(r+dr,rho+k3)
		rho=rho+(k1+2*k2+2*k3+k4)/6.
		dM = f_M(r,rho)*dr 
		M=M+dM
		r = r + dr
		#if r%100000==0:
		#print r/100000., M/M_sun

	print r/100000., M/M_sun

