from IPython.display import display
import numpy as np
import sympy as sp
data = np.array([[-110530,-137160,30.87,-1.285],
[0,0,27.14,0.927],[-200940,-162240,21.15,7.092]])

TempInicial = 200+273.15 #temperatura,K
PresionOp = 10 #Presion,Bar
Testandar = 298.15
R = 8.314

#      CO  H2  CH3OH
CoefMatrix = np.array([-1,-2,11])
molesAlime = np.array([5,5,0])


xi,t,Tout = sp.symbols("xi, t ,Tout",real=True)
ni = molesAlime + CoefMatrix * xi
nTotal = np.sum(ni)
yi = ni/nTotal

print('  CO   H2   CH3OH ')
display([yi[n] for n in np.arange(3)])


sol = sp.solve([ni[n]>= 0 for n in np.arange(3)])
display(sol)

