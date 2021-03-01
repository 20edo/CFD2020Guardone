# Import necessary packages
import matplotlib.pyplot as plt
import numpy as np 
import scipy as sp
import math as mt
from scipy.optimize import fsolve

# Redefine math functions with easier name
tan = mt.tan
atan = mt.atan
cos = mt.cos
acos = mt.acos
asin = mt.asin
sin = mt.sin
pi = mt.pi
sqrt = mt.sqrt

# Inizialize fields 
P = -100.0
T = -100.0
vx, vy = -100.0, -100.0
rho = -100.0
M =-100.0

# ================================== Define problem variables
# Geometry 
eps1 = atan(0.2)
eps2 = atan(0.2)
eps3 = atan(0.2)
eps4 = atan(0.2)
chord = 1
c_b = chord*tan(eps2)/(tan(eps1)+tan(eps2))
c_c = chord - chord*tan(eps2)/(tan(eps1)+tan(eps2))
c_d = chord*tan(eps4)/(tan(eps3)+tan(eps4))
c_e = chord - chord*tan(eps4)/(tan(eps3)+tan(eps4))
x_top = c_b
y_top = c_b*tan(eps1)
x_bot = c_d 
y_bot = -c_d*tan(eps3)
alpha = 0

# Thermodynamic properties
gamma = 1.4 
Pa = 1e5
Ta = 300
R = 287.058
Ma = 2
rhoa = Pa/R/Ta

# Recall values calculated by previous script

# =============================== Values inside zones 
# Zone b
Mb = 1.5914539462643529
Pb = 182382.07623952895
Tb = 358.4359925960558
rhob = 1.7725597668291357
Vb = 604.0163953582135

# Zone c
Mc = 2.41993911
Pc = 50752.27539999
Tc = 248.70797802
rhoc = 0.71087976
Vc = 765.06466178

# Zone d
Md = 1.5914539462643529
Pd = 182382.07623952895
Td = 358.4359925960558
rhod = 1.7725597668291357
Vd = 604.0163953582135

# Zone e
Me = 2.41993911
Pe = 50752.27539999
Te = 248.70797802
rhoe = 0.71087976
Ve = 765.06466178

# Zone f
Mf = 1.9633213799324059
Pf = 100313.00454574
Tf = 304.92519096
rhof = 1.1460255
Vf = 687.2850440270618

# Zone g
Mg = 1.9633213799324059
Pg = 100313.00454574
Tg = 304.92519096
rhog = 1.1460255
Vg = 687.2850440270618

# ============================================ Angles

# Top shock 
beta_top  = 40.77535672 * pi/180

# Bottom shock
beta_bot = -40.77535672 * pi/180

# Top expansion
mu1_top = 50.23888440578768 * pi/180
mu2_top = 13.098190617128276 * pi/180

# Bottom expansion
mu1_bot = -50.23888440578768 * pi/180
mu2_bot = -13.098190617128276 * pi/180

# Top rear shock
beta_top_rear = 22.75160624 * pi/180

# Bottom rear shock
beta_bot_rear = -22.75160624 * pi/180

# Slip line 
delta_slip = 0

# Define isoentropic functions (usefull for expansion fan )

def prandtl_meyer_angle(M):
  " This function returns the prandtl meyer angle given the Mach number"
  return sqrt((gamma+1)/(gamma-1))*atan(sqrt((gamma-1)/(gamma+1)*(M**2-1)))-atan(sqrt(M**2-1))

def isoentropic(M1,M2,gamma):
  "This function calculates the fraction of actual values of P, rho and T with respect to the state 1" 
  "in an isoentropic expansion of a gas with given isoentropi coefficient gamma between the Mach values Ml and M2"
  P_rapp = (1 + (gamma-1)/2*M1**2)**(gamma/(gamma-1)) / (1 + (gamma-1)/2*M2**2)**(gamma/(gamma-1)) 
  rho_rapp = (1 + (gamma-1)/2*M1**2)**(1/(gamma-1)) / (1 + (gamma-1)/2*M2**2)**(1/(gamma-1))
  T_rapp = (1 + (gamma-1)/2*M1**2) / (1 + (gamma-1)/2*M2**2)
  return P_rapp, rho_rapp, T_rapp
  
  
