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

# set scalar coloring
ColorBy(flowvtuDisplay, ('POINTS', 'Mach'))

# rescale color and/or opacity maps used to include current data range
flowvtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
flowvtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Mach'
machLUT = GetColorTransferFunction('Mach')

# get opacity transfer function/opacity map for 'Mach'
machPWF = GetOpacityTransferFunction('Mach')

# change representation type
flowvtuDisplay.SetRepresentationType('Surface With Edges')

# change representation type
flowvtuDisplay.SetRepresentationType('Surface')

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.9010898253281744, 0.04440396897944354, 10000.0]
renderView1.CameraFocalPoint = [0.9010898253281744, 0.04440396897944354, 0.0]
renderView1.CameraParallelScale = 0.9956240290281356

# save screenshot
SaveScreenshot('/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil3/Working_dir/POST-PROCESSING/Mach_image_near.png', renderView1, ImageResolution=[5740, 3180])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.9010898253281744, 0.04440396897944354, 10000.0]
renderView1.CameraFocalPoint = [0.9010898253281744, 0.04440396897944354, 0.0]
renderView1.CameraParallelScale = 0.9956240290281356

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).