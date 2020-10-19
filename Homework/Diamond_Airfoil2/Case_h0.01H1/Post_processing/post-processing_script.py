# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Unstructured Grid Reader'
flowvtu = XMLUnstructuredGridReader(FileName=['/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil2/Case_h0.01H1/CFD/flow.vtu'])

# create a new 'XML Unstructured Grid Reader'
surface_flowvtu = XMLUnstructuredGridReader(FileName=['/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil2/Case_h0.01H1/CFD/surface_flow.vtu'])

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

# set scalar coloring
ColorBy(surface_flowvtuDisplay, ('POINTS', 'Mach'))

# rescale color and/or opacity maps used to include current data range
surface_flowvtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
surface_flowvtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Mach'
machLUT = GetColorTransferFunction('Mach')
machLUT.RGBPoints = [0.8678892254829407, 0.231373, 0.298039, 0.752941, 1.639545351266861, 0.865003, 0.865003, 0.865003, 2.4112014770507812, 0.705882, 0.0156863, 0.14902]
machLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Mach'
machPWF = GetOpacityTransferFunction('Mach')
machPWF.Points = [0.8678892254829407, 0.0, 0.5, 0.0, 2.4112014770507812, 1.0, 0.5, 0.0]
machPWF.ScalarRangeInitialized = 1

# set active source
SetActiveSource(flowvtu)

# set scalar coloring
ColorBy(flowvtuDisplay, ('POINTS', 'Mach'))

# rescale color and/or opacity maps used to include current data range
flowvtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
flowvtuDisplay.SetScalarBarVisibility(renderView1, True)

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=flowvtu,
    Source='High Resolution Line Source')

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1)

# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
# uncomment following to set a specific view size
# lineChartView1.ViewSize = [400, 400]

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1)

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Energy', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Density', '0.889998', '0.100008', '0.110002', 'Energy', '0.220005', '0.489998', '0.719997', 'Mach', '0.300008', '0.689998', '0.289998', 'Momentum_X', '0.6', '0.310002', '0.639994', 'Momentum_Y', '1', '0.500008', '0', 'Momentum_Z', '0.650004', '0.340002', '0.160006', 'Momentum_Magnitude', '0', '0', '0', 'Pressure', '0.889998', '0.100008', '0.110002', 'Pressure_Coefficient', '0.220005', '0.489998', '0.719997', 'Temperature', '0.300008', '0.689998', '0.289998', 'vtkValidPointMask', '0.6', '0.310002', '0.639994', 'Points_X', '1', '0.500008', '0', 'Points_Y', '0.650004', '0.340002', '0.160006', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.889998', '0.100008', '0.110002']
plotOverLine1Display_1.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Density', '1', 'Energy', '1', 'Mach', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Density', '2', 'Energy', '2', 'Mach', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'arc_length', '0', 'vtkValidPointMask', '0']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Mach', 'Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Mach', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Mach', 'Temperature']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Mach']

# save data
SaveData('/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil2/Case_h0.01H1/CFD/M_at_y0.2.csv', proxy=plotOverLine1, Precision=6,
    UseScientificNotation=1)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = []

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Energy']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = []

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Pressure']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Energy', 'Pressure']

# save data
SaveData('/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil2/Case_h0.01H1/CFD/P_and_E_at_y0.2.csv', proxy=plotOverLine1, Precision=6,
    UseScientificNotation=1)

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(lineChartView1)

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(flowvtu)

# hide data in view
Hide(plotOverLine1, renderView1)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
machLUT.ApplyPreset('jet', True)

# set active source
SetActiveSource(surface_flowvtu)

# hide data in view
Hide(surface_flowvtu, renderView1)

# change representation type
surface_flowvtuDisplay.SetRepresentationType('Surface With Edges')

# set active source
SetActiveSource(flowvtu)

# change representation type
flowvtuDisplay.SetRepresentationType('Surface With Edges')

#change interaction mode for render view
renderView1.InteractionMode = '3D'

#change interaction mode for render view
renderView1.InteractionMode = '2D'

