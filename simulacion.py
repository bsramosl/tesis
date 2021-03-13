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

Ka = np.prod((yi * PresionOp)**CoefMatrix)
display(Ka)

DA = np.sum(data[:,2] * CoefMatrix)
DB = np.sum(data[:,3] * 1e-2 * CoefMatrix)


DHT0 = np.sum(data[:,0] * CoefMatrix)
DGT0 = np.sum(data[:,1] * CoefMatrix)
KT0 = np.exp(-DGT0/R/Testandar)

print('El calor de reaccion a 298.15 K es igual a {:.1f} J/mol'.format(DHT0))
print('El DG de reaccion a 298.15 K es igual a {:.1f} J/mol'.format(DGT0))
print('L constante de equilibrio quimico a 298.15 K es igual a {:.3e} J/mol'.format(KT0))

DHt = DHT0 +sp.integrate(DA +DB *t, (t, 298.15, Tout))
lnKe = np.log(KT0)+1/R *(sp.integrate(DHt/(Tout *Tout),(Tout,298.15,Tout)))
display (lnKe)


F1 = sp.log(Ka)/lnKe-1
F2 = np.sum([molesAlime[n] * sp.integrate(data[n,2]+ data[n,3]*1e-2+data[n,0]+data[n,1])
for n in np.arange(3)])+ xi * DHt

F1= lambdify((Tout, xi),F1,"numpy")
F2= lambdify((Tout, xi),F2,"numpy")







  

print('Ingresa los siguientes datos.')
A = int(input('factor de frecuencia A: '))
a=A
E = int(input('Energia de activacion: '))
e=E
T = int(input('Temperatura Inicial (R)): '))
s=T
C = int(input('capacidad calorifica de solucion (Btu/lbmolA) :'))
c=C
D = int(input('Entalpia de reaccion a la temperatura inicial:'))
d=D



def rk4(a,e,s,c,d):
    x0 = 0
    y0 = 0
    xf = int(input('Tiempo maximo(s): '))
    h = int(input('Numero del paso:'))
    n = round(((xf-x0)/h)+1)
    x = np.zeros(n)
    x[1]=x0
    
    for i in [n]:
        x[i]=x0+h*(i-1)
    y = np.zeros(n)
    y[1] = y0
    print('Tabla de resultados')
    for i in n:
        k1 = f((xi-1),y(i-1))
        k2 = f(x(i-1)+(0.5*h),y(i-1)+(0.5*k1*h))
        k3 = f(x(i-1)+(0.5*h),y(i-1)+(0.5*k2*h))
        k4 = f(x(i-1)+h,y(i-1)+(k3*h))
        y[i]=y(i-1)+((1/6)*(k1+2*k2+2*k3+k4)*h)
        u[i] = s-((d/c)*y(i))
        print(x(i),y(i),u(i))


