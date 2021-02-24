# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Unstructured Grid Reader'
flowvtu = XMLUnstructuredGridReader(FileName=['/home/edo20/CFD2020_Guardone/Homework/DIAMOND_AIRFOIL/CASE0/flow.vtu'])
flowvtu.CellArrayStatus = []
flowvtu.PointArrayStatus = ['Density', 'Momentum', 'Energy', 'Pressure', 'Temperature', 'Mach', 'Pressure_Coefficient']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1480, 795]

# show data in view
flowvtuDisplay = Show(flowvtu, renderView1)

# trace defaults for the display properties.
flowvtuDisplay.Representation = 'Surface'
flowvtuDisplay.AmbientColor = [1.0, 1.0, 1.0]
flowvtuDisplay.ColorArrayName = [None, '']
flowvtuDisplay.DiffuseColor = [1.0, 1.0, 1.0]
flowvtuDisplay.LookupTable = None
flowvtuDisplay.MapScalars = 1
flowvtuDisplay.MultiComponentsMapping = 0
flowvtuDisplay.InterpolateScalarsBeforeMapping = 1
flowvtuDisplay.Opacity = 1.0
flowvtuDisplay.PointSize = 2.0
flowvtuDisplay.LineWidth = 1.0
flowvtuDisplay.RenderLinesAsTubes = 0
flowvtuDisplay.RenderPointsAsSpheres = 0
flowvtuDisplay.Interpolation = 'Gouraud'
flowvtuDisplay.Specular = 0.0
flowvtuDisplay.SpecularColor = [1.0, 1.0, 1.0]
flowvtuDisplay.SpecularPower = 100.0
flowvtuDisplay.Luminosity = 0.0
flowvtuDisplay.Ambient = 0.0
flowvtuDisplay.Diffuse = 1.0
flowvtuDisplay.EdgeColor = [0.0, 0.0, 0.5]
flowvtuDisplay.BackfaceRepresentation = 'Follow Frontface'
flowvtuDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
flowvtuDisplay.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
flowvtuDisplay.BackfaceOpacity = 1.0
flowvtuDisplay.Position = [0.0, 0.0, 0.0]
flowvtuDisplay.Scale = [1.0, 1.0, 1.0]
flowvtuDisplay.Orientation = [0.0, 0.0, 0.0]
flowvtuDisplay.Origin = [0.0, 0.0, 0.0]
flowvtuDisplay.Pickable = 1
flowvtuDisplay.Texture = None
flowvtuDisplay.Triangulate = 0
flowvtuDisplay.UseShaderReplacements = 0
flowvtuDisplay.ShaderReplacements = ''
flowvtuDisplay.NonlinearSubdivisionLevel = 1
flowvtuDisplay.UseDataPartitions = 0
flowvtuDisplay.OSPRayUseScaleArray = 0
flowvtuDisplay.OSPRayScaleArray = 'Density'
flowvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
flowvtuDisplay.OSPRayMaterial = 'None'
flowvtuDisplay.Orient = 0
flowvtuDisplay.OrientationMode = 'Direction'
flowvtuDisplay.SelectOrientationVectors = 'Density'
flowvtuDisplay.Scaling = 0
flowvtuDisplay.ScaleMode = 'No Data Scaling Off'
flowvtuDisplay.ScaleFactor = 20.0
flowvtuDisplay.SelectScaleArray = 'Density'
flowvtuDisplay.GlyphType = 'Arrow'
flowvtuDisplay.UseGlyphTable = 0
flowvtuDisplay.GlyphTableIndexArray = 'Density'
flowvtuDisplay.UseCompositeGlyphTable = 0
flowvtuDisplay.UseGlyphCullingAndLOD = 0
flowvtuDisplay.LODValues = []
flowvtuDisplay.ColorByLODIndex = 0
flowvtuDisplay.GaussianRadius = 1.0
flowvtuDisplay.ShaderPreset = 'Sphere'
flowvtuDisplay.CustomTriangleScale = 3
flowvtuDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
flowvtuDisplay.Emissive = 0
flowvtuDisplay.ScaleByArray = 0
flowvtuDisplay.SetScaleArray = ['POINTS', 'Density']
flowvtuDisplay.ScaleArrayComponent = ''
flowvtuDisplay.UseScaleFunction = 1
flowvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
flowvtuDisplay.OpacityByArray = 0
flowvtuDisplay.OpacityArray = ['POINTS', 'Density']
flowvtuDisplay.OpacityArrayComponent = ''
flowvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
flowvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
flowvtuDisplay.SelectionCellLabelBold = 0
flowvtuDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
flowvtuDisplay.SelectionCellLabelFontFamily = 'Arial'
flowvtuDisplay.SelectionCellLabelFontFile = ''
flowvtuDisplay.SelectionCellLabelFontSize = 18
flowvtuDisplay.SelectionCellLabelItalic = 0
flowvtuDisplay.SelectionCellLabelJustification = 'Left'
flowvtuDisplay.SelectionCellLabelOpacity = 1.0
flowvtuDisplay.SelectionCellLabelShadow = 0
flowvtuDisplay.SelectionPointLabelBold = 0
flowvtuDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
flowvtuDisplay.SelectionPointLabelFontFamily = 'Arial'
flowvtuDisplay.SelectionPointLabelFontFile = ''
flowvtuDisplay.SelectionPointLabelFontSize = 18
flowvtuDisplay.SelectionPointLabelItalic = 0
flowvtuDisplay.SelectionPointLabelJustification = 'Left'
flowvtuDisplay.SelectionPointLabelOpacity = 1.0
flowvtuDisplay.SelectionPointLabelShadow = 0
flowvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
flowvtuDisplay.ScalarOpacityFunction = None
flowvtuDisplay.ScalarOpacityUnitDistance = 10.67438550346949
flowvtuDisplay.ExtractedBlockIndex = 0
flowvtuDisplay.SelectMapper = 'Projected tetra'
flowvtuDisplay.SamplingDimensions = [128, 128, 128]
flowvtuDisplay.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
flowvtuDisplay.OSPRayScaleFunction.Points = [270962.9375, 0.0, 0.5, 0.0, 809535.8125, 1.0, 0.5, 0.0]
flowvtuDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
flowvtuDisplay.GlyphType.TipResolution = 6
flowvtuDisplay.GlyphType.TipRadius = 0.1
flowvtuDisplay.GlyphType.TipLength = 0.35
flowvtuDisplay.GlyphType.ShaftResolution = 6
flowvtuDisplay.GlyphType.ShaftRadius = 0.03
flowvtuDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
flowvtuDisplay.ScaleTransferFunction.Points = [0.5517352223396301, 0.0, 0.5, 0.0, 1.9102725982666016, 1.0, 0.5, 0.0]
flowvtuDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
flowvtuDisplay.OpacityTransferFunction.Points = [0.5517352223396301, 0.0, 0.5, 0.0, 1.9102725982666016, 1.0, 0.5, 0.0]
flowvtuDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
flowvtuDisplay.DataAxesGrid.XTitle = 'X Axis'
flowvtuDisplay.DataAxesGrid.YTitle = 'Y Axis'
flowvtuDisplay.DataAxesGrid.ZTitle = 'Z Axis'
flowvtuDisplay.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
flowvtuDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
flowvtuDisplay.DataAxesGrid.XTitleFontFile = ''
flowvtuDisplay.DataAxesGrid.XTitleBold = 0
flowvtuDisplay.DataAxesGrid.XTitleItalic = 0
flowvtuDisplay.DataAxesGrid.XTitleFontSize = 12
flowvtuDisplay.DataAxesGrid.XTitleShadow = 0
flowvtuDisplay.DataAxesGrid.XTitleOpacity = 1.0
flowvtuDisplay.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
flowvtuDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
flowvtuDisplay.DataAxesGrid.YTitleFontFile = ''
flowvtuDisplay.DataAxesGrid.YTitleBold = 0
flowvtuDisplay.DataAxesGrid.YTitleItalic = 0
flowvtuDisplay.DataAxesGrid.YTitleFontSize = 12
flowvtuDisplay.DataAxesGrid.YTitleShadow = 0
flowvtuDisplay.DataAxesGrid.YTitleOpacity = 1.0
flowvtuDisplay.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
flowvtuDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
flowvtuDisplay.DataAxesGrid.ZTitleFontFile = ''
flowvtuDisplay.DataAxesGrid.ZTitleBold = 0
flowvtuDisplay.DataAxesGrid.ZTitleItalic = 0
flowvtuDisplay.DataAxesGrid.ZTitleFontSize = 12
flowvtuDisplay.DataAxesGrid.ZTitleShadow = 0
flowvtuDisplay.DataAxesGrid.ZTitleOpacity = 1.0
flowvtuDisplay.DataAxesGrid.FacesToRender = 63
flowvtuDisplay.DataAxesGrid.CullBackface = 0
flowvtuDisplay.DataAxesGrid.CullFrontface = 1
flowvtuDisplay.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
flowvtuDisplay.DataAxesGrid.ShowGrid = 0
flowvtuDisplay.DataAxesGrid.ShowEdges = 1
flowvtuDisplay.DataAxesGrid.ShowTicks = 1
flowvtuDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
flowvtuDisplay.DataAxesGrid.AxesToLabel = 63
flowvtuDisplay.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
flowvtuDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
flowvtuDisplay.DataAxesGrid.XLabelFontFile = ''
flowvtuDisplay.DataAxesGrid.XLabelBold = 0
flowvtuDisplay.DataAxesGrid.XLabelItalic = 0
flowvtuDisplay.DataAxesGrid.XLabelFontSize = 12
flowvtuDisplay.DataAxesGrid.XLabelShadow = 0
flowvtuDisplay.DataAxesGrid.XLabelOpacity = 1.0
flowvtuDisplay.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
flowvtuDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
flowvtuDisplay.DataAxesGrid.YLabelFontFile = ''
flowvtuDisplay.DataAxesGrid.YLabelBold = 0
flowvtuDisplay.DataAxesGrid.YLabelItalic = 0
flowvtuDisplay.DataAxesGrid.YLabelFontSize = 12
flowvtuDisplay.DataAxesGrid.YLabelShadow = 0
flowvtuDisplay.DataAxesGrid.YLabelOpacity = 1.0
flowvtuDisplay.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
flowvtuDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
flowvtuDisplay.DataAxesGrid.ZLabelFontFile = ''
flowvtuDisplay.DataAxesGrid.ZLabelBold = 0
flowvtuDisplay.DataAxesGrid.ZLabelItalic = 0
flowvtuDisplay.DataAxesGrid.ZLabelFontSize = 12
flowvtuDisplay.DataAxesGrid.ZLabelShadow = 0
flowvtuDisplay.DataAxesGrid.ZLabelOpacity = 1.0
flowvtuDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
flowvtuDisplay.DataAxesGrid.XAxisPrecision = 2
flowvtuDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
flowvtuDisplay.DataAxesGrid.XAxisLabels = []
flowvtuDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
flowvtuDisplay.DataAxesGrid.YAxisPrecision = 2
flowvtuDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
flowvtuDisplay.DataAxesGrid.YAxisLabels = []
flowvtuDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
flowvtuDisplay.DataAxesGrid.ZAxisPrecision = 2
flowvtuDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
flowvtuDisplay.DataAxesGrid.ZAxisLabels = []
flowvtuDisplay.DataAxesGrid.UseCustomBounds = 0
flowvtuDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
flowvtuDisplay.PolarAxes.Visibility = 0
flowvtuDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
flowvtuDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
flowvtuDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
flowvtuDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
flowvtuDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
flowvtuDisplay.PolarAxes.EnableCustomRange = 0
flowvtuDisplay.PolarAxes.CustomRange = [0.0, 1.0]
flowvtuDisplay.PolarAxes.PolarAxisVisibility = 1
flowvtuDisplay.PolarAxes.RadialAxesVisibility = 1
flowvtuDisplay.PolarAxes.DrawRadialGridlines = 1
flowvtuDisplay.PolarAxes.PolarArcsVisibility = 1
flowvtuDisplay.PolarAxes.DrawPolarArcsGridlines = 1
flowvtuDisplay.PolarAxes.NumberOfRadialAxes = 0
flowvtuDisplay.PolarAxes.AutoSubdividePolarAxis = 1
flowvtuDisplay.PolarAxes.NumberOfPolarAxis = 0
flowvtuDisplay.PolarAxes.MinimumRadius = 0.0
flowvtuDisplay.PolarAxes.MinimumAngle = 0.0
flowvtuDisplay.PolarAxes.MaximumAngle = 90.0
flowvtuDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
flowvtuDisplay.PolarAxes.Ratio = 1.0
flowvtuDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
flowvtuDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
flowvtuDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
flowvtuDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
flowvtuDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
flowvtuDisplay.PolarAxes.PolarAxisTitleVisibility = 1
flowvtuDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
flowvtuDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
flowvtuDisplay.PolarAxes.PolarLabelVisibility = 1
flowvtuDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
flowvtuDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
flowvtuDisplay.PolarAxes.RadialLabelVisibility = 1
flowvtuDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
flowvtuDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
flowvtuDisplay.PolarAxes.RadialUnitsVisibility = 1
flowvtuDisplay.PolarAxes.ScreenSize = 10.0
flowvtuDisplay.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
flowvtuDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
flowvtuDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
flowvtuDisplay.PolarAxes.PolarAxisTitleFontFile = ''
flowvtuDisplay.PolarAxes.PolarAxisTitleBold = 0
flowvtuDisplay.PolarAxes.PolarAxisTitleItalic = 0
flowvtuDisplay.PolarAxes.PolarAxisTitleShadow = 0
flowvtuDisplay.PolarAxes.PolarAxisTitleFontSize = 12
flowvtuDisplay.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
flowvtuDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
flowvtuDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
flowvtuDisplay.PolarAxes.PolarAxisLabelFontFile = ''
flowvtuDisplay.PolarAxes.PolarAxisLabelBold = 0
flowvtuDisplay.PolarAxes.PolarAxisLabelItalic = 0
flowvtuDisplay.PolarAxes.PolarAxisLabelShadow = 0
flowvtuDisplay.PolarAxes.PolarAxisLabelFontSize = 12
flowvtuDisplay.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
flowvtuDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
flowvtuDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
flowvtuDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
flowvtuDisplay.PolarAxes.LastRadialAxisTextBold = 0
flowvtuDisplay.PolarAxes.LastRadialAxisTextItalic = 0
flowvtuDisplay.PolarAxes.LastRadialAxisTextShadow = 0
flowvtuDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
flowvtuDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
flowvtuDisplay.PolarAxes.EnableDistanceLOD = 1
flowvtuDisplay.PolarAxes.DistanceLODThreshold = 0.7
flowvtuDisplay.PolarAxes.EnableViewAngleLOD = 1
flowvtuDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
flowvtuDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
flowvtuDisplay.PolarAxes.PolarTicksVisibility = 1
flowvtuDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
flowvtuDisplay.PolarAxes.TickLocation = 'Both'
flowvtuDisplay.PolarAxes.AxisTickVisibility = 1
flowvtuDisplay.PolarAxes.AxisMinorTickVisibility = 0
flowvtuDisplay.PolarAxes.ArcTickVisibility = 1
flowvtuDisplay.PolarAxes.ArcMinorTickVisibility = 0
flowvtuDisplay.PolarAxes.DeltaAngleMajor = 10.0
flowvtuDisplay.PolarAxes.DeltaAngleMinor = 5.0
flowvtuDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
flowvtuDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
flowvtuDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
flowvtuDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
flowvtuDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
flowvtuDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
flowvtuDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
flowvtuDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
flowvtuDisplay.PolarAxes.ArcMajorTickSize = 0.0
flowvtuDisplay.PolarAxes.ArcTickRatioSize = 0.3
flowvtuDisplay.PolarAxes.ArcMajorTickThickness = 1.0
flowvtuDisplay.PolarAxes.ArcTickRatioThickness = 0.5
flowvtuDisplay.PolarAxes.Use2DMode = 0
flowvtuDisplay.PolarAxes.UseLogAxis = 0

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
renderView1.CameraParallelScale = 116.8771539151318

# save screenshot
SaveScreenshot('/home/edo20/CFD2020_Guardone/Homework/DIAMOND_AIRFOIL/CASE0/POST-PROCESSING/Mesh_far.png', renderView1, ImageResolution=[2960, 1590],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='WhiteBackground',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

# reset view to fit data
renderView1.ResetCamera()

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.7836030255510886, 0.03130244750040027, 546.4101615137755]
renderView1.CameraFocalPoint = [0.7836030255510886, 0.03130244750040027, -1e-20]
renderView1.CameraParallelScale = 1.2047050751240445

