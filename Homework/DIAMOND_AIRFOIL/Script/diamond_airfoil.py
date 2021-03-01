# -*- coding: utf-8 -*-
"""Diamond Airfoil.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jQgLQupV2iXu5KAgMoqSNYdRC-pNZf0J
"""

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# # Spero tanto che fenics sia inutile in questo caso
# # !apt-get install -y -qq software-properties-common python-software-properties module-init-tools
# # !add-apt-repository -y ppa:fenics-packages/fenics
# # !apt-get update -qq
# # !apt install -y --no-install-recommends fenics
# # !rm -rf *
# # from fenics import *
# import matplotlib.pyplot as plt
# import numpy as np 
# import scipy as sp
# from math import *
# from scipy.optimize import fsolve

# define the geometry -> angles in degrees 
#         /\
#        /  \
#       /    \
# <eps1/      \<eps2 
# <eps3\      /<eps4     alpha = AoA
#       \    /
#        \  /
#         \/
#eps1 = 10/180*pi
#eps2 = 10/180*pi 
#eps3 = 6/180*pi 
#eps4 = 6/180*pi 
eps1 = atan(0.15)
eps2 = atan(0.15)
eps3 = atan(0.15)
eps4 = atan(0.15)
chord = 1
c_b = chord*tan(eps2)/(tan(eps1)+tan(eps2))
c_c = chord - chord*tan(eps2)/(tan(eps1)+tan(eps2))
c_d = chord*tan(eps4)/(tan(eps3)+tan(eps4))
c_e = chord - chord*tan(eps4)/(tan(eps3)+tan(eps4))
x_top = c_b
y_top = c_b*tan(eps1)
x_bot = c_d 
y_bot = -c_d*tan(eps3)

print(c_b)
print(c_c)
print(c_d)
print(c_e)

eps1*180/pi

# define the upstream conditions 
Ma = 2.5
alpha = 4*pi/180
gamma = 1.4
Pa = 1e5
Ta = 300
R = 287.058
rhoa = Pa/R/Ta

def obl_shk_ang(beta, *data):
  theta, Ml, gamma = data
  return 2/tan(beta)*((Ml**2 * sin(beta)**2 - 1)/(Ml**2 * (gamma + cos(2*beta)) + 2)) - tan(theta)
def obl_shk_M_n(Ml_n, gamma):
  return sqrt((Ml_n**2 + 2/(gamma-1))/(2*gamma/(gamma-1)*Ml_n**2 - 1))
def obl_shk_P(Ml, beta, gamma):
  return (2 * gamma * Ml**2 * sin(beta)**2 - (gamma-1))/(gamma + 1)
def obl_shk_rho(Ml, beta, gamma):
  return ((gamma+1)*Ml**2*sin(beta)**2)/((gamma-1)*Ml**2*sin(beta)**2+2)
def obl_shk_T(Ml, beta, gamma):
  return (2*gamma*Ml**2*sin(beta)**2-(gamma-1))*((gamma-1)*Ml**2*sin(beta)**2+2)/((gamma+1)**2*Ml**2*sin(beta)**2)

def prandtl_meyer_angle(M):
  return sqrt((gamma+1)/(gamma-1))*atan(sqrt((gamma-1)/(gamma+1)*(M**2-1)))-atan(sqrt(M**2-1))
def M_from_nu(M, *data2):
  gamma, nu = data2
  return sqrt((gamma+1)/(gamma-1))*atan(sqrt((gamma-1)/(gamma+1)*(M**2-1)))-atan(sqrt(M**2-1)) - nu
def isoentropic_P(Ml, M2, gamma):
  return (1 + (gamma-1)/2*M1**2)**(gamma/(gamma-1)) / (1 + (gamma-1)/2*M2**2)**(gamma/(gamma-1)) 
def isoentropic_rho(Ml, M2, gamma):
  return (1 + (gamma-1)/2*M1**2)**(1/(gamma-1)) / (1 + (gamma-1)/2*M2**2)**(1/(gamma-1))
