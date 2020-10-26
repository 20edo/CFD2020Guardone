# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Unstructured Grid Reader'
flowvtu = XMLUnstructuredGridReader(FileName=['/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil3/Working_dir/CFD/flow.vtu'])

# create a new 'XML Unstructured Grid Reader'
surface_flowvtu = XMLUnstructuredGridReader(FileName=['/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil3/Working_dir/CFD/surface_flow.vtu'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1435, 795]

# show data in view
flowvtuDisplay = Show(flowvtu, renderView1)

# trace defaults for the display properties.
flowvtuDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10000.0]

# show data in view
surface_flowvtuDisplay = Show(surface_flowvtu, renderView1)

# trace defaults for the display properties.
surface_flowvtuDisplay.Representation = 'Surface'

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(flowvtu)

# change representation type
flowvtuDisplay.SetRepresentationType('Surface With Edges')

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10000.0]
renderView1.CameraParallelScale = 141.4213562373095

# save screenshot
SaveScreenshot('/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil3/Working_dir/POST-PROCESSING/Mesh_far.png', renderView1, ImageResolution=[5740, 3180])

# create a new 'Programmable Filter'
programmableFilter1 = ProgrammableFilter(Input=flowvtu)

# Properties modified on programmableFilter1
programmableFilter1.Script = """# Import necessary packages
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
R = 8314/29
Ma = 2
rhoa = Pa/R/Ta

# Recall values calculated by previous script

# =============================== Values inside zones 
# Zone b
Mb = 1.5914539462643529
Pb = 182382.07623952895
rhob = 1.774837188458829
Tb = 358.4359925960558

# Zone c
Mc = 2.41993911
Pc = 50752.27539999
rhoc = 0.71179311
Tc = 248.70797802

# Zone d
Md = 1.5914539462643529
Pd = 182382.07623952895
rhod = 1.774837188458829
Td = 358.4359925960558 

# Zone e
Me = 2.41993911
Pe = 50752.27539999
rhoe = 0.71179311
Te = 248.70797802

# Zone f
Mf = 1.9633213799324059
Pf = 100313.00454574
rhof = 1.14749793
Tf = 304.92519096

# Zone g
Mg = 1.9633213799324059
Pg = 100313.00454574
rhog = 1.14749793
Tg = 304.92519096

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
coords\t\t= vtk.vtkDoubleArray()
V_exact\t\t= vtk.vtkDoubleArray()
P_exact\t\t= vtk.vtkDoubleArray()
rho_exact\t= vtk.vtkDoubleArray()
M_exact\t\t= vtk.vtkDoubleArray()
T_exact\t\t= vtk.vtkDoubleArray()

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
\t
\t# Get the coordinate of the point
\t
\tp=pdi.GetPoint(i)
\tx, y, z = p
\t
\t# Naso
\tif x == 0 and y == 0:
\t\tP_rapp, rho_rapp, T_rapp = isoentropic(Ma, 0.0 , gamma)
\t\tP = Pa*P_rapp
\t\tT = Ta * T_rapp
\t\trho = rho_rapp * rhoa
\t\tc = sqrt(gamma*R*T)
\t\tM = 0
\t\tv = 0
\t\tvx, vy = 0,0
\t\t
\t# Zone a
\tif y - tan(beta_top)*x > 0 or  y - tan(beta_bot)*x < 0  :
\t\tP = Pa
\t\tT = Ta
\t\trho = rhoa
\t\tM = Ma
\t\tc = sqrt(gamma*R*T)
\t\tv = M*c
\t\tvx, vy = v, 0


\t# Zone b 
\telif y > 0 and y- tan(beta_top)*x < 0 and y - y_top - tan(mu1_top)*(x-x_top) > 0:
        \tP = Pb
        \tT = Tb
        \trho = rhob
        \tM = Mb
        \tc = sqrt(gamma*R*T)
        \tv = M*c
        \tvx, vy = v*cos(eps1), v*sin(eps1)

\t# Expansion b-c
\telif y > 0 and y - y_top - tan(mu1_top)*(x-x_top) < 0 and y - y_top - tan(mu2_top)*(x-x_top) > 0:
\t#  mu_p = atan((yp-y_top)/(xp-x_top))  # Mu of the point p
\t#  M = 1 / sin(mu_p)                 # Mach of the point p
\t#  P_rapp, rho_rapp, T_rapp = isoentropic(Mb, M, gamma)
\t#  P = P_rapp * Pb
\t#  T = T_rapp * Tb
\t#  c = sqrt(gamma*R*T)             # Speed of sound of the point p
\t#  v = M * c                     # Magnitude of the speed of the point p
\t#  vx, vy = v*cos(mu_p), v*(-sin(mu_p))
\t\tM1 = Mb # Mach a monte del ventaglio di espansione 
\t\tP1 = Pb # Pressione a monte del ventaglio
\t\tT1 = Tb # Temperatura a monte del ventaglio
\t\ttheta1 = eps1 # direzione della corrente prima del ventaglio (alpha, eps1, -eps2)
\t\tk_minus = theta1 + prandtl_meyer_angle(M1)
\t\tdy_dx = (y-y_top)/(x-x_top)
\t\tdef func1(x,*data):
\t\t\tdy_dx, k_minus = data
\t\t\treturn [tan(x[0]+asin(1/x[1]))-dy_dx,
x[0]+prandtl_meyer_angle(x[1])-k_minus]   # x[0] = theta_p, x[1] = M_p

\t\tdata = (dy_dx, k_minus)
\t\t[theta_p, M_p] = fsolve(func1, [theta1, M1], args = data)

\t\tM = M_p
\t\tP_rapp, rho_rapp, T_rapp = isoentropic(M1, M_p, gamma)
\t\tP = P_rapp * P1
\t\tT = T_rapp * T1
\t\tc = sqrt(gamma*R*T)             # Speed of sound of the point p
\t\tv = M * c                     # Magnitude of the speed of the point p
\t\tvx, vy = v*cos(theta_p), v*sin(theta_p)


\t# Zone d
\telif y < 0 and y- tan(beta_bot)*x > 0 and y - y_bot - tan(mu1_bot)*(x-x_top) < 0:
\t\tP = Pd
\t\tT = Td
\t\trho = rhod
\t\tM = Md
\t\tc = sqrt(gamma*R*T)
\t\tv = M*c
\t\tvx, vy = v*cos(eps3), -v*sin(eps3)

\t# Expansion d-e
\telif y < 0 and y - y_bot - tan(mu1_bot)*(x-x_bot) > 0 and y - y_bot - tan(mu2_bot)*(x-x_bot) < 0:
\t#  mu_p = - atan((yp-y_bot)/(xp-x_bot))  # Mu of the point p
\t#  M = 1 / sin(mu_p)                   # Mach of the point p
\t#  P_rapp, rho_rapp, T_rapp = isoentropic(Mb, M, gamma)
\t#  P = P_rapp * Pb
\t#  T = T_rapp * T
\t#  c = sqrt(gamma*R*T)               # Speed of sound of the point p
\t#  v = M * c                       # Magnitude of the speed of the point p
\t#  vx, vy = v*cos(mu_p), v_p*(sin(mu_p))

\t\tM1 = Md # Mach a monte del ventaglio di espansione 
\t\tP1 = Pd # Pressione a monte del ventaglio
\t\tT1 = Td # Temperatura a monte del ventaglio
\t\ttheta1 = -eps3 # direzione della corrente prima del ventaglio (alpha, -eps3, eps4)
\t\tk_plus = theta1 - prandtl_meyer_angle(M1)
\t\tdy_dx = (y-y_bot)/(x-x_bot)
  
\t\tdef func1(x,*data):
\t\t\tdy_dx, k_plus = data
\t\t\treturn [tan(x[0]-asin(1/x[1]))-dy_dx, x[0]-prandtl_meyer_angle(x[1])-k_plus]   # x[0] = theta_p, x[1] = M_p
\t\t
\t\tdata = (dy_dx, k_plus)
\t\t[theta_p, M_p] = fsolve(func1, [theta1, M1], args = data)

\t\tM = M_p
\t\tP_rapp, rho_rapp, T_rapp = isoentropic(M1, M_p, gamma) 
\t\tP = P_rapp * P1
\t\tT = T_rapp * T1
\t\tc = sqrt(gamma*R*T)             # Speed of sound of the point p
\t\tv = M * c                     # Magnitude of the speed of the point p
\t\tvx, vy = v*cos(theta_p), v*sin(theta_p)



# if case == 5: # doppio shock
\t\t# Zone c
\telif y > 0 and y - y_top - tan(mu2_top)*(x-x_top) < 0 and y - tan(beta_top_rear)*(x- chord) > 0:
\t\tP = Pc
\t\tT = Tc
\t\trho = rhoc
\t\tM = Mc
\t\tc = sqrt(gamma*R*T)
\t\tv = M*c
\t\tvx, vy = v*cos(eps2), -v*sin(eps1)

\t\t# Zone e
\telif y < 0 and y - y_bot - tan(mu2_bot)*(x-x_bot) > 0 and y - tan(beta_bot_rear)*(x- chord) < 0:
\t\tP = Pe
\t\tT = Te
\t\trho = rhoe
\t\tM = Me
\t\tc = sqrt(gamma*R*T)
\t\tv = M*c
\t\tvx, vy = v*cos(eps4), v*sin(eps4)

\t\t# Zone f
\telif y - tan(beta_top_rear)*x < 0 and y - tan(delta_slip)*(x-chord) >= 0:
\t\tP = Pf
\t\tT = Tf
\t\trho = rhof
\t\tM = Mf
\t\tc = sqrt(gamma*R*T)
\t\tv = M*c
\t\tvx, vy = v*cos(delta_slip), v*sin(delta_slip)
\t\t# Zone g 
\telif y - tan(beta_bot_rear)*(x- chord) > 0 and y - tan(delta_slip)*(x- chord) < 0:
\t\tP = Pg
\t\tT = Tg
\t\trho = rhog
\t\tM = Mg
\t\tc = sqrt(gamma*R*T)
\t\tv = M*c
\t\tvx, vy = v*cos(delta_slip), v*sin(delta_slip)
\telse:
\t\tP = -10
\t\tT = -10
\t\trho = -10
\t\tM = -10
\t\tc = -10
\t\tv = -10
\t\tvx, vy = -10, -10\t
\t\t
    #    ================= Insert values in the arrays
\tcoords.InsertNextTuple3(x, y, z)
\tV_exact.InsertNextTuple3(vx,vy,0)
\tP_exact.InsertNextTuple2(P,0)
\trho_exact.InsertNextTuple2(rho,0)
\tT_exact.InsertNextTuple2(T,0)
\tM_exact.InsertNextTuple2(M,0)

# ================================= Append array fields to point data and output
pdo.GetPointData().AddArray(coords)
pdo.GetPointData().AddArray(V_exact)
pdo.GetPointData().AddArray(P_exact)
pdo.GetPointData().AddArray(rho_exact)
pdo.GetPointData().AddArray(M_exact)
pdo.GetPointData().AddArray(T_exact)
"""
programmableFilter1.RequestInformationScript = ''
programmableFilter1.RequestUpdateExtentScript = ''
programmableFilter1.PythonPath = ''