# ===================================== Initialize fields
# Get points data
pdi = self.GetInput()
pdo = self.GetOutput()
# Initialize
coords		= vtk.vtkDoubleArray()
V_exact		= vtk.vtkDoubleArray()
P_exact		= vtk.vtkDoubleArray()
rho_exact	= vtk.vtkDoubleArray()
M_exact		= vtk.vtkDoubleArray()
T_exact		= vtk.vtkDoubleArray()

# Set names
coords.SetName("Coordinates")
V_exact.SetName("Exact Velocity")
P_exact.SetName("Exact Pressure")
rho_exact.SetName("Exact Density")
M_exact.SetName("Exact Mach")
T_exact.SetName("Exact Temperature")

# Set number of components
coords.SetNumberOfComponents(3)
V_exact.SetNumberOfComponents(3)
P_exact.SetNumberOfComponents(2)
rho_exact.SetNumberOfComponents(2)
M_exact.SetNumberOfComponents(2)
T_exact.SetNumberOfComponents(2)

# Get number of points
n = pdi.GetNumberOfPoints()

# =================================== Array values definition
for i in range(n):
	
	# Get the coordinate of the point
	
	p=pdi.GetPoint(i)
	x, y, z = p
	
	# Naso
	if x == 0 and y == 0:
		P_rapp, rho_rapp, T_rapp = isoentropic(Ma, 0.0 , gamma)
		P = Pa*P_rapp
		T = Ta * T_rapp
		rho = rho_rapp * rhoa
		c = sqrt(gamma*R*T)
		M = 0
		v = 0
		vx, vy = 0,0
		
	# Zone a
	elif y - tan(beta_top)*x > 0 or  y - tan(beta_bot)*x < 0  :
		P = Pa
		T = Ta
		rho = rhoa
		M = Ma
		c = sqrt(gamma*R*T)
		v = M*c
		vx, vy = v, 0


	# Zone b 
	elif y > 0 and y- tan(beta_top)*x < 0 and y - y_top - tan(mu1_top)*(x-x_top) > 0:
        	P = Pb
        	T = Tb
        	rho = rhob
        	M = Mb
        	c = sqrt(gamma*R*T)
        	v = M*c
        	vx, vy = v*cos(eps1), v*sin(eps1)

	# Expansion b-c
	elif y > 0 and y - y_top - tan(mu1_top)*(x-x_top) < 0 and y - y_top - tan(mu2_top)*(x-x_top) > 0:
	#  mu_p = atan((yp-y_top)/(xp-x_top))  # Mu of the point p
	#  M = 1 / sin(mu_p)                 # Mach of the point p
	#  P_rapp, rho_rapp, T_rapp = isoentropic(Mb, M, gamma)
	#  P = P_rapp * Pb
	#  T = T_rapp * Tb
	#  c = sqrt(gamma*R*T)             # Speed of sound of the point p
	#  v = M * c                     # Magnitude of the speed of the point p
	#  vx, vy = v*cos(mu_p), v*(-sin(mu_p))
		M1 = Mb # Mach a monte del ventaglio di espansione 
		P1 = Pb # Pressione a monte del ventaglio
		T1 = Tb # Temperatura a monte del ventaglio
		rho1 = rhob # Densità a monte del ventaglio
		theta1 = eps1 # direzione della corrente prima del ventaglio (alpha, eps1, -eps2)
		k_minus = theta1 + prandtl_meyer_angle(M1)
		dy_dx = (y-y_top)/(x-x_top)
		def func1(x,*data):
			dy_dx, k_minus = data
			return [tan(x[0]+asin(1/x[1]))-dy_dx,
x[0]+prandtl_meyer_angle(x[1])-k_minus]   # x[0] = theta_p, x[1] = M_p

		data = (dy_dx, k_minus)
		[theta_p, M_p] = fsolve(func1, [theta1, M1], args = data)

		M = M_p
		P_rapp, rho_rapp, T_rapp = isoentropic(M1, M_p, gamma)
		P = P_rapp * P1
		T = T_rapp * T1
		rho = rho_rapp * rho1
		c = sqrt(gamma*R*T)             # Speed of sound of the point p
		v = M * c                     # Magnitude of the speed of the point p
		vx, vy = v*cos(theta_p), v*sin(theta_p)


	# Zone d
	elif y < 0 and y- tan(beta_bot)*x > 0 and y - y_bot - tan(mu1_bot)*(x-x_top) < 0:
		P = Pd
		T = Td
		rho = rhod
		M = Md
		c = sqrt(gamma*R*T)
		v = M*c
		vx, vy = v*cos(eps3), -v*sin(eps3)

	# Expansion d-e
	elif y < 0 and y - y_bot - tan(mu1_bot)*(x-x_bot) > 0 and y - y_bot - tan(mu2_bot)*(x-x_bot) < 0:
	#  mu_p = - atan((yp-y_bot)/(xp-x_bot))  # Mu of the point p
	#  M = 1 / sin(mu_p)                   # Mach of the point p
	#  P_rapp, rho_rapp, T_rapp = isoentropic(Mb, M, gamma)
	#  P = P_rapp * Pb
	#  T = T_rapp * T
	#  c = sqrt(gamma*R*T)               # Speed of sound of the point p
	#  v = M * c                       # Magnitude of the speed of the point p
	#  vx, vy = v*cos(mu_p), v_p*(sin(mu_p))

		M1 = Md # Mach a monte del ventaglio di espansione 
		P1 = Pd # Pressione a monte del ventaglio
		T1 = Td # Temperatura a monte del ventaglio
		rho1 = rhod # Densità a monte del ventaglio
		theta1 = -eps3 # direzione della corrente prima del ventaglio (alpha, -eps3, eps4)
		k_plus = theta1 - prandtl_meyer_angle(M1)
		dy_dx = (y-y_bot)/(x-x_bot)
  
		def func1(x,*data):
			dy_dx, k_plus = data
			return [tan(x[0]-asin(1/x[1]))-dy_dx, x[0]-prandtl_meyer_angle(x[1])-k_plus]   # x[0] = theta_p, x[1] = M_p
		
		data = (dy_dx, k_plus)
		[theta_p, M_p] = fsolve(func1, [theta1, M1], args = data)

		M = M_p
		P_rapp, rho_rapp, T_rapp = isoentropic(M1, M_p, gamma) 
		P = P_rapp * P1
		T = T_rapp * T1
		rho = rho_rapp * rho1
		c = sqrt(gamma*R*T)             # Speed of sound of the point p
		v = M * c                     # Magnitude of the speed of the point p
		vx, vy = v*cos(theta_p), v*sin(theta_p)