def isoentropic_T(Ml, M2, gamma):
  return (1 + (gamma-1)/2*M1**2) / (1 + (gamma-1)/2*M2**2)

# Function definitions can include multi-output.
def isoentropic(Ml,M2,gamma):
  "This function calculates the fraction of actual values of P, rho and T with respect to the state 1" 
  "in an isoentropic expansion of a gas with given isoentropi coefficient gamma between the Mach values Ml and M2"
  P_rapp = (1 + (gamma-1)/2*M1**2)**(gamma/(gamma-1)) / (1 + (gamma-1)/2*M2**2)**(gamma/(gamma-1)) 
  rho_rapp = (1 + (gamma-1)/2*M1**2)**(1/(gamma-1)) / (1 + (gamma-1)/2*M2**2)**(1/(gamma-1))
  T_rapp = (1 + (gamma-1)/2*M1**2) / (1 + (gamma-1)/2*M2**2)
  return P_rapp, rho_rapp, T_rapp

def obl_shk(Ml, beta, gamma):
  "This function calculates the jump in P, rho and T across a shockwave with Mach of Ml"
  " and a shock angle beta, for a gas with a given isoentropic coefficeint gamma"
  P_rapp = (2 * gamma * Ml**2 * sin(beta)**2 - (gamma-1))/(gamma + 1)
  rho_rapp = ((gamma+1)*Ml**2*sin(beta)**2)/((gamma-1)*Ml**2*sin(beta)**2+2)
  T_rapp = (2*gamma*Ml**2*sin(beta)**2-(gamma-1))*((gamma-1)*Ml**2*sin(beta)**2+2)/((gamma+1)**2*Ml**2*sin(beta)**2)
  return P_rapp, rho_rapp, T_rapp

# Zone b 
# zone 1 is zone a
M1 = Ma
P1 = Pa 
T1 = Ta
rho1 = rhoa

if eps1-alpha > 0: 
  # Oblique shock
  theta = eps1-alpha
  beta_0 = 2*theta # 2 volte theta funge da first try
  data = (theta, M1, gamma)
  beta = fsolve(obl_shk_ang, beta_0, args = data)
  M1_n = M1*sin(beta)
  M2_n = obl_shk_M_n(M1_n, gamma)
  M2 = M2_n/sin(beta-theta)
  P_rapp, rho_rapp, T_rapp = obl_shk(M1, beta, gamma)
  beta1 = beta
else: 
  # Expansion fan
  theta = alpha-eps1
  nu2 = theta + prandtl_meyer_angle(M1) 
  data2 = (gamma, nu2)
  M2 = fsolve(M_from_nu, M1, args = data2)  # in questo caso M1 funge da "first try"
  P_rapp, rho_rapp, T_rapp = isoentropic(M1, M2, gamma)
  # mu1 = asin(1/M1) # inclinazione inizio ventaglio di espansione
  # mu2 = asin(1/M2) # inclinazione fine ventaglio di espansione

# save data for zone b
Mb = M2 
Pb = P_rapp*P1
Tb = T_rapp*T1
rhob = rho_rapp*rho1

print(Mb)
print(Pb)
print(Tb)
print(rhob)

# Zone c 
# zone 1 is now zone b
M1 = Mb
P1 = Pb 
T1 = Tb
rho1 = rhob
 
# Expansion fan for sure
theta = eps1 + eps2
nu2 = theta + prandtl_meyer_angle(M1) 
data2 = (gamma, nu2)
M2 = fsolve(M_from_nu, M1, args = data2)  # in questo caso M1 funge da "first try"
P_rapp, rho_rapp, T_rapp = isoentropic(M1, M2, gamma)
mu1 = asin(1/M1) # inclinazione inizio ventaglio di espansione
#espansion
mu2 = asin(1/M2) # inclinazione fine ventaglio di espansione
print((mu1+eps1)*180/pi) 
print((mu2+eps1)*180/pi) 
# save data for zone c
Mc = M2 
Pc = P_rapp*P1
Tc = T_rapp*T1
rhoc = rho_rapp*rho1

