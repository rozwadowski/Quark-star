# -*- coding: utf-8 -*-
 
import numpy as np
import matplotlib.pyplot as plt


f = open("quark2.dat")

r = []
m = []

for line in f:
	column = line.split(" ")
	m.append(float(column[2]))
	r.append(float(column[1]))
	
plt.xlabel("Radius [km]")
plt.ylabel("Mass [Sun mass]")
plt.plot(r,m,"g-")
plt.show()
