# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Unstructured Grid Reader'
flowvtu = XMLUnstructuredGridReader(FileName=['/home/edo20/CFD2020_Guardone/Homework/DIAMOND_AIRFOIL/Working_dir/CFD/flow.vtu'])

# create a new 'XML Unstructured Grid Reader'
surface_flowvtu = XMLUnstructuredGridReader(FileName=['/home/edo20/CFD2020_Guardone/Homework/DIAMOND_AIRFOIL/Working_dir/CFD/surface_flow.vtu'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1435, 795]

# show data in view
surface_flowvtuDisplay = Show(surface_flowvtu, renderView1)

# trace defaults for the display properties.
surface_flowvtuDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.CameraPosition = [0.5, 0.0, 10000.0]
renderView1.CameraFocalPoint = [0.5, 0.0, 0.0]

# show data in view
flowvtuDisplay = Show(flowvtu, renderView1)

# trace defaults for the display properties.
flowvtuDisplay.Representation = 'Surface'

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(flowvtu)

# hide data in view
Hide(surface_flowvtu, renderView1)

# change representation type
flowvtuDisplay.SetRepresentationType('Surface With Edges')

# set scalar coloring
ColorBy(flowvtuDisplay, ('POINTS', 'Mach'))

# rescale color and/or opacity maps used to include current data range
flowvtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
flowvtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Mach'
machLUT = GetColorTransferFunction('Mach')
machLUT.RGBPoints = [0.8355953693389893, 0.0, 0.0, 0.34902, 0.882905900478363, 0.039216, 0.062745, 0.380392, 0.9302164316177368, 0.062745, 0.117647, 0.411765, 0.9775269627571106, 0.090196, 0.184314, 0.45098, 1.0248374938964844, 0.12549, 0.262745, 0.501961, 1.0721480250358582, 0.160784, 0.337255, 0.541176, 1.119458556175232, 0.2, 0.396078, 0.568627, 1.1667690873146057, 0.239216, 0.454902, 0.6, 1.2140796184539795, 0.286275, 0.521569, 0.65098, 1.2613901495933533, 0.337255, 0.592157, 0.701961, 1.308700680732727, 0.388235, 0.654902, 0.74902, 1.3560112118721008, 0.466667, 0.737255, 0.819608, 1.4033217430114746, 0.572549, 0.819608, 0.878431, 1.4506322741508484, 0.654902, 0.866667, 0.909804, 1.4979428052902222, 0.752941, 0.917647, 0.941176, 1.545253336429596, 0.823529, 0.956863, 0.968627, 1.5925638675689697, 0.988235, 0.960784, 0.901961, 1.5925638675689697, 0.941176, 0.984314, 0.988235, 1.622842607498169, 0.988235, 0.945098, 0.85098, 1.6531213474273683, 0.980392, 0.898039, 0.784314, 1.6871849298477173, 0.968627, 0.835294, 0.698039, 1.734495460987091, 0.94902, 0.733333, 0.588235, 1.7818059921264648, 0.929412, 0.65098, 0.509804, 1.8291165232658386, 0.909804, 0.564706, 0.435294, 1.8764270544052124, 0.878431, 0.458824, 0.352941, 1.9237375855445862, 0.839216, 0.388235, 0.286275, 1.97104811668396, 0.760784, 0.294118, 0.211765, 2.0183586478233337, 0.701961, 0.211765, 0.168627, 2.0656691789627075, 0.65098, 0.156863, 0.129412, 2.1129797101020813, 0.6, 0.094118, 0.094118, 2.160290241241455, 0.54902, 0.066667, 0.098039, 2.207600772380829, 0.501961, 0.05098, 0.12549, 2.2549113035202026, 0.45098, 0.054902, 0.172549, 2.3022218346595764, 0.4, 0.054902, 0.192157, 2.34953236579895, 0.34902, 0.070588, 0.211765]
machLUT.ColorSpace = 'Lab'
machLUT.NanColor = [0.25, 0.0, 0.0]
machLUT.Discretize = 0
machLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Mach'
machPWF = GetOpacityTransferFunction('Mach')
machPWF.Points = [0.8355953693389893, 0.0, 0.5, 0.0, 2.34953236579895, 1.0, 0.5, 0.0]
machPWF.ScalarRangeInitialized = 1

# change representation type
flowvtuDisplay.SetRepresentationType('Surface')

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.5, 0.0, 10000.0]
renderView1.CameraFocalPoint = [0.5, 0.0, 0.0]
renderView1.CameraParallelScale = 0.5099019516515143

# save screenshot
SaveScreenshot('/home/edo20/CFD2020_Guardone/Homework/DIAMOND_AIRFOIL/Working_dir/POST-PROCESSING/Mach_Near.png', renderView1, ImageResolution=[5740, 3180],
    OverrideColorPalette='BlackBackground')

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
R = 287.058
Ma = 2
rhoa = Pa/R/Ta

