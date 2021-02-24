# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Unstructured Grid Reader'
flowvtu = XMLUnstructuredGridReader(FileName=['/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil/CASE0/flow.vtu'])
flowvtu.PointArrayStatus = ['Density', 'Momentum', 'Energy', 'Pressure', 'Temperature', 'Mach', 'Pressure_Coefficient']

# create a new 'XML Unstructured Grid Reader'
surface_flowvtu = XMLUnstructuredGridReader(FileName=['/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil/CASE0/surface_flow.vtu'])
surface_flowvtu.PointArrayStatus = ['Density', 'Momentum', 'Energy', 'Pressure', 'Temperature', 'Mach', 'Pressure_Coefficient']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [511, 795]

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
flowvtuDisplay.ScalarOpacityUnitDistance = 10.933163826223883

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
flowvtuDisplay.OSPRayScaleFunction.Points = [1.5819250345230103, 0.0, 0.5, 0.0, 2.035494327545166, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
flowvtuDisplay.ScaleTransferFunction.Points = [0.6519656181335449, 0.0, 0.5, 0.0, 1.6912429332733154, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
flowvtuDisplay.OpacityTransferFunction.Points = [0.6519656181335449, 0.0, 0.5, 0.0, 1.6912429332733154, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10000.0]

# show data in view
surface_flowvtuDisplay = Show(surface_flowvtu, renderView1)

# trace defaults for the display properties.
surface_flowvtuDisplay.Representation = 'Surface'
surface_flowvtuDisplay.ColorArrayName = [None, '']
surface_flowvtuDisplay.OSPRayScaleArray = 'Density'
surface_flowvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
surface_flowvtuDisplay.SelectOrientationVectors = 'Density'
surface_flowvtuDisplay.ScaleFactor = 0.1
surface_flowvtuDisplay.SelectScaleArray = 'Density'
surface_flowvtuDisplay.GlyphType = 'Arrow'
surface_flowvtuDisplay.GlyphTableIndexArray = 'Density'
surface_flowvtuDisplay.GaussianRadius = 0.005
surface_flowvtuDisplay.SetScaleArray = ['POINTS', 'Density']
surface_flowvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
surface_flowvtuDisplay.OpacityArray = ['POINTS', 'Density']
surface_flowvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
surface_flowvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
surface_flowvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
surface_flowvtuDisplay.ScalarOpacityUnitDistance = 0.28886778482974806

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
surface_flowvtuDisplay.OSPRayScaleFunction.Points = [1.5819250345230103, 0.0, 0.5, 0.0, 2.035494327545166, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
surface_flowvtuDisplay.ScaleTransferFunction.Points = [0.6519656181335449, 0.0, 0.5, 0.0, 1.6912429332733154, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
surface_flowvtuDisplay.OpacityTransferFunction.Points = [0.6519656181335449, 0.0, 0.5, 0.0, 1.6912429332733154, 1.0, 0.5, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Programmable Filter'
programmableFilter1 = ProgrammableFilter(Input=surface_flowvtu)
programmableFilter1.Script = ''
programmableFilter1.RequestInformationScript = ''
programmableFilter1.RequestUpdateExtentScript = ''
programmableFilter1.PythonPath = ''

# Properties modified on programmableFilter1
programmableFilter1.Script = """pdi = self.GetInput()
pdo = self.GetOutput()

# Initialize outputs
coords = vtk.vtkDoubleArray()
coords.SetName("Coordinates")
coords.SetNumberOfComponents(3)
V_exact = vtk.vtkDoubleArray()
V_exact.SetName("Exact Velocity")
V_exact.SetNumberOfComponents(3)
n = pdi.GetNumberOfPoints()

# Array values definition
for i in range(n):
    p=pdi.GetPoint(i)
    x, y, z = p
    coords.InsertNextTuple3(x, y, z)
    
    # Freestream zone
    if x < 5:
        V_exact.InsertNextTuple3(100, 10, 0)
    else:
        V_exact.InsertNextTuple3(0, -10, 0)
    

pdo.GetPointData().AddArray(coords)
pdo.GetPointData().AddArray(V_exact)"""
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
programmableFilter1Display.ScaleFactor = 0.1
programmableFilter1Display.SelectScaleArray = 'Coordinates'
programmableFilter1Display.GlyphType = 'Arrow'
programmableFilter1Display.GlyphTableIndexArray = 'Coordinates'
programmableFilter1Display.GaussianRadius = 0.005
programmableFilter1Display.SetScaleArray = ['POINTS', 'Coordinates']
programmableFilter1Display.ScaleTransferFunction = 'PiecewiseFunction'
programmableFilter1Display.OpacityArray = ['POINTS', 'Coordinates']
programmableFilter1Display.OpacityTransferFunction = 'PiecewiseFunction'
programmableFilter1Display.DataAxesGrid = 'GridAxesRepresentation'
programmableFilter1Display.PolarAxes = 'PolarAxesRepresentation'
programmableFilter1Display.ScalarOpacityUnitDistance = 0.28886778482974806

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
programmableFilter1Display.OSPRayScaleFunction.Points = [1.5819250345230103, 0.0, 0.5, 0.0, 2.035494327545166, 1.0, 0.5, 0.0]

# hide data in view
Hide(surface_flowvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(flowvtu)

# set active source
SetActiveSource(programmableFilter1)

# set active source
SetActiveSource(flowvtu)

# create a new 'Programmable Filter'
programmableFilter2 = ProgrammableFilter(Input=flowvtu)
programmableFilter2.Script = ''
programmableFilter2.RequestInformationScript = ''
programmableFilter2.RequestUpdateExtentScript = ''
programmableFilter2.PythonPath = ''

# rename source object
RenameSource('Exact_solution', programmableFilter2)

# set active source
SetActiveSource(surface_flowvtu)

# set active source
SetActiveSource(programmableFilter1)

# rename source object
RenameSource('surface_Exact_Solution', programmableFilter1)

# Properties modified on programmableFilter2
programmableFilter2.Script = """pdi = self.GetInput()
pdo = self.GetOutput()

# Initialize outputs
coords = vtk.vtkDoubleArray()
coords.SetName("Coordinates")
coords.SetNumberOfComponents(3)
V_exact = vtk.vtkDoubleArray()
V_exact.SetName("Exact Velocity")
V_exact.SetNumberOfComponents(3)
n = pdi.GetNumberOfPoints()

# Array values definition
for i in range(n):
    p=pdi.GetPoint(i)
    x, y, z = p
    coords.InsertNextTuple3(x, y, z)
    
    # Freestream zone
    if x < 5:
        V_exact.InsertNextTuple3(100, 10, 0)
    else:
        V_exact.InsertNextTuple3(0, -10, 0)
    

pdo.GetPointData().AddArray(coords)
pdo.GetPointData().AddArray(V_exact)"""
programmableFilter2.RequestInformationScript = ''
programmableFilter2.RequestUpdateExtentScript = ''
programmableFilter2.PythonPath = ''

# show data in view
programmableFilter2Display = Show(programmableFilter2, renderView1)

# trace defaults for the display properties.
programmableFilter2Display.Representation = 'Surface'
programmableFilter2Display.ColorArrayName = [None, '']
programmableFilter2Display.OSPRayScaleArray = 'Coordinates'
programmableFilter2Display.OSPRayScaleFunction = 'PiecewiseFunction'
programmableFilter2Display.SelectOrientationVectors = 'Coordinates'
programmableFilter2Display.ScaleFactor = 20.0
programmableFilter2Display.SelectScaleArray = 'Coordinates'
programmableFilter2Display.GlyphType = 'Arrow'
programmableFilter2Display.GlyphTableIndexArray = 'Coordinates'
programmableFilter2Display.GaussianRadius = 1.0
programmableFilter2Display.SetScaleArray = ['POINTS', 'Coordinates']
programmableFilter2Display.ScaleTransferFunction = 'PiecewiseFunction'
programmableFilter2Display.OpacityArray = ['POINTS', 'Coordinates']
programmableFilter2Display.OpacityTransferFunction = 'PiecewiseFunction'
programmableFilter2Display.DataAxesGrid = 'GridAxesRepresentation'
programmableFilter2Display.PolarAxes = 'PolarAxesRepresentation'
programmableFilter2Display.ScalarOpacityUnitDistance = 10.933163826223883

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
programmableFilter2Display.OSPRayScaleFunction.Points = [1.5819250345230103, 0.0, 0.5, 0.0, 2.035494327545166, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
programmableFilter2Display.ScaleTransferFunction.Points = [-100.0, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
programmableFilter2Display.OpacityTransferFunction.Points = [-100.0, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(flowvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(programmableFilter1Display, ('POINTS', 'Exact Velocity', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
programmableFilter1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
programmableFilter1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'ExactVelocity'
exactVelocityLUT = GetColorTransferFunction('ExactVelocity')
exactVelocityLUT.RGBPoints = [100.4987562112089, 0.231373, 0.298039, 0.752941, 100.50656880995015, 0.865003, 0.865003, 0.865003, 100.5143814086914, 0.705882, 0.0156863, 0.14902]
exactVelocityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'ExactVelocity'
exactVelocityPWF = GetOpacityTransferFunction('ExactVelocity')
exactVelocityPWF.Points = [100.4987562112089, 0.0, 0.5, 0.0, 100.5143814086914, 1.0, 0.5, 0.0]
exactVelocityPWF.ScalarRangeInitialized = 1

# set scalar coloring
ColorBy(programmableFilter1Display, ('POINTS', 'Exact Velocity', 'X'))

# rescale color and/or opacity maps used to exactly fit the current data range
programmableFilter1Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(exactVelocityLUT, programmableFilter1Display)

# set active source
SetActiveSource(programmableFilter2)

# set scalar coloring
ColorBy(programmableFilter2Display, ('POINTS', 'Exact Velocity', 'X'))

# rescale color and/or opacity maps used to include current data range
programmableFilter2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
programmableFilter2Display.SetScalarBarVisibility(renderView1, True)

# save data
SaveData('/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil/CASE0/exact_flow.vtu', proxy=programmableFilter2, Writetimestepsasfileseries=1,
    DataMode='Binary')

# set active source
SetActiveSource(programmableFilter1)

# save data
SaveData('/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil/CASE0/exact_surface_flow.vtu', proxy=programmableFilter1, Writetimestepsasfileseries=1,
    DataMode='Binary')