import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import fsolve
from sympy import solve, integrate, symbols

#A
#Équation pour trouver k avec 4 chiffres après la virgule
def valeur_k(C, rho, r):
    return round(0.5 * C * rho * math.pi*r**2, 4)

#Valeurs des variables
C = 0.5
rho = 1.293
r = 0.15

#Obtenir le résultat (k)
print(valeur_k(C, rho, r))

#B
#Équation pour trouver t
def equation(t):
    m = 1
    g = 9.81
    k = 0.0228
    return 10 - ((m * g / k) ** 0.5 * t + m / k * np.log((np.exp(-2 * t * (k * g / m) ** 0.5) + 1) / 2))

#Estimation initiale de la solution
guess = 1

#Résolution de l'équation
t_solution = fsolve(equation, guess)

#Obtenir le résulat (t) avec 3 chiffres après la virgule
print("La valeur de t est :", round(t_solution[0], 3),'s')

#C
#Variables dans l'équation
vx, vx0, t, k, m = symbols('vx vx0 t k m')

#Équation de base
t=1/vx**2

#Borne inférieure
inf = symbols('vx0')

#Borne supérieure
sup = symbols('vx')

#Intégrale de la vitesse en x
v_x = integrate(t,(vx, inf, sup))
print("-kt/m =", v_x)

#Variables dans la deuxième intégrale
x, vx0, t, k, m = symbols('x vx0 t k m')

#Équation
x = (1/vx0 + k*t/m)**(-1)

#Borne inférieure
inf = 0

#Borne supérieure
sup = symbols('t')

#Intégrale de la position en x
x_integrale = integrate(x,(t, inf, sup))

#Obtenir l'équation de la positon en x
print("x =",x_integrale)

#D
#Ajouter les valeurs dans l'équation pour obtenir x_max
values = {vx0: 15, t: 1.483, k: 0.0228, m: 1}
x_max = x_integrale.subs(values)

#Obtenir le résultat avec 3 chiffres après la virgule
print("La valeur de x après intégration est :", round(x_max, 3),'m')
#E

# Définir les valeurs possibles dans le graphique 
valeur_t = np.linspace(0, 3)

# Définir les constantes
m = 1
g = 9.81
k = 0.0228
vx0 = 1
# Définir les équations dans l'air
def xair(t):
    return -m * np.log(m) / k + m * np.log(k * vx0 * t + m) / k
def yair(t):
    return 10 - ((m * g / k) ** 0.5 * t + m / k * np.log((np.exp(-2 * t * (k * g / m) ** 0.5) + 1) / 2))
# Définir les équations dans le vide
def xvide(t):
    return vx0 * t
def yvide(t):
    return 10 - 0.5 * g * t**2
#valeurs correspondantes de x et y pour chaque t
valeur_xair = xair(valeur_t)
valeur_yair = yair(valeur_t)
valeur_xvide = xvide(valeur_t)
valeur_yvide = yvide(valeur_t)
# tracer le graphique de y en fonction de x
plt.figure(figsize=(8, 6))
plt.plot(valeur_xair, valeur_yair, label='Dans l\'air')
plt.plot(valeur_xvide, valeur_yvide, label='Dans le vide')
plt.title('Graphique paramétrique de y en fonction de x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()