# Recall values calculated by previous script

# =============================== Values inside zones 
# Zone b
Mb = 1.5914539462643529
Pb = 182382.07623952895
rhob = 1.7725597668291357
Tb = 358.4359925960558

# Zone c
Mc = 2.41993911
Pc = 50752.27539999
rhoc = 0.71087976
Tc = 248.70797802

# Zone d
Md = 1.5914539462643529
Pd = 182382.07623952895
rhod = 1.7725597668291357
Td = 358.4359925960558

# Zone e
Me = 2.41993911
Pe = 50752.27539999
rhoe = 0.71087976
Te = 248.70797802

# Zone f
Mf = 1.9633213799324059
Pf = 100313.00454574
rhof = 1.1460255
Tf = 304.92519096

# Zone f
Mg = 1.9633213799324059
Pg = 100313.00454574
rhog = 1.1460255
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
\tif x == 0.0 and y == 0.0:
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
\telif y - tan(beta_top)*x > 0 or  y - tan(beta_bot)*x < 0  :
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
exactMachLUT.RGBPoints = [0.0, 0.0, 0.0, 0.34902, 0.0756230971875, 0.039216, 0.062745, 0.380392, 0.151246194375, 0.062745, 0.117647, 0.411765, 0.22686929156250002, 0.090196, 0.184314, 0.45098, 0.30249238875, 0.12549, 0.262745, 0.501961, 0.3781154859375, 0.160784, 0.337255, 0.541176, 0.45373858312500004, 0.2, 0.396078, 0.568627, 0.5293616803125, 0.239216, 0.454902, 0.6, 0.6049847775, 0.286275, 0.521569, 0.65098, 0.6806078746875001, 0.337255, 0.592157, 0.701961, 0.756230971875, 0.388235, 0.654902, 0.74902, 0.8318540690625, 0.466667, 0.737255, 0.819608, 0.9074771662500001, 0.572549, 0.819608, 0.878431, 0.9831002634375, 0.654902, 0.866667, 0.909804, 1.058723360625, 0.752941, 0.917647, 0.941176, 1.1343464578125, 0.823529, 0.956863, 0.968627, 1.209969555, 0.988235, 0.960784, 0.901961, 1.209969555, 0.941176, 0.984314, 0.988235, 1.2583683372, 0.988235, 0.945098, 0.85098, 1.3067671194000001, 0.980392, 0.898039, 0.784314, 1.3612157493750001, 0.968627, 0.835294, 0.698039, 1.4368388465625, 0.94902, 0.733333, 0.588235, 1.51246194375, 0.929412, 0.65098, 0.509804, 1.5880850409375, 0.909804, 0.564706, 0.435294, 1.663708138125, 0.878431, 0.458824, 0.352941, 1.7393312353125001, 0.839216, 0.388235, 0.286275, 1.8149543325000002, 0.760784, 0.294118, 0.211765, 1.8905774296875, 0.701961, 0.211765, 0.168627, 1.966200526875, 0.65098, 0.156863, 0.129412, 2.0418236240625, 0.6, 0.094118, 0.094118, 2.11744672125, 0.54902, 0.066667, 0.098039, 2.1930698184375, 0.501961, 0.05098, 0.12549, 2.268692915625, 0.45098, 0.054902, 0.172549, 2.3443160128125, 0.4, 0.054902, 0.192157, 2.41993911, 0.34902, 0.070588, 0.211765]
exactMachLUT.ColorSpace = 'Lab'
exactMachLUT.NanColor = [0.25, 0.0, 0.0]
exactMachLUT.Discretize = 0
exactMachLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'ExactMach'
exactMachPWF = GetOpacityTransferFunction('ExactMach')
exactMachPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.41993911, 1.0, 0.5, 0.0]
exactMachPWF.ScalarRangeInitialized = 1

# set active source
SetActiveSource(flowvtu)

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(Input=flowvtu)

# set active source
SetActiveSource(programmableFilter1)

# set active source
SetActiveSource(appendAttributes1)

# set active source
SetActiveSource(flowvtu)

# destroy appendAttributes1
Delete(appendAttributes1)
del appendAttributes1

# set active source
SetActiveSource(programmableFilter1)

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(Input=[flowvtu, programmableFilter1])

# show data in view
appendAttributes1Display = Show(appendAttributes1, renderView1)

# trace defaults for the display properties.
appendAttributes1Display.Representation = 'Surface'

# hide data in view
Hide(programmableFilter1, renderView1)

# hide data in view
Hide(flowvtu, renderView1)