print(Mc)
print(Pc)
print(Tc)
print(rhoc)

# Zone d 
M1 = Ma
P1 = Pa 
T1 = Ta
 
if eps3+alpha > 0: 
  # Oblique shock
  theta = eps3+alpha
  beta_0 = 2*theta # 2 volte theta funge da first try
  data = (theta, M1, gamma)
  beta = fsolve(obl_shk_ang, beta_0, args = data)
  print(beta)
  M1_n = M1*sin(beta)
  M2_n = obl_shk_M_n(M1_n, gamma)
  M2 = M2_n/sin(beta-theta)
  P_rapp, rho_rapp, T_rapp = obl_shk(M1, beta, gamma)
  beta2 = beta
else: 
  # Expansion fan
  theta = -(eps3+alpha)
  nu2 = theta + prandtl_meyer_angle(M1)
  data2 = (gamma, nu2)
  M2 = fsolve(M_from_nu, M1, args = data2)  # in questo caso M1 funge da "first try"
  P_rapp, rho_rapp, T_rapp = isoentropic(M1, M2, gamma)
  # mu1 = 1/sin(1/M1) # inclinazione inizio ventaglio di espansione
  # mu2 = 1/sin(1/M2) # inclinazione fine ventaglio di espansione
 
# save data for zone d
Md = M2 
Pd = P_rapp*P1
Td = T_rapp*T1

print(Md)
print(Pd/Pa)

# Zone e 
# zone 1 is now zone d
M1 = Md
P1 = Pd 
T1 = Td

# Expansion fan for sure
theta = eps3 + eps4
nu2 = theta + prandtl_meyer_angle(M1) 
data2 = (gamma, nu2)
M2 = fsolve(M_from_nu, M1, args = data2)  # in questo caso M1 funge da "first try"
P_rapp, rho_rapp, T_rapp = isoentropic(M1, M2, gamma)
# mu1 = 1/sin(1/M1) # inclinazione inizio ventaglio di espansione
# mu2 = 1/sin(1/M2) # inclinazione fine ventaglio di espansione

# save data for zone c
Me = M2 
Pe = P_rapp*P1
Te = T_rapp*T1

print(Me)
print(Pe)

# Aero coefficients 
Fb = c_b/cos(eps1)*Pb*np.array([ sin(eps1), -cos(eps1)])
Fc = c_c/cos(eps2)*Pc*np.array([-sin(eps2), -cos(eps2)])
Fd = c_d/cos(eps3)*Pd*np.array([ sin(eps3),  cos(eps3)])
Fe = c_e/cos(eps4)*Pe*np.array([-sin(eps4),  cos(eps2)])
F = Fb + Fc + Fd + Fe
cL = np.dot(F,np.array([-sin(alpha),cos(alpha)]))/(0.5*gamma*chord*Pa*Ma**2)
cD = np.dot(F,np.array([cos(alpha),sin(alpha)]))/(0.5*gamma*chord*Pa*Ma**2)
cM = (np.cross(Fb,np.array([c_b/2, c_b/2*tan(eps1)])) + 
      np.cross(Fc,np.array([chord-c_c/2,c_c/2*tan(eps2)])) + 
      np.cross(Fd,np.array([c_d/2,-c_d/2*tan(eps3)])) + 
      np.cross(Fe,np.array([chord-c_e/2,-c_e/2*tan(eps4)])))/(0.5*gamma* chord**2 *Pa*Ma**2)

print(cL)
print(cD)
print(cM)

"""Da ora in poi è solo per la slip line"""

# ora andiamo alla ricerca della slip line, devo capire in quale caso sono (2 shock, 1 shock e un ventaglio, un ventaglio e 1 shock)
# caso 1 - shock tra c ed f, continuità tra e ed g 
M1 = Mc 
P1 = Pc 
T1 = Tc