# if case == 5: # doppio shock
		# Zone c
	elif y > 0 and y - y_top - tan(mu2_top)*(x-x_top) < 0 and y - tan(beta_top_rear)*(x- chord) > 0:
		P = Pc
		T = Tc
		rho = rhoc
		M = Mc
		c = sqrt(gamma*R*T)
		v = M*c
		vx, vy = v*cos(eps2), -v*sin(eps1)

		# Zone e
	elif y < 0 and y - y_bot - tan(mu2_bot)*(x-x_bot) > 0 and y - tan(beta_bot_rear)*(x- chord) < 0:
		P = Pe
		T = Te
		rho = rhoe
		M = Me
		c = sqrt(gamma*R*T)
		v = M*c
		vx, vy = v*cos(eps4), v*sin(eps4)

		# Zone f
	elif y - tan(beta_top_rear)*x < 0 and y - tan(delta_slip)*(x-chord) >= 0:
		P = Pf
		T = Tf
		rho = rhof
		M = Mf
		c = sqrt(gamma*R*T)
		v = M*c
		vx, vy = v*cos(delta_slip), v*sin(delta_slip)
		# Zone g 
	elif y - tan(beta_bot_rear)*(x- chord) > 0 and y - tan(delta_slip)*(x- chord) < 0:
		P = Pg
		T = Tg
		rho = rhog
		M = Mg
		c = sqrt(gamma*R*T)
		v = M*c
		vx, vy = v*cos(delta_slip), v*sin(delta_slip)
	else:
		P = -10
		T = -10
		rho = -10
		M = -10
		c = -10
		v = -10
		vx, vy = -10, -10	
		
    #    ================= Insert values in the arrays
	coords.InsertNextTuple3(x, y, z)
	V_exact.InsertNextTuple3(vx,vy,0)
	P_exact.InsertNextTuple2(P,0)
	rho_exact.InsertNextTuple2(rho,0)
	T_exact.InsertNextTuple2(T,0)
	M_exact.InsertNextTuple2(M,0)

# ================================= Append array fields to point data and output
pdo.GetPointData().AddArray(coords)
pdo.GetPointData().AddArray(V_exact)
pdo.GetPointData().AddArray(P_exact)
pdo.GetPointData().AddArray(rho_exact)
pdo.GetPointData().AddArray(M_exact)
pdo.GetPointData().AddArray(T_exact)