# show color bar/color legend
appendAttributes1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(appendAttributes1Display, ('POINTS', 'Exact Mach', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(machLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
appendAttributes1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
appendAttributes1Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(appendAttributes1Display, ('POINTS', 'Mach'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(exactMachLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
appendAttributes1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
appendAttributes1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Calculator'
calculator1 = Calculator(Input=appendAttributes1)

# Properties modified on calculator1
calculator1.ResultArrayName = 'Mach_Difference'
calculator1.Function = 'Mach - Exact Mach_Y'

# show data in view
calculator1Display = Show(calculator1, renderView1)

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'

# hide data in view
Hide(appendAttributes1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'Mach_Difference'
mach_DifferenceLUT = GetColorTransferFunction('Mach_Difference')
mach_DifferenceLUT.RGBPoints = [0.8355953693389893, 0.0, 0.0, 0.34902, 0.882905900478363, 0.039216, 0.062745, 0.380392, 0.9302164316177368, 0.062745, 0.117647, 0.411765, 0.9775269627571106, 0.090196, 0.184314, 0.45098, 1.0248374938964844, 0.12549, 0.262745, 0.501961, 1.0721480250358582, 0.160784, 0.337255, 0.541176, 1.119458556175232, 0.2, 0.396078, 0.568627, 1.1667690873146057, 0.239216, 0.454902, 0.6, 1.2140796184539795, 0.286275, 0.521569, 0.65098, 1.2613901495933533, 0.337255, 0.592157, 0.701961, 1.308700680732727, 0.388235, 0.654902, 0.74902, 1.3560112118721008, 0.466667, 0.737255, 0.819608, 1.4033217430114746, 0.572549, 0.819608, 0.878431, 1.4506322741508484, 0.654902, 0.866667, 0.909804, 1.4979428052902222, 0.752941, 0.917647, 0.941176, 1.545253336429596, 0.823529, 0.956863, 0.968627, 1.5925638675689697, 0.988235, 0.960784, 0.901961, 1.5925638675689697, 0.941176, 0.984314, 0.988235, 1.622842607498169, 0.988235, 0.945098, 0.85098, 1.6531213474273683, 0.980392, 0.898039, 0.784314, 1.6871849298477173, 0.968627, 0.835294, 0.698039, 1.734495460987091, 0.94902, 0.733333, 0.588235, 1.7818059921264648, 0.929412, 0.65098, 0.509804, 1.8291165232658386, 0.909804, 0.564706, 0.435294, 1.8764270544052124, 0.878431, 0.458824, 0.352941, 1.9237375855445862, 0.839216, 0.388235, 0.286275, 1.97104811668396, 0.760784, 0.294118, 0.211765, 2.0183586478233337, 0.701961, 0.211765, 0.168627, 2.0656691789627075, 0.65098, 0.156863, 0.129412, 2.1129797101020813, 0.6, 0.094118, 0.094118, 2.160290241241455, 0.54902, 0.066667, 0.098039, 2.207600772380829, 0.501961, 0.05098, 0.12549, 2.2549113035202026, 0.45098, 0.054902, 0.172549, 2.3022218346595764, 0.4, 0.054902, 0.192157, 2.34953236579895, 0.34902, 0.070588, 0.211765]
mach_DifferenceLUT.ColorSpace = 'Lab'
mach_DifferenceLUT.NanColor = [0.25, 0.0, 0.0]
mach_DifferenceLUT.Discretize = 0
mach_DifferenceLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Mach_Difference'
mach_DifferencePWF = GetOpacityTransferFunction('Mach_Difference')
mach_DifferencePWF.Points = [0.8355953693389893, 0.0, 0.5, 0.0, 2.34953236579895, 1.0, 0.5, 0.0]
mach_DifferencePWF.ScalarRangeInitialized = 1

# set active source
SetActiveSource(appendAttributes1)

# set active source
SetActiveSource(calculator1)

# hide data in view
Hide(calculator1, renderView1)

# set active source
SetActiveSource(calculator1)

# show data in view
calculator1Display = Show(calculator1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.8546586948049825, -0.0303070459150703, 546.4101615137755]
renderView1.CameraFocalPoint = [0.8546586948049825, -0.0303070459150703, 0.0]
renderView1.CameraParallelScale = 0.9956240290281356

# save screenshot
SaveScreenshot('/home/edo20/CFD2020_Guardone/Homework/DIAMOND_AIRFOIL/Working_dir/POST-PROCESSING/Mach_Difference.png', renderView1, ImageResolution=[5740, 3180])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.8546586948049825, -0.0303070459150703, 546.4101615137755]
renderView1.CameraFocalPoint = [0.8546586948049825, -0.0303070459150703, 0.0]
renderView1.CameraParallelScale = 0.9956240290281356

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).