theta = eps2 + eps4
beta_0 = 2*theta # 2 volte theta funge da first try
data = (theta, M1, gamma)
beta = fsolve(obl_shk_ang, beta_0, args = data)
M1_n = M1*sin(beta)
M2_n = obl_shk_M_n(M1_n, gamma)
M2 = M2_n/sin(beta-theta)
P_rapp, rho_rapp, T_rapp = obl_shk(M1, beta, gamma)

Mf = M2 
Pf = P_rapp*P1
Tf = T_rapp*T1

Pe-Pf

# caso 2 - shock tra e ed g, continuità tra c ed f 
M1 = Me 
P1 = Pe 
T1 = Te

theta = eps2 + eps4
beta_0 = 2*theta # 2 volte theta funge da first try
data = (theta, M1, gamma)
beta = fsolve(obl_shk_ang, beta_0, args = data)
M1_n = M1*sin(beta)
M2_n = obl_shk_M_n(M1_n, gamma)
M2 = M2_n/sin(beta-theta)
P_rapp, rho_rapp, T_rapp = obl_shk(M1, beta, gamma)

Mg = M2 
Pg = P_rapp*P1
Tg = T_rapp*T1

Pc-Pg

# Le tre funzioni per risolvere il sistema non lineare nei tre casi
def case1(Delta, *data3):
  Msopra, Psopra, Tsopra, Msotto, Psotto, Tsotto, gamma, eps2, eps4 = data3
  theta = eps2 + Delta
  beta_0 = 2*theta # 2 volte theta funge da first try
  data = (theta, Msopra, gamma)
  beta = fsolve(obl_shk_ang, beta_0, args = data)
  Msopra_n = Msopra*sin(beta)
  M2sopra_n = obl_shk_M_n(Msopra_n, gamma)
  M2sopra = M2sopra_n/sin(beta-theta)
  P_rappsopra, rho_rappsopra, T_rappsopra = obl_shk(Msopra, beta, gamma)

  theta = Delta - eps4
  nu2 = theta + prandtl_meyer_angle(Msotto)
  data2 = (gamma, nu2)
  M2sotto = fsolve(M_from_nu, Msotto, args = data2)  # in questo caso M1 funge da "first try"
  P_rappsotto, rho_rappsotto, T_rappsotto = isoentropic(Msotto, M2sotto, gamma)
  return Psopra*P_rappsopra - Psotto*P_rappsotto

def case2(Delta, *data3):
  Msopra, Psopra, Tsopra, Msotto, Psotto, Tsotto, gamma, eps2, eps4 = data3

  theta = Delta - eps2
  nu2 = theta + prandtl_meyer_angle(Msopra)
  data2 = (gamma, nu2)
  M2sopra = fsolve(M_from_nu, Msopra, args = data2)  # in questo caso M1 funge da "first try"
  P_rappsopra, rho_rappsopra, T_rappsopra = isoentropic(Msopra, M2sopra, gamma)

  theta = eps4 + Delta
  beta_0 = 2*theta # 2 volte theta funge da first try
  data = (theta, Msotto, gamma)
  beta = fsolve(obl_shk_ang, beta_0, args = data)
  Msotto_n = Msotto*sin(beta)
  M2sotto_n = obl_shk_M_n(Msotto_n, gamma)
  M2sotto = M2sotto_n/sin(beta-theta)
  P_rappsotto, rho_rappsotto, T_rappsotto = obl_shk(Msotto, beta, gamma)

  return -Psopra*P_rappsopra + Psotto*P_rappsotto

