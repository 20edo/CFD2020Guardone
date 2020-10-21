# =================================== Import packages needed
import numpy as np
import math as mt
import scipy as sp
from scipy.optimize import fsolve

pdi = self.GetInput()
pdo = self.GetOutput()

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
R = 8314/29
Ma = 2

# Recall values calculated by previous script

# Top shock 
beta_top  = 40 * pi/180

# Bottom shock
beta_bot = 40 * pi/180

# Top expansion
mu1_top = 24 * pi/180
mu2_top = 16 * pi/180

# Zone b
Mb = 1.59
Pb = 1.823
rhob = 2
Tb = 400

# Zone c

# Define isoentropic functions (usefull for expansion fan )

def prandtl_meyer_angle(M):
  " This function returns the prandtl meyer angle given the Mach number"
  return sqrt((gamma+1)/(gamma-1))*atan(sqrt((gamma-1)/(gamma+1)*(M**2-1)))-atan(sqrt(M**2-1))

def isoentropic(Ml,M2,gamma):
  "This function calculates the fraction of actual values of P, rho and T with respect to the state 1" 
  "in an isoentropic expansion of a gas with given isoentropi coefficient gamma between the Mach values Ml and M2"
  P_rapp = (1 + (gamma-1)/2*M1**2)**(gamma/(gamma-1)) / (1 + (gamma-1)/2*M2**2)**(gamma/(gamma-1)) 
  rho_rapp = (1 + (gamma-1)/2*M1**2)**(1/(gamma-1)) / (1 + (gamma-1)/2*M2**2)**(1/(gamma-1))
  T_rapp = (1 + (gamma-1)/2*M1**2) / (1 + (gamma-1)/2*M2**2)
  return P_rapp, rho_rapp, T_rapp


# ===================================== Initialize fields
# Initialize
coords 		= vtk.vtkDoubleArray()
V_exact 	= vtk.vtkDoubleArray()
P_exact 	= vtk.vtkDoubleArray()
rho_exact	= vtk.vtkDoubleArray()
M_exact		= vtk.vtkDoubleArray()
T_exact		= vtk.vtkDoubleArray()

# Set names
coords.SetName("Coordinates")
V_exact.SetName("Exact Velocity")
P_exact.SetName("Exact Pressure")
rho_exact.SetName("Exact Density")
M_exact.SetName("Exact Mack")
T_exact.SetName("Exact Temperature")

# Set number of components
coords.SetNumberOfComponents(3)
V_exact.SetNumberOfComponents(3)
P_exact.SetNumberOfComponents(1)
rho_exact.SetNumberOfComponents(1)
M_exact.SetNumberOfComponents(1)
T_exact.SetNumberOfComponents(1)

# Get number of points
n = pdi.GetNumberOfPoints()

# =================================== Array values definition
for i in range(n):
	
	p=pdi.GetPoint(i)
	x, y, z = p
	coords.InsertNextTuple3(x, y, z)
	
	# Freestream zone
	if x < 5:
        	V_exact.InsertNextTuple3(np.cos(mt.pi+x), 10, 0)
	else:
		V_exact.InsertNextTuple3(0, -10, 0)
    

# ================================= Append array fields to point data and output
pdo.GetPointData().AddArray(coords)
pdo.GetPointData().AddArray(V_exact)
pdo.GetPointData().AddArray(P_exact)
pdo.GetPointData().AddArray(rho_exact)
pdo.GetPointData().AddArray(M_exact)
pdo.GetPointData().AddArray(T_exact)