# show data in view
programmableFilter1Display = Show(programmableFilter1, renderView1)

# trace defaults for the display properties.
programmableFilter1Display.Representation = 'Surface'

# hide data in view
Hide(flowvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(programmableFilter1Display, ('POINTS', 'Exact Mach', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
programmableFilter1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
programmableFilter1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'ExactMach'
exactMachLUT = GetColorTransferFunction('ExactMach')

# get opacity transfer function/opacity map for 'ExactMach'
exactMachPWF = GetOpacityTransferFunction('ExactMach')

# set scalar coloring
ColorBy(programmableFilter1Display, ('POINTS', 'Exact Mach', 'X'))

# rescale color and/or opacity maps used to exactly fit the current data range
programmableFilter1Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(exactMachLUT, programmableFilter1Display)

# Rescale transfer function
exactMachLUT.RescaleTransferFunction(0.0, 2.4199391099999996)

# Rescale transfer function
exactMachPWF.RescaleTransferFunction(0.0, 2.4199391099999996)

# change representation type
programmableFilter1Display.SetRepresentationType('Surface With Edges')

# change representation type
programmableFilter1Display.SetRepresentationType('Surface')

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.8429452549230618, 0.0429526244546783, 10000.0]
renderView1.CameraFocalPoint = [0.8429452549230618, 0.0429526244546783, 0.0]
renderView1.CameraParallelScale = 0.8228297760563104

# save screenshot
SaveScreenshot('/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil3/Working_dir/POST-PROCESSING/Mach_near.png', renderView1, ImageResolution=[5740, 3180])

# set active source
SetActiveSource(surface_flowvtu)

# create a new 'Plot Data'
plotData1 = PlotData(Input=surface_flowvtu)

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
# uncomment following to set a specific view size
# lineChartView1.ViewSize = [400, 400]

# show data in view
plotData1Display = Show(plotData1, lineChartView1)

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Rescale transfer function
exactMachLUT.RescaleTransferFunction(-10.0, 2.41993911)

# Rescale transfer function
exactMachPWF.RescaleTransferFunction(-10.0, 2.41993911)

# save data
SaveData('/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil3/Working_dir/POST-PROCESSING/Dati_surface.csv', proxy=plotData1, Precision=7,
    UseScientificNotation=1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.8429452549230618, 0.0429526244546783, 10000.0]
renderView1.CameraFocalPoint = [0.8429452549230618, 0.0429526244546783, 0.0]
renderView1.CameraParallelScale = 0.8228297760563104

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).