def case3(Delta, *data3):
  Msopra, Psopra, Tsopra, Msotto, Psotto, Tsotto, gamma, eps2, eps4 = data3

  theta = eps2 + Delta
  beta_0 = 2*theta # 2 volte theta funge da first try
  data = (theta, Msopra, gamma)
  beta = fsolve(obl_shk_ang, beta_0, args = data)
  Msopra_n = Msopra*sin(beta)
  M2sopra_n = obl_shk_M_n(Msopra_n, gamma)
  M2sopra = M2sopra_n/sin(beta-theta)
  P_rappsopra, rho_rappsopra, T_rappsopra = obl_shk(Msopra, beta, gamma)

  theta = eps4 - Delta
  beta_0 = 2*theta # 2 volte theta funge da first try
  data = (theta, Msotto, gamma)
  beta = fsolve(obl_shk_ang, beta_0, args = data)
  Msotto_n = Msotto*sin(beta)
  M2sotto_n = obl_shk_M_n(Msotto_n, gamma)
  M2sotto = M2sotto_n/sin(beta-theta)
  P_rappsotto, rho_rappsotto, T_rappsotto = obl_shk(Msotto, beta, gamma)

  return Psopra*P_rappsopra - Psotto*P_rappsotto

if Pe > Pf:
  print("caso 1") 
  pippo = 1
  # shock sopra, ventaglio di espansione sotto
  data3 = (Mc, Pc, Tc, Me, Pe, Te, gamma, eps2, eps4)
  Delta_slip = fsolve(case1, eps4, args = data3)
  # ora mi calcolo tutti i dati 
  theta = eps2 + Delta_slip
  beta_0 = 2*theta # 2 volte theta funge da first try
  data = (theta, Mc, gamma)
  beta = fsolve(obl_shk_ang, beta_0, args = data)
  Mc_n = Mc*sin(beta)
  M2sopra_n = obl_shk_M_n(Mc_n, gamma)
  M2sopra = M2sopra_n/sin(beta-theta)
  P_rappsopra, rho_rappsopra, T_rappsopra = obl_shk(Mc, beta, gamma)
  beta5 = beta 
  
  Mf = M2sopra 
  Pf = P_rappsopra*Pc
  Tf = T_rappsopra*Tc
 
  theta = Delta_slip - eps4
  nu2 = theta + prandtl_meyer_angle(Me)
  data2 = (gamma, nu2)
  M2sotto = fsolve(M_from_nu, Me, args = data2)  # in questo caso M1 funge da "first try"
  P_rappsotto, rho_rappsotto, T_rappsotto = isoentropic(Me, M2sotto, gamma)
 
  Mg = M2sotto
  Pg = P_rappsotto*Pe
  Tg = T_rappsotto*Te
elif Pc > Pg:
  pippo = 2 
  print("caso 2")
  # shock sotto, ventaglio di espansione sopr
  data3 = (Me, Pe, Te, Mc, Pc, Tc, gamma, eps4, eps2)
  Delta_slip = fsolve(case1, eps2, args = data3)
 
  theta = -Delta_slip - eps2
  nu2 = theta + prandtl_meyer_angle(Mc)
  data2 = (gamma, nu2)
  M2sopra = fsolve(M_from_nu, Mc, args = data2)  # in questo caso M1 funge da "first try"
  P_rappsopra, rho_rappsopra, T_rappsopra = isoentropic(Mc, M2sopra, gamma)
 
  Mf = M2sopra 
  Pf = P_rappsopra*Pc
  Tf = T_rappsopra*Tc
 
  theta = eps4 - Delta_slip
  beta_0 = 2*theta # 2 volte theta funge da first try
  data = (theta, Me, gamma)
  beta = fsolve(obl_shk_ang, beta_0, args = data)
  Msotto_n = Me*sin(beta)
  M2sotto_n = obl_shk_M_n(Msotto_n, gamma)
  M2sotto = M2sotto_n/sin(beta-theta)
  P_rappsotto, rho_rappsotto, T_rappsotto = obl_shk(Me, beta, gamma)
  beta6 = beta
 
  Mg = M2sotto
  Pg = P_rappsotto*Pe
  Tg = T_rappsotto*Te