# save screenshot
SaveScreenshot('/home/edo20/CFD2020_Guardone/Homework/DIAMOND_AIRFOIL/CASE0/POST-PROCESSING/Mesh_near.png', renderView1, ImageResolution=[2960, 1590],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='WhiteBackground',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

# create a new 'Calculator'
calculator1 = Calculator(Input=flowvtu)
calculator1.AttributeType = 'Point Data'
calculator1.CoordinateResults = 0
calculator1.ResultNormals = 0
calculator1.ResultTCoords = 0
calculator1.ResultArrayName = 'Result'
calculator1.Function = ''
calculator1.ReplaceInvalidResults = 1
calculator1.ReplacementValue = 0.0
calculator1.ResultArrayType = 'Double'

# Properties modified on calculator1
calculator1.ResultArrayName = 'Velocity'
calculator1.Function = 'Momentum/Density'

# show data in view
calculator1Display = Show(calculator1, renderView1)

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.AmbientColor = [1.0, 1.0, 1.0]
calculator1Display.ColorArrayName = [None, '']
calculator1Display.DiffuseColor = [1.0, 1.0, 1.0]
calculator1Display.LookupTable = None
calculator1Display.MapScalars = 1
calculator1Display.MultiComponentsMapping = 0
calculator1Display.InterpolateScalarsBeforeMapping = 1
calculator1Display.Opacity = 1.0
calculator1Display.PointSize = 2.0
calculator1Display.LineWidth = 1.0
calculator1Display.RenderLinesAsTubes = 0
calculator1Display.RenderPointsAsSpheres = 0
calculator1Display.Interpolation = 'Gouraud'
calculator1Display.Specular = 0.0
calculator1Display.SpecularColor = [1.0, 1.0, 1.0]
calculator1Display.SpecularPower = 100.0
calculator1Display.Luminosity = 0.0
calculator1Display.Ambient = 0.0
calculator1Display.Diffuse = 1.0
calculator1Display.EdgeColor = [0.0, 0.0, 0.5]
calculator1Display.BackfaceRepresentation = 'Follow Frontface'
calculator1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
calculator1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
calculator1Display.BackfaceOpacity = 1.0
calculator1Display.Position = [0.0, 0.0, 0.0]
calculator1Display.Scale = [1.0, 1.0, 1.0]
calculator1Display.Orientation = [0.0, 0.0, 0.0]
calculator1Display.Origin = [0.0, 0.0, 0.0]
calculator1Display.Pickable = 1
calculator1Display.Texture = None
calculator1Display.Triangulate = 0
calculator1Display.UseShaderReplacements = 0
calculator1Display.ShaderReplacements = ''
calculator1Display.NonlinearSubdivisionLevel = 1
calculator1Display.UseDataPartitions = 0
calculator1Display.OSPRayUseScaleArray = 0
calculator1Display.OSPRayScaleArray = 'Density'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.OSPRayMaterial = 'None'
calculator1Display.Orient = 0
calculator1Display.OrientationMode = 'Direction'
calculator1Display.SelectOrientationVectors = 'Velocity'
calculator1Display.Scaling = 0
calculator1Display.ScaleMode = 'No Data Scaling Off'
calculator1Display.ScaleFactor = 20.0
calculator1Display.SelectScaleArray = 'Density'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.UseGlyphTable = 0
calculator1Display.GlyphTableIndexArray = 'Density'
calculator1Display.UseCompositeGlyphTable = 0
calculator1Display.UseGlyphCullingAndLOD = 0
calculator1Display.LODValues = []
calculator1Display.ColorByLODIndex = 0
calculator1Display.GaussianRadius = 1.0
calculator1Display.ShaderPreset = 'Sphere'
calculator1Display.CustomTriangleScale = 3
calculator1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
calculator1Display.Emissive = 0
calculator1Display.ScaleByArray = 0
calculator1Display.SetScaleArray = ['POINTS', 'Density']
calculator1Display.ScaleArrayComponent = ''
calculator1Display.UseScaleFunction = 1
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityByArray = 0
calculator1Display.OpacityArray = ['POINTS', 'Density']
calculator1Display.OpacityArrayComponent = ''
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.SelectionCellLabelBold = 0
calculator1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
calculator1Display.SelectionCellLabelFontFamily = 'Arial'
calculator1Display.SelectionCellLabelFontFile = ''
calculator1Display.SelectionCellLabelFontSize = 18
calculator1Display.SelectionCellLabelItalic = 0
calculator1Display.SelectionCellLabelJustification = 'Left'
calculator1Display.SelectionCellLabelOpacity = 1.0
calculator1Display.SelectionCellLabelShadow = 0
calculator1Display.SelectionPointLabelBold = 0
calculator1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
calculator1Display.SelectionPointLabelFontFamily = 'Arial'
calculator1Display.SelectionPointLabelFontFile = ''
calculator1Display.SelectionPointLabelFontSize = 18
calculator1Display.SelectionPointLabelItalic = 0
calculator1Display.SelectionPointLabelJustification = 'Left'
calculator1Display.SelectionPointLabelOpacity = 1.0
calculator1Display.SelectionPointLabelShadow = 0
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = None
calculator1Display.ScalarOpacityUnitDistance = 10.67438550346949
calculator1Display.ExtractedBlockIndex = 0
calculator1Display.SelectMapper = 'Projected tetra'
calculator1Display.SamplingDimensions = [128, 128, 128]
calculator1Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator1Display.OSPRayScaleFunction.Points = [270962.9375, 0.0, 0.5, 0.0, 809535.8125, 1.0, 0.5, 0.0]
calculator1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
calculator1Display.GlyphType.TipResolution = 6
calculator1Display.GlyphType.TipRadius = 0.1
calculator1Display.GlyphType.TipLength = 0.35
calculator1Display.GlyphType.ShaftResolution = 6
calculator1Display.GlyphType.ShaftRadius = 0.03
calculator1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [0.5517352223396301, 0.0, 0.5, 0.0, 1.9102725982666016, 1.0, 0.5, 0.0]
calculator1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [0.5517352223396301, 0.0, 0.5, 0.0, 1.9102725982666016, 1.0, 0.5, 0.0]
calculator1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator1Display.DataAxesGrid.XTitle = 'X Axis'
calculator1Display.DataAxesGrid.YTitle = 'Y Axis'
calculator1Display.DataAxesGrid.ZTitle = 'Z Axis'
calculator1Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
calculator1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
calculator1Display.DataAxesGrid.XTitleFontFile = ''
calculator1Display.DataAxesGrid.XTitleBold = 0
calculator1Display.DataAxesGrid.XTitleItalic = 0
calculator1Display.DataAxesGrid.XTitleFontSize = 12
calculator1Display.DataAxesGrid.XTitleShadow = 0
calculator1Display.DataAxesGrid.XTitleOpacity = 1.0
calculator1Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
calculator1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
calculator1Display.DataAxesGrid.YTitleFontFile = ''
calculator1Display.DataAxesGrid.YTitleBold = 0
calculator1Display.DataAxesGrid.YTitleItalic = 0
calculator1Display.DataAxesGrid.YTitleFontSize = 12
calculator1Display.DataAxesGrid.YTitleShadow = 0
calculator1Display.DataAxesGrid.YTitleOpacity = 1.0
calculator1Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
calculator1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
calculator1Display.DataAxesGrid.ZTitleFontFile = ''
calculator1Display.DataAxesGrid.ZTitleBold = 0
calculator1Display.DataAxesGrid.ZTitleItalic = 0
calculator1Display.DataAxesGrid.ZTitleFontSize = 12
calculator1Display.DataAxesGrid.ZTitleShadow = 0
calculator1Display.DataAxesGrid.ZTitleOpacity = 1.0
calculator1Display.DataAxesGrid.FacesToRender = 63
calculator1Display.DataAxesGrid.CullBackface = 0
calculator1Display.DataAxesGrid.CullFrontface = 1
calculator1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
calculator1Display.DataAxesGrid.ShowGrid = 0
calculator1Display.DataAxesGrid.ShowEdges = 1
calculator1Display.DataAxesGrid.ShowTicks = 1
calculator1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
calculator1Display.DataAxesGrid.AxesToLabel = 63
calculator1Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
calculator1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
calculator1Display.DataAxesGrid.XLabelFontFile = ''
calculator1Display.DataAxesGrid.XLabelBold = 0
calculator1Display.DataAxesGrid.XLabelItalic = 0
calculator1Display.DataAxesGrid.XLabelFontSize = 12
calculator1Display.DataAxesGrid.XLabelShadow = 0
calculator1Display.DataAxesGrid.XLabelOpacity = 1.0
calculator1Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
calculator1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
calculator1Display.DataAxesGrid.YLabelFontFile = ''
calculator1Display.DataAxesGrid.YLabelBold = 0
calculator1Display.DataAxesGrid.YLabelItalic = 0
calculator1Display.DataAxesGrid.YLabelFontSize = 12
calculator1Display.DataAxesGrid.YLabelShadow = 0
calculator1Display.DataAxesGrid.YLabelOpacity = 1.0
calculator1Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
calculator1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
calculator1Display.DataAxesGrid.ZLabelFontFile = ''
calculator1Display.DataAxesGrid.ZLabelBold = 0
calculator1Display.DataAxesGrid.ZLabelItalic = 0
calculator1Display.DataAxesGrid.ZLabelFontSize = 12
calculator1Display.DataAxesGrid.ZLabelShadow = 0
calculator1Display.DataAxesGrid.ZLabelOpacity = 1.0
calculator1Display.DataAxesGrid.XAxisNotation = 'Mixed'
calculator1Display.DataAxesGrid.XAxisPrecision = 2
calculator1Display.DataAxesGrid.XAxisUseCustomLabels = 0
calculator1Display.DataAxesGrid.XAxisLabels = []
calculator1Display.DataAxesGrid.YAxisNotation = 'Mixed'
calculator1Display.DataAxesGrid.YAxisPrecision = 2
calculator1Display.DataAxesGrid.YAxisUseCustomLabels = 0
calculator1Display.DataAxesGrid.YAxisLabels = []
calculator1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
calculator1Display.DataAxesGrid.ZAxisPrecision = 2
calculator1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
calculator1Display.DataAxesGrid.ZAxisLabels = []
calculator1Display.DataAxesGrid.UseCustomBounds = 0
calculator1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator1Display.PolarAxes.Visibility = 0
calculator1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
calculator1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
calculator1Display.PolarAxes.EnableCustomRange = 0
calculator1Display.PolarAxes.CustomRange = [0.0, 1.0]
calculator1Display.PolarAxes.PolarAxisVisibility = 1
calculator1Display.PolarAxes.RadialAxesVisibility = 1
calculator1Display.PolarAxes.DrawRadialGridlines = 1
calculator1Display.PolarAxes.PolarArcsVisibility = 1
calculator1Display.PolarAxes.DrawPolarArcsGridlines = 1
calculator1Display.PolarAxes.NumberOfRadialAxes = 0
calculator1Display.PolarAxes.AutoSubdividePolarAxis = 1
calculator1Display.PolarAxes.NumberOfPolarAxis = 0
calculator1Display.PolarAxes.MinimumRadius = 0.0
calculator1Display.PolarAxes.MinimumAngle = 0.0
calculator1Display.PolarAxes.MaximumAngle = 90.0
calculator1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
calculator1Display.PolarAxes.Ratio = 1.0
calculator1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.PolarAxisTitleVisibility = 1
calculator1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
calculator1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
calculator1Display.PolarAxes.PolarLabelVisibility = 1
calculator1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
calculator1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
calculator1Display.PolarAxes.RadialLabelVisibility = 1
calculator1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
calculator1Display.PolarAxes.RadialLabelLocation = 'Bottom'
calculator1Display.PolarAxes.RadialUnitsVisibility = 1
calculator1Display.PolarAxes.ScreenSize = 10.0
calculator1Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
calculator1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
calculator1Display.PolarAxes.PolarAxisTitleFontFile = ''
calculator1Display.PolarAxes.PolarAxisTitleBold = 0
calculator1Display.PolarAxes.PolarAxisTitleItalic = 0
calculator1Display.PolarAxes.PolarAxisTitleShadow = 0
calculator1Display.PolarAxes.PolarAxisTitleFontSize = 12
calculator1Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
calculator1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
calculator1Display.PolarAxes.PolarAxisLabelFontFile = ''
calculator1Display.PolarAxes.PolarAxisLabelBold = 0
calculator1Display.PolarAxes.PolarAxisLabelItalic = 0
calculator1Display.PolarAxes.PolarAxisLabelShadow = 0
calculator1Display.PolarAxes.PolarAxisLabelFontSize = 12
calculator1Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
calculator1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
calculator1Display.PolarAxes.LastRadialAxisTextFontFile = ''
calculator1Display.PolarAxes.LastRadialAxisTextBold = 0
calculator1Display.PolarAxes.LastRadialAxisTextItalic = 0
calculator1Display.PolarAxes.LastRadialAxisTextShadow = 0
calculator1Display.PolarAxes.LastRadialAxisTextFontSize = 12
calculator1Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
calculator1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
calculator1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
calculator1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
calculator1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
calculator1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
calculator1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
calculator1Display.PolarAxes.EnableDistanceLOD = 1
calculator1Display.PolarAxes.DistanceLODThreshold = 0.7
calculator1Display.PolarAxes.EnableViewAngleLOD = 1
calculator1Display.PolarAxes.ViewAngleLODThreshold = 0.7
calculator1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
calculator1Display.PolarAxes.PolarTicksVisibility = 1
calculator1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
calculator1Display.PolarAxes.TickLocation = 'Both'
calculator1Display.PolarAxes.AxisTickVisibility = 1
calculator1Display.PolarAxes.AxisMinorTickVisibility = 0
calculator1Display.PolarAxes.ArcTickVisibility = 1
calculator1Display.PolarAxes.ArcMinorTickVisibility = 0
calculator1Display.PolarAxes.DeltaAngleMajor = 10.0
calculator1Display.PolarAxes.DeltaAngleMinor = 5.0
calculator1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
calculator1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
calculator1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
calculator1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
calculator1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
calculator1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
calculator1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
calculator1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
calculator1Display.PolarAxes.ArcMajorTickSize = 0.0
calculator1Display.PolarAxes.ArcTickRatioSize = 0.3
calculator1Display.PolarAxes.ArcMajorTickThickness = 1.0
calculator1Display.PolarAxes.ArcTickRatioThickness = 0.5
calculator1Display.PolarAxes.Use2DMode = 0
calculator1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(flowvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=calculator1,
    SeedType='High Resolution Line Source')
streamTracer1.Vectors = ['POINTS', 'Velocity']
streamTracer1.InterpolatorType = 'Interpolator with Point Locator'
streamTracer1.SurfaceStreamlines = 0
streamTracer1.IntegrationDirection = 'BOTH'
streamTracer1.IntegratorType = 'Runge-Kutta 4-5'
streamTracer1.IntegrationStepUnit = 'Cell Length'
streamTracer1.InitialStepLength = 0.2
streamTracer1.MinimumStepLength = 0.01
streamTracer1.MaximumStepLength = 0.5
streamTracer1.MaximumSteps = 2000
streamTracer1.MaximumStreamlineLength = 200.0
streamTracer1.TerminalSpeed = 1e-12
streamTracer1.MaximumError = 1e-06
streamTracer1.ComputeVorticity = 1

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-100.0, -100.0, 0.0]
streamTracer1.SeedType.Point2 = [100.0, 100.0, 0.0]
streamTracer1.SeedType.Resolution = 1000

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1)

# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.AmbientColor = [1.0, 1.0, 1.0]
streamTracer1Display.ColorArrayName = [None, '']
streamTracer1Display.DiffuseColor = [1.0, 1.0, 1.0]
streamTracer1Display.LookupTable = None
streamTracer1Display.MapScalars = 1
streamTracer1Display.MultiComponentsMapping = 0
streamTracer1Display.InterpolateScalarsBeforeMapping = 1
streamTracer1Display.Opacity = 1.0
streamTracer1Display.PointSize = 2.0
streamTracer1Display.LineWidth = 1.0
streamTracer1Display.RenderLinesAsTubes = 0
streamTracer1Display.RenderPointsAsSpheres = 0
streamTracer1Display.Interpolation = 'Gouraud'
streamTracer1Display.Specular = 0.0
streamTracer1Display.SpecularColor = [1.0, 1.0, 1.0]
streamTracer1Display.SpecularPower = 100.0
streamTracer1Display.Luminosity = 0.0
streamTracer1Display.Ambient = 0.0
streamTracer1Display.Diffuse = 1.0
streamTracer1Display.EdgeColor = [0.0, 0.0, 0.5]
streamTracer1Display.BackfaceRepresentation = 'Follow Frontface'
streamTracer1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
streamTracer1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
streamTracer1Display.BackfaceOpacity = 1.0
streamTracer1Display.Position = [0.0, 0.0, 0.0]
streamTracer1Display.Scale = [1.0, 1.0, 1.0]
streamTracer1Display.Orientation = [0.0, 0.0, 0.0]
streamTracer1Display.Origin = [0.0, 0.0, 0.0]
streamTracer1Display.Pickable = 1
streamTracer1Display.Texture = None
streamTracer1Display.Triangulate = 0
streamTracer1Display.UseShaderReplacements = 0
streamTracer1Display.ShaderReplacements = ''
streamTracer1Display.NonlinearSubdivisionLevel = 1
streamTracer1Display.UseDataPartitions = 0
streamTracer1Display.OSPRayUseScaleArray = 0
streamTracer1Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer1Display.OSPRayMaterial = 'None'
streamTracer1Display.Orient = 0
streamTracer1Display.OrientationMode = 'Direction'
streamTracer1Display.SelectOrientationVectors = 'Normals'
streamTracer1Display.Scaling = 0
streamTracer1Display.ScaleMode = 'No Data Scaling Off'
streamTracer1Display.ScaleFactor = 19.993501281738283
streamTracer1Display.SelectScaleArray = 'AngularVelocity'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.UseGlyphTable = 0
streamTracer1Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer1Display.UseCompositeGlyphTable = 0
streamTracer1Display.UseGlyphCullingAndLOD = 0
streamTracer1Display.LODValues = []
streamTracer1Display.ColorByLODIndex = 0
streamTracer1Display.GaussianRadius = 0.9996750640869141
streamTracer1Display.ShaderPreset = 'Sphere'
streamTracer1Display.CustomTriangleScale = 3
streamTracer1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
streamTracer1Display.Emissive = 0
streamTracer1Display.ScaleByArray = 0
streamTracer1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.ScaleArrayComponent = ''
streamTracer1Display.UseScaleFunction = 1
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityByArray = 0
streamTracer1Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.OpacityArrayComponent = ''
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.SelectionCellLabelBold = 0
streamTracer1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
streamTracer1Display.SelectionCellLabelFontFamily = 'Arial'
streamTracer1Display.SelectionCellLabelFontFile = ''
streamTracer1Display.SelectionCellLabelFontSize = 18
streamTracer1Display.SelectionCellLabelItalic = 0
streamTracer1Display.SelectionCellLabelJustification = 'Left'
streamTracer1Display.SelectionCellLabelOpacity = 1.0
streamTracer1Display.SelectionCellLabelShadow = 0
streamTracer1Display.SelectionPointLabelBold = 0
streamTracer1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
streamTracer1Display.SelectionPointLabelFontFamily = 'Arial'
streamTracer1Display.SelectionPointLabelFontFile = ''
streamTracer1Display.SelectionPointLabelFontSize = 18
streamTracer1Display.SelectionPointLabelItalic = 0
streamTracer1Display.SelectionPointLabelJustification = 'Left'
streamTracer1Display.SelectionPointLabelOpacity = 1.0
streamTracer1Display.SelectionPointLabelShadow = 0
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
streamTracer1Display.OSPRayScaleFunction.Points = [270962.9375, 0.0, 0.5, 0.0, 809535.8125, 1.0, 0.5, 0.0]
streamTracer1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
streamTracer1Display.GlyphType.TipResolution = 6
streamTracer1Display.GlyphType.TipRadius = 0.1
streamTracer1Display.GlyphType.TipLength = 0.35
streamTracer1Display.GlyphType.ShaftResolution = 6
streamTracer1Display.GlyphType.ShaftRadius = 0.03
streamTracer1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
streamTracer1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
streamTracer1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
streamTracer1Display.DataAxesGrid.XTitle = 'X Axis'
streamTracer1Display.DataAxesGrid.YTitle = 'Y Axis'
streamTracer1Display.DataAxesGrid.ZTitle = 'Z Axis'
streamTracer1Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
streamTracer1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
streamTracer1Display.DataAxesGrid.XTitleFontFile = ''
streamTracer1Display.DataAxesGrid.XTitleBold = 0
streamTracer1Display.DataAxesGrid.XTitleItalic = 0
streamTracer1Display.DataAxesGrid.XTitleFontSize = 12
streamTracer1Display.DataAxesGrid.XTitleShadow = 0
streamTracer1Display.DataAxesGrid.XTitleOpacity = 1.0
streamTracer1Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
streamTracer1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
streamTracer1Display.DataAxesGrid.YTitleFontFile = ''
streamTracer1Display.DataAxesGrid.YTitleBold = 0
streamTracer1Display.DataAxesGrid.YTitleItalic = 0
streamTracer1Display.DataAxesGrid.YTitleFontSize = 12
streamTracer1Display.DataAxesGrid.YTitleShadow = 0
streamTracer1Display.DataAxesGrid.YTitleOpacity = 1.0
streamTracer1Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
streamTracer1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
streamTracer1Display.DataAxesGrid.ZTitleFontFile = ''
streamTracer1Display.DataAxesGrid.ZTitleBold = 0
streamTracer1Display.DataAxesGrid.ZTitleItalic = 0
streamTracer1Display.DataAxesGrid.ZTitleFontSize = 12
streamTracer1Display.DataAxesGrid.ZTitleShadow = 0
streamTracer1Display.DataAxesGrid.ZTitleOpacity = 1.0
streamTracer1Display.DataAxesGrid.FacesToRender = 63
streamTracer1Display.DataAxesGrid.CullBackface = 0
streamTracer1Display.DataAxesGrid.CullFrontface = 1
streamTracer1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
streamTracer1Display.DataAxesGrid.ShowGrid = 0
streamTracer1Display.DataAxesGrid.ShowEdges = 1
streamTracer1Display.DataAxesGrid.ShowTicks = 1
streamTracer1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
streamTracer1Display.DataAxesGrid.AxesToLabel = 63
streamTracer1Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
streamTracer1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
streamTracer1Display.DataAxesGrid.XLabelFontFile = ''
streamTracer1Display.DataAxesGrid.XLabelBold = 0
streamTracer1Display.DataAxesGrid.XLabelItalic = 0
streamTracer1Display.DataAxesGrid.XLabelFontSize = 12
streamTracer1Display.DataAxesGrid.XLabelShadow = 0
streamTracer1Display.DataAxesGrid.XLabelOpacity = 1.0
streamTracer1Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
streamTracer1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
streamTracer1Display.DataAxesGrid.YLabelFontFile = ''
streamTracer1Display.DataAxesGrid.YLabelBold = 0
streamTracer1Display.DataAxesGrid.YLabelItalic = 0
streamTracer1Display.DataAxesGrid.YLabelFontSize = 12
streamTracer1Display.DataAxesGrid.YLabelShadow = 0
streamTracer1Display.DataAxesGrid.YLabelOpacity = 1.0
streamTracer1Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
streamTracer1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
streamTracer1Display.DataAxesGrid.ZLabelFontFile = ''
streamTracer1Display.DataAxesGrid.ZLabelBold = 0
streamTracer1Display.DataAxesGrid.ZLabelItalic = 0
streamTracer1Display.DataAxesGrid.ZLabelFontSize = 12
streamTracer1Display.DataAxesGrid.ZLabelShadow = 0
streamTracer1Display.DataAxesGrid.ZLabelOpacity = 1.0
streamTracer1Display.DataAxesGrid.XAxisNotation = 'Mixed'
streamTracer1Display.DataAxesGrid.XAxisPrecision = 2
streamTracer1Display.DataAxesGrid.XAxisUseCustomLabels = 0
streamTracer1Display.DataAxesGrid.XAxisLabels = []
streamTracer1Display.DataAxesGrid.YAxisNotation = 'Mixed'
streamTracer1Display.DataAxesGrid.YAxisPrecision = 2
streamTracer1Display.DataAxesGrid.YAxisUseCustomLabels = 0
streamTracer1Display.DataAxesGrid.YAxisLabels = []
streamTracer1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
streamTracer1Display.DataAxesGrid.ZAxisPrecision = 2
streamTracer1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
streamTracer1Display.DataAxesGrid.ZAxisLabels = []
streamTracer1Display.DataAxesGrid.UseCustomBounds = 0
streamTracer1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
streamTracer1Display.PolarAxes.Visibility = 0
streamTracer1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
streamTracer1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
streamTracer1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
streamTracer1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
streamTracer1Display.PolarAxes.EnableCustomRange = 0
streamTracer1Display.PolarAxes.CustomRange = [0.0, 1.0]
streamTracer1Display.PolarAxes.PolarAxisVisibility = 1
streamTracer1Display.PolarAxes.RadialAxesVisibility = 1
streamTracer1Display.PolarAxes.DrawRadialGridlines = 1
streamTracer1Display.PolarAxes.PolarArcsVisibility = 1
streamTracer1Display.PolarAxes.DrawPolarArcsGridlines = 1
streamTracer1Display.PolarAxes.NumberOfRadialAxes = 0
streamTracer1Display.PolarAxes.AutoSubdividePolarAxis = 1
streamTracer1Display.PolarAxes.NumberOfPolarAxis = 0
streamTracer1Display.PolarAxes.MinimumRadius = 0.0
streamTracer1Display.PolarAxes.MinimumAngle = 0.0
streamTracer1Display.PolarAxes.MaximumAngle = 90.0
streamTracer1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
streamTracer1Display.PolarAxes.Ratio = 1.0
streamTracer1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.PolarAxisTitleVisibility = 1
streamTracer1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
streamTracer1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
streamTracer1Display.PolarAxes.PolarLabelVisibility = 1
streamTracer1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
streamTracer1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
streamTracer1Display.PolarAxes.RadialLabelVisibility = 1
streamTracer1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
streamTracer1Display.PolarAxes.RadialLabelLocation = 'Bottom'
streamTracer1Display.PolarAxes.RadialUnitsVisibility = 1
streamTracer1Display.PolarAxes.ScreenSize = 10.0
streamTracer1Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
streamTracer1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
streamTracer1Display.PolarAxes.PolarAxisTitleFontFile = ''
streamTracer1Display.PolarAxes.PolarAxisTitleBold = 0
streamTracer1Display.PolarAxes.PolarAxisTitleItalic = 0
streamTracer1Display.PolarAxes.PolarAxisTitleShadow = 0
streamTracer1Display.PolarAxes.PolarAxisTitleFontSize = 12
streamTracer1Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
streamTracer1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
streamTracer1Display.PolarAxes.PolarAxisLabelFontFile = ''
streamTracer1Display.PolarAxes.PolarAxisLabelBold = 0
streamTracer1Display.PolarAxes.PolarAxisLabelItalic = 0
streamTracer1Display.PolarAxes.PolarAxisLabelShadow = 0
streamTracer1Display.PolarAxes.PolarAxisLabelFontSize = 12
streamTracer1Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
streamTracer1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
streamTracer1Display.PolarAxes.LastRadialAxisTextFontFile = ''
streamTracer1Display.PolarAxes.LastRadialAxisTextBold = 0
streamTracer1Display.PolarAxes.LastRadialAxisTextItalic = 0
streamTracer1Display.PolarAxes.LastRadialAxisTextShadow = 0
streamTracer1Display.PolarAxes.LastRadialAxisTextFontSize = 12
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
streamTracer1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
streamTracer1Display.PolarAxes.EnableDistanceLOD = 1
streamTracer1Display.PolarAxes.DistanceLODThreshold = 0.7
streamTracer1Display.PolarAxes.EnableViewAngleLOD = 1
streamTracer1Display.PolarAxes.ViewAngleLODThreshold = 0.7
streamTracer1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
streamTracer1Display.PolarAxes.PolarTicksVisibility = 1
streamTracer1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
streamTracer1Display.PolarAxes.TickLocation = 'Both'
streamTracer1Display.PolarAxes.AxisTickVisibility = 1
streamTracer1Display.PolarAxes.AxisMinorTickVisibility = 0
streamTracer1Display.PolarAxes.ArcTickVisibility = 1
streamTracer1Display.PolarAxes.ArcMinorTickVisibility = 0
streamTracer1Display.PolarAxes.DeltaAngleMajor = 10.0
streamTracer1Display.PolarAxes.DeltaAngleMinor = 5.0
streamTracer1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
streamTracer1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
streamTracer1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
streamTracer1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
streamTracer1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
streamTracer1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
streamTracer1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
streamTracer1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
streamTracer1Display.PolarAxes.ArcMajorTickSize = 0.0
streamTracer1Display.PolarAxes.ArcTickRatioSize = 0.3
streamTracer1Display.PolarAxes.ArcMajorTickThickness = 1.0
streamTracer1Display.PolarAxes.ArcTickRatioThickness = 0.5
streamTracer1Display.PolarAxes.Use2DMode = 0
streamTracer1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(calculator1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# change representation type
streamTracer1Display.SetRepresentationType('Wireframe')

# Properties modified on streamTracer1Display
streamTracer1Display.LineWidth = 4.0

# set scalar coloring
ColorBy(streamTracer1Display, ('POINTS', 'Velocity', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
streamTracer1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Velocity'
velocityLUT = GetColorTransferFunction('Velocity')
velocityLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
velocityLUT.InterpretValuesAsCategories = 0
velocityLUT.AnnotationsInitialized = 0
velocityLUT.ShowCategoricalColorsinDataRangeOnly = 0
velocityLUT.RescaleOnVisibilityChange = 0
velocityLUT.EnableOpacityMapping = 0
velocityLUT.RGBPoints = [392.9133964785527, 0.0, 0.0, 0.34902, 404.58566039930463, 0.039216, 0.062745, 0.380392, 416.25792432005653, 0.062745, 0.117647, 0.411765, 427.93018824080843, 0.090196, 0.184314, 0.45098, 439.60245216156034, 0.12549, 0.262745, 0.501961, 451.27471608231224, 0.160784, 0.337255, 0.541176, 462.94698000306414, 0.2, 0.396078, 0.568627, 474.61924392381604, 0.239216, 0.454902, 0.6, 486.29150784456795, 0.286275, 0.521569, 0.65098, 497.96377176531985, 0.337255, 0.592157, 0.701961, 509.63603568607175, 0.388235, 0.654902, 0.74902, 521.3082996068237, 0.466667, 0.737255, 0.819608, 532.9805635275754, 0.572549, 0.819608, 0.878431, 544.6528274483273, 0.654902, 0.866667, 0.909804, 556.3250913690792, 0.752941, 0.917647, 0.941176, 567.9973552898311, 0.823529, 0.956863, 0.968627, 579.669619210583, 0.988235, 0.960784, 0.901961, 579.669619210583, 0.941176, 0.984314, 0.988235, 587.1398681198643, 0.988235, 0.945098, 0.85098, 594.6101170291456, 0.980392, 0.898039, 0.784314, 603.0141470520869, 0.968627, 0.835294, 0.698039, 614.6864109728388, 0.94902, 0.733333, 0.588235, 626.3586748935907, 0.929412, 0.65098, 0.509804, 638.0309388143426, 0.909804, 0.564706, 0.435294, 649.7032027350945, 0.878431, 0.458824, 0.352941, 661.3754666558464, 0.839216, 0.388235, 0.286275, 673.0477305765983, 0.760784, 0.294118, 0.211765, 684.7199944973502, 0.701961, 0.211765, 0.168627, 696.3922584181021, 0.65098, 0.156863, 0.129412, 708.064522338854, 0.6, 0.094118, 0.094118, 719.7367862596059, 0.54902, 0.066667, 0.098039, 731.4090501803578, 0.501961, 0.05098, 0.12549, 743.0813141011097, 0.45098, 0.054902, 0.172549, 754.7535780218616, 0.4, 0.054902, 0.192157, 766.4258419426135, 0.34902, 0.070588, 0.211765]
velocityLUT.UseLogScale = 0
velocityLUT.ColorSpace = 'Lab'
velocityLUT.UseBelowRangeColor = 0
velocityLUT.BelowRangeColor = [0.0, 0.0, 0.0]
velocityLUT.UseAboveRangeColor = 0
velocityLUT.AboveRangeColor = [0.5, 0.5, 0.5]
velocityLUT.NanColor = [0.25, 0.0, 0.0]
velocityLUT.NanOpacity = 1.0
velocityLUT.Discretize = 0
velocityLUT.NumberOfTableValues = 256
velocityLUT.ScalarRangeInitialized = 1.0
velocityLUT.HSVWrap = 0
velocityLUT.VectorComponent = 0
velocityLUT.VectorMode = 'Magnitude'
velocityLUT.AllowDuplicateScalars = 1
velocityLUT.Annotations = []
velocityLUT.ActiveAnnotatedValues = []
velocityLUT.IndexedColors = []
velocityLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'Velocity'
velocityPWF = GetOpacityTransferFunction('Velocity')
velocityPWF.Points = [392.9133964785527, 0.0, 0.5, 0.0, 766.4258419426135, 1.0, 0.5, 0.0]
velocityPWF.AllowDuplicateScalars = 1
velocityPWF.UseLogScale = 0
velocityPWF.ScalarRangeInitialized = 1

# set active source
SetActiveSource(flowvtu)

# set active source
SetActiveSource(flowvtu)

# show data in view
flowvtuDisplay = Show(flowvtu, renderView1)

# change representation type
flowvtuDisplay.SetRepresentationType('Surface')

# set scalar coloring
ColorBy(flowvtuDisplay, ('POINTS', 'Density'))

# rescale color and/or opacity maps used to include current data range
flowvtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
flowvtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Density'
densityLUT = GetColorTransferFunction('Density')
densityLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
densityLUT.InterpretValuesAsCategories = 0
densityLUT.AnnotationsInitialized = 0
densityLUT.ShowCategoricalColorsinDataRangeOnly = 0
densityLUT.RescaleOnVisibilityChange = 0
densityLUT.EnableOpacityMapping = 0
densityLUT.RGBPoints = [0.5517352223396301, 0.0, 0.0, 0.34902, 0.594189515337348, 0.039216, 0.062745, 0.380392, 0.6366438083350658, 0.062745, 0.117647, 0.411765, 0.6790981013327837, 0.090196, 0.184314, 0.45098, 0.7215523943305016, 0.12549, 0.262745, 0.501961, 0.7640066873282194, 0.160784, 0.337255, 0.541176, 0.8064609803259373, 0.2, 0.396078, 0.568627, 0.8489152733236551, 0.239216, 0.454902, 0.6, 0.891369566321373, 0.286275, 0.521569, 0.65098, 0.9338238593190908, 0.337255, 0.592157, 0.701961, 0.9762781523168087, 0.388235, 0.654902, 0.74902, 1.0187324453145266, 0.466667, 0.737255, 0.819608, 1.0611867383122444, 0.572549, 0.819608, 0.878431, 1.1036410313099623, 0.654902, 0.866667, 0.909804, 1.1460953243076801, 0.752941, 0.917647, 0.941176, 1.188549617305398, 0.823529, 0.956863, 0.968627, 1.2310039103031158, 0.988235, 0.960784, 0.901961, 1.2310039103031158, 0.941176, 0.984314, 0.988235, 1.2581746578216553, 0.988235, 0.945098, 0.85098, 1.2853454053401947, 0.980392, 0.898039, 0.784314, 1.3159124962985516, 0.968627, 0.835294, 0.698039, 1.3583667892962694, 0.94902, 0.733333, 0.588235, 1.4008210822939873, 0.929412, 0.65098, 0.509804, 1.4432753752917051, 0.909804, 0.564706, 0.435294, 1.485729668289423, 0.878431, 0.458824, 0.352941, 1.5281839612871408, 0.839216, 0.388235, 0.286275, 1.5706382542848587, 0.760784, 0.294118, 0.211765, 1.6130925472825766, 0.701961, 0.211765, 0.168627, 1.6555468402802944, 0.65098, 0.156863, 0.129412, 1.6980011332780123, 0.6, 0.094118, 0.094118, 1.7404554262757301, 0.54902, 0.066667, 0.098039, 1.782909719273448, 0.501961, 0.05098, 0.12549, 1.8253640122711658, 0.45098, 0.054902, 0.172549, 1.8678183052688837, 0.4, 0.054902, 0.192157, 1.9102725982666016, 0.34902, 0.070588, 0.211765]
densityLUT.UseLogScale = 0
densityLUT.ColorSpace = 'Lab'
densityLUT.UseBelowRangeColor = 0
densityLUT.BelowRangeColor = [0.0, 0.0, 0.0]
densityLUT.UseAboveRangeColor = 0
densityLUT.AboveRangeColor = [0.5, 0.5, 0.5]
densityLUT.NanColor = [0.25, 0.0, 0.0]
densityLUT.NanOpacity = 1.0
densityLUT.Discretize = 0
densityLUT.NumberOfTableValues = 256
densityLUT.ScalarRangeInitialized = 1.0
densityLUT.HSVWrap = 0
densityLUT.VectorComponent = 0
densityLUT.VectorMode = 'Magnitude'
densityLUT.AllowDuplicateScalars = 1
densityLUT.Annotations = []
densityLUT.ActiveAnnotatedValues = []
densityLUT.IndexedColors = []
densityLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'Density'
densityPWF = GetOpacityTransferFunction('Density')
densityPWF.Points = [0.5517352223396301, 0.0, 0.5, 0.0, 1.9102725982666016, 1.0, 0.5, 0.0]
densityPWF.AllowDuplicateScalars = 1
densityPWF.UseLogScale = 0
densityPWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
densityLUT.ApplyPreset('X Ray', True)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.7861077400895242, 0.013769445731351335, 546.4101615137755]
renderView1.CameraFocalPoint = [0.7861077400895242, 0.013769445731351335, -1e-20]
renderView1.CameraParallelScale = 0.9956240290281357

# save screenshot
SaveScreenshot('/home/edo20/CFD2020_Guardone/Homework/DIAMOND_AIRFOIL/CASE0/POST-PROCESSING/Streamlines.png', renderView1, ImageResolution=[2960, 1590],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='WhiteBackground',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

# set active source
SetActiveSource(flowvtu)

# set active source
SetActiveSource(streamTracer1)

# Properties modified on streamTracer1Display
streamTracer1Display.LineWidth = 2.0

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.7861077400895242, 0.013769445731351335, 546.4101615137755]
renderView1.CameraFocalPoint = [0.7861077400895242, 0.013769445731351335, -1e-20]
renderView1.CameraParallelScale = 0.9956240290281357

# save screenshot
SaveScreenshot('/home/edo20/CFD2020_Guardone/Homework/DIAMOND_AIRFOIL/CASE0/POST-PROCESSING/Streamlines.png', renderView1, ImageResolution=[2960, 1590],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='WhiteBackground',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

# set active source
SetActiveSource(flowvtu)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.7861077400895242, 0.013769445731351335, 546.4101615137755]
renderView1.CameraFocalPoint = [0.7861077400895242, 0.013769445731351335, -1e-20]
renderView1.CameraParallelScale = 0.9956240290281357

# save screenshot
SaveScreenshot('/home/edo20/CFD2020_Guardone/Homework/DIAMOND_AIRFOIL/CASE0/POST-PROCESSING/Streamlines.png', renderView1, ImageResolution=[2960, 1590],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='WhiteBackground',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

# create a new 'Programmable Filter'
programmableFilter1 = ProgrammableFilter(Input=flowvtu)
programmableFilter1.OutputDataSetType = 'Same as Input'
programmableFilter1.Script = ''
programmableFilter1.RequestInformationScript = ''
programmableFilter1.RequestUpdateExtentScript = ''
programmableFilter1.CopyArrays = 0
programmableFilter1.PythonPath = ''

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
programmableFilter1Display.AmbientColor = [1.0, 1.0, 1.0]
programmableFilter1Display.ColorArrayName = [None, '']
programmableFilter1Display.DiffuseColor = [1.0, 1.0, 1.0]
programmableFilter1Display.LookupTable = None
programmableFilter1Display.MapScalars = 1
programmableFilter1Display.MultiComponentsMapping = 0
programmableFilter1Display.InterpolateScalarsBeforeMapping = 1
programmableFilter1Display.Opacity = 1.0
programmableFilter1Display.PointSize = 2.0
programmableFilter1Display.LineWidth = 1.0
programmableFilter1Display.RenderLinesAsTubes = 0
programmableFilter1Display.RenderPointsAsSpheres = 0
programmableFilter1Display.Interpolation = 'Gouraud'
programmableFilter1Display.Specular = 0.0
programmableFilter1Display.SpecularColor = [1.0, 1.0, 1.0]
programmableFilter1Display.SpecularPower = 100.0
programmableFilter1Display.Luminosity = 0.0
programmableFilter1Display.Ambient = 0.0
programmableFilter1Display.Diffuse = 1.0
programmableFilter1Display.EdgeColor = [0.0, 0.0, 0.5]
programmableFilter1Display.BackfaceRepresentation = 'Follow Frontface'
programmableFilter1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
programmableFilter1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
programmableFilter1Display.BackfaceOpacity = 1.0
programmableFilter1Display.Position = [0.0, 0.0, 0.0]
programmableFilter1Display.Scale = [1.0, 1.0, 1.0]
programmableFilter1Display.Orientation = [0.0, 0.0, 0.0]
programmableFilter1Display.Origin = [0.0, 0.0, 0.0]
programmableFilter1Display.Pickable = 1
programmableFilter1Display.Texture = None
programmableFilter1Display.Triangulate = 0
programmableFilter1Display.UseShaderReplacements = 0
programmableFilter1Display.ShaderReplacements = ''
programmableFilter1Display.NonlinearSubdivisionLevel = 1
programmableFilter1Display.UseDataPartitions = 0
programmableFilter1Display.OSPRayUseScaleArray = 0
programmableFilter1Display.OSPRayScaleArray = 'Coordinates'
programmableFilter1Display.OSPRayScaleFunction = 'PiecewiseFunction'
programmableFilter1Display.OSPRayMaterial = 'None'
programmableFilter1Display.Orient = 0
programmableFilter1Display.OrientationMode = 'Direction'
programmableFilter1Display.SelectOrientationVectors = 'Coordinates'
programmableFilter1Display.Scaling = 0
programmableFilter1Display.ScaleMode = 'No Data Scaling Off'
programmableFilter1Display.ScaleFactor = 20.0
programmableFilter1Display.SelectScaleArray = 'Coordinates'
programmableFilter1Display.GlyphType = 'Arrow'
programmableFilter1Display.UseGlyphTable = 0
programmableFilter1Display.GlyphTableIndexArray = 'Coordinates'
programmableFilter1Display.UseCompositeGlyphTable = 0
programmableFilter1Display.UseGlyphCullingAndLOD = 0
programmableFilter1Display.LODValues = []
programmableFilter1Display.ColorByLODIndex = 0
programmableFilter1Display.GaussianRadius = 1.0
programmableFilter1Display.ShaderPreset = 'Sphere'
programmableFilter1Display.CustomTriangleScale = 3
programmableFilter1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
programmableFilter1Display.Emissive = 0
programmableFilter1Display.ScaleByArray = 0
programmableFilter1Display.SetScaleArray = ['POINTS', 'Coordinates']
programmableFilter1Display.ScaleArrayComponent = 'X'
programmableFilter1Display.UseScaleFunction = 1
programmableFilter1Display.ScaleTransferFunction = 'PiecewiseFunction'
programmableFilter1Display.OpacityByArray = 0
programmableFilter1Display.OpacityArray = ['POINTS', 'Coordinates']
programmableFilter1Display.OpacityArrayComponent = 'X'
programmableFilter1Display.OpacityTransferFunction = 'PiecewiseFunction'
programmableFilter1Display.DataAxesGrid = 'GridAxesRepresentation'
programmableFilter1Display.SelectionCellLabelBold = 0
programmableFilter1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
programmableFilter1Display.SelectionCellLabelFontFamily = 'Arial'
programmableFilter1Display.SelectionCellLabelFontFile = ''
programmableFilter1Display.SelectionCellLabelFontSize = 18
programmableFilter1Display.SelectionCellLabelItalic = 0
programmableFilter1Display.SelectionCellLabelJustification = 'Left'
programmableFilter1Display.SelectionCellLabelOpacity = 1.0
programmableFilter1Display.SelectionCellLabelShadow = 0
programmableFilter1Display.SelectionPointLabelBold = 0
programmableFilter1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
programmableFilter1Display.SelectionPointLabelFontFamily = 'Arial'
programmableFilter1Display.SelectionPointLabelFontFile = ''
programmableFilter1Display.SelectionPointLabelFontSize = 18
programmableFilter1Display.SelectionPointLabelItalic = 0
programmableFilter1Display.SelectionPointLabelJustification = 'Left'
programmableFilter1Display.SelectionPointLabelOpacity = 1.0
programmableFilter1Display.SelectionPointLabelShadow = 0
programmableFilter1Display.PolarAxes = 'PolarAxesRepresentation'
programmableFilter1Display.ScalarOpacityFunction = None
programmableFilter1Display.ScalarOpacityUnitDistance = 10.67438550346949
programmableFilter1Display.ExtractedBlockIndex = 0
programmableFilter1Display.SelectMapper = 'Projected tetra'
programmableFilter1Display.SamplingDimensions = [128, 128, 128]
programmableFilter1Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
programmableFilter1Display.OSPRayScaleFunction.Points = [270962.9375, 0.0, 0.5, 0.0, 809535.8125, 1.0, 0.5, 0.0]
programmableFilter1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
programmableFilter1Display.GlyphType.TipResolution = 6
programmableFilter1Display.GlyphType.TipRadius = 0.1
programmableFilter1Display.GlyphType.TipLength = 0.35
programmableFilter1Display.GlyphType.ShaftResolution = 6
programmableFilter1Display.GlyphType.ShaftRadius = 0.03
programmableFilter1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
programmableFilter1Display.ScaleTransferFunction.Points = [-100.0, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]
programmableFilter1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
programmableFilter1Display.OpacityTransferFunction.Points = [-100.0, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]
programmableFilter1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
programmableFilter1Display.DataAxesGrid.XTitle = 'X Axis'
programmableFilter1Display.DataAxesGrid.YTitle = 'Y Axis'
programmableFilter1Display.DataAxesGrid.ZTitle = 'Z Axis'
programmableFilter1Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
programmableFilter1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
programmableFilter1Display.DataAxesGrid.XTitleFontFile = ''
programmableFilter1Display.DataAxesGrid.XTitleBold = 0
programmableFilter1Display.DataAxesGrid.XTitleItalic = 0
programmableFilter1Display.DataAxesGrid.XTitleFontSize = 12
programmableFilter1Display.DataAxesGrid.XTitleShadow = 0
programmableFilter1Display.DataAxesGrid.XTitleOpacity = 1.0
programmableFilter1Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
programmableFilter1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
programmableFilter1Display.DataAxesGrid.YTitleFontFile = ''
programmableFilter1Display.DataAxesGrid.YTitleBold = 0
programmableFilter1Display.DataAxesGrid.YTitleItalic = 0
programmableFilter1Display.DataAxesGrid.YTitleFontSize = 12
programmableFilter1Display.DataAxesGrid.YTitleShadow = 0
programmableFilter1Display.DataAxesGrid.YTitleOpacity = 1.0
programmableFilter1Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
programmableFilter1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
programmableFilter1Display.DataAxesGrid.ZTitleFontFile = ''
programmableFilter1Display.DataAxesGrid.ZTitleBold = 0
programmableFilter1Display.DataAxesGrid.ZTitleItalic = 0
programmableFilter1Display.DataAxesGrid.ZTitleFontSize = 12
programmableFilter1Display.DataAxesGrid.ZTitleShadow = 0
programmableFilter1Display.DataAxesGrid.ZTitleOpacity = 1.0
programmableFilter1Display.DataAxesGrid.FacesToRender = 63
programmableFilter1Display.DataAxesGrid.CullBackface = 0
programmableFilter1Display.DataAxesGrid.CullFrontface = 1
programmableFilter1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
programmableFilter1Display.DataAxesGrid.ShowGrid = 0
programmableFilter1Display.DataAxesGrid.ShowEdges = 1
programmableFilter1Display.DataAxesGrid.ShowTicks = 1
programmableFilter1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
programmableFilter1Display.DataAxesGrid.AxesToLabel = 63
programmableFilter1Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
programmableFilter1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
programmableFilter1Display.DataAxesGrid.XLabelFontFile = ''
programmableFilter1Display.DataAxesGrid.XLabelBold = 0
programmableFilter1Display.DataAxesGrid.XLabelItalic = 0
programmableFilter1Display.DataAxesGrid.XLabelFontSize = 12
programmableFilter1Display.DataAxesGrid.XLabelShadow = 0
programmableFilter1Display.DataAxesGrid.XLabelOpacity = 1.0
programmableFilter1Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
programmableFilter1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
programmableFilter1Display.DataAxesGrid.YLabelFontFile = ''
programmableFilter1Display.DataAxesGrid.YLabelBold = 0
programmableFilter1Display.DataAxesGrid.YLabelItalic = 0
programmableFilter1Display.DataAxesGrid.YLabelFontSize = 12
programmableFilter1Display.DataAxesGrid.YLabelShadow = 0
programmableFilter1Display.DataAxesGrid.YLabelOpacity = 1.0
programmableFilter1Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
programmableFilter1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
programmableFilter1Display.DataAxesGrid.ZLabelFontFile = ''
programmableFilter1Display.DataAxesGrid.ZLabelBold = 0
programmableFilter1Display.DataAxesGrid.ZLabelItalic = 0
programmableFilter1Display.DataAxesGrid.ZLabelFontSize = 12
programmableFilter1Display.DataAxesGrid.ZLabelShadow = 0
programmableFilter1Display.DataAxesGrid.ZLabelOpacity = 1.0
programmableFilter1Display.DataAxesGrid.XAxisNotation = 'Mixed'
programmableFilter1Display.DataAxesGrid.XAxisPrecision = 2
programmableFilter1Display.DataAxesGrid.XAxisUseCustomLabels = 0
programmableFilter1Display.DataAxesGrid.XAxisLabels = []
programmableFilter1Display.DataAxesGrid.YAxisNotation = 'Mixed'
programmableFilter1Display.DataAxesGrid.YAxisPrecision = 2
programmableFilter1Display.DataAxesGrid.YAxisUseCustomLabels = 0
programmableFilter1Display.DataAxesGrid.YAxisLabels = []
programmableFilter1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
programmableFilter1Display.DataAxesGrid.ZAxisPrecision = 2
programmableFilter1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
programmableFilter1Display.DataAxesGrid.ZAxisLabels = []
programmableFilter1Display.DataAxesGrid.UseCustomBounds = 0
programmableFilter1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
programmableFilter1Display.PolarAxes.Visibility = 0
programmableFilter1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
programmableFilter1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
programmableFilter1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
programmableFilter1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
programmableFilter1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
programmableFilter1Display.PolarAxes.EnableCustomRange = 0
programmableFilter1Display.PolarAxes.CustomRange = [0.0, 1.0]
programmableFilter1Display.PolarAxes.PolarAxisVisibility = 1
programmableFilter1Display.PolarAxes.RadialAxesVisibility = 1
programmableFilter1Display.PolarAxes.DrawRadialGridlines = 1
programmableFilter1Display.PolarAxes.PolarArcsVisibility = 1
programmableFilter1Display.PolarAxes.DrawPolarArcsGridlines = 1
programmableFilter1Display.PolarAxes.NumberOfRadialAxes = 0
programmableFilter1Display.PolarAxes.AutoSubdividePolarAxis = 1
programmableFilter1Display.PolarAxes.NumberOfPolarAxis = 0
programmableFilter1Display.PolarAxes.MinimumRadius = 0.0
programmableFilter1Display.PolarAxes.MinimumAngle = 0.0
programmableFilter1Display.PolarAxes.MaximumAngle = 90.0
programmableFilter1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
programmableFilter1Display.PolarAxes.Ratio = 1.0
programmableFilter1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
programmableFilter1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
programmableFilter1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
programmableFilter1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
programmableFilter1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
programmableFilter1Display.PolarAxes.PolarAxisTitleVisibility = 1
programmableFilter1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
programmableFilter1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
programmableFilter1Display.PolarAxes.PolarLabelVisibility = 1
programmableFilter1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
programmableFilter1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
programmableFilter1Display.PolarAxes.RadialLabelVisibility = 1
programmableFilter1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
programmableFilter1Display.PolarAxes.RadialLabelLocation = 'Bottom'
programmableFilter1Display.PolarAxes.RadialUnitsVisibility = 1
programmableFilter1Display.PolarAxes.ScreenSize = 10.0
programmableFilter1Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
programmableFilter1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
programmableFilter1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
programmableFilter1Display.PolarAxes.PolarAxisTitleFontFile = ''
programmableFilter1Display.PolarAxes.PolarAxisTitleBold = 0
programmableFilter1Display.PolarAxes.PolarAxisTitleItalic = 0
programmableFilter1Display.PolarAxes.PolarAxisTitleShadow = 0
programmableFilter1Display.PolarAxes.PolarAxisTitleFontSize = 12
programmableFilter1Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
programmableFilter1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
programmableFilter1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
programmableFilter1Display.PolarAxes.PolarAxisLabelFontFile = ''
programmableFilter1Display.PolarAxes.PolarAxisLabelBold = 0
programmableFilter1Display.PolarAxes.PolarAxisLabelItalic = 0
programmableFilter1Display.PolarAxes.PolarAxisLabelShadow = 0
programmableFilter1Display.PolarAxes.PolarAxisLabelFontSize = 12
programmableFilter1Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
programmableFilter1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
programmableFilter1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
programmableFilter1Display.PolarAxes.LastRadialAxisTextFontFile = ''
programmableFilter1Display.PolarAxes.LastRadialAxisTextBold = 0
programmableFilter1Display.PolarAxes.LastRadialAxisTextItalic = 0
programmableFilter1Display.PolarAxes.LastRadialAxisTextShadow = 0
programmableFilter1Display.PolarAxes.LastRadialAxisTextFontSize = 12
programmableFilter1Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
programmableFilter1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
programmableFilter1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
programmableFilter1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
programmableFilter1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
programmableFilter1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
programmableFilter1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
programmableFilter1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
programmableFilter1Display.PolarAxes.EnableDistanceLOD = 1
programmableFilter1Display.PolarAxes.DistanceLODThreshold = 0.7
programmableFilter1Display.PolarAxes.EnableViewAngleLOD = 1
programmableFilter1Display.PolarAxes.ViewAngleLODThreshold = 0.7
programmableFilter1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
programmableFilter1Display.PolarAxes.PolarTicksVisibility = 1
programmableFilter1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
programmableFilter1Display.PolarAxes.TickLocation = 'Both'
programmableFilter1Display.PolarAxes.AxisTickVisibility = 1
programmableFilter1Display.PolarAxes.AxisMinorTickVisibility = 0
programmableFilter1Display.PolarAxes.ArcTickVisibility = 1
programmableFilter1Display.PolarAxes.ArcMinorTickVisibility = 0
programmableFilter1Display.PolarAxes.DeltaAngleMajor = 10.0
programmableFilter1Display.PolarAxes.DeltaAngleMinor = 5.0
programmableFilter1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
programmableFilter1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
programmableFilter1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
programmableFilter1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
programmableFilter1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
programmableFilter1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
programmableFilter1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
programmableFilter1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
programmableFilter1Display.PolarAxes.ArcMajorTickSize = 0.0
programmableFilter1Display.PolarAxes.ArcTickRatioSize = 0.3
programmableFilter1Display.PolarAxes.ArcMajorTickThickness = 1.0
programmableFilter1Display.PolarAxes.ArcTickRatioThickness = 0.5
programmableFilter1Display.PolarAxes.Use2DMode = 0
programmableFilter1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(flowvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(calculator1)

# set active source
SetActiveSource(flowvtu)

# set active source
SetActiveSource(calculator1)

# set active source
SetActiveSource(programmableFilter1)

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(Input=[calculator1, programmableFilter1])

# show data in view
appendAttributes1Display = Show(appendAttributes1, renderView1)

# trace defaults for the display properties.
appendAttributes1Display.Representation = 'Surface'
appendAttributes1Display.AmbientColor = [1.0, 1.0, 1.0]
appendAttributes1Display.ColorArrayName = [None, '']
appendAttributes1Display.DiffuseColor = [1.0, 1.0, 1.0]
appendAttributes1Display.LookupTable = None
appendAttributes1Display.MapScalars = 1
appendAttributes1Display.MultiComponentsMapping = 0
appendAttributes1Display.InterpolateScalarsBeforeMapping = 1
appendAttributes1Display.Opacity = 1.0
appendAttributes1Display.PointSize = 2.0
appendAttributes1Display.LineWidth = 1.0
appendAttributes1Display.RenderLinesAsTubes = 0
appendAttributes1Display.RenderPointsAsSpheres = 0
appendAttributes1Display.Interpolation = 'Gouraud'
appendAttributes1Display.Specular = 0.0
appendAttributes1Display.SpecularColor = [1.0, 1.0, 1.0]
appendAttributes1Display.SpecularPower = 100.0
appendAttributes1Display.Luminosity = 0.0
appendAttributes1Display.Ambient = 0.0
appendAttributes1Display.Diffuse = 1.0
appendAttributes1Display.EdgeColor = [0.0, 0.0, 0.5]
appendAttributes1Display.BackfaceRepresentation = 'Follow Frontface'
appendAttributes1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
appendAttributes1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
appendAttributes1Display.BackfaceOpacity = 1.0
appendAttributes1Display.Position = [0.0, 0.0, 0.0]
appendAttributes1Display.Scale = [1.0, 1.0, 1.0]
appendAttributes1Display.Orientation = [0.0, 0.0, 0.0]
appendAttributes1Display.Origin = [0.0, 0.0, 0.0]
appendAttributes1Display.Pickable = 1
appendAttributes1Display.Texture = None
appendAttributes1Display.Triangulate = 0
appendAttributes1Display.UseShaderReplacements = 0
appendAttributes1Display.ShaderReplacements = ''
appendAttributes1Display.NonlinearSubdivisionLevel = 1
appendAttributes1Display.UseDataPartitions = 0
appendAttributes1Display.OSPRayUseScaleArray = 0
appendAttributes1Display.OSPRayScaleArray = 'Coordinates'
appendAttributes1Display.OSPRayScaleFunction = 'PiecewiseFunction'
appendAttributes1Display.OSPRayMaterial = 'None'
appendAttributes1Display.Orient = 0
appendAttributes1Display.OrientationMode = 'Direction'
appendAttributes1Display.SelectOrientationVectors = 'Velocity'
appendAttributes1Display.Scaling = 0
appendAttributes1Display.ScaleMode = 'No Data Scaling Off'
appendAttributes1Display.ScaleFactor = 20.0
appendAttributes1Display.SelectScaleArray = 'Coordinates'
appendAttributes1Display.GlyphType = 'Arrow'
appendAttributes1Display.UseGlyphTable = 0
appendAttributes1Display.GlyphTableIndexArray = 'Coordinates'
appendAttributes1Display.UseCompositeGlyphTable = 0
appendAttributes1Display.UseGlyphCullingAndLOD = 0
appendAttributes1Display.LODValues = []
appendAttributes1Display.ColorByLODIndex = 0
appendAttributes1Display.GaussianRadius = 1.0
appendAttributes1Display.ShaderPreset = 'Sphere'
appendAttributes1Display.CustomTriangleScale = 3
appendAttributes1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
appendAttributes1Display.Emissive = 0
appendAttributes1Display.ScaleByArray = 0
appendAttributes1Display.SetScaleArray = ['POINTS', 'Coordinates']
appendAttributes1Display.ScaleArrayComponent = 'X'
appendAttributes1Display.UseScaleFunction = 1
appendAttributes1Display.ScaleTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.OpacityByArray = 0
appendAttributes1Display.OpacityArray = ['POINTS', 'Coordinates']
appendAttributes1Display.OpacityArrayComponent = 'X'
appendAttributes1Display.OpacityTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.DataAxesGrid = 'GridAxesRepresentation'
appendAttributes1Display.SelectionCellLabelBold = 0
appendAttributes1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
appendAttributes1Display.SelectionCellLabelFontFamily = 'Arial'
appendAttributes1Display.SelectionCellLabelFontFile = ''
appendAttributes1Display.SelectionCellLabelFontSize = 18
appendAttributes1Display.SelectionCellLabelItalic = 0
appendAttributes1Display.SelectionCellLabelJustification = 'Left'
appendAttributes1Display.SelectionCellLabelOpacity = 1.0
appendAttributes1Display.SelectionCellLabelShadow = 0
appendAttributes1Display.SelectionPointLabelBold = 0
appendAttributes1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
appendAttributes1Display.SelectionPointLabelFontFamily = 'Arial'
appendAttributes1Display.SelectionPointLabelFontFile = ''
appendAttributes1Display.SelectionPointLabelFontSize = 18
appendAttributes1Display.SelectionPointLabelItalic = 0
appendAttributes1Display.SelectionPointLabelJustification = 'Left'
appendAttributes1Display.SelectionPointLabelOpacity = 1.0
appendAttributes1Display.SelectionPointLabelShadow = 0
appendAttributes1Display.PolarAxes = 'PolarAxesRepresentation'
appendAttributes1Display.ScalarOpacityFunction = None
appendAttributes1Display.ScalarOpacityUnitDistance = 10.67438550346949
appendAttributes1Display.ExtractedBlockIndex = 0
appendAttributes1Display.SelectMapper = 'Projected tetra'
appendAttributes1Display.SamplingDimensions = [128, 128, 128]
appendAttributes1Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
appendAttributes1Display.OSPRayScaleFunction.Points = [270962.9375, 0.0, 0.5, 0.0, 809535.8125, 1.0, 0.5, 0.0]
appendAttributes1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
appendAttributes1Display.GlyphType.TipResolution = 6
appendAttributes1Display.GlyphType.TipRadius = 0.1
appendAttributes1Display.GlyphType.TipLength = 0.35
appendAttributes1Display.GlyphType.ShaftResolution = 6
appendAttributes1Display.GlyphType.ShaftRadius = 0.03
appendAttributes1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
appendAttributes1Display.ScaleTransferFunction.Points = [-100.0, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]
appendAttributes1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
appendAttributes1Display.OpacityTransferFunction.Points = [-100.0, 0.0, 0.5, 0.0, 100.0, 1.0, 0.5, 0.0]
appendAttributes1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
appendAttributes1Display.DataAxesGrid.XTitle = 'X Axis'
appendAttributes1Display.DataAxesGrid.YTitle = 'Y Axis'
appendAttributes1Display.DataAxesGrid.ZTitle = 'Z Axis'
appendAttributes1Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
appendAttributes1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
appendAttributes1Display.DataAxesGrid.XTitleFontFile = ''
appendAttributes1Display.DataAxesGrid.XTitleBold = 0
appendAttributes1Display.DataAxesGrid.XTitleItalic = 0
appendAttributes1Display.DataAxesGrid.XTitleFontSize = 12
appendAttributes1Display.DataAxesGrid.XTitleShadow = 0
appendAttributes1Display.DataAxesGrid.XTitleOpacity = 1.0
appendAttributes1Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
appendAttributes1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
appendAttributes1Display.DataAxesGrid.YTitleFontFile = ''
appendAttributes1Display.DataAxesGrid.YTitleBold = 0
appendAttributes1Display.DataAxesGrid.YTitleItalic = 0
appendAttributes1Display.DataAxesGrid.YTitleFontSize = 12
appendAttributes1Display.DataAxesGrid.YTitleShadow = 0
appendAttributes1Display.DataAxesGrid.YTitleOpacity = 1.0
appendAttributes1Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
appendAttributes1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
appendAttributes1Display.DataAxesGrid.ZTitleFontFile = ''
appendAttributes1Display.DataAxesGrid.ZTitleBold = 0
appendAttributes1Display.DataAxesGrid.ZTitleItalic = 0
appendAttributes1Display.DataAxesGrid.ZTitleFontSize = 12
appendAttributes1Display.DataAxesGrid.ZTitleShadow = 0
appendAttributes1Display.DataAxesGrid.ZTitleOpacity = 1.0
appendAttributes1Display.DataAxesGrid.FacesToRender = 63
appendAttributes1Display.DataAxesGrid.CullBackface = 0
appendAttributes1Display.DataAxesGrid.CullFrontface = 1
appendAttributes1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
appendAttributes1Display.DataAxesGrid.ShowGrid = 0
appendAttributes1Display.DataAxesGrid.ShowEdges = 1
appendAttributes1Display.DataAxesGrid.ShowTicks = 1
appendAttributes1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
appendAttributes1Display.DataAxesGrid.AxesToLabel = 63
appendAttributes1Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
appendAttributes1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
appendAttributes1Display.DataAxesGrid.XLabelFontFile = ''
appendAttributes1Display.DataAxesGrid.XLabelBold = 0
appendAttributes1Display.DataAxesGrid.XLabelItalic = 0
appendAttributes1Display.DataAxesGrid.XLabelFontSize = 12
appendAttributes1Display.DataAxesGrid.XLabelShadow = 0
appendAttributes1Display.DataAxesGrid.XLabelOpacity = 1.0
appendAttributes1Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
appendAttributes1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
appendAttributes1Display.DataAxesGrid.YLabelFontFile = ''
appendAttributes1Display.DataAxesGrid.YLabelBold = 0
appendAttributes1Display.DataAxesGrid.YLabelItalic = 0
appendAttributes1Display.DataAxesGrid.YLabelFontSize = 12
appendAttributes1Display.DataAxesGrid.YLabelShadow = 0
appendAttributes1Display.DataAxesGrid.YLabelOpacity = 1.0
appendAttributes1Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
appendAttributes1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
appendAttributes1Display.DataAxesGrid.ZLabelFontFile = ''
appendAttributes1Display.DataAxesGrid.ZLabelBold = 0
appendAttributes1Display.DataAxesGrid.ZLabelItalic = 0
appendAttributes1Display.DataAxesGrid.ZLabelFontSize = 12
appendAttributes1Display.DataAxesGrid.ZLabelShadow = 0
appendAttributes1Display.DataAxesGrid.ZLabelOpacity = 1.0
appendAttributes1Display.DataAxesGrid.XAxisNotation = 'Mixed'
appendAttributes1Display.DataAxesGrid.XAxisPrecision = 2
appendAttributes1Display.DataAxesGrid.XAxisUseCustomLabels = 0
appendAttributes1Display.DataAxesGrid.XAxisLabels = []
appendAttributes1Display.DataAxesGrid.YAxisNotation = 'Mixed'
appendAttributes1Display.DataAxesGrid.YAxisPrecision = 2
appendAttributes1Display.DataAxesGrid.YAxisUseCustomLabels = 0
appendAttributes1Display.DataAxesGrid.YAxisLabels = []
appendAttributes1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
appendAttributes1Display.DataAxesGrid.ZAxisPrecision = 2
appendAttributes1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
appendAttributes1Display.DataAxesGrid.ZAxisLabels = []
appendAttributes1Display.DataAxesGrid.UseCustomBounds = 0
appendAttributes1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
appendAttributes1Display.PolarAxes.Visibility = 0
appendAttributes1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
appendAttributes1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
appendAttributes1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
appendAttributes1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
appendAttributes1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
appendAttributes1Display.PolarAxes.EnableCustomRange = 0
appendAttributes1Display.PolarAxes.CustomRange = [0.0, 1.0]
appendAttributes1Display.PolarAxes.PolarAxisVisibility = 1
appendAttributes1Display.PolarAxes.RadialAxesVisibility = 1
appendAttributes1Display.PolarAxes.DrawRadialGridlines = 1
appendAttributes1Display.PolarAxes.PolarArcsVisibility = 1
appendAttributes1Display.PolarAxes.DrawPolarArcsGridlines = 1
appendAttributes1Display.PolarAxes.NumberOfRadialAxes = 0
appendAttributes1Display.PolarAxes.AutoSubdividePolarAxis = 1
appendAttributes1Display.PolarAxes.NumberOfPolarAxis = 0
appendAttributes1Display.PolarAxes.MinimumRadius = 0.0
appendAttributes1Display.PolarAxes.MinimumAngle = 0.0
appendAttributes1Display.PolarAxes.MaximumAngle = 90.0
appendAttributes1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
appendAttributes1Display.PolarAxes.Ratio = 1.0
appendAttributes1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
appendAttributes1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
appendAttributes1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
appendAttributes1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
appendAttributes1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
appendAttributes1Display.PolarAxes.PolarAxisTitleVisibility = 1
appendAttributes1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
appendAttributes1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
appendAttributes1Display.PolarAxes.PolarLabelVisibility = 1
appendAttributes1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
appendAttributes1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
appendAttributes1Display.PolarAxes.RadialLabelVisibility = 1
appendAttributes1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
appendAttributes1Display.PolarAxes.RadialLabelLocation = 'Bottom'
appendAttributes1Display.PolarAxes.RadialUnitsVisibility = 1
appendAttributes1Display.PolarAxes.ScreenSize = 10.0
appendAttributes1Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
appendAttributes1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
appendAttributes1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
appendAttributes1Display.PolarAxes.PolarAxisTitleFontFile = ''
appendAttributes1Display.PolarAxes.PolarAxisTitleBold = 0
appendAttributes1Display.PolarAxes.PolarAxisTitleItalic = 0
appendAttributes1Display.PolarAxes.PolarAxisTitleShadow = 0
appendAttributes1Display.PolarAxes.PolarAxisTitleFontSize = 12
appendAttributes1Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
appendAttributes1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
appendAttributes1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
appendAttributes1Display.PolarAxes.PolarAxisLabelFontFile = ''
appendAttributes1Display.PolarAxes.PolarAxisLabelBold = 0
appendAttributes1Display.PolarAxes.PolarAxisLabelItalic = 0
appendAttributes1Display.PolarAxes.PolarAxisLabelShadow = 0
appendAttributes1Display.PolarAxes.PolarAxisLabelFontSize = 12
appendAttributes1Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
appendAttributes1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
appendAttributes1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
appendAttributes1Display.PolarAxes.LastRadialAxisTextFontFile = ''
appendAttributes1Display.PolarAxes.LastRadialAxisTextBold = 0
appendAttributes1Display.PolarAxes.LastRadialAxisTextItalic = 0
appendAttributes1Display.PolarAxes.LastRadialAxisTextShadow = 0
appendAttributes1Display.PolarAxes.LastRadialAxisTextFontSize = 12
appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
appendAttributes1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
appendAttributes1Display.PolarAxes.EnableDistanceLOD = 1
appendAttributes1Display.PolarAxes.DistanceLODThreshold = 0.7
appendAttributes1Display.PolarAxes.EnableViewAngleLOD = 1
appendAttributes1Display.PolarAxes.ViewAngleLODThreshold = 0.7
appendAttributes1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
appendAttributes1Display.PolarAxes.PolarTicksVisibility = 1
appendAttributes1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
appendAttributes1Display.PolarAxes.TickLocation = 'Both'
appendAttributes1Display.PolarAxes.AxisTickVisibility = 1
appendAttributes1Display.PolarAxes.AxisMinorTickVisibility = 0
appendAttributes1Display.PolarAxes.ArcTickVisibility = 1
appendAttributes1Display.PolarAxes.ArcMinorTickVisibility = 0
appendAttributes1Display.PolarAxes.DeltaAngleMajor = 10.0
appendAttributes1Display.PolarAxes.DeltaAngleMinor = 5.0
appendAttributes1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
appendAttributes1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
appendAttributes1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
appendAttributes1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
appendAttributes1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
appendAttributes1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
appendAttributes1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
appendAttributes1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
appendAttributes1Display.PolarAxes.ArcMajorTickSize = 0.0
appendAttributes1Display.PolarAxes.ArcTickRatioSize = 0.3
appendAttributes1Display.PolarAxes.ArcMajorTickThickness = 1.0
appendAttributes1Display.PolarAxes.ArcTickRatioThickness = 0.5
appendAttributes1Display.PolarAxes.Use2DMode = 0
appendAttributes1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(calculator1, renderView1)

# hide data in view
Hide(programmableFilter1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(appendAttributes1, renderView1)

# hide data in view
Hide(streamTracer1, renderView1)

# set active source
SetActiveSource(appendAttributes1)

# show data in view
appendAttributes1Display = Show(appendAttributes1, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# set active source
SetActiveSource(appendAttributes1)

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
plotOverLine1.PassPartialArrays = 1
plotOverLine1.ComputeTolerance = 1
plotOverLine1.Tolerance = 2.220446049250313e-16

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine1.Source.Point1 = [-100.0, -100.0, 0.0]
plotOverLine1.Source.Point2 = [100.0, 100.0, 0.0]
plotOverLine1.Source.Resolution = 1000

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1)

# trace defaults for the display properties.
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.AmbientColor = [1.0, 1.0, 1.0]
plotOverLine1Display.ColorArrayName = [None, '']
plotOverLine1Display.DiffuseColor = [1.0, 1.0, 1.0]
plotOverLine1Display.LookupTable = None
plotOverLine1Display.MapScalars = 1
plotOverLine1Display.MultiComponentsMapping = 0
plotOverLine1Display.InterpolateScalarsBeforeMapping = 1
plotOverLine1Display.Opacity = 1.0
plotOverLine1Display.PointSize = 2.0
plotOverLine1Display.LineWidth = 1.0
plotOverLine1Display.RenderLinesAsTubes = 0
plotOverLine1Display.RenderPointsAsSpheres = 0
plotOverLine1Display.Interpolation = 'Gouraud'
plotOverLine1Display.Specular = 0.0
plotOverLine1Display.SpecularColor = [1.0, 1.0, 1.0]
plotOverLine1Display.SpecularPower = 100.0
plotOverLine1Display.Luminosity = 0.0
plotOverLine1Display.Ambient = 0.0
plotOverLine1Display.Diffuse = 1.0
plotOverLine1Display.EdgeColor = [0.0, 0.0, 0.5]
plotOverLine1Display.BackfaceRepresentation = 'Follow Frontface'
plotOverLine1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
plotOverLine1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
plotOverLine1Display.BackfaceOpacity = 1.0
plotOverLine1Display.Position = [0.0, 0.0, 0.0]
plotOverLine1Display.Scale = [1.0, 1.0, 1.0]
plotOverLine1Display.Orientation = [0.0, 0.0, 0.0]
plotOverLine1Display.Origin = [0.0, 0.0, 0.0]
plotOverLine1Display.Pickable = 1
plotOverLine1Display.Texture = None
plotOverLine1Display.Triangulate = 0
plotOverLine1Display.UseShaderReplacements = 0
plotOverLine1Display.ShaderReplacements = ''
plotOverLine1Display.NonlinearSubdivisionLevel = 1
plotOverLine1Display.UseDataPartitions = 0
plotOverLine1Display.OSPRayUseScaleArray = 0
plotOverLine1Display.OSPRayScaleArray = 'Coordinates'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.OSPRayMaterial = 'None'
plotOverLine1Display.Orient = 0
plotOverLine1Display.OrientationMode = 'Direction'
plotOverLine1Display.SelectOrientationVectors = 'Velocity'
plotOverLine1Display.Scaling = 0
plotOverLine1Display.ScaleMode = 'No Data Scaling Off'
plotOverLine1Display.ScaleFactor = 0.25
plotOverLine1Display.SelectScaleArray = 'Coordinates'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.UseGlyphTable = 0
plotOverLine1Display.GlyphTableIndexArray = 'Coordinates'
plotOverLine1Display.UseCompositeGlyphTable = 0
plotOverLine1Display.UseGlyphCullingAndLOD = 0
plotOverLine1Display.LODValues = []
plotOverLine1Display.ColorByLODIndex = 0
plotOverLine1Display.GaussianRadius = 0.0125
plotOverLine1Display.ShaderPreset = 'Sphere'
plotOverLine1Display.CustomTriangleScale = 3
plotOverLine1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
plotOverLine1Display.Emissive = 0
plotOverLine1Display.ScaleByArray = 0
plotOverLine1Display.SetScaleArray = ['POINTS', 'Coordinates']
plotOverLine1Display.ScaleArrayComponent = 'X'
plotOverLine1Display.UseScaleFunction = 1
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityByArray = 0
plotOverLine1Display.OpacityArray = ['POINTS', 'Coordinates']
plotOverLine1Display.OpacityArrayComponent = 'X'
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.SelectionCellLabelBold = 0
plotOverLine1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
plotOverLine1Display.SelectionCellLabelFontFamily = 'Arial'
plotOverLine1Display.SelectionCellLabelFontFile = ''
plotOverLine1Display.SelectionCellLabelFontSize = 18
plotOverLine1Display.SelectionCellLabelItalic = 0
plotOverLine1Display.SelectionCellLabelJustification = 'Left'
plotOverLine1Display.SelectionCellLabelOpacity = 1.0
plotOverLine1Display.SelectionCellLabelShadow = 0
plotOverLine1Display.SelectionPointLabelBold = 0
plotOverLine1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
plotOverLine1Display.SelectionPointLabelFontFamily = 'Arial'
plotOverLine1Display.SelectionPointLabelFontFile = ''
plotOverLine1Display.SelectionPointLabelFontSize = 18
plotOverLine1Display.SelectionPointLabelItalic = 0
plotOverLine1Display.SelectionPointLabelJustification = 'Left'
plotOverLine1Display.SelectionPointLabelOpacity = 1.0
plotOverLine1Display.SelectionPointLabelShadow = 0
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
plotOverLine1Display.OSPRayScaleFunction.Points = [270962.9375, 0.0, 0.5, 0.0, 809535.8125, 1.0, 0.5, 0.0]
plotOverLine1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
plotOverLine1Display.GlyphType.TipResolution = 6
plotOverLine1Display.GlyphType.TipRadius = 0.1
plotOverLine1Display.GlyphType.TipLength = 0.35
plotOverLine1Display.GlyphType.ShaftResolution = 6
plotOverLine1Display.GlyphType.ShaftRadius = 0.03
plotOverLine1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display.ScaleTransferFunction.Points = [1.734723475976807e-18, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
plotOverLine1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display.OpacityTransferFunction.Points = [1.734723475976807e-18, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
plotOverLine1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
plotOverLine1Display.DataAxesGrid.XTitle = 'X Axis'
plotOverLine1Display.DataAxesGrid.YTitle = 'Y Axis'
plotOverLine1Display.DataAxesGrid.ZTitle = 'Z Axis'
plotOverLine1Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
plotOverLine1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
plotOverLine1Display.DataAxesGrid.XTitleFontFile = ''
plotOverLine1Display.DataAxesGrid.XTitleBold = 0
plotOverLine1Display.DataAxesGrid.XTitleItalic = 0
plotOverLine1Display.DataAxesGrid.XTitleFontSize = 12
plotOverLine1Display.DataAxesGrid.XTitleShadow = 0
plotOverLine1Display.DataAxesGrid.XTitleOpacity = 1.0
plotOverLine1Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
plotOverLine1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
plotOverLine1Display.DataAxesGrid.YTitleFontFile = ''
plotOverLine1Display.DataAxesGrid.YTitleBold = 0
plotOverLine1Display.DataAxesGrid.YTitleItalic = 0
plotOverLine1Display.DataAxesGrid.YTitleFontSize = 12
plotOverLine1Display.DataAxesGrid.YTitleShadow = 0
plotOverLine1Display.DataAxesGrid.YTitleOpacity = 1.0
plotOverLine1Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
plotOverLine1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
plotOverLine1Display.DataAxesGrid.ZTitleFontFile = ''
plotOverLine1Display.DataAxesGrid.ZTitleBold = 0
plotOverLine1Display.DataAxesGrid.ZTitleItalic = 0
plotOverLine1Display.DataAxesGrid.ZTitleFontSize = 12
plotOverLine1Display.DataAxesGrid.ZTitleShadow = 0
plotOverLine1Display.DataAxesGrid.ZTitleOpacity = 1.0
plotOverLine1Display.DataAxesGrid.FacesToRender = 63
plotOverLine1Display.DataAxesGrid.CullBackface = 0
plotOverLine1Display.DataAxesGrid.CullFrontface = 1
plotOverLine1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
plotOverLine1Display.DataAxesGrid.ShowGrid = 0
plotOverLine1Display.DataAxesGrid.ShowEdges = 1
plotOverLine1Display.DataAxesGrid.ShowTicks = 1
plotOverLine1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
plotOverLine1Display.DataAxesGrid.AxesToLabel = 63
plotOverLine1Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
plotOverLine1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
plotOverLine1Display.DataAxesGrid.XLabelFontFile = ''
plotOverLine1Display.DataAxesGrid.XLabelBold = 0
plotOverLine1Display.DataAxesGrid.XLabelItalic = 0
plotOverLine1Display.DataAxesGrid.XLabelFontSize = 12
plotOverLine1Display.DataAxesGrid.XLabelShadow = 0
plotOverLine1Display.DataAxesGrid.XLabelOpacity = 1.0
plotOverLine1Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
plotOverLine1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
plotOverLine1Display.DataAxesGrid.YLabelFontFile = ''
plotOverLine1Display.DataAxesGrid.YLabelBold = 0
plotOverLine1Display.DataAxesGrid.YLabelItalic = 0
plotOverLine1Display.DataAxesGrid.YLabelFontSize = 12
plotOverLine1Display.DataAxesGrid.YLabelShadow = 0
plotOverLine1Display.DataAxesGrid.YLabelOpacity = 1.0
plotOverLine1Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
plotOverLine1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
plotOverLine1Display.DataAxesGrid.ZLabelFontFile = ''
plotOverLine1Display.DataAxesGrid.ZLabelBold = 0
plotOverLine1Display.DataAxesGrid.ZLabelItalic = 0
plotOverLine1Display.DataAxesGrid.ZLabelFontSize = 12
plotOverLine1Display.DataAxesGrid.ZLabelShadow = 0
plotOverLine1Display.DataAxesGrid.ZLabelOpacity = 1.0
plotOverLine1Display.DataAxesGrid.XAxisNotation = 'Mixed'
plotOverLine1Display.DataAxesGrid.XAxisPrecision = 2
plotOverLine1Display.DataAxesGrid.XAxisUseCustomLabels = 0
plotOverLine1Display.DataAxesGrid.XAxisLabels = []
plotOverLine1Display.DataAxesGrid.YAxisNotation = 'Mixed'
plotOverLine1Display.DataAxesGrid.YAxisPrecision = 2
plotOverLine1Display.DataAxesGrid.YAxisUseCustomLabels = 0
plotOverLine1Display.DataAxesGrid.YAxisLabels = []
plotOverLine1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
plotOverLine1Display.DataAxesGrid.ZAxisPrecision = 2
plotOverLine1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
plotOverLine1Display.DataAxesGrid.ZAxisLabels = []
plotOverLine1Display.DataAxesGrid.UseCustomBounds = 0
plotOverLine1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
plotOverLine1Display.PolarAxes.Visibility = 0
plotOverLine1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
plotOverLine1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
plotOverLine1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
plotOverLine1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
plotOverLine1Display.PolarAxes.EnableCustomRange = 0
plotOverLine1Display.PolarAxes.CustomRange = [0.0, 1.0]
plotOverLine1Display.PolarAxes.PolarAxisVisibility = 1
plotOverLine1Display.PolarAxes.RadialAxesVisibility = 1
plotOverLine1Display.PolarAxes.DrawRadialGridlines = 1
plotOverLine1Display.PolarAxes.PolarArcsVisibility = 1
plotOverLine1Display.PolarAxes.DrawPolarArcsGridlines = 1
plotOverLine1Display.PolarAxes.NumberOfRadialAxes = 0
plotOverLine1Display.PolarAxes.AutoSubdividePolarAxis = 1
plotOverLine1Display.PolarAxes.NumberOfPolarAxis = 0
plotOverLine1Display.PolarAxes.MinimumRadius = 0.0
plotOverLine1Display.PolarAxes.MinimumAngle = 0.0
plotOverLine1Display.PolarAxes.MaximumAngle = 90.0
plotOverLine1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
plotOverLine1Display.PolarAxes.Ratio = 1.0
plotOverLine1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.PolarAxisTitleVisibility = 1
plotOverLine1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
plotOverLine1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
plotOverLine1Display.PolarAxes.PolarLabelVisibility = 1
plotOverLine1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
plotOverLine1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
plotOverLine1Display.PolarAxes.RadialLabelVisibility = 1
plotOverLine1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
plotOverLine1Display.PolarAxes.RadialLabelLocation = 'Bottom'
plotOverLine1Display.PolarAxes.RadialUnitsVisibility = 1
plotOverLine1Display.PolarAxes.ScreenSize = 10.0
plotOverLine1Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
plotOverLine1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
plotOverLine1Display.PolarAxes.PolarAxisTitleFontFile = ''
plotOverLine1Display.PolarAxes.PolarAxisTitleBold = 0
plotOverLine1Display.PolarAxes.PolarAxisTitleItalic = 0
plotOverLine1Display.PolarAxes.PolarAxisTitleShadow = 0
plotOverLine1Display.PolarAxes.PolarAxisTitleFontSize = 12
plotOverLine1Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
plotOverLine1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
plotOverLine1Display.PolarAxes.PolarAxisLabelFontFile = ''
plotOverLine1Display.PolarAxes.PolarAxisLabelBold = 0
plotOverLine1Display.PolarAxes.PolarAxisLabelItalic = 0
plotOverLine1Display.PolarAxes.PolarAxisLabelShadow = 0
plotOverLine1Display.PolarAxes.PolarAxisLabelFontSize = 12
plotOverLine1Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
plotOverLine1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
plotOverLine1Display.PolarAxes.LastRadialAxisTextFontFile = ''
plotOverLine1Display.PolarAxes.LastRadialAxisTextBold = 0
plotOverLine1Display.PolarAxes.LastRadialAxisTextItalic = 0
plotOverLine1Display.PolarAxes.LastRadialAxisTextShadow = 0
plotOverLine1Display.PolarAxes.LastRadialAxisTextFontSize = 12
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
plotOverLine1Display.PolarAxes.EnableDistanceLOD = 1
plotOverLine1Display.PolarAxes.DistanceLODThreshold = 0.7
plotOverLine1Display.PolarAxes.EnableViewAngleLOD = 1
plotOverLine1Display.PolarAxes.ViewAngleLODThreshold = 0.7
plotOverLine1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
plotOverLine1Display.PolarAxes.PolarTicksVisibility = 1
plotOverLine1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
plotOverLine1Display.PolarAxes.TickLocation = 'Both'
plotOverLine1Display.PolarAxes.AxisTickVisibility = 1
plotOverLine1Display.PolarAxes.AxisMinorTickVisibility = 0
plotOverLine1Display.PolarAxes.ArcTickVisibility = 1
plotOverLine1Display.PolarAxes.ArcMinorTickVisibility = 0
plotOverLine1Display.PolarAxes.DeltaAngleMajor = 10.0
plotOverLine1Display.PolarAxes.DeltaAngleMinor = 5.0
plotOverLine1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
plotOverLine1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
plotOverLine1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
plotOverLine1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
plotOverLine1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
plotOverLine1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
plotOverLine1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
plotOverLine1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
plotOverLine1Display.PolarAxes.ArcMajorTickSize = 0.0
plotOverLine1Display.PolarAxes.ArcTickRatioSize = 0.3
plotOverLine1Display.PolarAxes.ArcMajorTickThickness = 1.0
plotOverLine1Display.PolarAxes.ArcTickRatioThickness = 0.5
plotOverLine1Display.PolarAxes.Use2DMode = 0
plotOverLine1Display.PolarAxes.UseLogAxis = 0

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.UseCache = 0
lineChartView1.ViewSize = [400, 400]
lineChartView1.ChartTitle = ''
lineChartView1.ChartTitleAlignment = 'Center'
lineChartView1.ChartTitleFontFamily = 'Arial'
lineChartView1.ChartTitleFontFile = ''
lineChartView1.ChartTitleFontSize = 18
lineChartView1.ChartTitleBold = 0
lineChartView1.ChartTitleItalic = 0
lineChartView1.ChartTitleColor = [0.0, 0.0, 0.0]
lineChartView1.ShowLegend = 1
lineChartView1.LegendLocation = 'TopRight'
lineChartView1.SortByXAxis = 0
lineChartView1.LegendPosition = [0, 0]
lineChartView1.LegendFontFamily = 'Arial'
lineChartView1.LegendFontFile = ''
lineChartView1.LegendFontSize = 12
lineChartView1.LegendBold = 0
lineChartView1.LegendItalic = 0
lineChartView1.TooltipNotation = 'Mixed'
lineChartView1.TooltipPrecision = 6
lineChartView1.HideTimeMarker = 0
lineChartView1.LeftAxisTitle = ''
lineChartView1.ShowLeftAxisGrid = 1
lineChartView1.LeftAxisGridColor = [0.95, 0.95, 0.95]
lineChartView1.LeftAxisColor = [0.0, 0.0, 0.0]
lineChartView1.LeftAxisTitleFontFamily = 'Arial'
lineChartView1.LeftAxisTitleFontFile = ''
lineChartView1.LeftAxisTitleFontSize = 18
lineChartView1.LeftAxisTitleBold = 1
lineChartView1.LeftAxisTitleItalic = 0
lineChartView1.LeftAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView1.LeftAxisLogScale = 0
lineChartView1.LeftAxisUseCustomRange = 0
lineChartView1.LeftAxisRangeMinimum = 0.0
lineChartView1.LeftAxisRangeMaximum = 1.0
lineChartView1.ShowLeftAxisLabels = 1
lineChartView1.LeftAxisLabelNotation = 'Mixed'
lineChartView1.LeftAxisLabelPrecision = 2
lineChartView1.LeftAxisUseCustomLabels = 0
lineChartView1.LeftAxisLabels = []
lineChartView1.LeftAxisLabelFontFamily = 'Arial'
lineChartView1.LeftAxisLabelFontFile = ''
lineChartView1.LeftAxisLabelFontSize = 12
lineChartView1.LeftAxisLabelBold = 0
lineChartView1.LeftAxisLabelItalic = 0
lineChartView1.LeftAxisLabelColor = [0.0, 0.0, 0.0]
lineChartView1.BottomAxisTitle = ''
lineChartView1.ShowBottomAxisGrid = 1
lineChartView1.BottomAxisGridColor = [0.95, 0.95, 0.95]
lineChartView1.BottomAxisColor = [0.0, 0.0, 0.0]
lineChartView1.BottomAxisTitleFontFamily = 'Arial'
lineChartView1.BottomAxisTitleFontFile = ''
lineChartView1.BottomAxisTitleFontSize = 18
lineChartView1.BottomAxisTitleBold = 1
lineChartView1.BottomAxisTitleItalic = 0
lineChartView1.BottomAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView1.BottomAxisLogScale = 0
lineChartView1.BottomAxisUseCustomRange = 0
lineChartView1.BottomAxisRangeMinimum = 0.0
lineChartView1.BottomAxisRangeMaximum = 1.0
lineChartView1.ShowBottomAxisLabels = 1
lineChartView1.BottomAxisLabelNotation = 'Mixed'
lineChartView1.BottomAxisLabelPrecision = 2
lineChartView1.BottomAxisUseCustomLabels = 0
lineChartView1.BottomAxisLabels = []
lineChartView1.BottomAxisLabelFontFamily = 'Arial'
lineChartView1.BottomAxisLabelFontFile = ''
lineChartView1.BottomAxisLabelFontSize = 12
lineChartView1.BottomAxisLabelBold = 0
lineChartView1.BottomAxisLabelItalic = 0
lineChartView1.BottomAxisLabelColor = [0.0, 0.0, 0.0]
lineChartView1.RightAxisTitle = ''
lineChartView1.ShowRightAxisGrid = 1
lineChartView1.RightAxisGridColor = [0.95, 0.95, 0.95]
lineChartView1.RightAxisColor = [0.0, 0.0, 0.0]
lineChartView1.RightAxisTitleFontFamily = 'Arial'
lineChartView1.RightAxisTitleFontFile = ''
lineChartView1.RightAxisTitleFontSize = 18
lineChartView1.RightAxisTitleBold = 1
lineChartView1.RightAxisTitleItalic = 0
lineChartView1.RightAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView1.RightAxisLogScale = 0
lineChartView1.RightAxisUseCustomRange = 0
lineChartView1.RightAxisRangeMinimum = 0.0
lineChartView1.RightAxisRangeMaximum = 1.0
lineChartView1.ShowRightAxisLabels = 1
lineChartView1.RightAxisLabelNotation = 'Mixed'
lineChartView1.RightAxisLabelPrecision = 2
lineChartView1.RightAxisUseCustomLabels = 0
lineChartView1.RightAxisLabels = []
lineChartView1.RightAxisLabelFontFamily = 'Arial'
lineChartView1.RightAxisLabelFontFile = ''
lineChartView1.RightAxisLabelFontSize = 12
lineChartView1.RightAxisLabelBold = 0
lineChartView1.RightAxisLabelItalic = 0
lineChartView1.RightAxisLabelColor = [0.0, 0.0, 0.0]
lineChartView1.TopAxisTitle = ''
lineChartView1.ShowTopAxisGrid = 1
lineChartView1.TopAxisGridColor = [0.95, 0.95, 0.95]
lineChartView1.TopAxisColor = [0.0, 0.0, 0.0]
lineChartView1.TopAxisTitleFontFamily = 'Arial'
lineChartView1.TopAxisTitleFontFile = ''
lineChartView1.TopAxisTitleFontSize = 18
lineChartView1.TopAxisTitleBold = 1
lineChartView1.TopAxisTitleItalic = 0
lineChartView1.TopAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView1.TopAxisLogScale = 0
lineChartView1.TopAxisUseCustomRange = 0
lineChartView1.TopAxisRangeMinimum = 0.0
lineChartView1.TopAxisRangeMaximum = 1.0
lineChartView1.ShowTopAxisLabels = 1
lineChartView1.TopAxisLabelNotation = 'Mixed'
lineChartView1.TopAxisLabelPrecision = 2
lineChartView1.TopAxisUseCustomLabels = 0
lineChartView1.TopAxisLabels = []
lineChartView1.TopAxisLabelFontFamily = 'Arial'
lineChartView1.TopAxisLabelFontFile = ''
lineChartView1.TopAxisLabelFontSize = 12
lineChartView1.TopAxisLabelBold = 0
lineChartView1.TopAxisLabelItalic = 0
lineChartView1.TopAxisLabelColor = [0.0, 0.0, 0.0]

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1)

# trace defaults for the display properties.
plotOverLine1Display_1.CompositeDataSetIndex = [0]
plotOverLine1Display_1.AttributeType = 'Point Data'
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['Coordinates_Magnitude', 'Density', 'Energy', 'Exact Density_Magnitude', 'Exact Mach_Magnitude', 'Exact Pressure_Magnitude', 'Exact Temperature_Magnitude', 'Exact Velocity_Magnitude', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature', 'Velocity_Magnitude']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Coordinates_X', 'Coordinates_X', 'Coordinates_Y', 'Coordinates_Y', 'Coordinates_Z', 'Coordinates_Z', 'Coordinates_Magnitude', 'Coordinates_Magnitude', 'Density', 'Density', 'Energy', 'Energy', 'Exact Density_X', 'Exact Density_X', 'Exact Density_Y', 'Exact Density_Y', 'Exact Density_Magnitude', 'Exact Density_Magnitude', 'Exact Mach_X', 'Exact Mach_X', 'Exact Mach_Y', 'Exact Mach_Y', 'Exact Mach_Magnitude', 'Exact Mach_Magnitude', 'Exact Pressure_X', 'Exact Pressure_X', 'Exact Pressure_Y', 'Exact Pressure_Y', 'Exact Pressure_Magnitude', 'Exact Pressure_Magnitude', 'Exact Temperature_X', 'Exact Temperature_X', 'Exact Temperature_Y', 'Exact Temperature_Y', 'Exact Temperature_Magnitude', 'Exact Temperature_Magnitude', 'Exact Velocity_X', 'Exact Velocity_X', 'Exact Velocity_Y', 'Exact Velocity_Y', 'Exact Velocity_Z', 'Exact Velocity_Z', 'Exact Velocity_Magnitude', 'Exact Velocity_Magnitude', 'Mach', 'Mach', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', 'Pressure', 'Pressure', 'Pressure_Coefficient', 'Pressure_Coefficient', 'Temperature', 'Temperature', 'Velocity_X', 'Velocity_X', 'Velocity_Y', 'Velocity_Y', 'Velocity_Z', 'Velocity_Z', 'Velocity_Magnitude', 'Velocity_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Coordinates_X', '0.89', '0.1', '0.11', 'Coordinates_Y', '0.22', '0.49', '0.72', 'Coordinates_Z', '0.3', '0.69', '0.29', 'Coordinates_Magnitude', '0.6', '0.31', '0.64', 'Density', '1', '0.5', '0', 'Energy', '0.65', '0.34', '0.16', 'Exact Density_X', '0', '0', '0', 'Exact Density_Y', '0.89', '0.1', '0.11', 'Exact Density_Magnitude', '0.22', '0.49', '0.72', 'Exact Mach_X', '0.3', '0.69', '0.29', 'Exact Mach_Y', '0.6', '0.31', '0.64', 'Exact Mach_Magnitude', '1', '0.5', '0', 'Exact Pressure_X', '0.65', '0.34', '0.16', 'Exact Pressure_Y', '0', '0', '0', 'Exact Pressure_Magnitude', '0.89', '0.1', '0.11', 'Exact Temperature_X', '0.22', '0.49', '0.72', 'Exact Temperature_Y', '0.3', '0.69', '0.29', 'Exact Temperature_Magnitude', '0.6', '0.31', '0.64', 'Exact Velocity_X', '1', '0.5', '0', 'Exact Velocity_Y', '0.65', '0.34', '0.16', 'Exact Velocity_Z', '0', '0', '0', 'Exact Velocity_Magnitude', '0.89', '0.1', '0.11', 'Mach', '0.22', '0.49', '0.72', 'Momentum_X', '0.3', '0.69', '0.29', 'Momentum_Y', '0.6', '0.31', '0.64', 'Momentum_Z', '1', '0.5', '0', 'Momentum_Magnitude', '0.65', '0.34', '0.16', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.89', '0.1', '0.11', 'Temperature', '0.22', '0.49', '0.72', 'Velocity_X', '0.3', '0.69', '0.29', 'Velocity_Y', '0.6', '0.31', '0.64', 'Velocity_Z', '1', '0.5', '0', 'Velocity_Magnitude', '0.65', '0.34', '0.16', 'vtkValidPointMask', '0', '0', '0', 'Points_X', '0.89', '0.1', '0.11', 'Points_Y', '0.22', '0.49', '0.72', 'Points_Z', '0.3', '0.69', '0.29', 'Points_Magnitude', '0.6', '0.31', '0.64']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'Coordinates_X', '0', 'Coordinates_Y', '0', 'Coordinates_Z', '0', 'Coordinates_Magnitude', '0', 'Density', '0', 'Energy', '0', 'Exact Density_X', '0', 'Exact Density_Y', '0', 'Exact Density_Magnitude', '0', 'Exact Mach_X', '0', 'Exact Mach_Y', '0', 'Exact Mach_Magnitude', '0', 'Exact Pressure_X', '0', 'Exact Pressure_Y', '0', 'Exact Pressure_Magnitude', '0', 'Exact Temperature_X', '0', 'Exact Temperature_Y', '0', 'Exact Temperature_Magnitude', '0', 'Exact Velocity_X', '0', 'Exact Velocity_Y', '0', 'Exact Velocity_Z', '0', 'Exact Velocity_Magnitude', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Velocity_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'Coordinates_X', '1', 'Coordinates_Y', '1', 'Coordinates_Z', '1', 'Coordinates_Magnitude', '1', 'Density', '1', 'Energy', '1', 'Exact Density_X', '1', 'Exact Density_Y', '1', 'Exact Density_Magnitude', '1', 'Exact Mach_X', '1', 'Exact Mach_Y', '1', 'Exact Mach_Magnitude', '1', 'Exact Pressure_X', '1', 'Exact Pressure_Y', '1', 'Exact Pressure_Magnitude', '1', 'Exact Temperature_X', '1', 'Exact Temperature_Y', '1', 'Exact Temperature_Magnitude', '1', 'Exact Velocity_X', '1', 'Exact Velocity_Y', '1', 'Exact Velocity_Z', '1', 'Exact Velocity_Magnitude', '1', 'Mach', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Momentum_Magnitude', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1', 'Velocity_X', '1', 'Velocity_Y', '1', 'Velocity_Z', '1', 'Velocity_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'Coordinates_X', '2', 'Coordinates_Y', '2', 'Coordinates_Z', '2', 'Coordinates_Magnitude', '2', 'Density', '2', 'Energy', '2', 'Exact Density_X', '2', 'Exact Density_Y', '2', 'Exact Density_Magnitude', '2', 'Exact Mach_X', '2', 'Exact Mach_Y', '2', 'Exact Mach_Magnitude', '2', 'Exact Pressure_X', '2', 'Exact Pressure_Y', '2', 'Exact Pressure_Magnitude', '2', 'Exact Temperature_X', '2', 'Exact Temperature_Y', '2', 'Exact Temperature_Magnitude', '2', 'Exact Velocity_X', '2', 'Exact Velocity_Y', '2', 'Exact Velocity_Z', '2', 'Exact Velocity_Magnitude', '2', 'Mach', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Momentum_Magnitude', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2', 'Velocity_X', '2', 'Velocity_Y', '2', 'Velocity_Z', '2', 'Velocity_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Coordinates_X', '0', 'Coordinates_Y', '0', 'Coordinates_Z', '0', 'Coordinates_Magnitude', '0', 'Density', '0', 'Energy', '0', 'Exact Density_X', '0', 'Exact Density_Y', '0', 'Exact Density_Magnitude', '0', 'Exact Mach_X', '0', 'Exact Mach_Y', '0', 'Exact Mach_Magnitude', '0', 'Exact Pressure_X', '0', 'Exact Pressure_Y', '0', 'Exact Pressure_Magnitude', '0', 'Exact Temperature_X', '0', 'Exact Temperature_Y', '0', 'Exact Temperature_Magnitude', '0', 'Exact Velocity_X', '0', 'Exact Velocity_Y', '0', 'Exact Velocity_Z', '0', 'Exact Velocity_Magnitude', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'Velocity_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = []
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Coordinates_X', '0.889998', '0.100008', '0.110002', 'Coordinates_Y', '0.220005', '0.489998', '0.719997', 'Coordinates_Z', '0.300008', '0.689998', '0.289998', 'Coordinates_Magnitude', '0.6', '0.310002', '0.639994', 'Density', '1', '0.500008', '0', 'Energy', '0.650004', '0.340002', '0.160006', 'Exact Density_X', '0', '0', '0', 'Exact Density_Y', '0.889998', '0.100008', '0.110002', 'Exact Density_Magnitude', '0.220005', '0.489998', '0.719997', 'Exact Mach_X', '0.300008', '0.689998', '0.289998', 'Exact Mach_Y', '0.6', '0.310002', '0.639994', 'Exact Mach_Magnitude', '1', '0.500008', '0', 'Exact Pressure_X', '0.650004', '0.340002', '0.160006', 'Exact Pressure_Y', '0', '0', '0', 'Exact Pressure_Magnitude', '0.889998', '0.100008', '0.110002', 'Exact Temperature_X', '0.220005', '0.489998', '0.719997', 'Exact Temperature_Y', '0.300008', '0.689998', '0.289998', 'Exact Temperature_Magnitude', '0.6', '0.310002', '0.639994', 'Exact Velocity_X', '1', '0.500008', '0', 'Exact Velocity_Y', '0.650004', '0.340002', '0.160006', 'Exact Velocity_Z', '0', '0', '0', 'Exact Velocity_Magnitude', '0.889998', '0.100008', '0.110002', 'Mach', '0.220005', '0.489998', '0.719997', 'Momentum_X', '0.300008', '0.689998', '0.289998', 'Momentum_Y', '0.6', '0.310002', '0.639994', 'Momentum_Z', '1', '0.500008', '0', 'Momentum_Magnitude', '0.650004', '0.340002', '0.160006', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.889998', '0.100008', '0.110002', 'Temperature', '0.220005', '0.489998', '0.719997', 'Velocity_X', '0.300008', '0.689998', '0.289998', 'Velocity_Y', '0.6', '0.310002', '0.639994', 'Velocity_Z', '1', '0.500008', '0', 'Velocity_Magnitude', '0.650004', '0.340002', '0.160006', 'vtkValidPointMask', '0', '0', '0', 'Points_X', '0.889998', '0.100008', '0.110002', 'Points_Y', '0.220005', '0.489998', '0.719997', 'Points_Z', '0.300008', '0.689998', '0.289998', 'Points_Magnitude', '0.6', '0.310002', '0.639994']
plotOverLine1Display_1.SeriesPlotCorner = ['Coordinates_Magnitude', '0', 'Coordinates_X', '0', 'Coordinates_Y', '0', 'Coordinates_Z', '0', 'Density', '0', 'Energy', '0', 'Exact Density_Magnitude', '0', 'Exact Density_X', '0', 'Exact Density_Y', '0', 'Exact Mach_Magnitude', '0', 'Exact Mach_X', '0', 'Exact Mach_Y', '0', 'Exact Pressure_Magnitude', '0', 'Exact Pressure_X', '0', 'Exact Pressure_Y', '0', 'Exact Temperature_Magnitude', '0', 'Exact Temperature_X', '0', 'Exact Temperature_Y', '0', 'Exact Velocity_Magnitude', '0', 'Exact Velocity_X', '0', 'Exact Velocity_Y', '0', 'Exact Velocity_Z', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'Velocity_Magnitude', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Coordinates_Magnitude', '1', 'Coordinates_X', '1', 'Coordinates_Y', '1', 'Coordinates_Z', '1', 'Density', '1', 'Energy', '1', 'Exact Density_Magnitude', '1', 'Exact Density_X', '1', 'Exact Density_Y', '1', 'Exact Mach_Magnitude', '1', 'Exact Mach_X', '1', 'Exact Mach_Y', '1', 'Exact Pressure_Magnitude', '1', 'Exact Pressure_X', '1', 'Exact Pressure_Y', '1', 'Exact Temperature_Magnitude', '1', 'Exact Temperature_X', '1', 'Exact Temperature_Y', '1', 'Exact Velocity_Magnitude', '1', 'Exact Velocity_X', '1', 'Exact Velocity_Y', '1', 'Exact Velocity_Z', '1', 'Mach', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1', 'Velocity_Magnitude', '1', 'Velocity_X', '1', 'Velocity_Y', '1', 'Velocity_Z', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Coordinates_Magnitude', '2', 'Coordinates_X', '2', 'Coordinates_Y', '2', 'Coordinates_Z', '2', 'Density', '2', 'Energy', '2', 'Exact Density_Magnitude', '2', 'Exact Density_X', '2', 'Exact Density_Y', '2', 'Exact Mach_Magnitude', '2', 'Exact Mach_X', '2', 'Exact Mach_Y', '2', 'Exact Pressure_Magnitude', '2', 'Exact Pressure_X', '2', 'Exact Pressure_Y', '2', 'Exact Temperature_Magnitude', '2', 'Exact Temperature_X', '2', 'Exact Temperature_Y', '2', 'Exact Velocity_Magnitude', '2', 'Exact Velocity_X', '2', 'Exact Velocity_Y', '2', 'Exact Velocity_Z', '2', 'Mach', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2', 'Velocity_Magnitude', '2', 'Velocity_X', '2', 'Velocity_Y', '2', 'Velocity_Z', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Coordinates_Magnitude', '0', 'Coordinates_X', '0', 'Coordinates_Y', '0', 'Coordinates_Z', '0', 'Density', '0', 'Energy', '0', 'Exact Density_Magnitude', '0', 'Exact Density_X', '0', 'Exact Density_Y', '0', 'Exact Mach_Magnitude', '0', 'Exact Mach_X', '0', 'Exact Mach_Y', '0', 'Exact Pressure_Magnitude', '0', 'Exact Pressure_X', '0', 'Exact Pressure_Y', '0', 'Exact Temperature_Magnitude', '0', 'Exact Temperature_X', '0', 'Exact Temperature_Y', '0', 'Exact Velocity_Magnitude', '0', 'Exact Velocity_X', '0', 'Exact Velocity_Y', '0', 'Exact Velocity_Z', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'Velocity_Magnitude', '0', 'Velocity_X', '0', 'Velocity_Y', '0', 'Velocity_Z', '0', 'arc_length', '0', 'vtkValidPointMask', '0']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['arc_length', 'Coordinates_X', 'Coordinates_Y', 'Coordinates_Z', 'Coordinates_Magnitude', 'Density', 'Energy', 'Exact Density_X', 'Exact Density_Y', 'Exact Density_Magnitude', 'Exact Mach_X', 'Exact Mach_Y', 'Exact Mach_Magnitude', 'Exact Pressure_X', 'Exact Pressure_Y', 'Exact Pressure_Magnitude', 'Exact Temperature_X', 'Exact Temperature_Y', 'Exact Temperature_Magnitude', 'Exact Velocity_X', 'Exact Velocity_Y', 'Exact Velocity_Z', 'Exact Velocity_Magnitude', 'Mach', 'Momentum_X', 'Momentum_Y', 'Momentum_Z', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature', 'Velocity_X', 'Velocity_Y', 'Velocity_Z', 'Velocity_Magnitude', 'vtkValidPointMask', 'Points_X', 'Points_Y', 'Points_Z', 'Points_Magnitude']

# save data
SaveData('/home/edo20/CFD2020_Guardone/Homework/DIAMOND_AIRFOIL/CASE0/POST-PROCESSING/Data_over_line.csv', proxy=plotOverLine1, WriteTimeSteps=0,
    Filenamesuffix='_%d',
    Precision=8,
    FieldDelimiter=',',
    UseScientificNotation=1,
    FieldAssociation='Points',
    AddMetaData=1)

# split cell
layout1.SplitVertical(2, 0.5)

# set active view
SetActiveView(None)

# close an empty frame
layout1.Collapse(6)

# set active view
SetActiveView(lineChartView1)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = []

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.XArrayName = 'Coordinates_X'

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Exact Mach_X']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Exact Mach_X', 'Mach']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Density', 'Exact Mach_X', 'Mach']

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Density', 'Exact Density_X', 'Exact Mach_X', 'Mach']

# save screenshot
SaveScreenshot('/home/edo20/CFD2020_Guardone/Homework/DIAMOND_AIRFOIL/CASE0/POST-PROCESSING/Plot_over_line.png', lineChartView1, SaveAllViews=0,
    ImageResolution=[3050, 1590],
    FontScaling='Scale fonts proportionally',
    SeparatorWidth=1,
    SeparatorColor=[0.937, 0.922, 0.906],
    OverrideColorPalette='WhiteBackground',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(appendAttributes1)

# create a new 'Clip'
clip1 = Clip(Input=appendAttributes1)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'Density']
clip1.Value = 1.2310039103031158
clip1.Invert = 1
clip1.Crinkleclip = 0
clip1.Exact = 0

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.0, 0.0, 0.0]
clip1.ClipType.Normal = [1.0, 0.0, 0.0]
clip1.ClipType.Offset = 0.0

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# Properties modified on clip1
clip1.ClipType = 'Box'
clip1.Exact = 1

# Properties modified on clip1.ClipType
clip1.ClipType.Position = [-0.3, -0.3, -1.0]
clip1.ClipType.Length = [2.0, 0.6, 2.0]

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.AmbientColor = [1.0, 1.0, 1.0]
clip1Display.ColorArrayName = [None, '']
clip1Display.DiffuseColor = [1.0, 1.0, 1.0]
clip1Display.LookupTable = None
clip1Display.MapScalars = 1
clip1Display.MultiComponentsMapping = 0
clip1Display.InterpolateScalarsBeforeMapping = 1
clip1Display.Opacity = 1.0
clip1Display.PointSize = 2.0
clip1Display.LineWidth = 1.0
clip1Display.RenderLinesAsTubes = 0
clip1Display.RenderPointsAsSpheres = 0
clip1Display.Interpolation = 'Gouraud'
clip1Display.Specular = 0.0
clip1Display.SpecularColor = [1.0, 1.0, 1.0]
clip1Display.SpecularPower = 100.0
clip1Display.Luminosity = 0.0
clip1Display.Ambient = 0.0
clip1Display.Diffuse = 1.0
clip1Display.EdgeColor = [0.0, 0.0, 0.5]
clip1Display.BackfaceRepresentation = 'Follow Frontface'
clip1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
clip1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
clip1Display.BackfaceOpacity = 1.0
clip1Display.Position = [0.0, 0.0, 0.0]
clip1Display.Scale = [1.0, 1.0, 1.0]
clip1Display.Orientation = [0.0, 0.0, 0.0]
clip1Display.Origin = [0.0, 0.0, 0.0]
clip1Display.Pickable = 1
clip1Display.Texture = None
clip1Display.Triangulate = 0
clip1Display.UseShaderReplacements = 0
clip1Display.ShaderReplacements = ''
clip1Display.NonlinearSubdivisionLevel = 1
clip1Display.UseDataPartitions = 0
clip1Display.OSPRayUseScaleArray = 0
clip1Display.OSPRayScaleArray = 'Coordinates'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.OSPRayMaterial = 'None'
clip1Display.Orient = 0
clip1Display.OrientationMode = 'Direction'
clip1Display.SelectOrientationVectors = 'Velocity'
clip1Display.Scaling = 0
clip1Display.ScaleMode = 'No Data Scaling Off'
clip1Display.ScaleFactor = 0.2000000059604645
clip1Display.SelectScaleArray = 'Coordinates'
clip1Display.GlyphType = 'Arrow'
clip1Display.UseGlyphTable = 0
clip1Display.GlyphTableIndexArray = 'Coordinates'
clip1Display.UseCompositeGlyphTable = 0
clip1Display.UseGlyphCullingAndLOD = 0
clip1Display.LODValues = []
clip1Display.ColorByLODIndex = 0
clip1Display.GaussianRadius = 0.010000000298023224
clip1Display.ShaderPreset = 'Sphere'
clip1Display.CustomTriangleScale = 3
clip1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
clip1Display.Emissive = 0
clip1Display.ScaleByArray = 0
clip1Display.SetScaleArray = ['POINTS', 'Coordinates']
clip1Display.ScaleArrayComponent = 'X'
clip1Display.UseScaleFunction = 1
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityByArray = 0
clip1Display.OpacityArray = ['POINTS', 'Coordinates']
clip1Display.OpacityArrayComponent = 'X'
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.SelectionCellLabelBold = 0
clip1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
clip1Display.SelectionCellLabelFontFamily = 'Arial'
clip1Display.SelectionCellLabelFontFile = ''
clip1Display.SelectionCellLabelFontSize = 18
clip1Display.SelectionCellLabelItalic = 0
clip1Display.SelectionCellLabelJustification = 'Left'
clip1Display.SelectionCellLabelOpacity = 1.0
clip1Display.SelectionCellLabelShadow = 0
clip1Display.SelectionPointLabelBold = 0
clip1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
clip1Display.SelectionPointLabelFontFamily = 'Arial'
clip1Display.SelectionPointLabelFontFile = ''
clip1Display.SelectionPointLabelFontSize = 18
clip1Display.SelectionPointLabelItalic = 0
clip1Display.SelectionPointLabelJustification = 'Left'
clip1Display.SelectionPointLabelOpacity = 1.0
clip1Display.SelectionPointLabelShadow = 0
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = None
clip1Display.ScalarOpacityUnitDistance = 0.23275419942907455
clip1Display.ExtractedBlockIndex = 0
clip1Display.SelectMapper = 'Projected tetra'
clip1Display.SamplingDimensions = [128, 128, 128]
clip1Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
clip1Display.OSPRayScaleFunction.Points = [270962.9375, 0.0, 0.5, 0.0, 809535.8125, 1.0, 0.5, 0.0]
clip1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
clip1Display.GlyphType.TipResolution = 6
clip1Display.GlyphType.TipRadius = 0.1
clip1Display.GlyphType.TipLength = 0.35
clip1Display.GlyphType.ShaftResolution = 6
clip1Display.GlyphType.ShaftRadius = 0.03
clip1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [-0.3, 0.0, 0.5, 0.0, 1.7, 1.0, 0.5, 0.0]
clip1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [-0.3, 0.0, 0.5, 0.0, 1.7, 1.0, 0.5, 0.0]
clip1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip1Display.DataAxesGrid.XTitle = 'X Axis'
clip1Display.DataAxesGrid.YTitle = 'Y Axis'
clip1Display.DataAxesGrid.ZTitle = 'Z Axis'
clip1Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
clip1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
clip1Display.DataAxesGrid.XTitleFontFile = ''
clip1Display.DataAxesGrid.XTitleBold = 0
clip1Display.DataAxesGrid.XTitleItalic = 0
clip1Display.DataAxesGrid.XTitleFontSize = 12
clip1Display.DataAxesGrid.XTitleShadow = 0
clip1Display.DataAxesGrid.XTitleOpacity = 1.0
clip1Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
clip1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
clip1Display.DataAxesGrid.YTitleFontFile = ''
clip1Display.DataAxesGrid.YTitleBold = 0
clip1Display.DataAxesGrid.YTitleItalic = 0
clip1Display.DataAxesGrid.YTitleFontSize = 12
clip1Display.DataAxesGrid.YTitleShadow = 0
clip1Display.DataAxesGrid.YTitleOpacity = 1.0
clip1Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
clip1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
clip1Display.DataAxesGrid.ZTitleFontFile = ''
clip1Display.DataAxesGrid.ZTitleBold = 0
clip1Display.DataAxesGrid.ZTitleItalic = 0
clip1Display.DataAxesGrid.ZTitleFontSize = 12
clip1Display.DataAxesGrid.ZTitleShadow = 0
clip1Display.DataAxesGrid.ZTitleOpacity = 1.0
clip1Display.DataAxesGrid.FacesToRender = 63
clip1Display.DataAxesGrid.CullBackface = 0
clip1Display.DataAxesGrid.CullFrontface = 1
clip1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
clip1Display.DataAxesGrid.ShowGrid = 0
clip1Display.DataAxesGrid.ShowEdges = 1
clip1Display.DataAxesGrid.ShowTicks = 1
clip1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
clip1Display.DataAxesGrid.AxesToLabel = 63
clip1Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
clip1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
clip1Display.DataAxesGrid.XLabelFontFile = ''
clip1Display.DataAxesGrid.XLabelBold = 0
clip1Display.DataAxesGrid.XLabelItalic = 0
clip1Display.DataAxesGrid.XLabelFontSize = 12
clip1Display.DataAxesGrid.XLabelShadow = 0
clip1Display.DataAxesGrid.XLabelOpacity = 1.0
clip1Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
clip1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
clip1Display.DataAxesGrid.YLabelFontFile = ''
clip1Display.DataAxesGrid.YLabelBold = 0
clip1Display.DataAxesGrid.YLabelItalic = 0
clip1Display.DataAxesGrid.YLabelFontSize = 12
clip1Display.DataAxesGrid.YLabelShadow = 0
clip1Display.DataAxesGrid.YLabelOpacity = 1.0
clip1Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
clip1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
clip1Display.DataAxesGrid.ZLabelFontFile = ''
clip1Display.DataAxesGrid.ZLabelBold = 0
clip1Display.DataAxesGrid.ZLabelItalic = 0
clip1Display.DataAxesGrid.ZLabelFontSize = 12
clip1Display.DataAxesGrid.ZLabelShadow = 0
clip1Display.DataAxesGrid.ZLabelOpacity = 1.0
clip1Display.DataAxesGrid.XAxisNotation = 'Mixed'
clip1Display.DataAxesGrid.XAxisPrecision = 2
clip1Display.DataAxesGrid.XAxisUseCustomLabels = 0
clip1Display.DataAxesGrid.XAxisLabels = []
clip1Display.DataAxesGrid.YAxisNotation = 'Mixed'
clip1Display.DataAxesGrid.YAxisPrecision = 2
clip1Display.DataAxesGrid.YAxisUseCustomLabels = 0
clip1Display.DataAxesGrid.YAxisLabels = []
clip1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
clip1Display.DataAxesGrid.ZAxisPrecision = 2
clip1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
clip1Display.DataAxesGrid.ZAxisLabels = []
clip1Display.DataAxesGrid.UseCustomBounds = 0
clip1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip1Display.PolarAxes.Visibility = 0
clip1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
clip1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
clip1Display.PolarAxes.EnableCustomRange = 0
clip1Display.PolarAxes.CustomRange = [0.0, 1.0]
clip1Display.PolarAxes.PolarAxisVisibility = 1
clip1Display.PolarAxes.RadialAxesVisibility = 1
clip1Display.PolarAxes.DrawRadialGridlines = 1
clip1Display.PolarAxes.PolarArcsVisibility = 1
clip1Display.PolarAxes.DrawPolarArcsGridlines = 1
clip1Display.PolarAxes.NumberOfRadialAxes = 0
clip1Display.PolarAxes.AutoSubdividePolarAxis = 1
clip1Display.PolarAxes.NumberOfPolarAxis = 0
clip1Display.PolarAxes.MinimumRadius = 0.0
clip1Display.PolarAxes.MinimumAngle = 0.0
clip1Display.PolarAxes.MaximumAngle = 90.0
clip1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
clip1Display.PolarAxes.Ratio = 1.0
clip1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.PolarAxisTitleVisibility = 1
clip1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
clip1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
clip1Display.PolarAxes.PolarLabelVisibility = 1
clip1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
clip1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
clip1Display.PolarAxes.RadialLabelVisibility = 1
clip1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
clip1Display.PolarAxes.RadialLabelLocation = 'Bottom'
clip1Display.PolarAxes.RadialUnitsVisibility = 1
clip1Display.PolarAxes.ScreenSize = 10.0
clip1Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
clip1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
clip1Display.PolarAxes.PolarAxisTitleFontFile = ''
clip1Display.PolarAxes.PolarAxisTitleBold = 0
clip1Display.PolarAxes.PolarAxisTitleItalic = 0
clip1Display.PolarAxes.PolarAxisTitleShadow = 0
clip1Display.PolarAxes.PolarAxisTitleFontSize = 12
clip1Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
clip1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
clip1Display.PolarAxes.PolarAxisLabelFontFile = ''
clip1Display.PolarAxes.PolarAxisLabelBold = 0
clip1Display.PolarAxes.PolarAxisLabelItalic = 0
clip1Display.PolarAxes.PolarAxisLabelShadow = 0
clip1Display.PolarAxes.PolarAxisLabelFontSize = 12
clip1Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
clip1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
clip1Display.PolarAxes.LastRadialAxisTextFontFile = ''
clip1Display.PolarAxes.LastRadialAxisTextBold = 0
clip1Display.PolarAxes.LastRadialAxisTextItalic = 0
clip1Display.PolarAxes.LastRadialAxisTextShadow = 0
clip1Display.PolarAxes.LastRadialAxisTextFontSize = 12
clip1Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
clip1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
clip1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
clip1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
clip1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
clip1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
clip1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
clip1Display.PolarAxes.EnableDistanceLOD = 1
clip1Display.PolarAxes.DistanceLODThreshold = 0.7
clip1Display.PolarAxes.EnableViewAngleLOD = 1
clip1Display.PolarAxes.ViewAngleLODThreshold = 0.7
clip1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
clip1Display.PolarAxes.PolarTicksVisibility = 1
clip1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
clip1Display.PolarAxes.TickLocation = 'Both'
clip1Display.PolarAxes.AxisTickVisibility = 1
clip1Display.PolarAxes.AxisMinorTickVisibility = 0
clip1Display.PolarAxes.ArcTickVisibility = 1
clip1Display.PolarAxes.ArcMinorTickVisibility = 0
clip1Display.PolarAxes.DeltaAngleMajor = 10.0
clip1Display.PolarAxes.DeltaAngleMinor = 5.0
clip1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
clip1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
clip1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
clip1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
clip1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
clip1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
clip1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
clip1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
clip1Display.PolarAxes.ArcMajorTickSize = 0.0
clip1Display.PolarAxes.ArcTickRatioSize = 0.3
clip1Display.PolarAxes.ArcMajorTickThickness = 1.0
clip1Display.PolarAxes.ArcTickRatioThickness = 0.5
clip1Display.PolarAxes.Use2DMode = 0
clip1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(appendAttributes1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator2 = Calculator(Input=clip1)
calculator2.AttributeType = 'Point Data'
calculator2.CoordinateResults = 0
calculator2.ResultNormals = 0
calculator2.ResultTCoords = 0
calculator2.ResultArrayName = 'Result'
calculator2.Function = ''
calculator2.ReplaceInvalidResults = 1
calculator2.ReplacementValue = 0.0
calculator2.ResultArrayType = 'Double'

# Properties modified on calculator2
calculator2.ResultArrayName = 'Mach_error'
calculator2.Function = 'Mach-Exact Mach_X'

# show data in view
calculator2Display = Show(calculator2, renderView1)

# get color transfer function/color map for 'Mach_error'
mach_errorLUT = GetColorTransferFunction('Mach_error')
mach_errorLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
mach_errorLUT.InterpretValuesAsCategories = 0
mach_errorLUT.AnnotationsInitialized = 0
mach_errorLUT.ShowCategoricalColorsinDataRangeOnly = 0
mach_errorLUT.RescaleOnVisibilityChange = 0
mach_errorLUT.EnableOpacityMapping = 0
mach_errorLUT.RGBPoints = [-0.6205622321682835, 0.0, 0.0, 0.34902, -0.5732466577112911, 0.039216, 0.062745, 0.380392, -0.5259310832542986, 0.062745, 0.117647, 0.411765, -0.4786155087973062, 0.090196, 0.184314, 0.45098, -0.4312999343403138, 0.12549, 0.262745, 0.501961, -0.3839843598833213, 0.160784, 0.337255, 0.541176, -0.33666878542632883, 0.2, 0.396078, 0.568627, -0.2893532109693364, 0.239216, 0.454902, 0.6, -0.24203763651234395, 0.286275, 0.521569, 0.65098, -0.19472206205535147, 0.337255, 0.592157, 0.701961, -0.14740648759835906, 0.388235, 0.654902, 0.74902, -0.10009091314136664, 0.466667, 0.737255, 0.819608, -0.05277533868437412, 0.572549, 0.819608, 0.878431, -0.005459764227381703, 0.654902, 0.866667, 0.909804, 0.04185581022961071, 0.752941, 0.917647, 0.941176, 0.08917138468660324, 0.823529, 0.956863, 0.968627, 0.13648695914359565, 0.988235, 0.960784, 0.901961, 0.13648695914359565, 0.941176, 0.984314, 0.988235, 0.1667689267960708, 0.988235, 0.945098, 0.85098, 0.19705089444854607, 0.980392, 0.898039, 0.784314, 0.2311181080575806, 0.968627, 0.835294, 0.698039, 0.278433682514573, 0.94902, 0.733333, 0.588235, 0.3257492569715654, 0.929412, 0.65098, 0.509804, 0.37306483142855795, 0.909804, 0.564706, 0.435294, 0.42038040588555026, 0.878431, 0.458824, 0.352941, 0.4676959803425429, 0.839216, 0.388235, 0.286275, 0.5150115547995353, 0.760784, 0.294118, 0.211765, 0.5623271292565277, 0.701961, 0.211765, 0.168627, 0.6096427037135201, 0.65098, 0.156863, 0.129412, 0.6569582781705126, 0.6, 0.094118, 0.094118, 0.704273852627505, 0.54902, 0.066667, 0.098039, 0.7515894270844976, 0.501961, 0.05098, 0.12549, 0.79890500154149, 0.45098, 0.054902, 0.172549, 0.8462205759984824, 0.4, 0.054902, 0.192157, 0.8935361504554749, 0.34902, 0.070588, 0.211765]
mach_errorLUT.UseLogScale = 0
mach_errorLUT.ColorSpace = 'Lab'
mach_errorLUT.UseBelowRangeColor = 0
mach_errorLUT.BelowRangeColor = [0.0, 0.0, 0.0]
mach_errorLUT.UseAboveRangeColor = 0
mach_errorLUT.AboveRangeColor = [0.5, 0.5, 0.5]
mach_errorLUT.NanColor = [0.25, 0.0, 0.0]
mach_errorLUT.NanOpacity = 1.0
mach_errorLUT.Discretize = 0
mach_errorLUT.NumberOfTableValues = 256
mach_errorLUT.ScalarRangeInitialized = 1.0
mach_errorLUT.HSVWrap = 0
mach_errorLUT.VectorComponent = 0
mach_errorLUT.VectorMode = 'Magnitude'
mach_errorLUT.AllowDuplicateScalars = 1
mach_errorLUT.Annotations = []
mach_errorLUT.ActiveAnnotatedValues = []
mach_errorLUT.IndexedColors = []
mach_errorLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'Mach_error'
mach_errorPWF = GetOpacityTransferFunction('Mach_error')
mach_errorPWF.Points = [-0.6205622321682835, 0.0, 0.5, 0.0, 0.8935361504554749, 1.0, 0.5, 0.0]
mach_errorPWF.AllowDuplicateScalars = 1
mach_errorPWF.UseLogScale = 0
mach_errorPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator2Display.Representation = 'Surface'
calculator2Display.AmbientColor = [1.0, 1.0, 1.0]
calculator2Display.ColorArrayName = ['POINTS', 'Mach_error']
calculator2Display.DiffuseColor = [1.0, 1.0, 1.0]
calculator2Display.LookupTable = mach_errorLUT
calculator2Display.MapScalars = 1
calculator2Display.MultiComponentsMapping = 0
calculator2Display.InterpolateScalarsBeforeMapping = 1
calculator2Display.Opacity = 1.0
calculator2Display.PointSize = 2.0
calculator2Display.LineWidth = 1.0
calculator2Display.RenderLinesAsTubes = 0
calculator2Display.RenderPointsAsSpheres = 0
calculator2Display.Interpolation = 'Gouraud'
calculator2Display.Specular = 0.0
calculator2Display.SpecularColor = [1.0, 1.0, 1.0]
calculator2Display.SpecularPower = 100.0
calculator2Display.Luminosity = 0.0
calculator2Display.Ambient = 0.0
calculator2Display.Diffuse = 1.0
calculator2Display.EdgeColor = [0.0, 0.0, 0.5]
calculator2Display.BackfaceRepresentation = 'Follow Frontface'
calculator2Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
calculator2Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
calculator2Display.BackfaceOpacity = 1.0
calculator2Display.Position = [0.0, 0.0, 0.0]
calculator2Display.Scale = [1.0, 1.0, 1.0]
calculator2Display.Orientation = [0.0, 0.0, 0.0]
calculator2Display.Origin = [0.0, 0.0, 0.0]
calculator2Display.Pickable = 1
calculator2Display.Texture = None
calculator2Display.Triangulate = 0
calculator2Display.UseShaderReplacements = 0
calculator2Display.ShaderReplacements = ''
calculator2Display.NonlinearSubdivisionLevel = 1
calculator2Display.UseDataPartitions = 0
calculator2Display.OSPRayUseScaleArray = 0
calculator2Display.OSPRayScaleArray = 'Mach_error'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.OSPRayMaterial = 'None'
calculator2Display.Orient = 0
calculator2Display.OrientationMode = 'Direction'
calculator2Display.SelectOrientationVectors = 'Velocity'
calculator2Display.Scaling = 0
calculator2Display.ScaleMode = 'No Data Scaling Off'
calculator2Display.ScaleFactor = 0.2000000059604645
calculator2Display.SelectScaleArray = 'Mach_error'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.UseGlyphTable = 0
calculator2Display.GlyphTableIndexArray = 'Mach_error'
calculator2Display.UseCompositeGlyphTable = 0
calculator2Display.UseGlyphCullingAndLOD = 0
calculator2Display.LODValues = []
calculator2Display.ColorByLODIndex = 0
calculator2Display.GaussianRadius = 0.010000000298023224
calculator2Display.ShaderPreset = 'Sphere'
calculator2Display.CustomTriangleScale = 3
calculator2Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
calculator2Display.Emissive = 0
calculator2Display.ScaleByArray = 0
calculator2Display.SetScaleArray = ['POINTS', 'Mach_error']
calculator2Display.ScaleArrayComponent = ''
calculator2Display.UseScaleFunction = 1
calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display.OpacityByArray = 0
calculator2Display.OpacityArray = ['POINTS', 'Mach_error']
calculator2Display.OpacityArrayComponent = ''
calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display.SelectionCellLabelBold = 0
calculator2Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
calculator2Display.SelectionCellLabelFontFamily = 'Arial'
calculator2Display.SelectionCellLabelFontFile = ''
calculator2Display.SelectionCellLabelFontSize = 18
calculator2Display.SelectionCellLabelItalic = 0
calculator2Display.SelectionCellLabelJustification = 'Left'
calculator2Display.SelectionCellLabelOpacity = 1.0
calculator2Display.SelectionCellLabelShadow = 0
calculator2Display.SelectionPointLabelBold = 0
calculator2Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
calculator2Display.SelectionPointLabelFontFamily = 'Arial'
calculator2Display.SelectionPointLabelFontFile = ''
calculator2Display.SelectionPointLabelFontSize = 18
calculator2Display.SelectionPointLabelItalic = 0
calculator2Display.SelectionPointLabelJustification = 'Left'
calculator2Display.SelectionPointLabelOpacity = 1.0
calculator2Display.SelectionPointLabelShadow = 0
calculator2Display.PolarAxes = 'PolarAxesRepresentation'
calculator2Display.ScalarOpacityFunction = mach_errorPWF
calculator2Display.ScalarOpacityUnitDistance = 0.23275419942907455
calculator2Display.ExtractedBlockIndex = 0
calculator2Display.SelectMapper = 'Projected tetra'
calculator2Display.SamplingDimensions = [128, 128, 128]
calculator2Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator2Display.OSPRayScaleFunction.Points = [270962.9375, 0.0, 0.5, 0.0, 809535.8125, 1.0, 0.5, 0.0]
calculator2Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
calculator2Display.GlyphType.TipResolution = 6
calculator2Display.GlyphType.TipRadius = 0.1
calculator2Display.GlyphType.TipLength = 0.35
calculator2Display.GlyphType.ShaftResolution = 6
calculator2Display.GlyphType.ShaftRadius = 0.03
calculator2Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator2Display.ScaleTransferFunction.Points = [-0.6205622321682835, 0.0, 0.5, 0.0, 0.8935361504554749, 1.0, 0.5, 0.0]
calculator2Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator2Display.OpacityTransferFunction.Points = [-0.6205622321682835, 0.0, 0.5, 0.0, 0.8935361504554749, 1.0, 0.5, 0.0]
calculator2Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator2Display.DataAxesGrid.XTitle = 'X Axis'
calculator2Display.DataAxesGrid.YTitle = 'Y Axis'
calculator2Display.DataAxesGrid.ZTitle = 'Z Axis'
calculator2Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
calculator2Display.DataAxesGrid.XTitleFontFamily = 'Arial'
calculator2Display.DataAxesGrid.XTitleFontFile = ''
calculator2Display.DataAxesGrid.XTitleBold = 0
calculator2Display.DataAxesGrid.XTitleItalic = 0
calculator2Display.DataAxesGrid.XTitleFontSize = 12
calculator2Display.DataAxesGrid.XTitleShadow = 0
calculator2Display.DataAxesGrid.XTitleOpacity = 1.0
calculator2Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
calculator2Display.DataAxesGrid.YTitleFontFamily = 'Arial'
calculator2Display.DataAxesGrid.YTitleFontFile = ''
calculator2Display.DataAxesGrid.YTitleBold = 0
calculator2Display.DataAxesGrid.YTitleItalic = 0
calculator2Display.DataAxesGrid.YTitleFontSize = 12
calculator2Display.DataAxesGrid.YTitleShadow = 0
calculator2Display.DataAxesGrid.YTitleOpacity = 1.0
calculator2Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
calculator2Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
calculator2Display.DataAxesGrid.ZTitleFontFile = ''
calculator2Display.DataAxesGrid.ZTitleBold = 0
calculator2Display.DataAxesGrid.ZTitleItalic = 0
calculator2Display.DataAxesGrid.ZTitleFontSize = 12
calculator2Display.DataAxesGrid.ZTitleShadow = 0
calculator2Display.DataAxesGrid.ZTitleOpacity = 1.0
calculator2Display.DataAxesGrid.FacesToRender = 63
calculator2Display.DataAxesGrid.CullBackface = 0
calculator2Display.DataAxesGrid.CullFrontface = 1
calculator2Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
calculator2Display.DataAxesGrid.ShowGrid = 0
calculator2Display.DataAxesGrid.ShowEdges = 1
calculator2Display.DataAxesGrid.ShowTicks = 1
calculator2Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
calculator2Display.DataAxesGrid.AxesToLabel = 63
calculator2Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
calculator2Display.DataAxesGrid.XLabelFontFamily = 'Arial'
calculator2Display.DataAxesGrid.XLabelFontFile = ''
calculator2Display.DataAxesGrid.XLabelBold = 0
calculator2Display.DataAxesGrid.XLabelItalic = 0
calculator2Display.DataAxesGrid.XLabelFontSize = 12
calculator2Display.DataAxesGrid.XLabelShadow = 0
calculator2Display.DataAxesGrid.XLabelOpacity = 1.0
calculator2Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
calculator2Display.DataAxesGrid.YLabelFontFamily = 'Arial'
calculator2Display.DataAxesGrid.YLabelFontFile = ''
calculator2Display.DataAxesGrid.YLabelBold = 0
calculator2Display.DataAxesGrid.YLabelItalic = 0
calculator2Display.DataAxesGrid.YLabelFontSize = 12
calculator2Display.DataAxesGrid.YLabelShadow = 0
calculator2Display.DataAxesGrid.YLabelOpacity = 1.0
calculator2Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
calculator2Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
calculator2Display.DataAxesGrid.ZLabelFontFile = ''
calculator2Display.DataAxesGrid.ZLabelBold = 0
calculator2Display.DataAxesGrid.ZLabelItalic = 0
calculator2Display.DataAxesGrid.ZLabelFontSize = 12
calculator2Display.DataAxesGrid.ZLabelShadow = 0
calculator2Display.DataAxesGrid.ZLabelOpacity = 1.0
calculator2Display.DataAxesGrid.XAxisNotation = 'Mixed'
calculator2Display.DataAxesGrid.XAxisPrecision = 2
calculator2Display.DataAxesGrid.XAxisUseCustomLabels = 0
calculator2Display.DataAxesGrid.XAxisLabels = []
calculator2Display.DataAxesGrid.YAxisNotation = 'Mixed'
calculator2Display.DataAxesGrid.YAxisPrecision = 2
calculator2Display.DataAxesGrid.YAxisUseCustomLabels = 0
calculator2Display.DataAxesGrid.YAxisLabels = []
calculator2Display.DataAxesGrid.ZAxisNotation = 'Mixed'
calculator2Display.DataAxesGrid.ZAxisPrecision = 2
calculator2Display.DataAxesGrid.ZAxisUseCustomLabels = 0
calculator2Display.DataAxesGrid.ZAxisLabels = []
calculator2Display.DataAxesGrid.UseCustomBounds = 0
calculator2Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator2Display.PolarAxes.Visibility = 0
calculator2Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
calculator2Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
calculator2Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
calculator2Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
calculator2Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
calculator2Display.PolarAxes.EnableCustomRange = 0
calculator2Display.PolarAxes.CustomRange = [0.0, 1.0]
calculator2Display.PolarAxes.PolarAxisVisibility = 1
calculator2Display.PolarAxes.RadialAxesVisibility = 1
calculator2Display.PolarAxes.DrawRadialGridlines = 1
calculator2Display.PolarAxes.PolarArcsVisibility = 1
calculator2Display.PolarAxes.DrawPolarArcsGridlines = 1
calculator2Display.PolarAxes.NumberOfRadialAxes = 0
calculator2Display.PolarAxes.AutoSubdividePolarAxis = 1
calculator2Display.PolarAxes.NumberOfPolarAxis = 0
calculator2Display.PolarAxes.MinimumRadius = 0.0
calculator2Display.PolarAxes.MinimumAngle = 0.0
calculator2Display.PolarAxes.MaximumAngle = 90.0
calculator2Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
calculator2Display.PolarAxes.Ratio = 1.0
calculator2Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
calculator2Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
calculator2Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
calculator2Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
calculator2Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
calculator2Display.PolarAxes.PolarAxisTitleVisibility = 1
calculator2Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
calculator2Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
calculator2Display.PolarAxes.PolarLabelVisibility = 1
calculator2Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
calculator2Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
calculator2Display.PolarAxes.RadialLabelVisibility = 1
calculator2Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
calculator2Display.PolarAxes.RadialLabelLocation = 'Bottom'
calculator2Display.PolarAxes.RadialUnitsVisibility = 1
calculator2Display.PolarAxes.ScreenSize = 10.0
calculator2Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
calculator2Display.PolarAxes.PolarAxisTitleOpacity = 1.0
calculator2Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
calculator2Display.PolarAxes.PolarAxisTitleFontFile = ''
calculator2Display.PolarAxes.PolarAxisTitleBold = 0
calculator2Display.PolarAxes.PolarAxisTitleItalic = 0
calculator2Display.PolarAxes.PolarAxisTitleShadow = 0
calculator2Display.PolarAxes.PolarAxisTitleFontSize = 12
calculator2Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
calculator2Display.PolarAxes.PolarAxisLabelOpacity = 1.0
calculator2Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
calculator2Display.PolarAxes.PolarAxisLabelFontFile = ''
calculator2Display.PolarAxes.PolarAxisLabelBold = 0
calculator2Display.PolarAxes.PolarAxisLabelItalic = 0
calculator2Display.PolarAxes.PolarAxisLabelShadow = 0
calculator2Display.PolarAxes.PolarAxisLabelFontSize = 12
calculator2Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
calculator2Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
calculator2Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
calculator2Display.PolarAxes.LastRadialAxisTextFontFile = ''
calculator2Display.PolarAxes.LastRadialAxisTextBold = 0
calculator2Display.PolarAxes.LastRadialAxisTextItalic = 0
calculator2Display.PolarAxes.LastRadialAxisTextShadow = 0
calculator2Display.PolarAxes.LastRadialAxisTextFontSize = 12
calculator2Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
calculator2Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
calculator2Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
calculator2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
calculator2Display.PolarAxes.SecondaryRadialAxesTextBold = 0
calculator2Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
calculator2Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
calculator2Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
calculator2Display.PolarAxes.EnableDistanceLOD = 1
calculator2Display.PolarAxes.DistanceLODThreshold = 0.7
calculator2Display.PolarAxes.EnableViewAngleLOD = 1
calculator2Display.PolarAxes.ViewAngleLODThreshold = 0.7
calculator2Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
calculator2Display.PolarAxes.PolarTicksVisibility = 1
calculator2Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
calculator2Display.PolarAxes.TickLocation = 'Both'
calculator2Display.PolarAxes.AxisTickVisibility = 1
calculator2Display.PolarAxes.AxisMinorTickVisibility = 0
calculator2Display.PolarAxes.ArcTickVisibility = 1
calculator2Display.PolarAxes.ArcMinorTickVisibility = 0
calculator2Display.PolarAxes.DeltaAngleMajor = 10.0
calculator2Display.PolarAxes.DeltaAngleMinor = 5.0
calculator2Display.PolarAxes.PolarAxisMajorTickSize = 0.0
calculator2Display.PolarAxes.PolarAxisTickRatioSize = 0.3
calculator2Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
calculator2Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
calculator2Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
calculator2Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
calculator2Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
calculator2Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
calculator2Display.PolarAxes.ArcMajorTickSize = 0.0
calculator2Display.PolarAxes.ArcTickRatioSize = 0.3
calculator2Display.PolarAxes.ArcMajorTickThickness = 1.0
calculator2Display.PolarAxes.ArcTickRatioThickness = 0.5
calculator2Display.PolarAxes.Use2DMode = 0
calculator2Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(clip1, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(clip1)

# Properties modified on clip1.ClipType
clip1.ClipType.Position = [-0.3, -1.0, -1.0]
clip1.ClipType.Length = [2.0, 2.0, 2.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(flowvtu)

# hide data in view
Hide(plotOverLine1, renderView1)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.8254697654357902, 0.001774259954828104, 546.4101615137755]
renderView1.CameraFocalPoint = [0.8254697654357902, 0.001774259954828104, 0.0]
renderView1.CameraParallelScale = 1.2047050751240436

# save screenshot
SaveScreenshot('/home/edo20/CFD2020_Guardone/Homework/DIAMOND_AIRFOIL/CASE0/POST-PROCESSING/Mesh_error_clip.png', renderView1, ImageResolution=[3050, 1590],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='WhiteBackground',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

# set active source
SetActiveSource(calculator2)

# save data
SaveData('/home/edo20/CFD2020_Guardone/Homework/DIAMOND_AIRFOIL/CASE0/POST-PROCESSING/Data.csv', proxy=calculator2, WriteTimeSteps=0,
    Filenamesuffix='_%d',
    Precision=8,
    FieldDelimiter=',',
    UseScientificNotation=1,
    FieldAssociation='Points',
    AddMetaData=1)

# hide data in view
Hide(calculator2, renderView1)

# set active source
SetActiveSource(flowvtu)

# show data in view
flowvtuDisplay = Show(flowvtu, renderView1)

# show color bar/color legend
flowvtuDisplay.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# hide data in view
Hide(flowvtu, renderView1)

# show data in view
flowvtuDisplay = Show(flowvtu, renderView1)

# show color bar/color legend
flowvtuDisplay.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(flowvtuDisplay, ('POINTS', 'Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(densityLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
flowvtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
flowvtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Pressure'
pressureLUT = GetColorTransferFunction('Pressure')
pressureLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
pressureLUT.InterpretValuesAsCategories = 0
pressureLUT.AnnotationsInitialized = 0
pressureLUT.ShowCategoricalColorsinDataRangeOnly = 0
pressureLUT.RescaleOnVisibilityChange = 0
pressureLUT.EnableOpacityMapping = 0
pressureLUT.RGBPoints = [45163.34765625, 0.0, 0.0, 0.34902, 51996.91882324219, 0.039216, 0.062745, 0.380392, 58830.489990234375, 0.062745, 0.117647, 0.411765, 65664.06115722656, 0.090196, 0.184314, 0.45098, 72497.63232421875, 0.12549, 0.262745, 0.501961, 79331.20349121094, 0.160784, 0.337255, 0.541176, 86164.77465820312, 0.2, 0.396078, 0.568627, 92998.34582519531, 0.239216, 0.454902, 0.6, 99831.9169921875, 0.286275, 0.521569, 0.65098, 106665.48815917969, 0.337255, 0.592157, 0.701961, 113499.05932617188, 0.388235, 0.654902, 0.74902, 120332.63049316406, 0.466667, 0.737255, 0.819608, 127166.20166015625, 0.572549, 0.819608, 0.878431, 133999.77282714844, 0.654902, 0.866667, 0.909804, 140833.34399414062, 0.752941, 0.917647, 0.941176, 147666.9151611328, 0.823529, 0.956863, 0.968627, 154500.486328125, 0.988235, 0.960784, 0.901961, 154500.486328125, 0.941176, 0.984314, 0.988235, 158873.971875, 0.988235, 0.945098, 0.85098, 163247.457421875, 0.980392, 0.898039, 0.784314, 168167.62866210938, 0.968627, 0.835294, 0.698039, 175001.19982910156, 0.94902, 0.733333, 0.588235, 181834.77099609375, 0.929412, 0.65098, 0.509804, 188668.34216308594, 0.909804, 0.564706, 0.435294, 195501.91333007812, 0.878431, 0.458824, 0.352941, 202335.4844970703, 0.839216, 0.388235, 0.286275, 209169.0556640625, 0.760784, 0.294118, 0.211765, 216002.6268310547, 0.701961, 0.211765, 0.168627, 222836.19799804688, 0.65098, 0.156863, 0.129412, 229669.76916503906, 0.6, 0.094118, 0.094118, 236503.34033203125, 0.54902, 0.066667, 0.098039, 243336.91149902344, 0.501961, 0.05098, 0.12549, 250170.48266601562, 0.45098, 0.054902, 0.172549, 257004.0538330078, 0.4, 0.054902, 0.192157, 263837.625, 0.34902, 0.070588, 0.211765]
pressureLUT.UseLogScale = 0
pressureLUT.ColorSpace = 'Lab'
pressureLUT.UseBelowRangeColor = 0
pressureLUT.BelowRangeColor = [0.0, 0.0, 0.0]
pressureLUT.UseAboveRangeColor = 0
pressureLUT.AboveRangeColor = [0.5, 0.5, 0.5]
pressureLUT.NanColor = [0.25, 0.0, 0.0]
pressureLUT.NanOpacity = 1.0
pressureLUT.Discretize = 0
pressureLUT.NumberOfTableValues = 256
pressureLUT.ScalarRangeInitialized = 1.0
pressureLUT.HSVWrap = 0
pressureLUT.VectorComponent = 0
pressureLUT.VectorMode = 'Magnitude'
pressureLUT.AllowDuplicateScalars = 1
pressureLUT.Annotations = []
pressureLUT.ActiveAnnotatedValues = []
pressureLUT.IndexedColors = []
pressureLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'Pressure'
pressurePWF = GetOpacityTransferFunction('Pressure')
pressurePWF.Points = [45163.34765625, 0.0, 0.5, 0.0, 263837.625, 1.0, 0.5, 0.0]
pressurePWF.AllowDuplicateScalars = 1
pressurePWF.UseLogScale = 0
pressurePWF.ScalarRangeInitialized = 1

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.913120986375153, 0.025670067890064548, 546.4101615137755]
renderView1.CameraFocalPoint = [0.913120986375153, 0.025670067890064548, 0.0]
renderView1.CameraParallelScale = 1.2047050751240445

# save screenshot
SaveScreenshot('/home/edo20/CFD2020_Guardone/Homework/DIAMOND_AIRFOIL/CASE0/POST-PROCESSING/Pressure.png', renderView1, ImageResolution=[3050, 1590],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='WhiteBackground',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')