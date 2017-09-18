import math
import matplotlib.pyplot as plt

G=6.674 * 10**(-8) #cm^3 g^-1 s^-1
c= 2.99792458 * 10**(10) #cgs
a= 0.2 * (c**2)
b=0.3 * (c**2)
rho_0= 10**14
rho_c=8*(10**14)
h=5
vr=[]
vm=[]

def P (rho):
    if rho<rho_c :
        cis=a*(rho-rho_0)
    else:
        cis= a*(rho_c-rho_0) + b*(rho-rho_c)
        
    return cis
        
def dRHOdR (r,rho,m,rho00):
    if rho00<rho_c:
        x=a
    else:
        x=b
    dRHOdR=((-G*rho*m)/(x*r**2))*(1+(P(rho)/(rho*(c**2))))*(1+((4*math.pi*P(rho)*r**3)/(m*(c**2))))*(1-((2*G*m)/(r*(c**2))))**(-1)
    
    return dRHOdR
    
def K1(r,rho,m,rho00):
    k1=h* dRHOdR(r,rho,m,rho00)
    return k1
    
def K2 (r,rho,m,k1,rho00):
    k2=h*dRHOdR(r+0.5*h,rho+0.5*k1,m,rho00)
    return k2

def K3 (r,rho,m,k2,rho00):
    k3=h*dRHOdR(r+0.5*h,rho+0.5*k2,m,rho00)
    return k3
    
def K4 (r,rho,m,k3,rho00):
    k4=h*dRHOdR(r+h,rho+k3,m,rho00)
    return k4
    
#warunki brzegowe
rho1=500*(10**14)
rho=rho1
m=0.000000000001
r=0.00000000001

while P(rho)>0.:
    vm.append(m)
    vr.append(r)
    rho00=rho
    k1=K1(r,rho,m,rho00)
    k2=K2(r,rho,m,k1,rho00)
    k3=K3(r,rho,m,k2,rho00)
    k4=K4(r,rho,m,k3,rho00)
    
    drho=(1./6.) *(k1+2*k2+2*k3+k4)
    rho=rho+drho
    r=r+h
    dm=4*math.pi*(r**2)*rho*h
    m=m+dm
    
    #print P(rho)
    #print m
    #print r
    #print rho
    
print m/1.9891e33,r/100000    
f1=plt.figure()
plt.plot(vr,vm,'r-',label='m')
f1.savefig('wyk.png')
    