else: 
  pippo = 3
  print("caso 3")
  # Shock sopra e sotto
  data3 = (Mc, Pc, Tc, Me, Pe, Te, gamma, eps2, eps4)
  Delta_slip = fsolve(case3, 0, args = data3)
 
  theta = eps2 + Delta_slip
  beta_0 = 2*theta # 2 volte theta funge da first try
  data = (theta, Mc, gamma)
  beta = fsolve(obl_shk_ang, beta_0, args = data)
  print(beta) 
  Msopra_n = Mc*sin(beta)
  M2sopra_n = obl_shk_M_n(Msopra_n, gamma)
  M2sopra = M2sopra_n/sin(beta-theta)
  P_rappsopra, rho_rappsopra, T_rappsopra = obl_shk(Mc, beta, gamma)
  beta7 = beta
 
  Mf = M2sopra 
  Pf = P_rappsopra*Pc
  Tf = T_rappsopra*Tc
 
  theta = eps4 - Delta_slip
  beta_0 = 2*theta # 2 volte theta funge da first try
  data = (theta, Me, gamma)
  beta = fsolve(obl_shk_ang, beta_0, args = data)
  Msotto_n = Me*sin(beta)
  M2sotto_n = obl_shk_M_n(Msotto_n, gamma)
  M2sotto = M2sotto_n/sin(beta-theta)
  P_rappsotto, rho_rappsotto, T_rappsotto = obl_shk(Me, beta, gamma)
  beta8 = beta
 
  Mg = M2sotto
  Pg = P_rappsotto*Pe
  Tg = T_rappsotto*Te

print(Delta_slip*180/pi) # angolo della slip line rispetto all'orizzontale ----->x
print(Mf)
print(Pf)
print(Mg)
print(Pg)
# we have just one shock on the top part 
print(beta*180/pi)
print((beta-eps2)*180/pi) # angolo della shock wave rispetto all'orizzontale ----->x

# find the velocity of a point inside the top expansion fan
# Define fictional values of the point coordinstes
#xp = 2
#yp = 0.7
#mu_p = atan((yp-y_top)/(xp-x_top))  # Mu of the point p
#M_p = 1 / sin(mu_p)                 # Mach of the point p
#P_rapp, rho_rapp, T_rapp = isoentropic(Mb, M_p, gamma)
#P_p = P_rapp * Pb
#T_p = T_rapp * Tb
#c_p = sqrt(gamma*R*T_p)             # Speed of sound of the point p
#v_p = M_p * c_p                     # Magnitude of the speed of the point p
#vx_p, vy_p = v_p*cos(mu_p), v_p*(-sin(mu_p))

# VENTAGLIO DI ESPANSIONE SU TOP DEL PRFILO 
xp = 0.711306 # x del punto 
yp = 0.220404 # y del punto
xv = 0.5 # x del vertice del ventaglio di espansione 
yv = 0.1 # y del vertice del ventaglio di espansione 
M1 = 1.59 # Mach a monte del ventaglio di espansione 
P1 = 0 # Pressione a monte del ventaglio
T1 = 0 # Temperatura a monte del ventaglio
theta1 = eps1 # direzione della corrente prima del ventaglio (alpha, eps1, -eps2)
k_minus = theta1 + prandtl_meyer_angle(M1)
dy_dx = (yp-y_top)/(xp-x_top)

def func1(x,*data):
  dy_dx, k_minus = data
  return [tan(x[0]+asin(1/x[1]))-dy_dx,
          x[0]+prandtl_meyer_angle(x[1])-k_minus]   # x[0] = theta_p, x[1] = M_p

data = (dy_dx, k_minus)
[theta_p, M_p] = fsolve(func1, [theta1, M1], args = data)

P_rapp, rho_rapp, T_rapp = isoentropic(M1, M_p, gamma)
P_p = P_rapp * P1
T_p = T_rapp * T1
c_p = sqrt(gamma*R*T_p)             # Speed of sound of the point p
v_p = M_p * c_p                     # Magnitude of the speed of the point p
vx_p, vy_p = v_p*cos(theta_p), v_p*sin(theta_p)

print(M_p)
print(theta_p*180/pi)
print(dy_dx*180/pi)