# set scalar coloring
ColorBy(flowvtuDisplay, ('POINTS', 'Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(machLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
flowvtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
flowvtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Pressure'
pressureLUT = GetColorTransferFunction('Pressure')
pressureLUT.RGBPoints = [42195.6015625, 0.231373, 0.298039, 0.752941, 151043.72265625, 0.865003, 0.865003, 0.865003, 259891.84375, 0.705882, 0.0156863, 0.14902]
pressureLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Pressure'
pressurePWF = GetOpacityTransferFunction('Pressure')
pressurePWF.Points = [42195.6015625, 0.0, 0.5, 0.0, 259891.84375, 1.0, 0.5, 0.0]
pressurePWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pressureLUT.ApplyPreset('jet', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pressureLUT.ApplyPreset('Cool to Warm', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pressureLUT.ApplyPreset('Cool to Warm', True)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.6410634770718353, 0.06449427205655713, 9999.999999999996]
renderView1.CameraFocalPoint = [0.6410634770718353, 0.06449427205655713, 0.0]
renderView1.CameraViewUp = [-0.005292212529591838, 0.999985996145217, 0.0]
renderView1.CameraParallelScale = 0.5620038085214868

# save screenshot
SaveScreenshot('/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil2/Case_h0.01H1/Post_processing/Pressure_with_edges.png', renderView1, ImageResolution=[5740, 3180])

# change representation type
flowvtuDisplay.SetRepresentationType('Surface')

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.6410634770718353, 0.06449427205655713, 9999.999999999996]
renderView1.CameraFocalPoint = [0.6410634770718353, 0.06449427205655713, 0.0]
renderView1.CameraViewUp = [-0.005292212529591838, 0.999985996145217, 0.0]
renderView1.CameraParallelScale = 0.5620038085214868

# save screenshot
SaveScreenshot('/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil2/Case_h0.01H1/Post_processing/Pressure.png', renderView1, ImageResolution=[5740, 3180])

# set active source
SetActiveSource(surface_flowvtu)

# hide data in view
Hide(flowvtu, renderView1)

# set active source
SetActiveSource(surface_flowvtu)

# show data in view
surface_flowvtuDisplay = Show(surface_flowvtu, renderView1)

# show color bar/color legend
surface_flowvtuDisplay.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Clip'
clip1 = Clip(Input=surface_flowvtu)

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [0.0, 0.0, 0.0]
clip1.ClipType.Normal = [0.0, 1.0, 0.0]

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'

# hide data in view
Hide(surface_flowvtu, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Plot Data'
plotData1 = PlotData(Input=clip1)

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
# uncomment following to set a specific view size
# lineChartView1.ViewSize = [400, 400]

# show data in view
plotData1Display = Show(plotData1, lineChartView1)

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Density', 'Energy', 'Mach', 'Momentum_Magnitude', 'Pressure_Coefficient', 'Temperature']
plotData1Display.SeriesColor = ['Density', '0', '0', '0', 'Energy', '0.889998', '0.100008', '0.110002', 'Mach', '0.220005', '0.489998', '0.719997', 'Momentum_X', '0.300008', '0.689998', '0.289998', 'Momentum_Y', '0.6', '0.310002', '0.639994', 'Momentum_Z', '1', '0.500008', '0', 'Momentum_Magnitude', '0.650004', '0.340002', '0.160006', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.889998', '0.100008', '0.110002', 'Temperature', '0.220005', '0.489998', '0.719997', 'Points_X', '0.300008', '0.689998', '0.289998', 'Points_Y', '0.6', '0.310002', '0.639994', 'Points_Z', '1', '0.500008', '0', 'Points_Magnitude', '0.650004', '0.340002', '0.160006']
plotData1Display.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']
plotData1Display.SeriesLineStyle = ['Density', '1', 'Energy', '1', 'Mach', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1']
plotData1Display.SeriesLineThickness = ['Density', '2', 'Energy', '2', 'Mach', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2']
plotData1Display.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Density', 'Energy', 'Mach', 'Momentum_Magnitude', 'Pressure_Coefficient']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Density', 'Energy', 'Mach', 'Pressure_Coefficient']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Density', 'Energy', 'Pressure_Coefficient']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Density', 'Pressure_Coefficient']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Pressure_Coefficient']

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(surface_flowvtu)

# create a new 'Clip'
clip2 = Clip(Input=surface_flowvtu)

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [0.0, 0.0, 0.0]
clip2.ClipType.Normal = [0.0, -1.0, 0.0]

# show data in view
clip2Display = Show(clip2, renderView1)

# trace defaults for the display properties.
clip2Display.Representation = 'Surface'

# hide data in view
Hide(surface_flowvtu, renderView1)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(clip1, renderView1)

# set active source
SetActiveSource(clip1)

# show data in view
clip1Display = Show(clip1, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(clip1, renderView1)

# set active source
SetActiveSource(clip2)

# create a new 'Plot Data'
plotData2 = PlotData(Input=clip2)

# Create a new 'Line Chart View'
lineChartView2 = CreateView('XYChartView')
# uncomment following to set a specific view size
# lineChartView2.ViewSize = [400, 400]

# show data in view
plotData2Display = Show(plotData2, lineChartView2)

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView2, layout=layout1, hint=1)

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['Energy', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']
plotData2Display.SeriesColor = ['Density', '0', '0', '0', 'Energy', '0.889998', '0.100008', '0.110002', 'Mach', '0.220005', '0.489998', '0.719997', 'Momentum_X', '0.300008', '0.689998', '0.289998', 'Momentum_Y', '0.6', '0.310002', '0.639994', 'Momentum_Z', '1', '0.500008', '0', 'Momentum_Magnitude', '0.650004', '0.340002', '0.160006', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.889998', '0.100008', '0.110002', 'Temperature', '0.220005', '0.489998', '0.719997', 'Points_X', '0.300008', '0.689998', '0.289998', 'Points_Y', '0.6', '0.310002', '0.639994', 'Points_Z', '1', '0.500008', '0', 'Points_Magnitude', '0.650004', '0.340002', '0.160006']
plotData2Display.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']
plotData2Display.SeriesLineStyle = ['Density', '1', 'Energy', '1', 'Mach', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1']
plotData2Display.SeriesLineThickness = ['Density', '2', 'Energy', '2', 'Mach', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2']
plotData2Display.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['Pressure_Coefficient', 'Temperature']

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['Pressure_Coefficient']

# set active view
SetActiveView(lineChartView1)

# split cell
layout1.SplitVertical(2, 0.5)

# set active view
SetActiveView(None)

# set active view
SetActiveView(lineChartView2)

# set active view
SetActiveView(lineChartView1)

# set active view
SetActiveView(None)

# close an empty frame
layout1.Collapse(6)

# set active view
SetActiveView(lineChartView1)

# set active view
SetActiveView(renderView1)

# split cell
layout1.SplitHorizontal(3, 0.5)

# set active view
SetActiveView(None)

# close an empty frame
layout1.Collapse(8)

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(lineChartView2)

# set active view
SetActiveView(lineChartView1)

# split cell
layout1.SplitVertical(2, 0.5)

# set active view
SetActiveView(None)

# set active view
SetActiveView(lineChartView2)

# split cell
layout1.SplitHorizontal(4, 0.5)

# set active view
SetActiveView(None)

# close an empty frame
layout1.Collapse(10)

# set active view
SetActiveView(lineChartView2)

# set active view
SetActiveView(None)

# close an empty frame
layout1.Collapse(6)

# set active view
SetActiveView(lineChartView1)

# set active view
SetActiveView(lineChartView2)

# set active view
SetActiveView(lineChartView1)

# split cell
layout1.SplitVertical(2, 0.5)

# set active view
SetActiveView(None)

# set active view
SetActiveView(lineChartView2)

# set active view
SetActiveView(None)

# Create a new 'Python View'
pythonView1 = CreateView('PythonView')
pythonView1.Script = ''
# uncomment following to set a specific view size
# pythonView1.ViewSize = [400, 400]

# assign view to a particular cell in the layout
AssignViewToLayout(view=pythonView1, layout=layout1, hint=6)

# destroy pythonView1
Delete(pythonView1)
del pythonView1

# close an empty frame
layout1.Collapse(6)

# set active view
SetActiveView(lineChartView1)

# set active view
SetActiveView(lineChartView2)

# set active view
SetActiveView(lineChartView1)

# split cell
layout1.SplitVertical(2, 0.5)

# set active view
SetActiveView(None)

# set active view
SetActiveView(lineChartView2)

# destroy lineChartView2
Delete(lineChartView2)
del lineChartView2

# close an empty frame
layout1.Collapse(4)

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(None)

# set active source
SetActiveSource(plotData2)

# Create a new 'Line Chart View'
lineChartView2 = CreateView('XYChartView')
# uncomment following to set a specific view size
# lineChartView2.ViewSize = [400, 400]

# show data in view
plotData2Display = Show(plotData2, lineChartView2)

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView2, layout=layout1, hint=6)

# set active view
SetActiveView(lineChartView1)

# set active view
SetActiveView(renderView1)

# destroy renderView1
Delete(renderView1)
del renderView1

# close an empty frame
layout1.Collapse(1)

# set active view
SetActiveView(None)

# set active view
SetActiveView(lineChartView2)

# Properties modified on plotData2Display
plotData2Display.UseIndexForXAxis = 0

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['Energy', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']
plotData2Display.SeriesColor = ['Density', '0', '0', '0', 'Energy', '0.889998', '0.100008', '0.110002', 'Mach', '0.220005', '0.489998', '0.719997', 'Momentum_X', '0.300008', '0.689998', '0.289998', 'Momentum_Y', '0.6', '0.310002', '0.639994', 'Momentum_Z', '1', '0.500008', '0', 'Momentum_Magnitude', '0.650004', '0.340002', '0.160006', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.889998', '0.100008', '0.110002', 'Temperature', '0.220005', '0.489998', '0.719997', 'Points_X', '0.300008', '0.689998', '0.289998', 'Points_Y', '0.6', '0.310002', '0.639994', 'Points_Z', '1', '0.500008', '0', 'Points_Magnitude', '0.650004', '0.340002', '0.160006']
plotData2Display.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']
plotData2Display.SeriesLineStyle = ['Density', '1', 'Energy', '1', 'Mach', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1']
plotData2Display.SeriesLineThickness = ['Density', '2', 'Energy', '2', 'Mach', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2']
plotData2Display.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['Pressure_Coefficient', 'Temperature']

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['Pressure_Coefficient']

# Properties modified on lineChartView2
lineChartView2.LeftAxisUseCustomRange = 0

# Properties modified on plotData2Display
plotData2Display.XArrayName = 'Points_X'

# Properties modified on plotData2Display
plotData2Display.XArrayName = 'Points_Magnitude'

# Properties modified on plotData2Display
plotData2Display.XArrayName = 'Momentum_X'

# Properties modified on plotData2Display
plotData2Display.XArrayName = 'Points_X'

# Properties modified on lineChartView2
lineChartView2.BottomAxisUseCustomRange = 0

# set active view
SetActiveView(lineChartView1)

# Properties modified on lineChartView1
lineChartView1.BottomAxisUseCustomRange = 0

# Properties modified on lineChartView1
lineChartView1.SortByXAxis = 1

# Properties modified on lineChartView1
lineChartView1.SortByXAxis = 0

# set active source
SetActiveSource(plotData1)

# Properties modified on plotData1Display
plotData1Display.AttributeType = 'Field Data'

# Properties modified on plotData1Display
plotData1Display.UseIndexForXAxis = 0

# Properties modified on plotData1Display
plotData1Display.UseIndexForXAxis = 1

# Properties modified on lineChartView1
lineChartView1.ShowLegend = 0

# Properties modified on lineChartView1
lineChartView1.ShowLegend = 1

# Properties modified on lineChartView1
lineChartView1.SortByXAxis = 1

# Properties modified on lineChartView1
lineChartView1.SortByXAxis = 0

# Properties modified on lineChartView1
lineChartView1.ShowLegend = 0

# Properties modified on lineChartView1
lineChartView1.ShowLegend = 1

# Properties modified on plotData1Display
plotData1Display.UseIndexForXAxis = 0

# Properties modified on plotData1Display
plotData1Display.UseIndexForXAxis = 1

# Properties modified on plotData1Display
plotData1Display.AttributeType = 'Point Data'

# Properties modified on plotData1Display
plotData1Display.UseIndexForXAxis = 0

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Points_X'

# Properties modified on lineChartView1
lineChartView1.BottomAxisUseCustomRange = 0

# set active view
SetActiveView(lineChartView2)

# set active source
SetActiveSource(plotData2)

# Properties modified on lineChartView2
lineChartView2.LeftAxisUseCustomRange = 0

# Properties modified on lineChartView2
lineChartView2.BottomAxisUseCustomRange = 0

# set active view
SetActiveView(lineChartView1)

# set active view
SetActiveView(lineChartView2)

# save screenshot
SaveScreenshot('/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil2/Case_h0.01H1/Post_processing/CP_Upper_Lower.png', lineChartView2, ImageResolution=[1435, 382])

# destroy lineChartView2
Delete(lineChartView2)
del lineChartView2

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(lineChartView1)

# set active source
SetActiveSource(plotData2)

# show data in view
plotData2Display = Show(plotData2, lineChartView1)

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['Density', 'Energy', 'Mach', 'Momentum_Magnitude', 'Pressure_Coefficient', 'Temperature']
plotData2Display.SeriesColor = ['Density', '0', '0', '0', 'Energy', '0.889998', '0.100008', '0.110002', 'Mach', '0.220005', '0.489998', '0.719997', 'Momentum_X', '0.300008', '0.689998', '0.289998', 'Momentum_Y', '0.6', '0.310002', '0.639994', 'Momentum_Z', '1', '0.500008', '0', 'Momentum_Magnitude', '0.650004', '0.340002', '0.160006', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.889998', '0.100008', '0.110002', 'Temperature', '0.220005', '0.489998', '0.719997', 'Points_X', '0.300008', '0.689998', '0.289998', 'Points_Y', '0.6', '0.310002', '0.639994', 'Points_Z', '1', '0.500008', '0', 'Points_Magnitude', '0.650004', '0.340002', '0.160006']
plotData2Display.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']
plotData2Display.SeriesLineStyle = ['Density', '1', 'Energy', '1', 'Mach', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1']
plotData2Display.SeriesLineThickness = ['Density', '2', 'Energy', '2', 'Mach', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2']
plotData2Display.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['Density', 'Energy', 'Mach', 'Momentum_Magnitude', 'Pressure_Coefficient']

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['Density', 'Energy', 'Mach', 'Pressure_Coefficient']

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['Density', 'Energy', 'Pressure_Coefficient']

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['Energy', 'Pressure_Coefficient']

# Properties modified on plotData2Display
plotData2Display.SeriesVisibility = ['Pressure_Coefficient']

# Properties modified on plotData2Display
plotData2Display.SeriesLabel = ['Density', 'Density', 'Energy', 'Energy', 'Mach', 'Mach', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', 'Pressure', 'Pressure', 'Pressure_Coefficient', 'Lower CP', 'Temperature', 'Temperature', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']

# set active source
SetActiveSource(plotData1)

# set active source
SetActiveSource(clip1)

CreateLayout('Layout #2')

# set active view
SetActiveView(None)

# set active source
SetActiveSource(clip1)

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraFocalDisk = 1.0
renderView1.Background = [0.32, 0.34, 0.43]
# uncomment following to set a specific view size
# renderView1.ViewSize = [400, 400]

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'

# get layout
layout2 = GetLayoutByName("Layout #2")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=renderView1, layout=layout2, hint=0)

# reset view to fit data
renderView1.ResetCamera()

# hide data in view
Hide(clip1, renderView1)

# show data in view
clip1Display = Show(clip1, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# hide data in view
Hide(clip1, renderView1)

# set active source
SetActiveSource(plotData2)

# set active view
SetActiveView(lineChartView1)

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

RemoveLayout(layout1)

# set active source
SetActiveSource(plotData2)

# show data in view
plotData2Display = Show(plotData2, renderView1)

# trace defaults for the display properties.
plotData2Display.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera()

# set active source
SetActiveSource(plotData1)

# show data in view
plotData1Display = Show(plotData1, renderView1)

# trace defaults for the display properties.
plotData1Display.Representation = 'Surface'

CreateLayout('Layout #2')

# set active view
SetActiveView(None)

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
# uncomment following to set a specific view size
# lineChartView1.ViewSize = [400, 400]

# show data in view
plotData1Display_1 = Show(plotData1, lineChartView1)

# get layout
layout2_1 = GetLayoutByName("Layout #2")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout2_1, hint=0)

# Properties modified on plotData1Display_1
plotData1Display_1.SeriesVisibility = ['Energy', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']
plotData1Display_1.SeriesColor = ['Density', '0', '0', '0', 'Energy', '0.889998', '0.100008', '0.110002', 'Mach', '0.220005', '0.489998', '0.719997', 'Momentum_X', '0.300008', '0.689998', '0.289998', 'Momentum_Y', '0.6', '0.310002', '0.639994', 'Momentum_Z', '1', '0.500008', '0', 'Momentum_Magnitude', '0.650004', '0.340002', '0.160006', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.889998', '0.100008', '0.110002', 'Temperature', '0.220005', '0.489998', '0.719997', 'Points_X', '0.300008', '0.689998', '0.289998', 'Points_Y', '0.6', '0.310002', '0.639994', 'Points_Z', '1', '0.500008', '0', 'Points_Magnitude', '0.650004', '0.340002', '0.160006']
plotData1Display_1.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']
plotData1Display_1.SeriesLineStyle = ['Density', '1', 'Energy', '1', 'Mach', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1']
plotData1Display_1.SeriesLineThickness = ['Density', '2', 'Energy', '2', 'Mach', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2']
plotData1Display_1.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']

# Properties modified on plotData1Display_1
plotData1Display_1.SeriesVisibility = ['Energy', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData1Display_1
plotData1Display_1.SeriesVisibility = ['Energy', 'Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData1Display_1
plotData1Display_1.SeriesVisibility = ['Energy', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData1Display_1
plotData1Display_1.SeriesVisibility = ['Energy', 'Pressure_Coefficient']

# Properties modified on plotData1Display_1
plotData1Display_1.SeriesVisibility = ['Pressure_Coefficient']

# Properties modified on plotData1Display_1
plotData1Display_1.SeriesLabel = ['Density', 'Density', 'Energy', 'Energy', 'Mach', 'Mach', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', 'Pressure', 'Pressure', 'Pressure_Coefficient', 'Lower CP', 'Temperature', 'Temperature', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']

# set active source
SetActiveSource(plotData2)

# set active source
SetActiveSource(plotData1)

# Properties modified on plotData1Display_1
plotData1Display_1.SeriesLabel = ['Density', 'Density', 'Energy', 'Energy', 'Mach', 'Mach', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', 'Pressure', 'Pressure', 'Pressure_Coefficient', 'CP Bottom', 'Temperature', 'Temperature', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']

# set active source
SetActiveSource(plotData2)

# set active source
SetActiveSource(plotData2)

# show data in view
plotData2Display_1 = Show(plotData2, lineChartView1)

# Properties modified on plotData2Display_1
plotData2Display_1.SeriesVisibility = ['Energy', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']
plotData2Display_1.SeriesColor = ['Density', '0', '0', '0', 'Energy', '0.889998', '0.100008', '0.110002', 'Mach', '0.220005', '0.489998', '0.719997', 'Momentum_X', '0.300008', '0.689998', '0.289998', 'Momentum_Y', '0.6', '0.310002', '0.639994', 'Momentum_Z', '1', '0.500008', '0', 'Momentum_Magnitude', '0.650004', '0.340002', '0.160006', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.889998', '0.100008', '0.110002', 'Temperature', '0.220005', '0.489998', '0.719997', 'Points_X', '0.300008', '0.689998', '0.289998', 'Points_Y', '0.6', '0.310002', '0.639994', 'Points_Z', '1', '0.500008', '0', 'Points_Magnitude', '0.650004', '0.340002', '0.160006']
plotData2Display_1.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']
plotData2Display_1.SeriesLineStyle = ['Density', '1', 'Energy', '1', 'Mach', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1']
plotData2Display_1.SeriesLineThickness = ['Density', '2', 'Energy', '2', 'Mach', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2']
plotData2Display_1.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']

# Properties modified on plotData2Display_1
plotData2Display_1.SeriesVisibility = ['Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData2Display_1
plotData2Display_1.SeriesVisibility = ['Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData2Display_1
plotData2Display_1.SeriesVisibility = ['Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData2Display_1
plotData2Display_1.SeriesVisibility = ['Pressure_Coefficient', 'Temperature']

# Properties modified on plotData2Display_1
plotData2Display_1.SeriesVisibility = ['Pressure_Coefficient']

# Properties modified on plotData2Display_1
plotData2Display_1.SeriesLabel = ['Density', 'Density', 'Energy', 'Energy', 'Mach', 'Mach', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', 'Pressure', 'Pressure', 'Pressure_Coefficient', 'CP Top', 'Temperature', 'Temperature', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']

# Properties modified on plotData2Display_1
plotData2Display_1.SeriesColor = ['Density', '0', '0', '0', 'Energy', '0.889998', '0.100008', '0.110002', 'Mach', '0.220005', '0.489998', '0.719997', 'Momentum_X', '0.300008', '0.689998', '0.289998', 'Momentum_Y', '0.6', '0.310002', '0.639994', 'Momentum_Z', '1', '0.500008', '0', 'Momentum_Magnitude', '0.650004', '0.340002', '0.160006', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0', '0', '0', 'Temperature', '0.220005', '0.489998', '0.719997', 'Points_X', '0.300008', '0.689998', '0.289998', 'Points_Y', '0.6', '0.310002', '0.639994', 'Points_Z', '1', '0.500008', '0', 'Points_Magnitude', '0.650004', '0.340002', '0.160006']

# save screenshot
SaveScreenshot('/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil2/Case_h0.01H1/Post_processing/CP_Upper_Lower.png', lineChartView1, ImageResolution=[1435, 795])

# save data
SaveData('/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil2/Case_h0.01H1/CFD/CP_Top_Bottom.csv', proxy=plotData2)

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# set active source
SetActiveSource(flowvtu)

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraFocalDisk = 1.0
renderView2.Background = [0.32, 0.34, 0.43]
# uncomment following to set a specific view size
# renderView2.ViewSize = [400, 400]

# show data in view
flowvtuDisplay = Show(flowvtu, renderView2)

# trace defaults for the display properties.
flowvtuDisplay.Representation = 'Surface'

# add view to a layout so it's visible in UI
AssignViewToLayout(view=renderView2, layout=layout2_1, hint=0)

# reset view to fit data
renderView2.ResetCamera()

# destroy renderView2
Delete(renderView2)
del renderView2

RemoveLayout(layout2_1)

# get layout
layout3 = GetLayoutByName("Layout #3")

RemoveLayout(layout3)

# destroy renderView1
Delete(renderView1)
del renderView1

RemoveLayout(layout2)

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraFocalDisk = 1.0
renderView1.Background = [0.32, 0.34, 0.43]
# uncomment following to set a specific view size
# renderView1.ViewSize = [400, 400]

# show data in view
flowvtuDisplay = Show(flowvtu, renderView1)

# trace defaults for the display properties.
flowvtuDisplay.Representation = 'Surface'

# get layout
layout1_1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=renderView1, layout=layout1_1, hint=0)

# reset view to fit data
renderView1.ResetCamera()

#change interaction mode for render view
renderView1.InteractionMode = '2D'

#change interaction mode for render view
renderView1.InteractionMode = '3D'

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

#change interaction mode for render view
renderView1.InteractionMode = '2D'

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.834819405814347, -0.12337451351794113, 118.91477123719842]
renderView1.CameraFocalPoint = [0.834819405814347, -0.12337451351794113, -1e-20]
renderView1.CameraParallelScale = 0.9956240290281357

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).