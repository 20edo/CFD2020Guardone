# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Unstructured Grid Reader'
flowvtu = XMLUnstructuredGridReader(FileName=['/home/edo20/CFD2020Guardone/Homework/DIAMOND_AIRFOIL/Working_dir/CFD/flow.vtu'])
flowvtu.PointArrayStatus = ['Density', 'Momentum', 'Energy', 'Pressure', 'Temperature', 'Mach', 'Pressure_Coefficient']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
renderView1.ViewSize = [1132, 795]

# show data in view
flowvtuDisplay = Show(flowvtu, renderView1)

# trace defaults for the display properties.
flowvtuDisplay.Representation = 'Surface'
flowvtuDisplay.ColorArrayName = [None, '']
flowvtuDisplay.OSPRayScaleArray = 'Density'
flowvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
flowvtuDisplay.SelectOrientationVectors = 'Density'
flowvtuDisplay.ScaleFactor = 20.0
flowvtuDisplay.SelectScaleArray = 'Density'
flowvtuDisplay.GlyphType = 'Arrow'
flowvtuDisplay.GlyphTableIndexArray = 'Density'
flowvtuDisplay.GaussianRadius = 1.0
flowvtuDisplay.SetScaleArray = ['POINTS', 'Density']
flowvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
flowvtuDisplay.OpacityArray = ['POINTS', 'Density']
flowvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
flowvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
flowvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
flowvtuDisplay.ScalarOpacityUnitDistance = 10.67438550346949

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
flowvtuDisplay.ScaleTransferFunction.Points = [0.5517352223396301, 0.0, 0.5, 0.0, 1.9102725982666016, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
flowvtuDisplay.OpacityTransferFunction.Points = [0.5517352223396301, 0.0, 0.5, 0.0, 1.9102725982666016, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10000.0]

# update the view to ensure updated data information
renderView1.Update()

# change representation type
flowvtuDisplay.SetRepresentationType('Surface With Edges')

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10000.0]
renderView1.CameraParallelScale = 1

# save screenshot
SaveScreenshot('/home/edo20/CFD2020Guardone/Homework/DIAMOND_AIRFOIL/Working_dir/POST-PROCESSING/Mesh_far.png', renderView1, ImageResolution=[2264, 1590],
    OverrideColorPalette='WhiteBackground')

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.44005830668682094, -0.01100145766717052, 10000.0]
renderView1.CameraFocalPoint = [0.44005830668682094, -0.01100145766717052, 0.0]
renderView1.CameraParallelScale = 1.2047050751240445

# save screenshot
SaveScreenshot('/home/edo20/CFD2020Guardone/Homework/DIAMOND_AIRFOIL/Working_dir/POST-PROCESSING/Mesh_near.png', renderView1, ImageResolution=[2264, 1590],
    OverrideColorPalette='WhiteBackground')

# change representation type
flowvtuDisplay.SetRepresentationType('Surface')

# create a new 'Calculator'
calculator1 = Calculator(Input=flowvtu)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'Velocity'
calculator1.Function = 'Momentum/Density'

# show data in view
calculator1Display = Show(calculator1, renderView1)

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = [None, '']
calculator1Display.OSPRayScaleArray = 'Density'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'Velocity'
calculator1Display.ScaleFactor = 20.0
calculator1Display.SelectScaleArray = 'Density'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'Density'
calculator1Display.GaussianRadius = 1.0
calculator1Display.SetScaleArray = ['POINTS', 'Density']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'Density']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityUnitDistance = 10.67438550346949

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [0.5517352223396301, 0.0, 0.5, 0.0, 1.9102725982666016, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [0.5517352223396301, 0.0, 0.5, 0.0, 1.9102725982666016, 1.0, 0.5, 0.0]

# hide data in view
Hide(flowvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=calculator1,
    SeedType='High Resolution Line Source')
streamTracer1.Vectors = ['POINTS', 'Velocity']
streamTracer1.MaximumStreamlineLength = 200.0

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-50.0, -50.0, 0.0]
streamTracer1.SeedType.Point2 = [50.0, 50.0, 0.0]

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1)

# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.ColorArrayName = [None, '']
streamTracer1Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer1Display.SelectOrientationVectors = 'Normals'
streamTracer1Display.ScaleFactor = 19.997671508789065
streamTracer1Display.SelectScaleArray = 'AngularVelocity'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer1Display.GaussianRadius = 0.9998835754394532
streamTracer1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(streamTracer1Display, ('POINTS', 'Velocity', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
streamTracer1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Velocity'
velocityLUT = GetColorTransferFunction('Velocity')
velocityLUT.RGBPoints = [490, 0.231373, 0.298039, 0.752941, 579.669619210583, 0.865003, 0.865003, 0.865003, 720, 0.705882, 0.0156863, 0.14902]
velocityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Velocity'
velocityPWF = GetOpacityTransferFunction('Velocity')
velocityPWF.Points = [392.9133964785527, 0.0, 0.5, 0.0, 766.4258419426135, 1.0, 0.5, 0.0]
velocityPWF.ScalarRangeInitialized = 1

# set active source
SetActiveSource(flowvtu)

# set active source
SetActiveSource(flowvtu)

# show data in view
flowvtuDisplay = Show(flowvtu, renderView1)

# set scalar coloring
ColorBy(flowvtuDisplay, ('POINTS', 'Density'))

# rescale color and/or opacity maps used to include current data range
flowvtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
flowvtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Density'
densityLUT = GetColorTransferFunction('Density')
densityLUT.RGBPoints = [0.65, 0.231373, 0.298039, 0.752941, 1.2310039103031158, 0.865003, 0.865003, 0.865003, 1.9, 0.705882, 0.0156863, 0.14902]
densityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Density'
densityPWF = GetOpacityTransferFunction('Density')
densityPWF.Points = [0.5517352223396301, 0.0, 0.5, 0.0, 1.9102725982666016, 1.0, 0.5, 0.0]
densityPWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
densityLUT.ApplyPreset('X Ray', True)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.44005830668682094, -0.01100145766717052, 10000.0]
renderView1.CameraFocalPoint = [0.44005830668682094, -0.01100145766717052, 0.0]
renderView1.CameraParallelScale = 1.4576931409000935

# save screenshot
SaveScreenshot('/home/edo20/CFD2020Guardone/Homework/DIAMOND_AIRFOIL/Working_dir/POST-PROCESSING/Streamlines.png', renderView1, ImageResolution=[3056, 1590],
    OverrideColorPalette='WhiteBackground')

# set active source
SetActiveSource(streamTracer1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(flowvtu)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.44005830668682094, -0.01100145766717052, 10000.0]
renderView1.CameraFocalPoint = [0.44005830668682094, -0.01100145766717052, 0.0]
renderView1.CameraParallelScale = 1.4576931409000935

# save screenshot
SaveScreenshot('/home/edo20/CFD2020Guardone/Homework/DIAMOND_AIRFOIL/Working_dir/POST-PROCESSING/Streamlines.png', renderView1, ImageResolution=[3056, 1590],
    OverrideColorPalette='WhiteBackground')

# set active source
SetActiveSource(calculator1)

# rename source object
RenameSource('Velocity', calculator1)

# set active source
SetActiveSource(flowvtu)

# set active source
SetActiveSource(calculator1)

# create a new 'Calculator'
calculator1_1 = Calculator(Input=calculator1)
calculator1_1.Function = ''

# Properties modified on calculator1_1
calculator1_1.ResultArrayName = 'Total enthalpy'
calculator1_1.Function = 'Energy+Pressure/Density+0.5*Velocity.Velocity'

# show data in view
calculator1_1Display = Show(calculator1_1, renderView1)

# trace defaults for the display properties.
calculator1_1Display.Representation = 'Surface'
calculator1_1Display.ColorArrayName = [None, '']
calculator1_1Display.OSPRayScaleArray = 'Density'
calculator1_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1_1Display.SelectOrientationVectors = 'Velocity'
calculator1_1Display.ScaleFactor = 20.0
calculator1_1Display.SelectScaleArray = 'Density'
calculator1_1Display.GlyphType = 'Arrow'
calculator1_1Display.GlyphTableIndexArray = 'Density'
calculator1_1Display.GaussianRadius = 1.0
calculator1_1Display.SetScaleArray = ['POINTS', 'Density']
calculator1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_1Display.OpacityArray = ['POINTS', 'Density']
calculator1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_1Display.ScalarOpacityUnitDistance = 10.67438550346949

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1_1Display.ScaleTransferFunction.Points = [0.5517352223396301, 0.0, 0.5, 0.0, 1.9102725982666016, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1_1Display.OpacityTransferFunction.Points = [0.5517352223396301, 0.0, 0.5, 0.0, 1.9102725982666016, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on calculator1_1
calculator1_1.Function = 'Energy+Pressure/Density+0.5*Velocity.Velocity'

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(calculator1_1Display, ('POINTS', 'Total enthalpy'))

# rescale color and/or opacity maps used to include current data range
calculator1_1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
calculator1_1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Totalenthalpy'
totalenthalpyLUT = GetColorTransferFunction('Totalenthalpy')
totalenthalpyLUT.RGBPoints = [594065.4500980072, 0.231373, 0.298039, 0.752941, 841829.7432298816, 0.865003, 0.865003, 0.865003, 1089594.036361756, 0.705882, 0.0156863, 0.14902]
totalenthalpyLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Totalenthalpy'
totalenthalpyPWF = GetOpacityTransferFunction('Totalenthalpy')
totalenthalpyPWF.Points = [594065.4500980072, 0.0, 0.5, 0.0, 1089594.036361756, 1.0, 0.5, 0.0]
totalenthalpyPWF.ScalarRangeInitialized = 1

# hide data in view
Hide(streamTracer1, renderView1)

# Properties modified on calculator1_1
calculator1_1.Function = 'Energy/Density+Pressure/Density+0.5*Velocity.Velocity'

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(flowvtu, renderView1)

# Properties modified on calculator1_1
calculator1_1.Function = 'Energy/Density+Pressure/Density+0.5*mag(Velocity)^2'

# update the view to ensure updated data information
renderView1.Update()

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.Play()

# Properties modified on calculator1_1
calculator1_1.Function = 'Energy+Pressure/Density+0.5*mag(Velocity)^2'

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on calculator1_1
calculator1_1.Function = 'Energy/Density+Pressure/Density+0.5*mag(Velocity)^2'

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
totalenthalpyLUT.RescaleTransferFunction(637784.0526817071, 835069.9065900634)

# Rescale transfer function
totalenthalpyPWF.RescaleTransferFunction(637784.0526817071, 835069.9065900634)

# Properties modified on calculator1_1
calculator1_1.Function = 'Energy+Pressure/Density+0.5*mag(Velocity)^2'

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
totalenthalpyLUT.RescaleTransferFunction(594065.4500980072, 1089594.036361756)

# Rescale transfer function
totalenthalpyPWF.RescaleTransferFunction(594065.4500980072, 1089594.036361756)

# Properties modified on calculator1_1
calculator1_1.Function = 'Energy/Density+Pressure/Density+0.5*mag(Velocity)^2'

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
totalenthalpyLUT.RescaleTransferFunction(6e5, 8e5)

# Rescale transfer function
totalenthalpyPWF.RescaleTransferFunction(6e5, 8e5)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.9791297323781771, 0.014668610222894018, 10000.0]
renderView1.CameraFocalPoint = [0.9791297323781771, 0.014668610222894018, 0.0]
renderView1.CameraParallelScale = 1.4576931409000935

# save screenshot
SaveScreenshot('/home/edo20/CFD2020Guardone/Homework/DIAMOND_AIRFOIL/Working_dir/POST-PROCESSING/Total_enthalpy.png', renderView1, ImageResolution=[2904, 1590],
    OverrideColorPalette='WhiteBackground')

# create a new 'Calculator'
calculator2 = Calculator(Input=calculator1_1)
calculator2.Function = ''

# The following are my variables 
E_tot_inf = 410608
P_inf = 1e5
rho_inf = 1.16121
e_tot_inf = E_tot_inf - rho_inf
h_tot_inf = e_tot_inf + P_inf * rho_inf
stringa = 'Energy+Pressure/Density+0.5*Velocity.Velocity - ' + str(h_tot_inf)
# Properties modified on calculator2
calculator2.ResultArrayName = 'Total enthalpy - Total enthalpy at freestream'
calculator2.Function = stringa

# show data in view
calculator2Display = Show(calculator2, renderView1)

# trace defaults for the display properties.
calculator2Display.Representation = 'Surface'
calculator2Display.ColorArrayName = [None, '']
calculator2Display.OSPRayScaleArray = 'Density'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.SelectOrientationVectors = 'Velocity'
calculator2Display.ScaleFactor = 20.0
calculator2Display.SelectScaleArray = 'Density'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.GlyphTableIndexArray = 'Density'
calculator2Display.GaussianRadius = 1.0
calculator2Display.SetScaleArray = ['POINTS', 'Density']
calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display.OpacityArray = ['POINTS', 'Density']
calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display.PolarAxes = 'PolarAxesRepresentation'
calculator2Display.ScalarOpacityUnitDistance = 10.67438550346949

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator2Display.ScaleTransferFunction.Points = [0.5517352223396301, 0.0, 0.5, 0.0, 1.9102725982666016, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator2Display.OpacityTransferFunction.Points = [0.5517352223396301, 0.0, 0.5, 0.0, 1.9102725982666016, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on calculator2
calculator2.Function = stringa

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(calculator2Display, ('POINTS', 'Total enthalpy - Total enthalpy at freestream'))

# rescale color and/or opacity maps used to include current data range
calculator2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Totalenthalpy'
totalenthalpyLUT = GetColorTransferFunction('Total enthalpy - Total enthalpy at freestream')
totalenthalpyLUT.RGBPoints = [594065.4500980072, 0.231373, 0.298039, 0.752941, 841829.7432298816, 0.865003, 0.865003, 0.865003, 1089594.036361756, 0.705882, 0.0156863, 0.14902]
totalenthalpyLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Totalenthalpy'
totalenthalpyPWF = GetOpacityTransferFunction('Total enthalpy - Total enthalpy at freestream')
totalenthalpyPWF.Points = [594065.4500980072, 0.0, 0.5, 0.0, 1089594.036361756, 1.0, 0.5, 0.0]
totalenthalpyPWF.ScalarRangeInitialized = 1

# hide data in view
Hide(streamTracer1, renderView1)
Hide(calculator1_1)
# Properties modified on calculator2
calculator2.Function = stringa

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(flowvtu, renderView1)

# Properties modified on calculator2
calculator2.Function = stringa

# update the view to ensure updated data information
renderView1.Update()

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.Play()

# Properties modified on calculator2
calculator2.Function = stringa

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on calculator2
calculator2.Function = stringa

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
totalenthalpyLUT.RescaleTransferFunction(637784.0526817071, 835069.9065900634)

# Rescale transfer function
totalenthalpyPWF.RescaleTransferFunction(637784.0526817071, 835069.9065900634)

# Properties modified on calculator2
calculator2.Function = stringa

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
totalenthalpyLUT.RescaleTransferFunction(594065.4500980072, 1089594.036361756)

# Rescale transfer function
totalenthalpyPWF.RescaleTransferFunction(594065.4500980072, 1089594.036361756)

# Properties modified on calculator1_1
calculator2.Function = stringa

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
totalenthalpyLUT.RescaleTransferFunction(-1e5, 5e5)

# Rescale transfer function
totalenthalpyPWF.RescaleTransferFunction(-1e5, 5e5)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.9791297323781771, 0.014668610222894018, 10000.0]
renderView1.CameraFocalPoint = [0.9791297323781771, 0.014668610222894018, 0.0]
renderView1.CameraParallelScale = 1.4576931409000935

# save screenshot
SaveScreenshot('/home/edo20/CFD2020Guardone/Homework/DIAMOND_AIRFOIL/Working_dir/POST-PROCESSING/Total_enthalpy-htotinf.png', renderView1, ImageResolution=[2904, 1590],
    OverrideColorPalette='WhiteBackground')
    
Hide(calculator2)

#################################################
# set active source
SetActiveSource(flowvtu)

# create a new 'Programmable Filter'
programmableFilter1 = ProgrammableFilter(Input=flowvtu)
programmableFilter1.Script = ''
programmableFilter1.RequestInformationScript = ''
programmableFilter1.RequestUpdateExtentScript = ''
programmableFilter1.PythonPath = ''

# Properties modified on programmableFilter1
programmableFilter1.Script = """# Import necessary packages
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
Ma = 1.8
rhoa = Pa/R/Ta

# Recall values calculated by previous script

# =============================== Values inside zones 
# Zone b
Mb = 1.5113818942649062
Pb = 152768.9873626066
Tb = 339.36114738132915
rhob = rhob = 1.5682071357235274
Vb = 558.1541011988293

# Zone c
Mc = 2.32313549
Pc = 43975.95965155
Tc = 237.7618413
rhoc = 0.64432282
Vc = 718.11576776

# Zone d
Md = 1.2759125784687726
Pd = 206218.2578942544
Td = 372.9658364131552
rhod = 1.9261424673680811
Vd = 493.9742269758489

# Zone e
Me = 2.06433611
Pe = 63940.06852015
Te = 248.70797802
rhoe = 0.71087976
Ve = 676.10353686

# Zone f
Mf = 1.7545215148574134
Pf = 100497.06834558
Tf = 306.00324345
rhof = 1.14408346
Vf = 615.2768263116847

# Zone g
Mg = 1.7655629480860935
Pg = 100497.06834558
Tg = 304.53804096
rhog = 1.14958791
Vg = 617.664763175894

# ============================================ Angles

# Top shock 
beta_top  = 45.02919028 * pi/180

# Bottom shock
beta_bot = -47.16406711 * pi/180

# Top expansion
mu1_top = 62.91540263417585 * pi/180
mu2_top = 17.664366055971083 * pi/180

# Bottom expansion
mu1_bot = -62.91540263417585 * pi/180
mu2_bot = -17.664366055971083 * pi/180

# Top rear shock
beta_top_rear = 27.30125049 * pi/180

# Bottom rear shock
beta_bot_rear = -24.94071889 * pi/180

# Slip line 
delta_slip = 3.08497876

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

"""
programmableFilter1.RequestInformationScript = ''
programmableFilter1.RequestUpdateExtentScript = ''
programmableFilter1.PythonPath = ''

# show data in view
programmableFilter1Display = Show(programmableFilter1, renderView1)

# trace defaults for the display properties.
programmableFilter1Display.Representation = 'Surface'
programmableFilter1Display.ColorArrayName = [None, '']
programmableFilter1Display.OSPRayScaleArray = 'Coordinates'
programmableFilter1Display.OSPRayScaleFunction = 'PiecewiseFunction'
programmableFilter1Display.SelectOrientationVectors = 'Coordinates'
programmableFilter1Display.ScaleFactor = 20.0
programmableFilter1Display.SelectScaleArray = 'Coordinates'
programmableFilter1Display.GlyphType = 'Arrow'
programmableFilter1Display.GlyphTableIndexArray = 'Coordinates'
programmableFilter1Display.GaussianRadius = 1.0
programmableFilter1Display.SetScaleArray = ['POINTS', 'Coordinates']
programmableFilter1Display.ScaleTransferFunction = 'PiecewiseFunction'
programmableFilter1Display.OpacityArray = ['POINTS', 'Coordinates']
programmableFilter1Display.OpacityTransferFunction = 'PiecewiseFunction'
programmableFilter1Display.DataAxesGrid = 'GridAxesRepresentation'
programmableFilter1Display.PolarAxes = 'PolarAxesRepresentation'
programmableFilter1Display.ScalarOpacityUnitDistance = 10.67438550346949

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
programmableFilter1Display.ScaleTransferFunction.Points = [-100.0, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
programmableFilter1Display.OpacityTransferFunction.Points = [-100.0, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(flowvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(calculator1_1, renderView1)

# set active source
SetActiveSource(calculator1_1)

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(Input=[programmableFilter1, calculator1_1])

# show data in view
appendAttributes1Display = Show(appendAttributes1, renderView1)

# trace defaults for the display properties.
appendAttributes1Display.Representation = 'Surface'
appendAttributes1Display.ColorArrayName = [None, '']
appendAttributes1Display.OSPRayScaleArray = 'Coordinates'
appendAttributes1Display.OSPRayScaleFunction = 'PiecewiseFunction'
appendAttributes1Display.SelectOrientationVectors = 'Coordinates'
appendAttributes1Display.ScaleFactor = 20.0
appendAttributes1Display.SelectScaleArray = 'Coordinates'
appendAttributes1Display.GlyphType = 'Arrow'
appendAttributes1Display.GlyphTableIndexArray = 'Coordinates'
appendAttributes1Display.GaussianRadius = 1.0
appendAttributes1Display.SetScaleArray = ['POINTS', 'Coordinates']
appendAttributes1Display.ScaleTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.OpacityArray = ['POINTS', 'Coordinates']
appendAttributes1Display.OpacityTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.DataAxesGrid = 'GridAxesRepresentation'
appendAttributes1Display.PolarAxes = 'PolarAxesRepresentation'
appendAttributes1Display.ScalarOpacityUnitDistance = 10.67438550346949

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
appendAttributes1Display.ScaleTransferFunction.Points = [-100.0, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
appendAttributes1Display.OpacityTransferFunction.Points = [-100.0, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(programmableFilter1, renderView1)

# hide data in view
Hide(calculator1_1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(appendAttributes1, renderView1)

# set active source
SetActiveSource(appendAttributes1)

# show data in view
appendAttributes1Display = Show(appendAttributes1, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# set active source
SetActiveSource(appendAttributes1)

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=appendAttributes1,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine1.Source.Point1 = [0.0, 0.3, 0.0]
plotOverLine1.Source.Point2 = [2.5, 0.3, 0.0]

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1)

# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.ColorArrayName = [None, '']
plotOverLine1Display.OSPRayScaleArray = 'Coordinates'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.SelectOrientationVectors = 'Coordinates'
plotOverLine1Display.ScaleFactor = 0.25
plotOverLine1Display.SelectScaleArray = 'Coordinates'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.GlyphTableIndexArray = 'Coordinates'
plotOverLine1Display.GaussianRadius = 0.0125
plotOverLine1Display.SetScaleArray = ['POINTS', 'Coordinates']
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityArray = ['POINTS', 'Coordinates']
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display.ScaleTransferFunction.Points = [1.734723475976807e-18, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display.OpacityTransferFunction.Points = [1.734723475976807e-18, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
# uncomment following to set a specific view size
lineChartView1.ViewSize = [2904, 1590] # 400,400 #1132, 795

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1)

# trace defaults for the display properties.
plotOverLine1Display_1.CompositeDataSetIndex = [0]
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['Coordinates_Magnitude', 'Density', 'Energy', 'Exact Density_Magnitude', 'Exact Mach_Magnitude', 'Exact Pressure_Magnitude', 'Exact Temperature_Magnitude', 'Exact Velocity_Magnitude', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature', 'Total enthalpy', 'Velocity_Magnitude']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Coordinates_X', 'Coordinates_X', 'Coordinates_Y', 'Coordinates_Y', 'Coordinates_Z', 'Coordinates_Z', 'Coordinates_Magnitude', 'Coordinates_Magnitude', 'Density', 'Density', 'Energy', 'Energy', 'Exact Density_X', 'Exact Density_X', 'Exact Density_Y', 'Exact Density_Y', 'Exact Density_Magnitude', 'Exact Density_Magnitude', 'Exact Mach_X', 'Exact Mach_X', 'Exact Mach_Y', 'Exact Mach_Y', 'Exact Mach_Magnitude', 'Exact Mach_Magnitude', 'Exact Pressure_X', 'Exact Pressure_X', 'Exact Pressure_Y', 'Exact Pressure_Y', 'Exact Pressure_Magnitude', 'Exact Pressure_Magnitude', 'Exact Temperature_X', 'Exact Temperature_X', 'Exact Temperature_Y', 'Exact Temperature_Y', 'Exact Temperature_Magnitude', 'Exact Temperature_Magnitude', 'Exact Velocity_X', 'Exact Velocity_X', 'Exact Velocity_Y', 'Exact Velocity_Y', 'Exact Velocity_Z', 'Exact Velocity_Z', 'Exact Velocity_Magnitude', 'Exact Velocity_Magnitude', 'Mach', 'Mach', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', 'Pressure', 'Pressure', 'Pressure_Coefficient', 'Pressure_Coefficient', 'Temperature', 'Temperature', 'Total enthalpy', 'Total enthalpy', 'Velocity_X', 'Velocity_X', 'Velocity_Y', 'Velocity_Y', 'Velocity_Z', 'Velocity_Z', 'Velocity_Magnitude', 'Velocity_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Coordinates_X', '0.89', '0.1', '0.11', 'Coordinates_Y', '0.22', '0.49', '0.72', 'Coordinates_Z', '0.3', '0.69', '0.29', 'Coordinates_Magnitude', '0.6', '0.31', '0.64', 'Density', '1', '0.5', '0', 'Energy', '0.65', '0.34', '0.16', 'Exact Density_X', '0', '0', '0', 'Exact Density_Y', '0.89', '0.1', '0.11', 'Exact Density_Magnitude', '0.22', '0.49', '0.72', 'Exact Mach_X', '0.3', '0.69', '0.29', 'Exact Mach_Y', '0.6', '0.31', '0.64', 'Exact Mach_Magnitude', '1', '0.5', '0', 'Exact Pressure_X', '0.65', '0.34', '0.16', 'Exact Pressure_Y', '0', '0', '0', 'Exact Pressure_Magnitude', '0.89', '0.1', '0.11', 'Exact Temperature_X', '0.22', '0.49', '0.72', 'Exact Temperature_Y', '0.3', '0.69', '0.29', 'Exact Temperature_Magnitude', '0.6', '0.31', '0.64', 'Exact Velocity_X', '1', '0.5', '0', 'Exact Velocity_Y', '0.65', '0.34', '0.16', 'Exact Velocity_Z', '0', '0', '0', 'Exact Velocity_Magnitude', '0.89', '0.1', '0.11', 'Mach', '0.22', '0.49', '0.72', 'Momentum_X', '0.3', '0.69', '0.29', 'Momentum_Y', '0.6', '0.31', '0.64', 'Momentum_Z', '1', '0.5', '0', 'Momentum_Magnitude', '0.65', '0.34', '0.16', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.89', '0.1', '0.11', 'Temperature', '0.22', '0.49', '0.72', 'Total enthalpy', '0.3', '0.69', '0.29', 'Velocity_X', '0.6', '0.31', '0.64', 'Velocity_Y', '1', '0.5', '0', 'Velocity_Z', '0.65', '0.34', '0.16', 'Velocity_Magnitude', '0', '0', '0', 'vtkValidPointMask', '0.89', '0.1', '0.11', 'Points_X', '0.22', '0.49', '0.72', 'Points_Y', '0.3', '0.69', '0.29', 'Points_Z', '0.6', '0.31', '0.64', 'Points_Magnitude', '1', '0.5', '0']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'Coordinates_X', '0', 'Coordinates_Y', '0', 'Coordinates_Z', '0', 'Coordinates_Magnitude', '0', 'Density', '0', 'Energy', '0', 'Exact Density_X', '0', 'Exact Density_Y', '0', 'Exact Density_Magnitude', '0', 'Exact Mach_X', '0', 'Exact Mach_Y', '0', 'Exact Mach_Magnitude', '0', 'Exact Pressure_X', '0', 'Exact Pressure_Y', '0', 'Exact Pressure_Magnitude', '0', 'Exact Temperature_X', '0', 'Exact Temperature_Y', '0', 'Exact Temperature_Magnitude', '0', 'Exact Velocity_X', '0', 'Exact Velocity_Y', '0', 'Exact Velocity_Z', '0', 'Exact Velocity_Magnitude', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'Total enthalpy', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Velocity_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'Coordinates_X', '1', 'Coordinates_Y', '1', 'Coordinates_Z', '1', 'Coordinates_Magnitude', '1', 'Density', '1', 'Energy', '1', 'Exact Density_X', '1', 'Exact Density_Y', '1', 'Exact Density_Magnitude', '1', 'Exact Mach_X', '1', 'Exact Mach_Y', '1', 'Exact Mach_Magnitude', '1', 'Exact Pressure_X', '1', 'Exact Pressure_Y', '1', 'Exact Pressure_Magnitude', '1', 'Exact Temperature_X', '1', 'Exact Temperature_Y', '1', 'Exact Temperature_Magnitude', '1', 'Exact Velocity_X', '1', 'Exact Velocity_Y', '1', 'Exact Velocity_Z', '1', 'Exact Velocity_Magnitude', '1', 'Mach', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Momentum_Magnitude', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1', 'Total enthalpy', '1', 'Velocity_X', '1', 'Velocity_Y', '1', 'Velocity_Z', '1', 'Velocity_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'Coordinates_X', '2', 'Coordinates_Y', '2', 'Coordinates_Z', '2', 'Coordinates_Magnitude', '2', 'Density', '2', 'Energy', '2', 'Exact Density_X', '2', 'Exact Density_Y', '2', 'Exact Density_Magnitude', '2', 'Exact Mach_X', '2', 'Exact Mach_Y', '2', 'Exact Mach_Magnitude', '2', 'Exact Pressure_X', '2', 'Exact Pressure_Y', '2', 'Exact Pressure_Magnitude', '2', 'Exact Temperature_X', '2', 'Exact Temperature_Y', '2', 'Exact Temperature_Magnitude', '2', 'Exact Velocity_X', '2', 'Exact Velocity_Y', '2', 'Exact Velocity_Z', '2', 'Exact Velocity_Magnitude', '2', 'Mach', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Momentum_Magnitude', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2', 'Total enthalpy', '2', 'Velocity_X', '2', 'Velocity_Y', '2', 'Velocity_Z', '2', 'Velocity_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Coordinates_X', '0', 'Coordinates_Y', '0', 'Coordinates_Z', '0', 'Coordinates_Magnitude', '0', 'Density', '0', 'Energy', '0', 'Exact Density_X', '0', 'Exact Density_Y', '0', 'Exact Density_Magnitude', '0', 'Exact Mach_X', '0', 'Exact Mach_Y', '0', 'Exact Mach_Magnitude', '0', 'Exact Pressure_X', '0', 'Exact Pressure_Y', '0', 'Exact Pressure_Magnitude', '0', 'Exact Temperature_X', '0', 'Exact Temperature_Y', '0', 'Exact Temperature_Magnitude', '0', 'Exact Velocity_X', '0', 'Exact Velocity_Y', '0', 'Exact Velocity_Z', '0', 'Exact Velocity_Magnitude', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'Total enthalpy', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Velocity_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Density', 'Energy', 'Exact Density_Magnitude', 'Exact Mach_Magnitude', 'Exact Pressure_Magnitude', 'Exact Temperature_Magnitude', 'Exact Velocity_Magnitude', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature', 'Total enthalpy', 'Velocity_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Coordinates_X', '0.889998', '0.100008', '0.110002', 'Coordinates_Y', '0.220005', '0.489998', '0.719997', 'Coordinates_Z', '0.300008', '0.689998', '0.289998', 'Coordinates_Magnitude', '0.6', '0.310002', '0.639994', 'Density', '1', '0.500008', '0', 'Energy', '0.650004', '0.340002', '0.160006', 'Exact Density_X', '0', '0', '0', 'Exact Density_Y', '0.889998', '0.100008', '0.110002', 'Exact Density_Magnitude', '0.220005', '0.489998', '0.719997', 'Exact Mach_X', '0.300008', '0.689998', '0.289998', 'Exact Mach_Y', '0.6', '0.310002', '0.639994', 'Exact Mach_Magnitude', '1', '0.500008', '0', 'Exact Pressure_X', '0.650004', '0.340002', '0.160006', 'Exact Pressure_Y', '0', '0', '0', 'Exact Pressure_Magnitude', '0.889998', '0.100008', '0.110002', 'Exact Temperature_X', '0.220005', '0.489998', '0.719997', 'Exact Temperature_Y', '0.300008', '0.689998', '0.289998', 'Exact Temperature_Magnitude', '0.6', '0.310002', '0.639994', 'Exact Velocity_X', '1', '0.500008', '0', 'Exact Velocity_Y', '0.650004', '0.340002', '0.160006', 'Exact Velocity_Z', '0', '0', '0', 'Exact Velocity_Magnitude', '0.889998', '0.100008', '0.110002', 'Mach', '0.220005', '0.489998', '0.719997', 'Momentum_X', '0.300008', '0.689998', '0.289998', 'Momentum_Y', '0.6', '0.310002', '0.639994', 'Momentum_Z', '1', '0.500008', '0', 'Momentum_Magnitude', '0.650004', '0.340002', '0.160006', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.889998', '0.100008', '0.110002', 'Temperature', '0.220005', '0.489998', '0.719997', 'Total enthalpy', '0.300008', '0.689998', '0.289998', 'Velocity_X', '0.6', '0.310002', '0.639994', 'Velocity_Y', '1', '0.500008', '0', 'Velocity_Z', '0.650004', '0.340002', '0.160006', 'Velocity_Magnitude', '0', '0', '0', 'vtkValidPointMask', '0.889998', '0.100008', '0.110002', 'Points_X', '0.220005', '0.489998', '0.719997', 'Points_Y', '0.300008', '0.689998', '0.289998', 'Points_Z', '0.6', '0.310002', '0.639994', 'Points_Magnitude', '1', '0.500008', '0']
plotOverLine1Display_1.SeriesPlotCorner = ['Coordinates_Magnitude', '0', 'Coordinates_X', '0', 'Coordinates_Y', '0', 'Coordinates_Z', '0', 'Density', '0', 'Energy', '0', 'Exact Density_Magnitude', '0', 'Exact Density_X', '0', 'Exact Density_Y', '0', 'Exact Mach_Magnitude', '0', 'Exact Mach_X', '0', 'Exact Mach_Y', '0', 'Exact Pressure_Magnitude', '0', 'Exact Pressure_X', '0', 'Exact Pressure_Y', '0', 'Exact Temperature_Magnitude', '0', 'Exact Temperature_X', '0', 'Exact Temperature_Y', '0', 'Exact Velocity_Magnitude', '0', 'Exact Velocity_X', '0', 'Exact Velocity_Y', '0', 'Exact Velocity_Z', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'Total enthalpy', '0', 'Velocity_Magnitude', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Coordinates_Magnitude', '1', 'Coordinates_X', '1', 'Coordinates_Y', '1', 'Coordinates_Z', '1', 'Density', '1', 'Energy', '1', 'Exact Density_Magnitude', '1', 'Exact Density_X', '1', 'Exact Density_Y', '1', 'Exact Mach_Magnitude', '1', 'Exact Mach_X', '1', 'Exact Mach_Y', '1', 'Exact Pressure_Magnitude', '1', 'Exact Pressure_X', '1', 'Exact Pressure_Y', '1', 'Exact Temperature_Magnitude', '1', 'Exact Temperature_X', '1', 'Exact Temperature_Y', '1', 'Exact Velocity_Magnitude', '1', 'Exact Velocity_X', '1', 'Exact Velocity_Y', '1', 'Exact Velocity_Z', '1', 'Mach', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1', 'Total enthalpy', '1', 'Velocity_Magnitude', '1', 'Velocity_X', '1', 'Velocity_Y', '1', 'Velocity_Z', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Coordinates_Magnitude', '2', 'Coordinates_X', '2', 'Coordinates_Y', '2', 'Coordinates_Z', '2', 'Density', '2', 'Energy', '2', 'Exact Density_Magnitude', '2', 'Exact Density_X', '2', 'Exact Density_Y', '2', 'Exact Mach_Magnitude', '2', 'Exact Mach_X', '2', 'Exact Mach_Y', '2', 'Exact Pressure_Magnitude', '2', 'Exact Pressure_X', '2', 'Exact Pressure_Y', '2', 'Exact Temperature_Magnitude', '2', 'Exact Temperature_X', '2', 'Exact Temperature_Y', '2', 'Exact Velocity_Magnitude', '2', 'Exact Velocity_X', '2', 'Exact Velocity_Y', '2', 'Exact Velocity_Z', '2', 'Mach', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2', 'Total enthalpy', '2', 'Velocity_Magnitude', '2', 'Velocity_X', '2', 'Velocity_Y', '2', 'Velocity_Z', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Coordinates_Magnitude', '0', 'Coordinates_X', '0', 'Coordinates_Y', '0', 'Coordinates_Z', '0', 'Density', '0', 'Energy', '0', 'Exact Density_Magnitude', '0', 'Exact Density_X', '0', 'Exact Density_Y', '0', 'Exact Mach_Magnitude', '0', 'Exact Mach_X', '0', 'Exact Mach_Y', '0', 'Exact Pressure_Magnitude', '0', 'Exact Pressure_X', '0', 'Exact Pressure_Y', '0', 'Exact Temperature_Magnitude', '0', 'Exact Temperature_X', '0', 'Exact Temperature_Y', '0', 'Exact Velocity_Magnitude', '0', 'Exact Velocity_X', '0', 'Exact Velocity_Y', '0', 'Exact Velocity_Z', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'Total enthalpy', '0', 'Velocity_Magnitude', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.XArrayName = 'Points_X'

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Density', 'Exact Density_Magnitude', 'Exact Mach_Magnitude', 'Exact Pressure_Magnitude', 'Exact Temperature_Magnitude', 'Exact Velocity_Magnitude', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature', 'Total enthalpy', 'Velocity_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Density', 'Exact Density_Magnitude', 'Exact Mach_Magnitude', 'Exact Temperature_Magnitude', 'Exact Velocity_Magnitude', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature', 'Total enthalpy', 'Velocity_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Density', 'Exact Density_Magnitude', 'Exact Mach_Magnitude', 'Exact Velocity_Magnitude', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature', 'Total enthalpy', 'Velocity_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Density', 'Exact Density_Magnitude', 'Exact Mach_Magnitude', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature', 'Total enthalpy', 'Velocity_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Density', 'Exact Density_Magnitude', 'Exact Mach_Magnitude', 'Mach', 'Pressure', 'Pressure_Coefficient', 'Temperature', 'Total enthalpy', 'Velocity_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Density', 'Exact Density_Magnitude', 'Exact Mach_Magnitude', 'Mach', 'Pressure_Coefficient', 'Temperature', 'Total enthalpy', 'Velocity_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Density', 'Exact Density_Magnitude', 'Exact Mach_Magnitude', 'Mach', 'Temperature', 'Total enthalpy', 'Velocity_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Density', 'Exact Density_Magnitude', 'Exact Mach_Magnitude', 'Mach', 'Total enthalpy', 'Velocity_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Density', 'Exact Density_Magnitude', 'Exact Mach_Magnitude', 'Mach', 'Velocity_Magnitude']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Density', 'Exact Density_Magnitude', 'Exact Mach_Magnitude', 'Mach']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Coordinates_X', '0.889998', '0.100008', '0.110002', 'Coordinates_Y', '0.220005', '0.489998', '0.719997', 'Coordinates_Z', '0.300008', '0.689998', '0.289998', 'Coordinates_Magnitude', '0.6', '0.310002', '0.639994', 'Density', '1', '0', '0', 'Energy', '0.650004', '0.340002', '0.160006', 'Exact Density_X', '0', '0', '0', 'Exact Density_Y', '0.889998', '0.100008', '0.110002', 'Exact Density_Magnitude', '0.220005', '0.489998', '0.719997', 'Exact Mach_X', '0.300008', '0.689998', '0.289998', 'Exact Mach_Y', '0.6', '0.310002', '0.639994', 'Exact Mach_Magnitude', '1', '0.500008', '0', 'Exact Pressure_X', '0.650004', '0.340002', '0.160006', 'Exact Pressure_Y', '0', '0', '0', 'Exact Pressure_Magnitude', '0.889998', '0.100008', '0.110002', 'Exact Temperature_X', '0.220005', '0.489998', '0.719997', 'Exact Temperature_Y', '0.300008', '0.689998', '0.289998', 'Exact Temperature_Magnitude', '0.6', '0.310002', '0.639994', 'Exact Velocity_X', '1', '0.500008', '0', 'Exact Velocity_Y', '0.650004', '0.340002', '0.160006', 'Exact Velocity_Z', '0', '0', '0', 'Exact Velocity_Magnitude', '0.889998', '0.100008', '0.110002', 'Mach', '0.220005', '0.489998', '0.719997', 'Momentum_X', '0.300008', '0.689998', '0.289998', 'Momentum_Y', '0.6', '0.310002', '0.639994', 'Momentum_Z', '1', '0.500008', '0', 'Momentum_Magnitude', '0.650004', '0.340002', '0.160006', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.889998', '0.100008', '0.110002', 'Temperature', '0.220005', '0.489998', '0.719997', 'Total enthalpy', '0.300008', '0.689998', '0.289998', 'Velocity_X', '0.6', '0.310002', '0.639994', 'Velocity_Y', '1', '0.500008', '0', 'Velocity_Z', '0.650004', '0.340002', '0.160006', 'Velocity_Magnitude', '0', '0', '0', 'vtkValidPointMask', '0.889998', '0.100008', '0.110002', 'Points_X', '0.220005', '0.489998', '0.719997', 'Points_Y', '0.300008', '0.689998', '0.289998', 'Points_Z', '0.6', '0.310002', '0.639994', 'Points_Magnitude', '1', '0.500008', '0']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Coordinates_X', '0.889998', '0.100008', '0.110002', 'Coordinates_Y', '0.220005', '0.489998', '0.719997', 'Coordinates_Z', '0.300008', '0.689998', '0.289998', 'Coordinates_Magnitude', '0.6', '0.310002', '0.639994', 'Density', '1', '0', '0', 'Energy', '0.650004', '0.340002', '0.160006', 'Exact Density_X', '0', '0', '0', 'Exact Density_Y', '0.889998', '0.100008', '0.110002', 'Exact Density_Magnitude', '0', '0', '1', 'Exact Mach_X', '0.300008', '0.689998', '0.289998', 'Exact Mach_Y', '0.6', '0.310002', '0.639994', 'Exact Mach_Magnitude', '1', '0.500008', '0', 'Exact Pressure_X', '0.650004', '0.340002', '0.160006', 'Exact Pressure_Y', '0', '0', '0', 'Exact Pressure_Magnitude', '0.889998', '0.100008', '0.110002', 'Exact Temperature_X', '0.220005', '0.489998', '0.719997', 'Exact Temperature_Y', '0.300008', '0.689998', '0.289998', 'Exact Temperature_Magnitude', '0.6', '0.310002', '0.639994', 'Exact Velocity_X', '1', '0.500008', '0', 'Exact Velocity_Y', '0.650004', '0.340002', '0.160006', 'Exact Velocity_Z', '0', '0', '0', 'Exact Velocity_Magnitude', '0.889998', '0.100008', '0.110002', 'Mach', '0.220005', '0.489998', '0.719997', 'Momentum_X', '0.300008', '0.689998', '0.289998', 'Momentum_Y', '0.6', '0.310002', '0.639994', 'Momentum_Z', '1', '0.500008', '0', 'Momentum_Magnitude', '0.650004', '0.340002', '0.160006', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.889998', '0.100008', '0.110002', 'Temperature', '0.220005', '0.489998', '0.719997', 'Total enthalpy', '0.300008', '0.689998', '0.289998', 'Velocity_X', '0.6', '0.310002', '0.639994', 'Velocity_Y', '1', '0.500008', '0', 'Velocity_Z', '0.650004', '0.340002', '0.160006', 'Velocity_Magnitude', '0', '0', '0', 'vtkValidPointMask', '0.889998', '0.100008', '0.110002', 'Points_X', '0.220005', '0.489998', '0.719997', 'Points_Y', '0.300008', '0.689998', '0.289998', 'Points_Z', '0.6', '0.310002', '0.639994', 'Points_Magnitude', '1', '0.500008', '0']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Coordinates_X', '0.889998', '0.100008', '0.110002', 'Coordinates_Y', '0.220005', '0.489998', '0.719997', 'Coordinates_Z', '0.300008', '0.689998', '0.289998', 'Coordinates_Magnitude', '0.6', '0.310002', '0.639994', 'Density', '1', '0', '0', 'Energy', '0.650004', '0.340002', '0.160006', 'Exact Density_X', '0', '0', '0', 'Exact Density_Y', '0.889998', '0.100008', '0.110002', 'Exact Density_Magnitude', '0', '0', '1', 'Exact Mach_X', '0.300008', '0.689998', '0.289998', 'Exact Mach_Y', '0.6', '0.310002', '0.639994', 'Exact Mach_Magnitude', '1', '0.501961', '0', 'Exact Pressure_X', '0.650004', '0.340002', '0.160006', 'Exact Pressure_Y', '0', '0', '0', 'Exact Pressure_Magnitude', '0.889998', '0.100008', '0.110002', 'Exact Temperature_X', '0.220005', '0.489998', '0.719997', 'Exact Temperature_Y', '0.300008', '0.689998', '0.289998', 'Exact Temperature_Magnitude', '0.6', '0.310002', '0.639994', 'Exact Velocity_X', '1', '0.500008', '0', 'Exact Velocity_Y', '0.650004', '0.340002', '0.160006', 'Exact Velocity_Z', '0', '0', '0', 'Exact Velocity_Magnitude', '0.889998', '0.100008', '0.110002', 'Mach', '0.220005', '0.489998', '0.719997', 'Momentum_X', '0.300008', '0.689998', '0.289998', 'Momentum_Y', '0.6', '0.310002', '0.639994', 'Momentum_Z', '1', '0.500008', '0', 'Momentum_Magnitude', '0.650004', '0.340002', '0.160006', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.889998', '0.100008', '0.110002', 'Temperature', '0.220005', '0.489998', '0.719997', 'Total enthalpy', '0.300008', '0.689998', '0.289998', 'Velocity_X', '0.6', '0.310002', '0.639994', 'Velocity_Y', '1', '0.500008', '0', 'Velocity_Z', '0.650004', '0.340002', '0.160006', 'Velocity_Magnitude', '0', '0', '0', 'vtkValidPointMask', '0.889998', '0.100008', '0.110002', 'Points_X', '0.220005', '0.489998', '0.719997', 'Points_Y', '0.300008', '0.689998', '0.289998', 'Points_Z', '0.6', '0.310002', '0.639994', 'Points_Magnitude', '1', '0.500008', '0']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Coordinates_X', '0.889998', '0.100008', '0.110002', 'Coordinates_Y', '0.220005', '0.489998', '0.719997', 'Coordinates_Z', '0.300008', '0.689998', '0.289998', 'Coordinates_Magnitude', '0.6', '0.310002', '0.639994', 'Density', '1', '0', '0', 'Energy', '0.650004', '0.340002', '0.160006', 'Exact Density_X', '0', '0', '0', 'Exact Density_Y', '0.889998', '0.100008', '0.110002', 'Exact Density_Magnitude', '0', '0', '1', 'Exact Mach_X', '0.300008', '0.689998', '0.289998', 'Exact Mach_Y', '0.6', '0.310002', '0.639994', 'Exact Mach_Magnitude', '0', '0', '0', 'Exact Pressure_X', '0.650004', '0.340002', '0.160006', 'Exact Pressure_Y', '0', '0', '0', 'Exact Pressure_Magnitude', '0.889998', '0.100008', '0.110002', 'Exact Temperature_X', '0.220005', '0.489998', '0.719997', 'Exact Temperature_Y', '0.300008', '0.689998', '0.289998', 'Exact Temperature_Magnitude', '0.6', '0.310002', '0.639994', 'Exact Velocity_X', '1', '0.500008', '0', 'Exact Velocity_Y', '0.650004', '0.340002', '0.160006', 'Exact Velocity_Z', '0', '0', '0', 'Exact Velocity_Magnitude', '0.889998', '0.100008', '0.110002', 'Mach', '0.220005', '0.489998', '0.719997', 'Momentum_X', '0.300008', '0.689998', '0.289998', 'Momentum_Y', '0.6', '0.310002', '0.639994', 'Momentum_Z', '1', '0.500008', '0', 'Momentum_Magnitude', '0.650004', '0.340002', '0.160006', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.889998', '0.100008', '0.110002', 'Temperature', '0.220005', '0.489998', '0.719997', 'Total enthalpy', '0.300008', '0.689998', '0.289998', 'Velocity_X', '0.6', '0.310002', '0.639994', 'Velocity_Y', '1', '0.500008', '0', 'Velocity_Z', '0.650004', '0.340002', '0.160006', 'Velocity_Magnitude', '0', '0', '0', 'vtkValidPointMask', '0.889998', '0.100008', '0.110002', 'Points_X', '0.220005', '0.489998', '0.719997', 'Points_Y', '0.300008', '0.689998', '0.289998', 'Points_Z', '0.6', '0.310002', '0.639994', 'Points_Magnitude', '1', '0.500008', '0']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Coordinates_X', '0.889998', '0.100008', '0.110002', 'Coordinates_Y', '0.220005', '0.489998', '0.719997', 'Coordinates_Z', '0.300008', '0.689998', '0.289998', 'Coordinates_Magnitude', '0.6', '0.310002', '0.639994', 'Density', '1', '0', '0', 'Energy', '0.650004', '0.340002', '0.160006', 'Exact Density_X', '0', '0', '0', 'Exact Density_Y', '0.889998', '0.100008', '0.110002', 'Exact Density_Magnitude', '0', '0', '1', 'Exact Mach_X', '0.300008', '0.689998', '0.289998', 'Exact Mach_Y', '0.6', '0.310002', '0.639994', 'Exact Mach_Magnitude', '0', '0', '0', 'Exact Pressure_X', '0.650004', '0.340002', '0.160006', 'Exact Pressure_Y', '0', '0', '0', 'Exact Pressure_Magnitude', '0.889998', '0.100008', '0.110002', 'Exact Temperature_X', '0.220005', '0.489998', '0.719997', 'Exact Temperature_Y', '0.300008', '0.689998', '0.289998', 'Exact Temperature_Magnitude', '0.6', '0.310002', '0.639994', 'Exact Velocity_X', '1', '0.500008', '0', 'Exact Velocity_Y', '0.650004', '0.340002', '0.160006', 'Exact Velocity_Z', '0', '0', '0', 'Exact Velocity_Magnitude', '0.889998', '0.100008', '0.110002', 'Mach', '0.87', '1.0', '0', 'Momentum_X', '0.300008', '0.689998', '0.289998', 'Momentum_Y', '0.6', '0.310002', '0.639994', 'Momentum_Z', '1', '0.500008', '0', 'Momentum_Magnitude', '0.650004', '0.340002', '0.160006', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.889998', '0.100008', '0.110002', 'Temperature', '0.220005', '0.489998', '0.719997', 'Total enthalpy', '0.300008', '0.689998', '0.289998', 'Velocity_X', '0.6', '0.310002', '0.639994', 'Velocity_Y', '1', '0.500008', '0', 'Velocity_Z', '0.650004', '0.340002', '0.160006', 'Velocity_Magnitude', '0', '0', '0', 'vtkValidPointMask', '0.889998', '0.100008', '0.110002', 'Points_X', '0.220005', '0.489998', '0.719997', 'Points_Y', '0.300008', '0.689998', '0.289998', 'Points_Z', '0.6', '0.310002', '0.639994', 'Points_Magnitude', '1', '0.500008', '0']

# save screenshot
SaveScreenshot('/home/edo20/CFD2020Guardone/Homework/DIAMOND_AIRFOIL/Working_dir/POST-PROCESSING/Plot_over_line.png', lineChartView1, ImageResolution=[2904, 1590], FontScaling='Scale fonts proportionally', OverrideColorPalette='WhiteBackground')

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = []

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['arc_length', 'Coordinates_X', 'Coordinates_Y', 'Coordinates_Z', 'Coordinates_Magnitude', 'Density', 'Energy', 'Exact Density_X', 'Exact Density_Y', 'Exact Density_Magnitude', 'Exact Mach_X', 'Exact Mach_Y', 'Exact Mach_Magnitude', 'Exact Pressure_X', 'Exact Pressure_Y', 'Exact Pressure_Magnitude', 'Exact Temperature_X', 'Exact Temperature_Y', 'Exact Temperature_Magnitude', 'Exact Velocity_X', 'Exact Velocity_Y', 'Exact Velocity_Z', 'Exact Velocity_Magnitude', 'Mach', 'Momentum_X', 'Momentum_Y', 'Momentum_Z', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature', 'Total enthalpy', 'Velocity_X', 'Velocity_Y', 'Velocity_Z', 'Velocity_Magnitude', 'vtkValidPointMask', 'Points_X', 'Points_Y', 'Points_Z', 'Points_Magnitude']

# save data
SaveData('/home/edo20/CFD2020Guardone/Homework/DIAMOND_AIRFOIL/Working_dir/POST-PROCESSING/Data_over_line.csv', proxy=plotOverLine1, Precision=8)

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
# layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(appendAttributes1)

# set active source
SetActiveSource(calculator1_1)

# hide data in view
Hide(plotOverLine1, renderView1)

# set active source
SetActiveSource(appendAttributes1)

# create a new 'Slice'
slice1 = Slice(Input=appendAttributes1)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=slice1.SliceType)

# set active source
SetActiveSource(appendAttributes1)

# set active source
SetActiveSource(slice1)

# Properties modified on slice1
slice1.SliceType = 'Box'

# Properties modified on slice1.SliceType
slice1.SliceType.Position = [-0.3, -0.6, -1.0]
slice1.SliceType.Length = [2.0, 1.2, 2.0]

# show data in view
slice1Display = Show(slice1, renderView1)

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = [None, '']
slice1Display.OSPRayScaleArray = 'Coordinates'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'Coordinates'
slice1Display.ScaleFactor = 0.2000000059604645
slice1Display.SelectScaleArray = 'Coordinates'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'Coordinates'
slice1Display.GaussianRadius = 0.010000000298023224
slice1Display.SetScaleArray = ['POINTS', 'Coordinates']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'Coordinates']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [-0.30000000000000004, 0.0, 0.5, 0.0, 1.7, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [-0.30000000000000004, 0.0, 0.5, 0.0, 1.7, 1.0, 0.5, 0.0]

# hide data in view
Hide(appendAttributes1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(appendAttributes1)

# show data in view
appendAttributes1Display = Show(appendAttributes1, renderView1)

# set active source
SetActiveSource(appendAttributes1)

# hide data in view
Hide(appendAttributes1, renderView1)

# set active source
SetActiveSource(slice1)

# set active source
SetActiveSource(appendAttributes1)

# set active source
SetActiveSource(appendAttributes1)

# show data in view
appendAttributes1Display = Show(appendAttributes1, renderView1)

#change interaction mode for render view
renderView1.InteractionMode = '3D'

# set active source
SetActiveSource(slice1)

# set active source
SetActiveSource(appendAttributes1)

# hide data in view
Hide(slice1, renderView1)

# set active source
SetActiveSource(slice1)

# show data in view
slice1Display = Show(slice1, renderView1)

# set active source
SetActiveSource(slice1)

# hide data in view
Hide(appendAttributes1, renderView1)

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'Density'))

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(appendAttributes1)

# hide data in view
Hide(slice1, renderView1)

# show data in view
appendAttributes1Display = Show(appendAttributes1, renderView1)

# destroy slice1
Delete(slice1)
del slice1

# set active source
SetActiveSource(appendAttributes1)

# create a new 'Clip'
clip1 = Clip(Input=appendAttributes1)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'Density']
clip1.Value = 1.2310039103031158

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# Properties modified on clip1
clip1.ClipType = 'Box'
clip1.Exact = 1

# Properties modified on clip1.ClipType
clip1.ClipType.Position = [-0.3, -0.6, -1.0]
clip1.ClipType.Length = [2.0, 1.2, 2.0]

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = [None, '']
clip1Display.OSPRayScaleArray = 'Coordinates'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'Coordinates'
clip1Display.ScaleFactor = 0.2000000059604645
clip1Display.SelectScaleArray = 'Coordinates'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'Coordinates'
clip1Display.GaussianRadius = 0.010000000298023224
clip1Display.SetScaleArray = ['POINTS', 'Coordinates']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'Coordinates']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityUnitDistance = 0.2168085209818751

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [-0.3, 0.0, 0.5, 0.0, 1.7, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [-0.3, 0.0, 0.5, 0.0, 1.7, 1.0, 0.5, 0.0]

# hide data in view
Hide(appendAttributes1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

#change interaction mode for render view
renderView1.InteractionMode = '2D'

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Calculator'
calculator2 = Calculator(Input=clip1)
calculator2.Function = ''

# Properties modified on calculator2
calculator2.ResultArrayName = 'Mach_error'
calculator2.Function = 'Mach-Exact Mach_X'

# show data in view
calculator2Display = Show(calculator2, renderView1)

# get color transfer function/color map for 'Mach_error'
mach_errorLUT = GetColorTransferFunction('Mach_error')
mach_errorLUT.RGBPoints = [-0.6205622321682835, 0.231373, 0.298039, 0.752941, 0.13648695914359565, 0.865003, 0.865003, 0.865003, 0.8935361504554749, 0.705882, 0.0156863, 0.14902]
mach_errorLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Mach_error'
mach_errorPWF = GetOpacityTransferFunction('Mach_error')
mach_errorPWF.Points = [-0.6205622321682835, 0.0, 0.5, 0.0, 0.8935361504554749, 1.0, 0.5, 0.0]
mach_errorPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator2Display.Representation = 'Surface'
calculator2Display.ColorArrayName = ['POINTS', 'Mach_error']
calculator2Display.LookupTable = mach_errorLUT
calculator2Display.OSPRayScaleArray = 'Mach_error'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.SelectOrientationVectors = 'Coordinates'
calculator2Display.ScaleFactor = 0.2000000059604645
calculator2Display.SelectScaleArray = 'Mach_error'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.GlyphTableIndexArray = 'Mach_error'
calculator2Display.GaussianRadius = 0.010000000298023224
calculator2Display.SetScaleArray = ['POINTS', 'Mach_error']
calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display.OpacityArray = ['POINTS', 'Mach_error']
calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display.PolarAxes = 'PolarAxesRepresentation'
calculator2Display.ScalarOpacityFunction = mach_errorPWF
calculator2Display.ScalarOpacityUnitDistance = 0.2168085209818751

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator2Display.ScaleTransferFunction.Points = [-0.6205622321682835, 0.0, 0.5, 0.0, 0.8935361504554749, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator2Display.OpacityTransferFunction.Points = [-0.6205622321682835, 0.0, 0.5, 0.0, 0.8935361504554749, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
mach_errorLUT.RescaleTransferFunction(-0.5, 0.5)

# Rescale transfer function
mach_errorPWF.RescaleTransferFunction(-0.5, 0.5)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
mach_errorLUT.ApplyPreset('jet', True)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.7000000178813934, 0.0, 5.935533753618102]
renderView1.CameraFocalPoint = [0.7000000178813934, 0.0, 0.0]
renderView1.CameraParallelScale = 0.7166622493635877

# save screenshot
SaveScreenshot('/home/edo20/CFD2020Guardone/Homework/DIAMOND_AIRFOIL/Working_dir/POST-PROCESSING/Mesh_error_clip.png', renderView1, ImageResolution=[2904, 1590],
    OverrideColorPalette='WhiteBackground')

# save data
SaveData('/home/edo20/CFD2020Guardone/Homework/DIAMOND_AIRFOIL/Working_dir/POST-PROCESSING/Data.csv', proxy=calculator2, Precision=8,
    UseScientificNotation=1)