# find the velocity of a point inside the bottom expansion fan
# Define fictional values of the point coordinstes
#xp = 2
#yp = -0.7
#mu_p = - atan((yp-y_bot)/(xp-x_bot))  # Mu of the point p
#M_p = 1 / sin(mu_p)                   # Mach of the point p
#P_rapp, rho_rapp, T_rapp = isoentropic(Mb, M_p, gamma)
#P_p = P_rapp * Pb
#T_p = T_rapp * Tb
#c_p = sqrt(gamma*R*T_p)               # Speed of sound of the point p
#v_p = M_p * c_p                       # Magnitude of the speed of the point p
#vx_p, vy_p = v_p*cos(mu_p), v_p*(sin(mu_p))

# VENTAGLIO DI ESPANSIONE SU BOTTOM DEL PRFILO 
xp = 1.5 # x del punto 
yp = -0.4 # y del punto
xv = 0.5 # x del vertice del ventaglio di espansione 
yv = -0.1 # y del vertice del ventaglio di espansione 
M1 = 1.59 # Mach a monte del ventaglio di espansione 
P1 = 0 # Pressione a monte del ventaglio
T1 = 0 # Temperatura a monte del ventaglio
theta1 = -eps3 # direzione della corrente prima del ventaglio (alpha, -eps3, eps4)
k_plus = theta1 - prandtl_meyer_angle(M1)
dy_dx = (yp-yv)/(xp-xv)

def func2(x,*data):
  dy_dx, k_plus = data
  return [tan(x[0]-asin(1/x[1]))-dy_dx,
          x[0]-prandtl_meyer_angle(x[1])-k_plus]   # x[0] = theta_p, x[1] = M_p

data = (dy_dx, k_plus)
[theta_p, M_p] = fsolve(func2, [theta1, M1], args = data)

P_rapp, rho_rapp, T_rapp = isoentropic(M1, M_p, gamma)
P_p = P_rapp * P1
T_p = T_rapp * T1
c_p = sqrt(gamma*R*T_p)             # Speed of sound of the point p
v_p = M_p * c_p                     # Magnitude of the speed of the point p
vx_p, vy_p = v_p*cos(theta_p), v_p*sin(theta_p)

print(M_p)
print(theta_p*180/pi)
print(dy_dx*180/pi)

print("TUTTI GLI ANGOLI SONO DATI RISPETTO ALL'ORIZZONTALE ")
print("----->")
print("     x \n")

print("Zone a - Ma = " + str(Ma))
print("Zone a - Pa = " + str(Pa) + " Pa")
print("Zone a - Ta = " + str(Ta) + " K")
print("Zone a - rhoa = " + str(Pa/R/Ta) + " Kg/m^3")
print("Zone a - Va = " + str(Ma*sqrt(gamma*R*Ta)) + " m/s \n")

if eps1-alpha > 0:
  print("Tra zona a e b ho shock con angolo beta = " + str((beta1+alpha)*180/pi) + " [deg]\n")
else: 
  print("Tra zona a e b ho ventaglio con angoli: ")
  print("Inizio ventaglio = " + str((alpha+asin(1/Ma))*180/pi) +" [deg]")
  print("Fine ventaglio = " + str((eps1 + asin(1/Mb))*180/pi) + " [deg]\n")

print("Zone b - Mb = " + str(Mb))
print("Zone b - Pb = " + str(Pb) + " Pa")
print("Zone b - Tb = " + str(Tb) + " K")
print("Zone b - rhob = " + str(Pb/R/Tb) + " Kg/m^3")
print("Zone b - Vb = " + str(Mb*sqrt(gamma*R*Tb)) + " m/s \n")

print("Tra zona b e c ho ventaglio con angoli: ")
print("Inizio ventaglio = " + str((eps1+asin(1/Mb))*180/pi) +" [deg]")
print("Fine ventaglio = " + str((-eps2 + asin(1/Mc))*180/pi) + " [deg]\n")

print("Zone c - Mc = " + str(Mc))
print("Zone c - Pc = " + str(Pc) + " Pa")
print("Zone c - Tc = " + str(Tc) + " K")
print("Zone c - rhoc = " + str(Pc/R/Tc) + " Kg/m^3")
print("Zone c - Vc = " + str(Mc*sqrt(gamma*R*Tc)) + " m/s \n")

if eps3+alpha > 0:
  print("Tra zona a e d ho shock con angolo beta = " + str((-beta2+alpha)*180/pi) + " [deg]\n")
else: 
  print("Tra zona a e d ho ventaglio con angoli: ")
  print("Inizio ventaglio = " + str((alpha-asin(1/Ma))*180/pi) +" [deg]")
  print("Fine ventaglio = " + str((-eps3 - asin(1/Md))*180/pi) + " [deg]\n")

print("Zone d - Md = " + str(Md))
print("Zone d - Pd = " + str(Pd) + " Pa")
print("Zone d - Td = " + str(Td) + " K")
print("Zone d - rhod = " + str(Pd/R/Td) + " Kg/m^3")
print("Zone d - Vd = " + str(Md*sqrt(gamma*R*Td)) + " m/s \n")

print("Tra zona d e e ho ventaglio con angoli: ")
print("Inizio ventaglio = " + str((-eps3 - asin(1/Md))*180/pi) +" [deg]")
print("Fine ventaglio = " + str((eps4 - asin(1/Me))*180/pi) + " [deg]\n")

print("Zone e - Me = " + str(Me))
print("Zone e - Pe = " + str(Pe) + " Pa")
print("Zone e - Te = " + str(Te) + " K")
print("Zone e - rhoe = " + str(Pe/R/Te) + " Kg/m^3")
print("Zone e - Ve = " + str(Me*sqrt(gamma*R*Te)) + " m/s \n")

print("La slip line ha un angolo rispetto all'orizzontale di " + str(Delta_slip*180/pi) + " [deg]\n")
if pippo == 1: 
  print("Tra zona c e f ho una shock con angolo rispetto all'orizzontale di " + str((beta5-eps2)*180/pi) + " [deg]\n")
  print("Tra zona e e g ho un ventaglio:")
  print("Inizio ventaglio = " + str((eps4 - asin(1/Me))*180/pi) +" [deg]")
  print("Fine ventaglio = " + str((Delta_slip - asin(1/Mg))*180/pi) + " [deg]\n")
elif pippo == 2:
  print("Tra zona c e f ho un ventaglio:")
  print("Inizio ventaglio = " + str((-eps2 + asin(1/Mc))*180/pi) +" [deg]")
  print("Fine ventaglio = " + str((Delta_slip + asin(1/Mf))*180/pi) + " [deg]\n")
  print("Tra zona e e g ho una shock con angolo rispetto all'orizzontale di " + str((-beta6+eps4)*180/pi) + " [deg]\n")
elif pippo == 3: 
  print("Tra zona c e f ho una shock con angolo rispetto all'orizzontale di " + str((beta7-eps2)*180/pi) + " [deg]\n")
  print("Tra zona e e g ho una shock con angolo rispetto all'orizzontale di " + str((-beta8+eps4)*180/pi) + " [deg]\n")


print("Zone f - Mf = " + str(Mf))
print("Zone f - Pf = " + str(Pf) + " Pa")
print("Zone f - Tf = " + str(Tf) + " K")
print("Zone f - rhof = " + str(Pf/R/Tf) + " Kg/m^3")
print("Zone f - Vf = " + str(Mf*sqrt(gamma*R*Tf)) + " m/s \n")

print("Zone g - Mg = " + str(Mg))
print("Zone g - Pg = " + str(Pg) + " Pa")
print("Zone g - Tg = " + str(Tg) + " K")
print("Zone g - rhog = " + str(Pg/R/Tg) + " Kg/m^3")
print("Zone g - Vg = " + str(Mg*sqrt(gamma*R*Tg)) + " m/s \n")