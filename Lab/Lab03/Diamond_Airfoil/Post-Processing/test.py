# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Unstructured Grid Reader'
flow2ndvtu = XMLUnstructuredGridReader(FileName=['/home/edo20/CFD2020_Guardone/Lab/Lab03/Diamond_Airfoil/CFD/flow2nd.vtu'])
flow2ndvtu.CellArrayStatus = []
flow2ndvtu.PointArrayStatus = ['Density', 'Momentum', 'Energy', 'Pressure', 'Temperature', 'Mach', 'Pressure_Coefficient']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1118, 795]

# show data in view
flow2ndvtuDisplay = Show(flow2ndvtu, renderView1)

# trace defaults for the display properties.
flow2ndvtuDisplay.Representation = 'Surface'
flow2ndvtuDisplay.AmbientColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.ColorArrayName = [None, '']
flow2ndvtuDisplay.DiffuseColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.LookupTable = None
flow2ndvtuDisplay.MapScalars = 1
flow2ndvtuDisplay.MultiComponentsMapping = 0
flow2ndvtuDisplay.InterpolateScalarsBeforeMapping = 1
flow2ndvtuDisplay.Opacity = 1.0
flow2ndvtuDisplay.PointSize = 2.0
flow2ndvtuDisplay.LineWidth = 1.0
flow2ndvtuDisplay.RenderLinesAsTubes = 0
flow2ndvtuDisplay.RenderPointsAsSpheres = 0
flow2ndvtuDisplay.Interpolation = 'Gouraud'
flow2ndvtuDisplay.Specular = 0.0
flow2ndvtuDisplay.SpecularColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.SpecularPower = 100.0
flow2ndvtuDisplay.Luminosity = 0.0
flow2ndvtuDisplay.Ambient = 0.0
flow2ndvtuDisplay.Diffuse = 1.0
flow2ndvtuDisplay.EdgeColor = [0.0, 0.0, 0.5]
flow2ndvtuDisplay.BackfaceRepresentation = 'Follow Frontface'
flow2ndvtuDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.BackfaceOpacity = 1.0
flow2ndvtuDisplay.Position = [0.0, 0.0, 0.0]
flow2ndvtuDisplay.Scale = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.Orientation = [0.0, 0.0, 0.0]
flow2ndvtuDisplay.Origin = [0.0, 0.0, 0.0]
flow2ndvtuDisplay.Pickable = 1
flow2ndvtuDisplay.Texture = None
flow2ndvtuDisplay.Triangulate = 0
flow2ndvtuDisplay.UseShaderReplacements = 0
flow2ndvtuDisplay.ShaderReplacements = ''
flow2ndvtuDisplay.NonlinearSubdivisionLevel = 1
flow2ndvtuDisplay.UseDataPartitions = 0
flow2ndvtuDisplay.OSPRayUseScaleArray = 0
flow2ndvtuDisplay.OSPRayScaleArray = 'Density'
flow2ndvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
flow2ndvtuDisplay.OSPRayMaterial = 'None'
flow2ndvtuDisplay.Orient = 0
flow2ndvtuDisplay.OrientationMode = 'Direction'
flow2ndvtuDisplay.SelectOrientationVectors = 'Density'
flow2ndvtuDisplay.Scaling = 0
flow2ndvtuDisplay.ScaleMode = 'No Data Scaling Off'
flow2ndvtuDisplay.ScaleFactor = 20.0
flow2ndvtuDisplay.SelectScaleArray = 'Density'
flow2ndvtuDisplay.GlyphType = 'Arrow'
flow2ndvtuDisplay.UseGlyphTable = 0
flow2ndvtuDisplay.GlyphTableIndexArray = 'Density'
flow2ndvtuDisplay.UseCompositeGlyphTable = 0
flow2ndvtuDisplay.UseGlyphCullingAndLOD = 0
flow2ndvtuDisplay.LODValues = []
flow2ndvtuDisplay.ColorByLODIndex = 0
flow2ndvtuDisplay.GaussianRadius = 1.0
flow2ndvtuDisplay.ShaderPreset = 'Sphere'
flow2ndvtuDisplay.CustomTriangleScale = 3
flow2ndvtuDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
flow2ndvtuDisplay.Emissive = 0
flow2ndvtuDisplay.ScaleByArray = 0
flow2ndvtuDisplay.SetScaleArray = ['POINTS', 'Density']
flow2ndvtuDisplay.ScaleArrayComponent = ''
flow2ndvtuDisplay.UseScaleFunction = 1
flow2ndvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
flow2ndvtuDisplay.OpacityByArray = 0
flow2ndvtuDisplay.OpacityArray = ['POINTS', 'Density']
flow2ndvtuDisplay.OpacityArrayComponent = ''
flow2ndvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
flow2ndvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
flow2ndvtuDisplay.SelectionCellLabelBold = 0
flow2ndvtuDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
flow2ndvtuDisplay.SelectionCellLabelFontFamily = 'Arial'
flow2ndvtuDisplay.SelectionCellLabelFontFile = ''
flow2ndvtuDisplay.SelectionCellLabelFontSize = 18
flow2ndvtuDisplay.SelectionCellLabelItalic = 0
flow2ndvtuDisplay.SelectionCellLabelJustification = 'Left'
flow2ndvtuDisplay.SelectionCellLabelOpacity = 1.0
flow2ndvtuDisplay.SelectionCellLabelShadow = 0
flow2ndvtuDisplay.SelectionPointLabelBold = 0
flow2ndvtuDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
flow2ndvtuDisplay.SelectionPointLabelFontFamily = 'Arial'
flow2ndvtuDisplay.SelectionPointLabelFontFile = ''
flow2ndvtuDisplay.SelectionPointLabelFontSize = 18
flow2ndvtuDisplay.SelectionPointLabelItalic = 0
flow2ndvtuDisplay.SelectionPointLabelJustification = 'Left'
flow2ndvtuDisplay.SelectionPointLabelOpacity = 1.0
flow2ndvtuDisplay.SelectionPointLabelShadow = 0
flow2ndvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
flow2ndvtuDisplay.ScalarOpacityFunction = None
flow2ndvtuDisplay.ScalarOpacityUnitDistance = 10.933163826223883
flow2ndvtuDisplay.ExtractedBlockIndex = 0
flow2ndvtuDisplay.SelectMapper = 'Projected tetra'
flow2ndvtuDisplay.SamplingDimensions = [128, 128, 128]
flow2ndvtuDisplay.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
flow2ndvtuDisplay.OSPRayScaleFunction.Points = [1.5819250345230103, 0.0, 0.5, 0.0, 2.035494327545166, 1.0, 0.5, 0.0]
flow2ndvtuDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
flow2ndvtuDisplay.GlyphType.TipResolution = 6
flow2ndvtuDisplay.GlyphType.TipRadius = 0.1
flow2ndvtuDisplay.GlyphType.TipLength = 0.35
flow2ndvtuDisplay.GlyphType.ShaftResolution = 6
flow2ndvtuDisplay.GlyphType.ShaftRadius = 0.03
flow2ndvtuDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
flow2ndvtuDisplay.ScaleTransferFunction.Points = [0.6519656181335449, 0.0, 0.5, 0.0, 1.6912429332733154, 1.0, 0.5, 0.0]
flow2ndvtuDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
flow2ndvtuDisplay.OpacityTransferFunction.Points = [0.6519656181335449, 0.0, 0.5, 0.0, 1.6912429332733154, 1.0, 0.5, 0.0]
flow2ndvtuDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
flow2ndvtuDisplay.DataAxesGrid.XTitle = 'X Axis'
flow2ndvtuDisplay.DataAxesGrid.YTitle = 'Y Axis'
flow2ndvtuDisplay.DataAxesGrid.ZTitle = 'Z Axis'
flow2ndvtuDisplay.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
flow2ndvtuDisplay.DataAxesGrid.XTitleFontFile = ''
flow2ndvtuDisplay.DataAxesGrid.XTitleBold = 0
flow2ndvtuDisplay.DataAxesGrid.XTitleItalic = 0
flow2ndvtuDisplay.DataAxesGrid.XTitleFontSize = 12
flow2ndvtuDisplay.DataAxesGrid.XTitleShadow = 0
flow2ndvtuDisplay.DataAxesGrid.XTitleOpacity = 1.0
flow2ndvtuDisplay.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
flow2ndvtuDisplay.DataAxesGrid.YTitleFontFile = ''
flow2ndvtuDisplay.DataAxesGrid.YTitleBold = 0
flow2ndvtuDisplay.DataAxesGrid.YTitleItalic = 0
flow2ndvtuDisplay.DataAxesGrid.YTitleFontSize = 12
flow2ndvtuDisplay.DataAxesGrid.YTitleShadow = 0
flow2ndvtuDisplay.DataAxesGrid.YTitleOpacity = 1.0
flow2ndvtuDisplay.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
flow2ndvtuDisplay.DataAxesGrid.ZTitleFontFile = ''
flow2ndvtuDisplay.DataAxesGrid.ZTitleBold = 0
flow2ndvtuDisplay.DataAxesGrid.ZTitleItalic = 0
flow2ndvtuDisplay.DataAxesGrid.ZTitleFontSize = 12
flow2ndvtuDisplay.DataAxesGrid.ZTitleShadow = 0
flow2ndvtuDisplay.DataAxesGrid.ZTitleOpacity = 1.0
flow2ndvtuDisplay.DataAxesGrid.FacesToRender = 63
flow2ndvtuDisplay.DataAxesGrid.CullBackface = 0
flow2ndvtuDisplay.DataAxesGrid.CullFrontface = 1
flow2ndvtuDisplay.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.DataAxesGrid.ShowGrid = 0
flow2ndvtuDisplay.DataAxesGrid.ShowEdges = 1
flow2ndvtuDisplay.DataAxesGrid.ShowTicks = 1
flow2ndvtuDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
flow2ndvtuDisplay.DataAxesGrid.AxesToLabel = 63
flow2ndvtuDisplay.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
flow2ndvtuDisplay.DataAxesGrid.XLabelFontFile = ''
flow2ndvtuDisplay.DataAxesGrid.XLabelBold = 0
flow2ndvtuDisplay.DataAxesGrid.XLabelItalic = 0
flow2ndvtuDisplay.DataAxesGrid.XLabelFontSize = 12
flow2ndvtuDisplay.DataAxesGrid.XLabelShadow = 0
flow2ndvtuDisplay.DataAxesGrid.XLabelOpacity = 1.0
flow2ndvtuDisplay.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
flow2ndvtuDisplay.DataAxesGrid.YLabelFontFile = ''
flow2ndvtuDisplay.DataAxesGrid.YLabelBold = 0
flow2ndvtuDisplay.DataAxesGrid.YLabelItalic = 0
flow2ndvtuDisplay.DataAxesGrid.YLabelFontSize = 12
flow2ndvtuDisplay.DataAxesGrid.YLabelShadow = 0
flow2ndvtuDisplay.DataAxesGrid.YLabelOpacity = 1.0
flow2ndvtuDisplay.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
flow2ndvtuDisplay.DataAxesGrid.ZLabelFontFile = ''
flow2ndvtuDisplay.DataAxesGrid.ZLabelBold = 0
flow2ndvtuDisplay.DataAxesGrid.ZLabelItalic = 0
flow2ndvtuDisplay.DataAxesGrid.ZLabelFontSize = 12
flow2ndvtuDisplay.DataAxesGrid.ZLabelShadow = 0
flow2ndvtuDisplay.DataAxesGrid.ZLabelOpacity = 1.0
flow2ndvtuDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
flow2ndvtuDisplay.DataAxesGrid.XAxisPrecision = 2
flow2ndvtuDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
flow2ndvtuDisplay.DataAxesGrid.XAxisLabels = []
flow2ndvtuDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
flow2ndvtuDisplay.DataAxesGrid.YAxisPrecision = 2
flow2ndvtuDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
flow2ndvtuDisplay.DataAxesGrid.YAxisLabels = []
flow2ndvtuDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
flow2ndvtuDisplay.DataAxesGrid.ZAxisPrecision = 2
flow2ndvtuDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
flow2ndvtuDisplay.DataAxesGrid.ZAxisLabels = []
flow2ndvtuDisplay.DataAxesGrid.UseCustomBounds = 0
flow2ndvtuDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
flow2ndvtuDisplay.PolarAxes.Visibility = 0
flow2ndvtuDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
flow2ndvtuDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
flow2ndvtuDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
flow2ndvtuDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
flow2ndvtuDisplay.PolarAxes.EnableCustomRange = 0
flow2ndvtuDisplay.PolarAxes.CustomRange = [0.0, 1.0]
flow2ndvtuDisplay.PolarAxes.PolarAxisVisibility = 1
flow2ndvtuDisplay.PolarAxes.RadialAxesVisibility = 1
flow2ndvtuDisplay.PolarAxes.DrawRadialGridlines = 1
flow2ndvtuDisplay.PolarAxes.PolarArcsVisibility = 1
flow2ndvtuDisplay.PolarAxes.DrawPolarArcsGridlines = 1
flow2ndvtuDisplay.PolarAxes.NumberOfRadialAxes = 0
flow2ndvtuDisplay.PolarAxes.AutoSubdividePolarAxis = 1
flow2ndvtuDisplay.PolarAxes.NumberOfPolarAxis = 0
flow2ndvtuDisplay.PolarAxes.MinimumRadius = 0.0
flow2ndvtuDisplay.PolarAxes.MinimumAngle = 0.0
flow2ndvtuDisplay.PolarAxes.MaximumAngle = 90.0
flow2ndvtuDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
flow2ndvtuDisplay.PolarAxes.Ratio = 1.0
flow2ndvtuDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.PolarAxes.PolarAxisTitleVisibility = 1
flow2ndvtuDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
flow2ndvtuDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
flow2ndvtuDisplay.PolarAxes.PolarLabelVisibility = 1
flow2ndvtuDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
flow2ndvtuDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
flow2ndvtuDisplay.PolarAxes.RadialLabelVisibility = 1
flow2ndvtuDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
flow2ndvtuDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
flow2ndvtuDisplay.PolarAxes.RadialUnitsVisibility = 1
flow2ndvtuDisplay.PolarAxes.ScreenSize = 10.0
flow2ndvtuDisplay.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
flow2ndvtuDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
flow2ndvtuDisplay.PolarAxes.PolarAxisTitleFontFile = ''
flow2ndvtuDisplay.PolarAxes.PolarAxisTitleBold = 0
flow2ndvtuDisplay.PolarAxes.PolarAxisTitleItalic = 0
flow2ndvtuDisplay.PolarAxes.PolarAxisTitleShadow = 0
flow2ndvtuDisplay.PolarAxes.PolarAxisTitleFontSize = 12
flow2ndvtuDisplay.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
flow2ndvtuDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
flow2ndvtuDisplay.PolarAxes.PolarAxisLabelFontFile = ''
flow2ndvtuDisplay.PolarAxes.PolarAxisLabelBold = 0
flow2ndvtuDisplay.PolarAxes.PolarAxisLabelItalic = 0
flow2ndvtuDisplay.PolarAxes.PolarAxisLabelShadow = 0
flow2ndvtuDisplay.PolarAxes.PolarAxisLabelFontSize = 12
flow2ndvtuDisplay.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
flow2ndvtuDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
flow2ndvtuDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
flow2ndvtuDisplay.PolarAxes.LastRadialAxisTextBold = 0
flow2ndvtuDisplay.PolarAxes.LastRadialAxisTextItalic = 0
flow2ndvtuDisplay.PolarAxes.LastRadialAxisTextShadow = 0
flow2ndvtuDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
flow2ndvtuDisplay.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
flow2ndvtuDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
flow2ndvtuDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
flow2ndvtuDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
flow2ndvtuDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
flow2ndvtuDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
flow2ndvtuDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
flow2ndvtuDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
flow2ndvtuDisplay.PolarAxes.EnableDistanceLOD = 1
flow2ndvtuDisplay.PolarAxes.DistanceLODThreshold = 0.7
flow2ndvtuDisplay.PolarAxes.EnableViewAngleLOD = 1
flow2ndvtuDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
flow2ndvtuDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
flow2ndvtuDisplay.PolarAxes.PolarTicksVisibility = 1
flow2ndvtuDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
flow2ndvtuDisplay.PolarAxes.TickLocation = 'Both'
flow2ndvtuDisplay.PolarAxes.AxisTickVisibility = 1
flow2ndvtuDisplay.PolarAxes.AxisMinorTickVisibility = 0
flow2ndvtuDisplay.PolarAxes.ArcTickVisibility = 1
flow2ndvtuDisplay.PolarAxes.ArcMinorTickVisibility = 0
flow2ndvtuDisplay.PolarAxes.DeltaAngleMajor = 10.0
flow2ndvtuDisplay.PolarAxes.DeltaAngleMinor = 5.0
flow2ndvtuDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
flow2ndvtuDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
flow2ndvtuDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
flow2ndvtuDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
flow2ndvtuDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
flow2ndvtuDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
flow2ndvtuDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
flow2ndvtuDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
flow2ndvtuDisplay.PolarAxes.ArcMajorTickSize = 0.0
flow2ndvtuDisplay.PolarAxes.ArcTickRatioSize = 0.3
flow2ndvtuDisplay.PolarAxes.ArcMajorTickThickness = 1.0
flow2ndvtuDisplay.PolarAxes.ArcTickRatioThickness = 0.5
flow2ndvtuDisplay.PolarAxes.Use2DMode = 0
flow2ndvtuDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 10000.0]

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(flow2ndvtuDisplay, ('POINTS', 'Mach'))

# rescale color and/or opacity maps used to include current data range
flow2ndvtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
flow2ndvtuDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Mach'
machLUT = GetColorTransferFunction('Mach')
machLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
machLUT.InterpretValuesAsCategories = 0
machLUT.AnnotationsInitialized = 0
machLUT.ShowCategoricalColorsinDataRangeOnly = 0
machLUT.RescaleOnVisibilityChange = 0
machLUT.EnableOpacityMapping = 0
machLUT.RGBPoints = [1.109570026397705, 0.231373, 0.298039, 0.752941, 1.6111890077590942, 0.865003, 0.865003, 0.865003, 2.1128079891204834, 0.705882, 0.0156863, 0.14902]
machLUT.UseLogScale = 0
machLUT.ColorSpace = 'Diverging'
machLUT.UseBelowRangeColor = 0
machLUT.BelowRangeColor = [0.0, 0.0, 0.0]
machLUT.UseAboveRangeColor = 0
machLUT.AboveRangeColor = [0.5, 0.5, 0.5]
machLUT.NanColor = [1.0, 1.0, 0.0]
machLUT.NanOpacity = 1.0
machLUT.Discretize = 1
machLUT.NumberOfTableValues = 256
machLUT.ScalarRangeInitialized = 1.0
machLUT.HSVWrap = 0
machLUT.VectorComponent = 0
machLUT.VectorMode = 'Magnitude'
machLUT.AllowDuplicateScalars = 1
machLUT.Annotations = []
machLUT.ActiveAnnotatedValues = []
machLUT.IndexedColors = []
machLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'Mach'
machPWF = GetOpacityTransferFunction('Mach')
machPWF.Points = [1.109570026397705, 0.0, 0.5, 0.0, 2.1128079891204834, 1.0, 0.5, 0.0]
machPWF.AllowDuplicateScalars = 1
machPWF.UseLogScale = 0
machPWF.ScalarRangeInitialized = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
machLUT.ApplyPreset('jet', True)

# create a new 'Contour'
contour1 = Contour(Input=flow2ndvtu)
contour1.ContourBy = ['POINTS', 'Density']
contour1.ComputeNormals = 1
contour1.ComputeGradients = 0
contour1.ComputeScalars = 1
contour1.OutputPointsPrecision = 'Same as input'
contour1.GenerateTriangles = 1
contour1.Isosurfaces = [1.1716042757034302]
contour1.PointMergeMethod = 'Uniform Binning'

# init the 'Uniform Binning' selected for 'PointMergeMethod'
contour1.PointMergeMethod.Divisions = [50, 50, 50]
contour1.PointMergeMethod.Numberofpointsperbucket = 8

# Properties modified on contour1
contour1.ContourBy = ['POINTS', 'Mach']
contour1.Isosurfaces = [1.1716042757034302, 1.109570026397705, 1.2210409111446803, 1.332511795891656, 1.4439826806386313, 1.5554535653856065, 1.666924450132582, 1.7783953348795571, 1.8898662196265326, 2.001337104373508, 2.1128079891204834]

# show data in view
contour1Display = Show(contour1, renderView1)

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.AmbientColor = [1.0, 1.0, 1.0]
contour1Display.ColorArrayName = ['POINTS', 'Mach']
contour1Display.DiffuseColor = [1.0, 1.0, 1.0]
contour1Display.LookupTable = machLUT
contour1Display.MapScalars = 1
contour1Display.MultiComponentsMapping = 0
contour1Display.InterpolateScalarsBeforeMapping = 1
contour1Display.Opacity = 1.0
contour1Display.PointSize = 2.0
contour1Display.LineWidth = 1.0
contour1Display.RenderLinesAsTubes = 0
contour1Display.RenderPointsAsSpheres = 0
contour1Display.Interpolation = 'Gouraud'
contour1Display.Specular = 0.0
contour1Display.SpecularColor = [1.0, 1.0, 1.0]
contour1Display.SpecularPower = 100.0
contour1Display.Luminosity = 0.0
contour1Display.Ambient = 0.0
contour1Display.Diffuse = 1.0
contour1Display.EdgeColor = [0.0, 0.0, 0.5]
contour1Display.BackfaceRepresentation = 'Follow Frontface'
contour1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
contour1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
contour1Display.BackfaceOpacity = 1.0
contour1Display.Position = [0.0, 0.0, 0.0]
contour1Display.Scale = [1.0, 1.0, 1.0]
contour1Display.Orientation = [0.0, 0.0, 0.0]
contour1Display.Origin = [0.0, 0.0, 0.0]
contour1Display.Pickable = 1
contour1Display.Texture = None
contour1Display.Triangulate = 0
contour1Display.UseShaderReplacements = 0
contour1Display.ShaderReplacements = ''
contour1Display.NonlinearSubdivisionLevel = 1
contour1Display.UseDataPartitions = 0
contour1Display.OSPRayUseScaleArray = 0
contour1Display.OSPRayScaleArray = 'Mach'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.OSPRayMaterial = 'None'
contour1Display.Orient = 0
contour1Display.OrientationMode = 'Direction'
contour1Display.SelectOrientationVectors = 'Density'
contour1Display.Scaling = 0
contour1Display.ScaleMode = 'No Data Scaling Off'
contour1Display.ScaleFactor = 0.412397163361311
contour1Display.SelectScaleArray = 'Mach'
contour1Display.GlyphType = 'Arrow'
contour1Display.UseGlyphTable = 0
contour1Display.GlyphTableIndexArray = 'Mach'
contour1Display.UseCompositeGlyphTable = 0
contour1Display.UseGlyphCullingAndLOD = 0
contour1Display.LODValues = []
contour1Display.ColorByLODIndex = 0
contour1Display.GaussianRadius = 0.02061985816806555
contour1Display.ShaderPreset = 'Sphere'
contour1Display.CustomTriangleScale = 3
contour1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
contour1Display.Emissive = 0
contour1Display.ScaleByArray = 0
contour1Display.SetScaleArray = ['POINTS', 'Mach']
contour1Display.ScaleArrayComponent = ''
contour1Display.UseScaleFunction = 1
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityByArray = 0
contour1Display.OpacityArray = ['POINTS', 'Mach']
contour1Display.OpacityArrayComponent = ''
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.SelectionCellLabelBold = 0
contour1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
contour1Display.SelectionCellLabelFontFamily = 'Arial'
contour1Display.SelectionCellLabelFontFile = ''
contour1Display.SelectionCellLabelFontSize = 18
contour1Display.SelectionCellLabelItalic = 0
contour1Display.SelectionCellLabelJustification = 'Left'
contour1Display.SelectionCellLabelOpacity = 1.0
contour1Display.SelectionCellLabelShadow = 0
contour1Display.SelectionPointLabelBold = 0
contour1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
contour1Display.SelectionPointLabelFontFamily = 'Arial'
contour1Display.SelectionPointLabelFontFile = ''
contour1Display.SelectionPointLabelFontSize = 18
contour1Display.SelectionPointLabelItalic = 0
contour1Display.SelectionPointLabelJustification = 'Left'
contour1Display.SelectionPointLabelOpacity = 1.0
contour1Display.SelectionPointLabelShadow = 0
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display.OSPRayScaleFunction.Points = [1.5819250345230103, 0.0, 0.5, 0.0, 2.035494327545166, 1.0, 0.5, 0.0]
contour1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
contour1Display.GlyphType.TipResolution = 6
contour1Display.GlyphType.TipRadius = 0.1
contour1Display.GlyphType.TipLength = 0.35
contour1Display.GlyphType.ShaftResolution = 6
contour1Display.GlyphType.ShaftRadius = 0.03
contour1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [1.1716042757034302, 0.0, 0.5, 0.0, 2.1128079891204834, 1.0, 0.5, 0.0]
contour1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [1.1716042757034302, 0.0, 0.5, 0.0, 2.1128079891204834, 1.0, 0.5, 0.0]
contour1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
contour1Display.DataAxesGrid.XTitle = 'X Axis'
contour1Display.DataAxesGrid.YTitle = 'Y Axis'
contour1Display.DataAxesGrid.ZTitle = 'Z Axis'
contour1Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
contour1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
contour1Display.DataAxesGrid.XTitleFontFile = ''
contour1Display.DataAxesGrid.XTitleBold = 0
contour1Display.DataAxesGrid.XTitleItalic = 0
contour1Display.DataAxesGrid.XTitleFontSize = 12
contour1Display.DataAxesGrid.XTitleShadow = 0
contour1Display.DataAxesGrid.XTitleOpacity = 1.0
contour1Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
contour1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
contour1Display.DataAxesGrid.YTitleFontFile = ''
contour1Display.DataAxesGrid.YTitleBold = 0
contour1Display.DataAxesGrid.YTitleItalic = 0
contour1Display.DataAxesGrid.YTitleFontSize = 12
contour1Display.DataAxesGrid.YTitleShadow = 0
contour1Display.DataAxesGrid.YTitleOpacity = 1.0
contour1Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
contour1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
contour1Display.DataAxesGrid.ZTitleFontFile = ''
contour1Display.DataAxesGrid.ZTitleBold = 0
contour1Display.DataAxesGrid.ZTitleItalic = 0
contour1Display.DataAxesGrid.ZTitleFontSize = 12
contour1Display.DataAxesGrid.ZTitleShadow = 0
contour1Display.DataAxesGrid.ZTitleOpacity = 1.0
contour1Display.DataAxesGrid.FacesToRender = 63
contour1Display.DataAxesGrid.CullBackface = 0
contour1Display.DataAxesGrid.CullFrontface = 1
contour1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
contour1Display.DataAxesGrid.ShowGrid = 0
contour1Display.DataAxesGrid.ShowEdges = 1
contour1Display.DataAxesGrid.ShowTicks = 1
contour1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
contour1Display.DataAxesGrid.AxesToLabel = 63
contour1Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
contour1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
contour1Display.DataAxesGrid.XLabelFontFile = ''
contour1Display.DataAxesGrid.XLabelBold = 0
contour1Display.DataAxesGrid.XLabelItalic = 0
contour1Display.DataAxesGrid.XLabelFontSize = 12
contour1Display.DataAxesGrid.XLabelShadow = 0
contour1Display.DataAxesGrid.XLabelOpacity = 1.0
contour1Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
contour1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
contour1Display.DataAxesGrid.YLabelFontFile = ''
contour1Display.DataAxesGrid.YLabelBold = 0
contour1Display.DataAxesGrid.YLabelItalic = 0
contour1Display.DataAxesGrid.YLabelFontSize = 12
contour1Display.DataAxesGrid.YLabelShadow = 0
contour1Display.DataAxesGrid.YLabelOpacity = 1.0
contour1Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
contour1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
contour1Display.DataAxesGrid.ZLabelFontFile = ''
contour1Display.DataAxesGrid.ZLabelBold = 0
contour1Display.DataAxesGrid.ZLabelItalic = 0
contour1Display.DataAxesGrid.ZLabelFontSize = 12
contour1Display.DataAxesGrid.ZLabelShadow = 0
contour1Display.DataAxesGrid.ZLabelOpacity = 1.0
contour1Display.DataAxesGrid.XAxisNotation = 'Mixed'
contour1Display.DataAxesGrid.XAxisPrecision = 2
contour1Display.DataAxesGrid.XAxisUseCustomLabels = 0
contour1Display.DataAxesGrid.XAxisLabels = []
contour1Display.DataAxesGrid.YAxisNotation = 'Mixed'
contour1Display.DataAxesGrid.YAxisPrecision = 2
contour1Display.DataAxesGrid.YAxisUseCustomLabels = 0
contour1Display.DataAxesGrid.YAxisLabels = []
contour1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
contour1Display.DataAxesGrid.ZAxisPrecision = 2
contour1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
contour1Display.DataAxesGrid.ZAxisLabels = []
contour1Display.DataAxesGrid.UseCustomBounds = 0
contour1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
contour1Display.PolarAxes.Visibility = 0
contour1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
contour1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
contour1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
contour1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
contour1Display.PolarAxes.EnableCustomRange = 0
contour1Display.PolarAxes.CustomRange = [0.0, 1.0]
contour1Display.PolarAxes.PolarAxisVisibility = 1
contour1Display.PolarAxes.RadialAxesVisibility = 1
contour1Display.PolarAxes.DrawRadialGridlines = 1
contour1Display.PolarAxes.PolarArcsVisibility = 1
contour1Display.PolarAxes.DrawPolarArcsGridlines = 1
contour1Display.PolarAxes.NumberOfRadialAxes = 0
contour1Display.PolarAxes.AutoSubdividePolarAxis = 1
contour1Display.PolarAxes.NumberOfPolarAxis = 0
contour1Display.PolarAxes.MinimumRadius = 0.0
contour1Display.PolarAxes.MinimumAngle = 0.0
contour1Display.PolarAxes.MaximumAngle = 90.0
contour1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
contour1Display.PolarAxes.Ratio = 1.0
contour1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.PolarAxisTitleVisibility = 1
contour1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
contour1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
contour1Display.PolarAxes.PolarLabelVisibility = 1
contour1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
contour1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
contour1Display.PolarAxes.RadialLabelVisibility = 1
contour1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
contour1Display.PolarAxes.RadialLabelLocation = 'Bottom'
contour1Display.PolarAxes.RadialUnitsVisibility = 1
contour1Display.PolarAxes.ScreenSize = 10.0
contour1Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
contour1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
contour1Display.PolarAxes.PolarAxisTitleFontFile = ''
contour1Display.PolarAxes.PolarAxisTitleBold = 0
contour1Display.PolarAxes.PolarAxisTitleItalic = 0
contour1Display.PolarAxes.PolarAxisTitleShadow = 0
contour1Display.PolarAxes.PolarAxisTitleFontSize = 12
contour1Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
contour1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
contour1Display.PolarAxes.PolarAxisLabelFontFile = ''
contour1Display.PolarAxes.PolarAxisLabelBold = 0
contour1Display.PolarAxes.PolarAxisLabelItalic = 0
contour1Display.PolarAxes.PolarAxisLabelShadow = 0
contour1Display.PolarAxes.PolarAxisLabelFontSize = 12
contour1Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
contour1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
contour1Display.PolarAxes.LastRadialAxisTextFontFile = ''
contour1Display.PolarAxes.LastRadialAxisTextBold = 0
contour1Display.PolarAxes.LastRadialAxisTextItalic = 0
contour1Display.PolarAxes.LastRadialAxisTextShadow = 0
contour1Display.PolarAxes.LastRadialAxisTextFontSize = 12
contour1Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
contour1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
contour1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
contour1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
contour1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
contour1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
contour1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
contour1Display.PolarAxes.EnableDistanceLOD = 1
contour1Display.PolarAxes.DistanceLODThreshold = 0.7
contour1Display.PolarAxes.EnableViewAngleLOD = 1
contour1Display.PolarAxes.ViewAngleLODThreshold = 0.7
contour1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
contour1Display.PolarAxes.PolarTicksVisibility = 1
contour1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
contour1Display.PolarAxes.TickLocation = 'Both'
contour1Display.PolarAxes.AxisTickVisibility = 1
contour1Display.PolarAxes.AxisMinorTickVisibility = 0
contour1Display.PolarAxes.ArcTickVisibility = 1
contour1Display.PolarAxes.ArcMinorTickVisibility = 0
contour1Display.PolarAxes.DeltaAngleMajor = 10.0
contour1Display.PolarAxes.DeltaAngleMinor = 5.0
contour1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
contour1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
contour1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
contour1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
contour1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
contour1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
contour1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
contour1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
contour1Display.PolarAxes.ArcMajorTickSize = 0.0
contour1Display.PolarAxes.ArcTickRatioSize = 0.3
contour1Display.PolarAxes.ArcMajorTickThickness = 1.0
contour1Display.PolarAxes.ArcTickRatioThickness = 0.5
contour1Display.PolarAxes.Use2DMode = 0
contour1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(flow2ndvtu, renderView1)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(flow2ndvtu)

# show data in view
flow2ndvtuDisplay = Show(flow2ndvtu, renderView1)

# show color bar/color legend
flow2ndvtuDisplay.SetScalarBarVisibility(renderView1, True)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.9399829755251181, 0.057912975143308815, 10000.0]
renderView1.CameraFocalPoint = [0.9399829755251181, 0.057912975143308815, 0.0]
renderView1.CameraParallelScale = 0.9956240290281356

# save screenshot
SaveScreenshot('/home/edo20/CFD2020_Guardone/Lab/Lab03/Diamond_Airfoil/Post-Processing/Mach.png', renderView1, ImageResolution=[12112, 6360],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='BlackBackground',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='0')

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=flow2ndvtu,
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
plotOverLine1Display.ColorArrayName = ['POINTS', 'Mach']
plotOverLine1Display.DiffuseColor = [1.0, 1.0, 1.0]
plotOverLine1Display.LookupTable = machLUT
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
plotOverLine1Display.OSPRayScaleArray = 'Density'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.OSPRayMaterial = 'None'
plotOverLine1Display.Orient = 0
plotOverLine1Display.OrientationMode = 'Direction'
plotOverLine1Display.SelectOrientationVectors = 'Density'
plotOverLine1Display.Scaling = 0
plotOverLine1Display.ScaleMode = 'No Data Scaling Off'
plotOverLine1Display.ScaleFactor = 0.3200000002980232
plotOverLine1Display.SelectScaleArray = 'Density'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.UseGlyphTable = 0
plotOverLine1Display.GlyphTableIndexArray = 'Density'
plotOverLine1Display.UseCompositeGlyphTable = 0
plotOverLine1Display.UseGlyphCullingAndLOD = 0
plotOverLine1Display.LODValues = []
plotOverLine1Display.ColorByLODIndex = 0
plotOverLine1Display.GaussianRadius = 0.01600000001490116
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
plotOverLine1Display.SetScaleArray = ['POINTS', 'Density']
plotOverLine1Display.ScaleArrayComponent = ''
plotOverLine1Display.UseScaleFunction = 1
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityByArray = 0
plotOverLine1Display.OpacityArray = ['POINTS', 'Density']
plotOverLine1Display.OpacityArrayComponent = ''
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
plotOverLine1Display.OSPRayScaleFunction.Points = [1.5819250345230103, 0.0, 0.5, 0.0, 2.035494327545166, 1.0, 0.5, 0.0]
plotOverLine1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
plotOverLine1Display.GlyphType.TipResolution = 6
plotOverLine1Display.GlyphType.TipRadius = 0.1
plotOverLine1Display.GlyphType.TipLength = 0.35
plotOverLine1Display.GlyphType.ShaftResolution = 6
plotOverLine1Display.GlyphType.ShaftRadius = 0.03
plotOverLine1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display.ScaleTransferFunction.Points = [0.8552923798561096, 0.0, 0.5, 0.0, 1.6738836765289307, 1.0, 0.5, 0.0]
plotOverLine1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display.OpacityTransferFunction.Points = [0.8552923798561096, 0.0, 0.5, 0.0, 1.6738836765289307, 1.0, 0.5, 0.0]
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
plotOverLine1Display_1.SeriesVisibility = ['Density', 'Energy', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'Density', 'Density', 'Energy', 'Energy', 'Mach', 'Mach', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', 'Pressure', 'Pressure', 'Pressure_Coefficient', 'Pressure_Coefficient', 'Temperature', 'Temperature', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'Density', '0.89', '0.1', '0.11', 'Energy', '0.22', '0.49', '0.72', 'Mach', '0.3', '0.69', '0.29', 'Momentum_X', '0.6', '0.31', '0.64', 'Momentum_Y', '1', '0.5', '0', 'Momentum_Z', '0.65', '0.34', '0.16', 'Momentum_Magnitude', '0', '0', '0', 'Pressure', '0.89', '0.1', '0.11', 'Pressure_Coefficient', '0.22', '0.49', '0.72', 'Temperature', '0.3', '0.69', '0.29', 'vtkValidPointMask', '0.6', '0.31', '0.64', 'Points_X', '1', '0.5', '0', 'Points_Y', '0.65', '0.34', '0.16', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.89', '0.1', '0.11']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'Density', '1', 'Energy', '1', 'Mach', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Momentum_Magnitude', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'Density', '2', 'Energy', '2', 'Mach', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Momentum_Magnitude', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
lineChartView1.Update()

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

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.AttributeType = 'Cell Data'

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '1', 'Temperature', '0', 'arc_length', '0', 'vtkValidPointMask', '0']

# Properties modified on lineChartView1
lineChartView1.LeftAxisUseCustomRange = 0

# Properties modified on lineChartView1
lineChartView1.LeftAxisUseCustomRange = 1

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = []

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['Mach']

# Properties modified on lineChartView1
lineChartView1.LeftAxisLogScale = 1

# Properties modified on lineChartView1
lineChartView1.LeftAxisUseCustomRange = 0

# Properties modified on lineChartView1
lineChartView1.LeftAxisUseCustomRange = 1

# Properties modified on lineChartView1
lineChartView1.LeftAxisLogScale = 0

# Properties modified on lineChartView1
lineChartView1.LeftAxisRangeMaximum = 1.0

# Properties modified on lineChartView1
lineChartView1.LeftAxisRangeMaximum = 2.0

# set active source
SetActiveSource(flow2ndvtu)

# hide data in view
Hide(plotOverLine1, lineChartView1)

# hide data in view
Hide(plotOverLine1, renderView1)

# show data in view
flow2ndvtuDisplay = Show(flow2ndvtu, renderView1)

# show color bar/color legend
flow2ndvtuDisplay.SetScalarBarVisibility(renderView1, True)

# destroy plotOverLine1
Delete(plotOverLine1)
del plotOverLine1

# set active source
SetActiveSource(flow2ndvtu)

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=flow2ndvtu,
    Source='High Resolution Line Source')
plotOverLine1.PassPartialArrays = 1
plotOverLine1.ComputeTolerance = 1
plotOverLine1.Tolerance = 2.220446049250313e-16

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine1.Source.Point1 = [-100.0, -100.0, 0.0]
plotOverLine1.Source.Point2 = [100.0, 100.0, 0.0]
plotOverLine1.Source.Resolution = 1000

# show data in view
plotOverLine1Display = Show(plotOverLine1, lineChartView1)

# trace defaults for the display properties.
plotOverLine1Display.CompositeDataSetIndex = [0]
plotOverLine1Display.AttributeType = 'Point Data'
plotOverLine1Display.UseIndexForXAxis = 0
plotOverLine1Display.XArrayName = 'arc_length'
plotOverLine1Display.SeriesVisibility = ['Density', 'Energy', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']
plotOverLine1Display.SeriesLabel = ['arc_length', 'arc_length', 'Density', 'Density', 'Energy', 'Energy', 'Mach', 'Mach', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', 'Pressure', 'Pressure', 'Pressure_Coefficient', 'Pressure_Coefficient', 'Temperature', 'Temperature', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display.SeriesColor = ['arc_length', '0', '0', '0', 'Density', '0.89', '0.1', '0.11', 'Energy', '0.22', '0.49', '0.72', 'Mach', '0.3', '0.69', '0.29', 'Momentum_X', '0.6', '0.31', '0.64', 'Momentum_Y', '1', '0.5', '0', 'Momentum_Z', '0.65', '0.34', '0.16', 'Momentum_Magnitude', '0', '0', '0', 'Pressure', '0.89', '0.1', '0.11', 'Pressure_Coefficient', '0.22', '0.49', '0.72', 'Temperature', '0.3', '0.69', '0.29', 'vtkValidPointMask', '0.6', '0.31', '0.64', 'Points_X', '1', '0.5', '0', 'Points_Y', '0.65', '0.34', '0.16', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.89', '0.1', '0.11']
plotOverLine1Display.SeriesPlotCorner = ['arc_length', '0', 'Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display.SeriesLabelPrefix = ''
plotOverLine1Display.SeriesLineStyle = ['arc_length', '1', 'Density', '1', 'Energy', '1', 'Mach', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Momentum_Magnitude', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display.SeriesLineThickness = ['arc_length', '2', 'Density', '2', 'Energy', '2', 'Mach', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Momentum_Magnitude', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display.SeriesMarkerStyle = ['arc_length', '0', 'Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# update the view to ensure updated data information
lineChartView1.Update()

# update the view to ensure updated data information
lineChartView1.Update()

# Properties modified on plotOverLine1Display
plotOverLine1Display.SeriesVisibility = []
plotOverLine1Display.SeriesColor = ['arc_length', '0', '0', '0', 'Density', '0.889998', '0.100008', '0.110002', 'Energy', '0.220005', '0.489998', '0.719997', 'Mach', '0.300008', '0.689998', '0.289998', 'Momentum_X', '0.6', '0.310002', '0.639994', 'Momentum_Y', '1', '0.500008', '0', 'Momentum_Z', '0.650004', '0.340002', '0.160006', 'Momentum_Magnitude', '0', '0', '0', 'Pressure', '0.889998', '0.100008', '0.110002', 'Pressure_Coefficient', '0.220005', '0.489998', '0.719997', 'Temperature', '0.300008', '0.689998', '0.289998', 'vtkValidPointMask', '0.6', '0.310002', '0.639994', 'Points_X', '1', '0.500008', '0', 'Points_Y', '0.650004', '0.340002', '0.160006', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.889998', '0.100008', '0.110002']
plotOverLine1Display.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'arc_length', '0', 'vtkValidPointMask', '0']
plotOverLine1Display.SeriesLineStyle = ['Density', '1', 'Energy', '1', 'Mach', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1', 'arc_length', '1', 'vtkValidPointMask', '1']
plotOverLine1Display.SeriesLineThickness = ['Density', '2', 'Energy', '2', 'Mach', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2', 'arc_length', '2', 'vtkValidPointMask', '2']
plotOverLine1Display.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'arc_length', '0', 'vtkValidPointMask', '0']

# Properties modified on plotOverLine1Display
plotOverLine1Display.SeriesVisibility = ['Mach']

# update the view to ensure updated data information
lineChartView1.Update()

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(plotOverLine1)

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, renderView1)

# trace defaults for the display properties.
plotOverLine1Display_1.Representation = 'Surface'
plotOverLine1Display_1.AmbientColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.ColorArrayName = ['POINTS', 'Mach']
plotOverLine1Display_1.DiffuseColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.LookupTable = machLUT
plotOverLine1Display_1.MapScalars = 1
plotOverLine1Display_1.MultiComponentsMapping = 0
plotOverLine1Display_1.InterpolateScalarsBeforeMapping = 1
plotOverLine1Display_1.Opacity = 1.0
plotOverLine1Display_1.PointSize = 2.0
plotOverLine1Display_1.LineWidth = 1.0
plotOverLine1Display_1.RenderLinesAsTubes = 0
plotOverLine1Display_1.RenderPointsAsSpheres = 0
plotOverLine1Display_1.Interpolation = 'Gouraud'
plotOverLine1Display_1.Specular = 0.0
plotOverLine1Display_1.SpecularColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.SpecularPower = 100.0
plotOverLine1Display_1.Luminosity = 0.0
plotOverLine1Display_1.Ambient = 0.0
plotOverLine1Display_1.Diffuse = 1.0
plotOverLine1Display_1.EdgeColor = [0.0, 0.0, 0.5]
plotOverLine1Display_1.BackfaceRepresentation = 'Follow Frontface'
plotOverLine1Display_1.BackfaceAmbientColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.BackfaceOpacity = 1.0
plotOverLine1Display_1.Position = [0.0, 0.0, 0.0]
plotOverLine1Display_1.Scale = [1.0, 1.0, 1.0]
plotOverLine1Display_1.Orientation = [0.0, 0.0, 0.0]
plotOverLine1Display_1.Origin = [0.0, 0.0, 0.0]
plotOverLine1Display_1.Pickable = 1
plotOverLine1Display_1.Texture = None
plotOverLine1Display_1.Triangulate = 0
plotOverLine1Display_1.UseShaderReplacements = 0
plotOverLine1Display_1.ShaderReplacements = ''
plotOverLine1Display_1.NonlinearSubdivisionLevel = 1
plotOverLine1Display_1.UseDataPartitions = 0
plotOverLine1Display_1.OSPRayUseScaleArray = 0
plotOverLine1Display_1.OSPRayScaleArray = 'Density'
plotOverLine1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display_1.OSPRayMaterial = 'None'
plotOverLine1Display_1.Orient = 0
plotOverLine1Display_1.OrientationMode = 'Direction'
plotOverLine1Display_1.SelectOrientationVectors = 'Density'
plotOverLine1Display_1.Scaling = 0
plotOverLine1Display_1.ScaleMode = 'No Data Scaling Off'
plotOverLine1Display_1.ScaleFactor = 0.27000000029802323
plotOverLine1Display_1.SelectScaleArray = 'Density'
plotOverLine1Display_1.GlyphType = 'Arrow'
plotOverLine1Display_1.UseGlyphTable = 0
plotOverLine1Display_1.GlyphTableIndexArray = 'Density'
plotOverLine1Display_1.UseCompositeGlyphTable = 0
plotOverLine1Display_1.UseGlyphCullingAndLOD = 0
plotOverLine1Display_1.LODValues = []
plotOverLine1Display_1.ColorByLODIndex = 0
plotOverLine1Display_1.GaussianRadius = 0.013500000014901162
plotOverLine1Display_1.ShaderPreset = 'Sphere'
plotOverLine1Display_1.CustomTriangleScale = 3
plotOverLine1Display_1.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
plotOverLine1Display_1.Emissive = 0
plotOverLine1Display_1.ScaleByArray = 0
plotOverLine1Display_1.SetScaleArray = ['POINTS', 'Density']
plotOverLine1Display_1.ScaleArrayComponent = ''
plotOverLine1Display_1.UseScaleFunction = 1
plotOverLine1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display_1.OpacityByArray = 0
plotOverLine1Display_1.OpacityArray = ['POINTS', 'Density']
plotOverLine1Display_1.OpacityArrayComponent = ''
plotOverLine1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display_1.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display_1.SelectionCellLabelBold = 0
plotOverLine1Display_1.SelectionCellLabelColor = [0.0, 1.0, 0.0]
plotOverLine1Display_1.SelectionCellLabelFontFamily = 'Arial'
plotOverLine1Display_1.SelectionCellLabelFontFile = ''
plotOverLine1Display_1.SelectionCellLabelFontSize = 18
plotOverLine1Display_1.SelectionCellLabelItalic = 0
plotOverLine1Display_1.SelectionCellLabelJustification = 'Left'
plotOverLine1Display_1.SelectionCellLabelOpacity = 1.0
plotOverLine1Display_1.SelectionCellLabelShadow = 0
plotOverLine1Display_1.SelectionPointLabelBold = 0
plotOverLine1Display_1.SelectionPointLabelColor = [1.0, 1.0, 0.0]
plotOverLine1Display_1.SelectionPointLabelFontFamily = 'Arial'
plotOverLine1Display_1.SelectionPointLabelFontFile = ''
plotOverLine1Display_1.SelectionPointLabelFontSize = 18
plotOverLine1Display_1.SelectionPointLabelItalic = 0
plotOverLine1Display_1.SelectionPointLabelJustification = 'Left'
plotOverLine1Display_1.SelectionPointLabelOpacity = 1.0
plotOverLine1Display_1.SelectionPointLabelShadow = 0
plotOverLine1Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
plotOverLine1Display_1.OSPRayScaleFunction.Points = [1.5819250345230103, 0.0, 0.5, 0.0, 2.035494327545166, 1.0, 0.5, 0.0]
plotOverLine1Display_1.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
plotOverLine1Display_1.GlyphType.TipResolution = 6
plotOverLine1Display_1.GlyphType.TipRadius = 0.1
plotOverLine1Display_1.GlyphType.TipLength = 0.35
plotOverLine1Display_1.GlyphType.ShaftResolution = 6
plotOverLine1Display_1.GlyphType.ShaftRadius = 0.03
plotOverLine1Display_1.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display_1.ScaleTransferFunction.Points = [0.9047207832336426, 0.0, 0.5, 0.0, 1.648597240447998, 1.0, 0.5, 0.0]
plotOverLine1Display_1.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display_1.OpacityTransferFunction.Points = [0.9047207832336426, 0.0, 0.5, 0.0, 1.648597240447998, 1.0, 0.5, 0.0]
plotOverLine1Display_1.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
plotOverLine1Display_1.DataAxesGrid.XTitle = 'X Axis'
plotOverLine1Display_1.DataAxesGrid.YTitle = 'Y Axis'
plotOverLine1Display_1.DataAxesGrid.ZTitle = 'Z Axis'
plotOverLine1Display_1.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.DataAxesGrid.XTitleFontFamily = 'Arial'
plotOverLine1Display_1.DataAxesGrid.XTitleFontFile = ''
plotOverLine1Display_1.DataAxesGrid.XTitleBold = 0
plotOverLine1Display_1.DataAxesGrid.XTitleItalic = 0
plotOverLine1Display_1.DataAxesGrid.XTitleFontSize = 12
plotOverLine1Display_1.DataAxesGrid.XTitleShadow = 0
plotOverLine1Display_1.DataAxesGrid.XTitleOpacity = 1.0
plotOverLine1Display_1.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.DataAxesGrid.YTitleFontFamily = 'Arial'
plotOverLine1Display_1.DataAxesGrid.YTitleFontFile = ''
plotOverLine1Display_1.DataAxesGrid.YTitleBold = 0
plotOverLine1Display_1.DataAxesGrid.YTitleItalic = 0
plotOverLine1Display_1.DataAxesGrid.YTitleFontSize = 12
plotOverLine1Display_1.DataAxesGrid.YTitleShadow = 0
plotOverLine1Display_1.DataAxesGrid.YTitleOpacity = 1.0
plotOverLine1Display_1.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.DataAxesGrid.ZTitleFontFamily = 'Arial'
plotOverLine1Display_1.DataAxesGrid.ZTitleFontFile = ''
plotOverLine1Display_1.DataAxesGrid.ZTitleBold = 0
plotOverLine1Display_1.DataAxesGrid.ZTitleItalic = 0
plotOverLine1Display_1.DataAxesGrid.ZTitleFontSize = 12
plotOverLine1Display_1.DataAxesGrid.ZTitleShadow = 0
plotOverLine1Display_1.DataAxesGrid.ZTitleOpacity = 1.0
plotOverLine1Display_1.DataAxesGrid.FacesToRender = 63
plotOverLine1Display_1.DataAxesGrid.CullBackface = 0
plotOverLine1Display_1.DataAxesGrid.CullFrontface = 1
plotOverLine1Display_1.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.DataAxesGrid.ShowGrid = 0
plotOverLine1Display_1.DataAxesGrid.ShowEdges = 1
plotOverLine1Display_1.DataAxesGrid.ShowTicks = 1
plotOverLine1Display_1.DataAxesGrid.LabelUniqueEdgesOnly = 1
plotOverLine1Display_1.DataAxesGrid.AxesToLabel = 63
plotOverLine1Display_1.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.DataAxesGrid.XLabelFontFamily = 'Arial'
plotOverLine1Display_1.DataAxesGrid.XLabelFontFile = ''
plotOverLine1Display_1.DataAxesGrid.XLabelBold = 0
plotOverLine1Display_1.DataAxesGrid.XLabelItalic = 0
plotOverLine1Display_1.DataAxesGrid.XLabelFontSize = 12
plotOverLine1Display_1.DataAxesGrid.XLabelShadow = 0
plotOverLine1Display_1.DataAxesGrid.XLabelOpacity = 1.0
plotOverLine1Display_1.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.DataAxesGrid.YLabelFontFamily = 'Arial'
plotOverLine1Display_1.DataAxesGrid.YLabelFontFile = ''
plotOverLine1Display_1.DataAxesGrid.YLabelBold = 0
plotOverLine1Display_1.DataAxesGrid.YLabelItalic = 0
plotOverLine1Display_1.DataAxesGrid.YLabelFontSize = 12
plotOverLine1Display_1.DataAxesGrid.YLabelShadow = 0
plotOverLine1Display_1.DataAxesGrid.YLabelOpacity = 1.0
plotOverLine1Display_1.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.DataAxesGrid.ZLabelFontFamily = 'Arial'
plotOverLine1Display_1.DataAxesGrid.ZLabelFontFile = ''
plotOverLine1Display_1.DataAxesGrid.ZLabelBold = 0
plotOverLine1Display_1.DataAxesGrid.ZLabelItalic = 0
plotOverLine1Display_1.DataAxesGrid.ZLabelFontSize = 12
plotOverLine1Display_1.DataAxesGrid.ZLabelShadow = 0
plotOverLine1Display_1.DataAxesGrid.ZLabelOpacity = 1.0
plotOverLine1Display_1.DataAxesGrid.XAxisNotation = 'Mixed'
plotOverLine1Display_1.DataAxesGrid.XAxisPrecision = 2
plotOverLine1Display_1.DataAxesGrid.XAxisUseCustomLabels = 0
plotOverLine1Display_1.DataAxesGrid.XAxisLabels = []
plotOverLine1Display_1.DataAxesGrid.YAxisNotation = 'Mixed'
plotOverLine1Display_1.DataAxesGrid.YAxisPrecision = 2
plotOverLine1Display_1.DataAxesGrid.YAxisUseCustomLabels = 0
plotOverLine1Display_1.DataAxesGrid.YAxisLabels = []
plotOverLine1Display_1.DataAxesGrid.ZAxisNotation = 'Mixed'
plotOverLine1Display_1.DataAxesGrid.ZAxisPrecision = 2
plotOverLine1Display_1.DataAxesGrid.ZAxisUseCustomLabels = 0
plotOverLine1Display_1.DataAxesGrid.ZAxisLabels = []
plotOverLine1Display_1.DataAxesGrid.UseCustomBounds = 0
plotOverLine1Display_1.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
plotOverLine1Display_1.PolarAxes.Visibility = 0
plotOverLine1Display_1.PolarAxes.Translation = [0.0, 0.0, 0.0]
plotOverLine1Display_1.PolarAxes.Scale = [1.0, 1.0, 1.0]
plotOverLine1Display_1.PolarAxes.Orientation = [0.0, 0.0, 0.0]
plotOverLine1Display_1.PolarAxes.EnableCustomBounds = [0, 0, 0]
plotOverLine1Display_1.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
plotOverLine1Display_1.PolarAxes.EnableCustomRange = 0
plotOverLine1Display_1.PolarAxes.CustomRange = [0.0, 1.0]
plotOverLine1Display_1.PolarAxes.PolarAxisVisibility = 1
plotOverLine1Display_1.PolarAxes.RadialAxesVisibility = 1
plotOverLine1Display_1.PolarAxes.DrawRadialGridlines = 1
plotOverLine1Display_1.PolarAxes.PolarArcsVisibility = 1
plotOverLine1Display_1.PolarAxes.DrawPolarArcsGridlines = 1
plotOverLine1Display_1.PolarAxes.NumberOfRadialAxes = 0
plotOverLine1Display_1.PolarAxes.AutoSubdividePolarAxis = 1
plotOverLine1Display_1.PolarAxes.NumberOfPolarAxis = 0
plotOverLine1Display_1.PolarAxes.MinimumRadius = 0.0
plotOverLine1Display_1.PolarAxes.MinimumAngle = 0.0
plotOverLine1Display_1.PolarAxes.MaximumAngle = 90.0
plotOverLine1Display_1.PolarAxes.RadialAxesOriginToPolarAxis = 1
plotOverLine1Display_1.PolarAxes.Ratio = 1.0
plotOverLine1Display_1.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.PolarAxes.PolarAxisTitleVisibility = 1
plotOverLine1Display_1.PolarAxes.PolarAxisTitle = 'Radial Distance'
plotOverLine1Display_1.PolarAxes.PolarAxisTitleLocation = 'Bottom'
plotOverLine1Display_1.PolarAxes.PolarLabelVisibility = 1
plotOverLine1Display_1.PolarAxes.PolarLabelFormat = '%-#6.3g'
plotOverLine1Display_1.PolarAxes.PolarLabelExponentLocation = 'Labels'
plotOverLine1Display_1.PolarAxes.RadialLabelVisibility = 1
plotOverLine1Display_1.PolarAxes.RadialLabelFormat = '%-#3.1f'
plotOverLine1Display_1.PolarAxes.RadialLabelLocation = 'Bottom'
plotOverLine1Display_1.PolarAxes.RadialUnitsVisibility = 1
plotOverLine1Display_1.PolarAxes.ScreenSize = 10.0
plotOverLine1Display_1.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.PolarAxes.PolarAxisTitleOpacity = 1.0
plotOverLine1Display_1.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
plotOverLine1Display_1.PolarAxes.PolarAxisTitleFontFile = ''
plotOverLine1Display_1.PolarAxes.PolarAxisTitleBold = 0
plotOverLine1Display_1.PolarAxes.PolarAxisTitleItalic = 0
plotOverLine1Display_1.PolarAxes.PolarAxisTitleShadow = 0
plotOverLine1Display_1.PolarAxes.PolarAxisTitleFontSize = 12
plotOverLine1Display_1.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.PolarAxes.PolarAxisLabelOpacity = 1.0
plotOverLine1Display_1.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
plotOverLine1Display_1.PolarAxes.PolarAxisLabelFontFile = ''
plotOverLine1Display_1.PolarAxes.PolarAxisLabelBold = 0
plotOverLine1Display_1.PolarAxes.PolarAxisLabelItalic = 0
plotOverLine1Display_1.PolarAxes.PolarAxisLabelShadow = 0
plotOverLine1Display_1.PolarAxes.PolarAxisLabelFontSize = 12
plotOverLine1Display_1.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.PolarAxes.LastRadialAxisTextOpacity = 1.0
plotOverLine1Display_1.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
plotOverLine1Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
plotOverLine1Display_1.PolarAxes.LastRadialAxisTextBold = 0
plotOverLine1Display_1.PolarAxes.LastRadialAxisTextItalic = 0
plotOverLine1Display_1.PolarAxes.LastRadialAxisTextShadow = 0
plotOverLine1Display_1.PolarAxes.LastRadialAxisTextFontSize = 12
plotOverLine1Display_1.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
plotOverLine1Display_1.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
plotOverLine1Display_1.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
plotOverLine1Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''
plotOverLine1Display_1.PolarAxes.SecondaryRadialAxesTextBold = 0
plotOverLine1Display_1.PolarAxes.SecondaryRadialAxesTextItalic = 0
plotOverLine1Display_1.PolarAxes.SecondaryRadialAxesTextShadow = 0
plotOverLine1Display_1.PolarAxes.SecondaryRadialAxesTextFontSize = 12
plotOverLine1Display_1.PolarAxes.EnableDistanceLOD = 1
plotOverLine1Display_1.PolarAxes.DistanceLODThreshold = 0.7
plotOverLine1Display_1.PolarAxes.EnableViewAngleLOD = 1
plotOverLine1Display_1.PolarAxes.ViewAngleLODThreshold = 0.7
plotOverLine1Display_1.PolarAxes.SmallestVisiblePolarAngle = 0.5
plotOverLine1Display_1.PolarAxes.PolarTicksVisibility = 1
plotOverLine1Display_1.PolarAxes.ArcTicksOriginToPolarAxis = 1
plotOverLine1Display_1.PolarAxes.TickLocation = 'Both'
plotOverLine1Display_1.PolarAxes.AxisTickVisibility = 1
plotOverLine1Display_1.PolarAxes.AxisMinorTickVisibility = 0
plotOverLine1Display_1.PolarAxes.ArcTickVisibility = 1
plotOverLine1Display_1.PolarAxes.ArcMinorTickVisibility = 0
plotOverLine1Display_1.PolarAxes.DeltaAngleMajor = 10.0
plotOverLine1Display_1.PolarAxes.DeltaAngleMinor = 5.0
plotOverLine1Display_1.PolarAxes.PolarAxisMajorTickSize = 0.0
plotOverLine1Display_1.PolarAxes.PolarAxisTickRatioSize = 0.3
plotOverLine1Display_1.PolarAxes.PolarAxisMajorTickThickness = 1.0
plotOverLine1Display_1.PolarAxes.PolarAxisTickRatioThickness = 0.5
plotOverLine1Display_1.PolarAxes.LastRadialAxisMajorTickSize = 0.0
plotOverLine1Display_1.PolarAxes.LastRadialAxisTickRatioSize = 0.3
plotOverLine1Display_1.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
plotOverLine1Display_1.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
plotOverLine1Display_1.PolarAxes.ArcMajorTickSize = 0.0
plotOverLine1Display_1.PolarAxes.ArcTickRatioSize = 0.3
plotOverLine1Display_1.PolarAxes.ArcMajorTickThickness = 1.0
plotOverLine1Display_1.PolarAxes.ArcTickRatioThickness = 0.5
plotOverLine1Display_1.PolarAxes.Use2DMode = 0
plotOverLine1Display_1.PolarAxes.UseLogAxis = 0

# show color bar/color legend
plotOverLine1Display_1.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(plotOverLine1, renderView1)

# set active source
SetActiveSource(plotOverLine1)

# set active source
SetActiveSource(contour1)

# set active source
SetActiveSource(flow2ndvtu)

# create a new 'XML Unstructured Grid Reader'
surface_flow2ndvtu = XMLUnstructuredGridReader(FileName=['/home/edo20/CFD2020_Guardone/Lab/Lab03/Diamond_Airfoil/CFD/surface_flow2nd.vtu'])
surface_flow2ndvtu.CellArrayStatus = []
surface_flow2ndvtu.PointArrayStatus = ['Density', 'Momentum', 'Energy', 'Pressure', 'Temperature', 'Mach', 'Pressure_Coefficient']

# show data in view
surface_flow2ndvtuDisplay = Show(surface_flow2ndvtu, renderView1)

# trace defaults for the display properties.
surface_flow2ndvtuDisplay.Representation = 'Surface'
surface_flow2ndvtuDisplay.AmbientColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.ColorArrayName = [None, '']
surface_flow2ndvtuDisplay.DiffuseColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.LookupTable = None
surface_flow2ndvtuDisplay.MapScalars = 1
surface_flow2ndvtuDisplay.MultiComponentsMapping = 0
surface_flow2ndvtuDisplay.InterpolateScalarsBeforeMapping = 1
surface_flow2ndvtuDisplay.Opacity = 1.0
surface_flow2ndvtuDisplay.PointSize = 2.0
surface_flow2ndvtuDisplay.LineWidth = 1.0
surface_flow2ndvtuDisplay.RenderLinesAsTubes = 0
surface_flow2ndvtuDisplay.RenderPointsAsSpheres = 0
surface_flow2ndvtuDisplay.Interpolation = 'Gouraud'
surface_flow2ndvtuDisplay.Specular = 0.0
surface_flow2ndvtuDisplay.SpecularColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.SpecularPower = 100.0
surface_flow2ndvtuDisplay.Luminosity = 0.0
surface_flow2ndvtuDisplay.Ambient = 0.0
surface_flow2ndvtuDisplay.Diffuse = 1.0
surface_flow2ndvtuDisplay.EdgeColor = [0.0, 0.0, 0.5]
surface_flow2ndvtuDisplay.BackfaceRepresentation = 'Follow Frontface'
surface_flow2ndvtuDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.BackfaceOpacity = 1.0
surface_flow2ndvtuDisplay.Position = [0.0, 0.0, 0.0]
surface_flow2ndvtuDisplay.Scale = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.Orientation = [0.0, 0.0, 0.0]
surface_flow2ndvtuDisplay.Origin = [0.0, 0.0, 0.0]
surface_flow2ndvtuDisplay.Pickable = 1
surface_flow2ndvtuDisplay.Texture = None
surface_flow2ndvtuDisplay.Triangulate = 0
surface_flow2ndvtuDisplay.UseShaderReplacements = 0
surface_flow2ndvtuDisplay.ShaderReplacements = ''
surface_flow2ndvtuDisplay.NonlinearSubdivisionLevel = 1
surface_flow2ndvtuDisplay.UseDataPartitions = 0
surface_flow2ndvtuDisplay.OSPRayUseScaleArray = 0
surface_flow2ndvtuDisplay.OSPRayScaleArray = 'Density'
surface_flow2ndvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
surface_flow2ndvtuDisplay.OSPRayMaterial = 'None'
surface_flow2ndvtuDisplay.Orient = 0
surface_flow2ndvtuDisplay.OrientationMode = 'Direction'
surface_flow2ndvtuDisplay.SelectOrientationVectors = 'Density'
surface_flow2ndvtuDisplay.Scaling = 0
surface_flow2ndvtuDisplay.ScaleMode = 'No Data Scaling Off'
surface_flow2ndvtuDisplay.ScaleFactor = 0.1
surface_flow2ndvtuDisplay.SelectScaleArray = 'Density'
surface_flow2ndvtuDisplay.GlyphType = 'Arrow'
surface_flow2ndvtuDisplay.UseGlyphTable = 0
surface_flow2ndvtuDisplay.GlyphTableIndexArray = 'Density'
surface_flow2ndvtuDisplay.UseCompositeGlyphTable = 0
surface_flow2ndvtuDisplay.UseGlyphCullingAndLOD = 0
surface_flow2ndvtuDisplay.LODValues = []
surface_flow2ndvtuDisplay.ColorByLODIndex = 0
surface_flow2ndvtuDisplay.GaussianRadius = 0.005
surface_flow2ndvtuDisplay.ShaderPreset = 'Sphere'
surface_flow2ndvtuDisplay.CustomTriangleScale = 3
surface_flow2ndvtuDisplay.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
surface_flow2ndvtuDisplay.Emissive = 0
surface_flow2ndvtuDisplay.ScaleByArray = 0
surface_flow2ndvtuDisplay.SetScaleArray = ['POINTS', 'Density']
surface_flow2ndvtuDisplay.ScaleArrayComponent = ''
surface_flow2ndvtuDisplay.UseScaleFunction = 1
surface_flow2ndvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
surface_flow2ndvtuDisplay.OpacityByArray = 0
surface_flow2ndvtuDisplay.OpacityArray = ['POINTS', 'Density']
surface_flow2ndvtuDisplay.OpacityArrayComponent = ''
surface_flow2ndvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
surface_flow2ndvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
surface_flow2ndvtuDisplay.SelectionCellLabelBold = 0
surface_flow2ndvtuDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
surface_flow2ndvtuDisplay.SelectionCellLabelFontFamily = 'Arial'
surface_flow2ndvtuDisplay.SelectionCellLabelFontFile = ''
surface_flow2ndvtuDisplay.SelectionCellLabelFontSize = 18
surface_flow2ndvtuDisplay.SelectionCellLabelItalic = 0
surface_flow2ndvtuDisplay.SelectionCellLabelJustification = 'Left'
surface_flow2ndvtuDisplay.SelectionCellLabelOpacity = 1.0
surface_flow2ndvtuDisplay.SelectionCellLabelShadow = 0
surface_flow2ndvtuDisplay.SelectionPointLabelBold = 0
surface_flow2ndvtuDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
surface_flow2ndvtuDisplay.SelectionPointLabelFontFamily = 'Arial'
surface_flow2ndvtuDisplay.SelectionPointLabelFontFile = ''
surface_flow2ndvtuDisplay.SelectionPointLabelFontSize = 18
surface_flow2ndvtuDisplay.SelectionPointLabelItalic = 0
surface_flow2ndvtuDisplay.SelectionPointLabelJustification = 'Left'
surface_flow2ndvtuDisplay.SelectionPointLabelOpacity = 1.0
surface_flow2ndvtuDisplay.SelectionPointLabelShadow = 0
surface_flow2ndvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
surface_flow2ndvtuDisplay.ScalarOpacityFunction = None
surface_flow2ndvtuDisplay.ScalarOpacityUnitDistance = 0.28886778482974806
surface_flow2ndvtuDisplay.ExtractedBlockIndex = 0
surface_flow2ndvtuDisplay.SelectMapper = 'Projected tetra'
surface_flow2ndvtuDisplay.SamplingDimensions = [128, 128, 128]
surface_flow2ndvtuDisplay.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
surface_flow2ndvtuDisplay.OSPRayScaleFunction.Points = [1.5819250345230103, 0.0, 0.5, 0.0, 2.035494327545166, 1.0, 0.5, 0.0]
surface_flow2ndvtuDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
surface_flow2ndvtuDisplay.GlyphType.TipResolution = 6
surface_flow2ndvtuDisplay.GlyphType.TipRadius = 0.1
surface_flow2ndvtuDisplay.GlyphType.TipLength = 0.35
surface_flow2ndvtuDisplay.GlyphType.ShaftResolution = 6
surface_flow2ndvtuDisplay.GlyphType.ShaftRadius = 0.03
surface_flow2ndvtuDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
surface_flow2ndvtuDisplay.ScaleTransferFunction.Points = [0.6519656181335449, 0.0, 0.5, 0.0, 1.6912429332733154, 1.0, 0.5, 0.0]
surface_flow2ndvtuDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
surface_flow2ndvtuDisplay.OpacityTransferFunction.Points = [0.6519656181335449, 0.0, 0.5, 0.0, 1.6912429332733154, 1.0, 0.5, 0.0]
surface_flow2ndvtuDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
surface_flow2ndvtuDisplay.DataAxesGrid.XTitle = 'X Axis'
surface_flow2ndvtuDisplay.DataAxesGrid.YTitle = 'Y Axis'
surface_flow2ndvtuDisplay.DataAxesGrid.ZTitle = 'Z Axis'
surface_flow2ndvtuDisplay.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
surface_flow2ndvtuDisplay.DataAxesGrid.XTitleFontFile = ''
surface_flow2ndvtuDisplay.DataAxesGrid.XTitleBold = 0
surface_flow2ndvtuDisplay.DataAxesGrid.XTitleItalic = 0
surface_flow2ndvtuDisplay.DataAxesGrid.XTitleFontSize = 12
surface_flow2ndvtuDisplay.DataAxesGrid.XTitleShadow = 0
surface_flow2ndvtuDisplay.DataAxesGrid.XTitleOpacity = 1.0
surface_flow2ndvtuDisplay.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
surface_flow2ndvtuDisplay.DataAxesGrid.YTitleFontFile = ''
surface_flow2ndvtuDisplay.DataAxesGrid.YTitleBold = 0
surface_flow2ndvtuDisplay.DataAxesGrid.YTitleItalic = 0
surface_flow2ndvtuDisplay.DataAxesGrid.YTitleFontSize = 12
surface_flow2ndvtuDisplay.DataAxesGrid.YTitleShadow = 0
surface_flow2ndvtuDisplay.DataAxesGrid.YTitleOpacity = 1.0
surface_flow2ndvtuDisplay.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
surface_flow2ndvtuDisplay.DataAxesGrid.ZTitleFontFile = ''
surface_flow2ndvtuDisplay.DataAxesGrid.ZTitleBold = 0
surface_flow2ndvtuDisplay.DataAxesGrid.ZTitleItalic = 0
surface_flow2ndvtuDisplay.DataAxesGrid.ZTitleFontSize = 12
surface_flow2ndvtuDisplay.DataAxesGrid.ZTitleShadow = 0
surface_flow2ndvtuDisplay.DataAxesGrid.ZTitleOpacity = 1.0
surface_flow2ndvtuDisplay.DataAxesGrid.FacesToRender = 63
surface_flow2ndvtuDisplay.DataAxesGrid.CullBackface = 0
surface_flow2ndvtuDisplay.DataAxesGrid.CullFrontface = 1
surface_flow2ndvtuDisplay.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.DataAxesGrid.ShowGrid = 0
surface_flow2ndvtuDisplay.DataAxesGrid.ShowEdges = 1
surface_flow2ndvtuDisplay.DataAxesGrid.ShowTicks = 1
surface_flow2ndvtuDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
surface_flow2ndvtuDisplay.DataAxesGrid.AxesToLabel = 63
surface_flow2ndvtuDisplay.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
surface_flow2ndvtuDisplay.DataAxesGrid.XLabelFontFile = ''
surface_flow2ndvtuDisplay.DataAxesGrid.XLabelBold = 0
surface_flow2ndvtuDisplay.DataAxesGrid.XLabelItalic = 0
surface_flow2ndvtuDisplay.DataAxesGrid.XLabelFontSize = 12
surface_flow2ndvtuDisplay.DataAxesGrid.XLabelShadow = 0
surface_flow2ndvtuDisplay.DataAxesGrid.XLabelOpacity = 1.0
surface_flow2ndvtuDisplay.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
surface_flow2ndvtuDisplay.DataAxesGrid.YLabelFontFile = ''
surface_flow2ndvtuDisplay.DataAxesGrid.YLabelBold = 0
surface_flow2ndvtuDisplay.DataAxesGrid.YLabelItalic = 0
surface_flow2ndvtuDisplay.DataAxesGrid.YLabelFontSize = 12
surface_flow2ndvtuDisplay.DataAxesGrid.YLabelShadow = 0
surface_flow2ndvtuDisplay.DataAxesGrid.YLabelOpacity = 1.0
surface_flow2ndvtuDisplay.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
surface_flow2ndvtuDisplay.DataAxesGrid.ZLabelFontFile = ''
surface_flow2ndvtuDisplay.DataAxesGrid.ZLabelBold = 0
surface_flow2ndvtuDisplay.DataAxesGrid.ZLabelItalic = 0
surface_flow2ndvtuDisplay.DataAxesGrid.ZLabelFontSize = 12
surface_flow2ndvtuDisplay.DataAxesGrid.ZLabelShadow = 0
surface_flow2ndvtuDisplay.DataAxesGrid.ZLabelOpacity = 1.0
surface_flow2ndvtuDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
surface_flow2ndvtuDisplay.DataAxesGrid.XAxisPrecision = 2
surface_flow2ndvtuDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
surface_flow2ndvtuDisplay.DataAxesGrid.XAxisLabels = []
surface_flow2ndvtuDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
surface_flow2ndvtuDisplay.DataAxesGrid.YAxisPrecision = 2
surface_flow2ndvtuDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
surface_flow2ndvtuDisplay.DataAxesGrid.YAxisLabels = []
surface_flow2ndvtuDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
surface_flow2ndvtuDisplay.DataAxesGrid.ZAxisPrecision = 2
surface_flow2ndvtuDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
surface_flow2ndvtuDisplay.DataAxesGrid.ZAxisLabels = []
surface_flow2ndvtuDisplay.DataAxesGrid.UseCustomBounds = 0
surface_flow2ndvtuDisplay.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
surface_flow2ndvtuDisplay.PolarAxes.Visibility = 0
surface_flow2ndvtuDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
surface_flow2ndvtuDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
surface_flow2ndvtuDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
surface_flow2ndvtuDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
surface_flow2ndvtuDisplay.PolarAxes.EnableCustomRange = 0
surface_flow2ndvtuDisplay.PolarAxes.CustomRange = [0.0, 1.0]
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisVisibility = 1
surface_flow2ndvtuDisplay.PolarAxes.RadialAxesVisibility = 1
surface_flow2ndvtuDisplay.PolarAxes.DrawRadialGridlines = 1
surface_flow2ndvtuDisplay.PolarAxes.PolarArcsVisibility = 1
surface_flow2ndvtuDisplay.PolarAxes.DrawPolarArcsGridlines = 1
surface_flow2ndvtuDisplay.PolarAxes.NumberOfRadialAxes = 0
surface_flow2ndvtuDisplay.PolarAxes.AutoSubdividePolarAxis = 1
surface_flow2ndvtuDisplay.PolarAxes.NumberOfPolarAxis = 0
surface_flow2ndvtuDisplay.PolarAxes.MinimumRadius = 0.0
surface_flow2ndvtuDisplay.PolarAxes.MinimumAngle = 0.0
surface_flow2ndvtuDisplay.PolarAxes.MaximumAngle = 90.0
surface_flow2ndvtuDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
surface_flow2ndvtuDisplay.PolarAxes.Ratio = 1.0
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisTitleVisibility = 1
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
surface_flow2ndvtuDisplay.PolarAxes.PolarLabelVisibility = 1
surface_flow2ndvtuDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
surface_flow2ndvtuDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
surface_flow2ndvtuDisplay.PolarAxes.RadialLabelVisibility = 1
surface_flow2ndvtuDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
surface_flow2ndvtuDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
surface_flow2ndvtuDisplay.PolarAxes.RadialUnitsVisibility = 1
surface_flow2ndvtuDisplay.PolarAxes.ScreenSize = 10.0
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisTitleFontFile = ''
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisTitleBold = 0
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisTitleItalic = 0
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisTitleShadow = 0
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisTitleFontSize = 12
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisLabelFontFile = ''
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisLabelBold = 0
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisLabelItalic = 0
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisLabelShadow = 0
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisLabelFontSize = 12
surface_flow2ndvtuDisplay.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
surface_flow2ndvtuDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
surface_flow2ndvtuDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
surface_flow2ndvtuDisplay.PolarAxes.LastRadialAxisTextBold = 0
surface_flow2ndvtuDisplay.PolarAxes.LastRadialAxisTextItalic = 0
surface_flow2ndvtuDisplay.PolarAxes.LastRadialAxisTextShadow = 0
surface_flow2ndvtuDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
surface_flow2ndvtuDisplay.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
surface_flow2ndvtuDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
surface_flow2ndvtuDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
surface_flow2ndvtuDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
surface_flow2ndvtuDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
surface_flow2ndvtuDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
surface_flow2ndvtuDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
surface_flow2ndvtuDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
surface_flow2ndvtuDisplay.PolarAxes.EnableDistanceLOD = 1
surface_flow2ndvtuDisplay.PolarAxes.DistanceLODThreshold = 0.7
surface_flow2ndvtuDisplay.PolarAxes.EnableViewAngleLOD = 1
surface_flow2ndvtuDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
surface_flow2ndvtuDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
surface_flow2ndvtuDisplay.PolarAxes.PolarTicksVisibility = 1
surface_flow2ndvtuDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
surface_flow2ndvtuDisplay.PolarAxes.TickLocation = 'Both'
surface_flow2ndvtuDisplay.PolarAxes.AxisTickVisibility = 1
surface_flow2ndvtuDisplay.PolarAxes.AxisMinorTickVisibility = 0
surface_flow2ndvtuDisplay.PolarAxes.ArcTickVisibility = 1
surface_flow2ndvtuDisplay.PolarAxes.ArcMinorTickVisibility = 0
surface_flow2ndvtuDisplay.PolarAxes.DeltaAngleMajor = 10.0
surface_flow2ndvtuDisplay.PolarAxes.DeltaAngleMinor = 5.0
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
surface_flow2ndvtuDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
surface_flow2ndvtuDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
surface_flow2ndvtuDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
surface_flow2ndvtuDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
surface_flow2ndvtuDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
surface_flow2ndvtuDisplay.PolarAxes.ArcMajorTickSize = 0.0
surface_flow2ndvtuDisplay.PolarAxes.ArcTickRatioSize = 0.3
surface_flow2ndvtuDisplay.PolarAxes.ArcMajorTickThickness = 1.0
surface_flow2ndvtuDisplay.PolarAxes.ArcTickRatioThickness = 0.5
surface_flow2ndvtuDisplay.PolarAxes.Use2DMode = 0
surface_flow2ndvtuDisplay.PolarAxes.UseLogAxis = 0

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(plotOverLine1)

# set active source
SetActiveSource(surface_flow2ndvtu)

# create a new 'Plot Over Line'
plotOverLine2 = PlotOverLine(Input=surface_flow2ndvtu,
    Source='High Resolution Line Source')
plotOverLine2.PassPartialArrays = 1
plotOverLine2.ComputeTolerance = 1
plotOverLine2.Tolerance = 2.220446049250313e-16

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine2.Source.Point1 = [0.0, -0.10000000149011612, 0.0]
plotOverLine2.Source.Point2 = [1.0, 0.10000000149011612, 0.0]
plotOverLine2.Source.Resolution = 1000

# set active source
SetActiveSource(surface_flow2ndvtu)

# destroy plotOverLine2
Delete(plotOverLine2)
del plotOverLine2

# create a new 'Plot Data'
plotData1 = PlotData(Input=surface_flow2ndvtu)

# set active source
SetActiveSource(surface_flow2ndvtu)

# Create a new 'Line Chart View'
lineChartView2 = CreateView('XYChartView')
lineChartView2.UseCache = 0
lineChartView2.ViewSize = [400, 400]
lineChartView2.ChartTitle = ''
lineChartView2.ChartTitleAlignment = 'Center'
lineChartView2.ChartTitleFontFamily = 'Arial'
lineChartView2.ChartTitleFontFile = ''
lineChartView2.ChartTitleFontSize = 18
lineChartView2.ChartTitleBold = 0
lineChartView2.ChartTitleItalic = 0
lineChartView2.ChartTitleColor = [0.0, 0.0, 0.0]
lineChartView2.ShowLegend = 1
lineChartView2.LegendLocation = 'TopRight'
lineChartView2.SortByXAxis = 0
lineChartView2.LegendPosition = [0, 0]
lineChartView2.LegendFontFamily = 'Arial'
lineChartView2.LegendFontFile = ''
lineChartView2.LegendFontSize = 12
lineChartView2.LegendBold = 0
lineChartView2.LegendItalic = 0
lineChartView2.TooltipNotation = 'Mixed'
lineChartView2.TooltipPrecision = 6
lineChartView2.HideTimeMarker = 0
lineChartView2.LeftAxisTitle = ''
lineChartView2.ShowLeftAxisGrid = 1
lineChartView2.LeftAxisGridColor = [0.95, 0.95, 0.95]
lineChartView2.LeftAxisColor = [0.0, 0.0, 0.0]
lineChartView2.LeftAxisTitleFontFamily = 'Arial'
lineChartView2.LeftAxisTitleFontFile = ''
lineChartView2.LeftAxisTitleFontSize = 18
lineChartView2.LeftAxisTitleBold = 1
lineChartView2.LeftAxisTitleItalic = 0
lineChartView2.LeftAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView2.LeftAxisLogScale = 0
lineChartView2.LeftAxisUseCustomRange = 0
lineChartView2.LeftAxisRangeMinimum = 0.0
lineChartView2.LeftAxisRangeMaximum = 1.0
lineChartView2.ShowLeftAxisLabels = 1
lineChartView2.LeftAxisLabelNotation = 'Mixed'
lineChartView2.LeftAxisLabelPrecision = 2
lineChartView2.LeftAxisUseCustomLabels = 0
lineChartView2.LeftAxisLabels = []
lineChartView2.LeftAxisLabelFontFamily = 'Arial'
lineChartView2.LeftAxisLabelFontFile = ''
lineChartView2.LeftAxisLabelFontSize = 12
lineChartView2.LeftAxisLabelBold = 0
lineChartView2.LeftAxisLabelItalic = 0
lineChartView2.LeftAxisLabelColor = [0.0, 0.0, 0.0]
lineChartView2.BottomAxisTitle = ''
lineChartView2.ShowBottomAxisGrid = 1
lineChartView2.BottomAxisGridColor = [0.95, 0.95, 0.95]
lineChartView2.BottomAxisColor = [0.0, 0.0, 0.0]
lineChartView2.BottomAxisTitleFontFamily = 'Arial'
lineChartView2.BottomAxisTitleFontFile = ''
lineChartView2.BottomAxisTitleFontSize = 18
lineChartView2.BottomAxisTitleBold = 1
lineChartView2.BottomAxisTitleItalic = 0
lineChartView2.BottomAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView2.BottomAxisLogScale = 0
lineChartView2.BottomAxisUseCustomRange = 0
lineChartView2.BottomAxisRangeMinimum = 0.0
lineChartView2.BottomAxisRangeMaximum = 1.0
lineChartView2.ShowBottomAxisLabels = 1
lineChartView2.BottomAxisLabelNotation = 'Mixed'
lineChartView2.BottomAxisLabelPrecision = 2
lineChartView2.BottomAxisUseCustomLabels = 0
lineChartView2.BottomAxisLabels = []
lineChartView2.BottomAxisLabelFontFamily = 'Arial'
lineChartView2.BottomAxisLabelFontFile = ''
lineChartView2.BottomAxisLabelFontSize = 12
lineChartView2.BottomAxisLabelBold = 0
lineChartView2.BottomAxisLabelItalic = 0
lineChartView2.BottomAxisLabelColor = [0.0, 0.0, 0.0]
lineChartView2.RightAxisTitle = ''
lineChartView2.ShowRightAxisGrid = 1
lineChartView2.RightAxisGridColor = [0.95, 0.95, 0.95]
lineChartView2.RightAxisColor = [0.0, 0.0, 0.0]
lineChartView2.RightAxisTitleFontFamily = 'Arial'
lineChartView2.RightAxisTitleFontFile = ''
lineChartView2.RightAxisTitleFontSize = 18
lineChartView2.RightAxisTitleBold = 1
lineChartView2.RightAxisTitleItalic = 0
lineChartView2.RightAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView2.RightAxisLogScale = 0
lineChartView2.RightAxisUseCustomRange = 0
lineChartView2.RightAxisRangeMinimum = 0.0
lineChartView2.RightAxisRangeMaximum = 1.0
lineChartView2.ShowRightAxisLabels = 1
lineChartView2.RightAxisLabelNotation = 'Mixed'
lineChartView2.RightAxisLabelPrecision = 2
lineChartView2.RightAxisUseCustomLabels = 0
lineChartView2.RightAxisLabels = []
lineChartView2.RightAxisLabelFontFamily = 'Arial'
lineChartView2.RightAxisLabelFontFile = ''
lineChartView2.RightAxisLabelFontSize = 12
lineChartView2.RightAxisLabelBold = 0
lineChartView2.RightAxisLabelItalic = 0
lineChartView2.RightAxisLabelColor = [0.0, 0.0, 0.0]
lineChartView2.TopAxisTitle = ''
lineChartView2.ShowTopAxisGrid = 1
lineChartView2.TopAxisGridColor = [0.95, 0.95, 0.95]
lineChartView2.TopAxisColor = [0.0, 0.0, 0.0]
lineChartView2.TopAxisTitleFontFamily = 'Arial'
lineChartView2.TopAxisTitleFontFile = ''
lineChartView2.TopAxisTitleFontSize = 18
lineChartView2.TopAxisTitleBold = 1
lineChartView2.TopAxisTitleItalic = 0
lineChartView2.TopAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView2.TopAxisLogScale = 0
lineChartView2.TopAxisUseCustomRange = 0
lineChartView2.TopAxisRangeMinimum = 0.0
lineChartView2.TopAxisRangeMaximum = 1.0
lineChartView2.ShowTopAxisLabels = 1
lineChartView2.TopAxisLabelNotation = 'Mixed'
lineChartView2.TopAxisLabelPrecision = 2
lineChartView2.TopAxisUseCustomLabels = 0
lineChartView2.TopAxisLabels = []
lineChartView2.TopAxisLabelFontFamily = 'Arial'
lineChartView2.TopAxisLabelFontFile = ''
lineChartView2.TopAxisLabelFontSize = 12
lineChartView2.TopAxisLabelBold = 0
lineChartView2.TopAxisLabelItalic = 0
lineChartView2.TopAxisLabelColor = [0.0, 0.0, 0.0]

# show data in view
plotData1Display = Show(plotData1, lineChartView2)

# trace defaults for the display properties.
plotData1Display.CompositeDataSetIndex = [0]
plotData1Display.AttributeType = 'Point Data'
plotData1Display.UseIndexForXAxis = 1
plotData1Display.XArrayName = 'Density'
plotData1Display.SeriesVisibility = ['Density', 'Energy', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']
plotData1Display.SeriesLabel = ['Density', 'Density', 'Energy', 'Energy', 'Mach', 'Mach', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', 'Pressure', 'Pressure', 'Pressure_Coefficient', 'Pressure_Coefficient', 'Temperature', 'Temperature', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotData1Display.SeriesColor = ['Density', '0', '0', '0', 'Energy', '0.89', '0.1', '0.11', 'Mach', '0.22', '0.49', '0.72', 'Momentum_X', '0.3', '0.69', '0.29', 'Momentum_Y', '0.6', '0.31', '0.64', 'Momentum_Z', '1', '0.5', '0', 'Momentum_Magnitude', '0.65', '0.34', '0.16', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.89', '0.1', '0.11', 'Temperature', '0.22', '0.49', '0.72', 'Points_X', '0.3', '0.69', '0.29', 'Points_Y', '0.6', '0.31', '0.64', 'Points_Z', '1', '0.5', '0', 'Points_Magnitude', '0.65', '0.34', '0.16']
plotData1Display.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotData1Display.SeriesLabelPrefix = ''
plotData1Display.SeriesLineStyle = ['Density', '1', 'Energy', '1', 'Mach', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Momentum_Magnitude', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotData1Display.SeriesLineThickness = ['Density', '2', 'Energy', '2', 'Mach', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Momentum_Magnitude', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotData1Display.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView2, layout=layout1, hint=1)

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Energy', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']
plotData1Display.SeriesColor = ['Density', '0', '0', '0', 'Energy', '0.889998', '0.100008', '0.110002', 'Mach', '0.220005', '0.489998', '0.719997', 'Momentum_X', '0.300008', '0.689998', '0.289998', 'Momentum_Y', '0.6', '0.310002', '0.639994', 'Momentum_Z', '1', '0.500008', '0', 'Momentum_Magnitude', '0.650004', '0.340002', '0.160006', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.889998', '0.100008', '0.110002', 'Temperature', '0.220005', '0.489998', '0.719997', 'Points_X', '0.300008', '0.689998', '0.289998', 'Points_Y', '0.6', '0.310002', '0.639994', 'Points_Z', '1', '0.500008', '0', 'Points_Magnitude', '0.650004', '0.340002', '0.160006']
plotData1Display.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']
plotData1Display.SeriesLineStyle = ['Density', '1', 'Energy', '1', 'Mach', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1']
plotData1Display.SeriesLineThickness = ['Density', '2', 'Energy', '2', 'Mach', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2']
plotData1Display.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Mach', 'Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Mach', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Mach', 'Temperature']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Mach']

# Properties modified on lineChartView2
lineChartView2.LeftAxisUseCustomRange = 0

# Properties modified on lineChartView2
lineChartView2.LeftAxisUseCustomRange = 1

# Properties modified on lineChartView2
lineChartView2.LeftAxisUseCustomRange = 0

# Properties modified on lineChartView2
lineChartView2.LeftAxisUseCustomRange = 0

# Properties modified on lineChartView2
lineChartView2.LeftAxisUseCustomRange = 1

# Properties modified on lineChartView2
lineChartView2.LeftAxisRangeMinimum = 0.0

# Properties modified on lineChartView2
lineChartView2.LeftAxisUseCustomRange = 0

# Properties modified on lineChartView2
lineChartView2.LeftAxisUseCustomRange = 1

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMinimum = 0.0

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMaximum = 5.0

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMinimum = -0.5

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMinimum = 0.0

# Properties modified on plotData1Display
plotData1Display.UseIndexForXAxis = 0

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Points_X'

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMaximum = 1.0

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = []

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Mach']

# Properties modified on plotData1Display
plotData1Display.UseIndexForXAxis = 1

# Properties modified on plotData1Display
plotData1Display.UseIndexForXAxis = 0

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Points_Z'

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Points_Y'

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Points_X'

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Points_Y'

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Points_Z'

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Points_Y'

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Points_X'

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Points_Y'

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Points_X'

# set active view
SetActiveView(renderView1)

# hide data in view
Hide(surface_flow2ndvtu, renderView1)

# hide data in view
Hide(contour1, renderView1)

# hide data in view
Hide(flow2ndvtu, renderView1)

# set active source
SetActiveSource(surface_flow2ndvtu)

# show data in view
surface_flow2ndvtuDisplay = Show(surface_flow2ndvtu, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(surface_flow2ndvtuDisplay, ('POINTS', 'Mach'))

# rescale color and/or opacity maps used to include current data range
surface_flow2ndvtuDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
surface_flow2ndvtuDisplay.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(plotData1)

# set active view
SetActiveView(lineChartView2)

# Properties modified on plotData1Display
plotData1Display.AttributeType = 'Field Data'

# Properties modified on plotData1Display
plotData1Display.AttributeType = 'Point Data'

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Mach'

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Density'

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Energy'

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Momentum_X'

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Points_X'

# set active source
SetActiveSource(surface_flow2ndvtu)

# hide data in view
Hide(plotData1, lineChartView2)

# destroy plotData1
Delete(plotData1)
del plotData1

# set active source
SetActiveSource(surface_flow2ndvtu)

# destroy lineChartView2
Delete(lineChartView2)
del lineChartView2

# close an empty frame
layout1.Collapse(4)

# set active view
SetActiveView(renderView1)

# create a new 'Plot Data'
plotData1 = PlotData(Input=surface_flow2ndvtu)

# Create a new 'Line Chart View'
lineChartView2 = CreateView('XYChartView')
lineChartView2.UseCache = 0
lineChartView2.ViewSize = [400, 400]
lineChartView2.ChartTitle = ''
lineChartView2.ChartTitleAlignment = 'Center'
lineChartView2.ChartTitleFontFamily = 'Arial'
lineChartView2.ChartTitleFontFile = ''
lineChartView2.ChartTitleFontSize = 18
lineChartView2.ChartTitleBold = 0
lineChartView2.ChartTitleItalic = 0
lineChartView2.ChartTitleColor = [0.0, 0.0, 0.0]
lineChartView2.ShowLegend = 1
lineChartView2.LegendLocation = 'TopRight'
lineChartView2.SortByXAxis = 0
lineChartView2.LegendPosition = [0, 0]
lineChartView2.LegendFontFamily = 'Arial'
lineChartView2.LegendFontFile = ''
lineChartView2.LegendFontSize = 12
lineChartView2.LegendBold = 0
lineChartView2.LegendItalic = 0
lineChartView2.TooltipNotation = 'Mixed'
lineChartView2.TooltipPrecision = 6
lineChartView2.HideTimeMarker = 0
lineChartView2.LeftAxisTitle = ''
lineChartView2.ShowLeftAxisGrid = 1
lineChartView2.LeftAxisGridColor = [0.95, 0.95, 0.95]
lineChartView2.LeftAxisColor = [0.0, 0.0, 0.0]
lineChartView2.LeftAxisTitleFontFamily = 'Arial'
lineChartView2.LeftAxisTitleFontFile = ''
lineChartView2.LeftAxisTitleFontSize = 18
lineChartView2.LeftAxisTitleBold = 1
lineChartView2.LeftAxisTitleItalic = 0
lineChartView2.LeftAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView2.LeftAxisLogScale = 0
lineChartView2.LeftAxisUseCustomRange = 0
lineChartView2.LeftAxisRangeMinimum = 0.0
lineChartView2.LeftAxisRangeMaximum = 1.0
lineChartView2.ShowLeftAxisLabels = 1
lineChartView2.LeftAxisLabelNotation = 'Mixed'
lineChartView2.LeftAxisLabelPrecision = 2
lineChartView2.LeftAxisUseCustomLabels = 0
lineChartView2.LeftAxisLabels = []
lineChartView2.LeftAxisLabelFontFamily = 'Arial'
lineChartView2.LeftAxisLabelFontFile = ''
lineChartView2.LeftAxisLabelFontSize = 12
lineChartView2.LeftAxisLabelBold = 0
lineChartView2.LeftAxisLabelItalic = 0
lineChartView2.LeftAxisLabelColor = [0.0, 0.0, 0.0]
lineChartView2.BottomAxisTitle = ''
lineChartView2.ShowBottomAxisGrid = 1
lineChartView2.BottomAxisGridColor = [0.95, 0.95, 0.95]
lineChartView2.BottomAxisColor = [0.0, 0.0, 0.0]
lineChartView2.BottomAxisTitleFontFamily = 'Arial'
lineChartView2.BottomAxisTitleFontFile = ''
lineChartView2.BottomAxisTitleFontSize = 18
lineChartView2.BottomAxisTitleBold = 1
lineChartView2.BottomAxisTitleItalic = 0
lineChartView2.BottomAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView2.BottomAxisLogScale = 0
lineChartView2.BottomAxisUseCustomRange = 0
lineChartView2.BottomAxisRangeMinimum = 0.0
lineChartView2.BottomAxisRangeMaximum = 1.0
lineChartView2.ShowBottomAxisLabels = 1
lineChartView2.BottomAxisLabelNotation = 'Mixed'
lineChartView2.BottomAxisLabelPrecision = 2
lineChartView2.BottomAxisUseCustomLabels = 0
lineChartView2.BottomAxisLabels = []
lineChartView2.BottomAxisLabelFontFamily = 'Arial'
lineChartView2.BottomAxisLabelFontFile = ''
lineChartView2.BottomAxisLabelFontSize = 12
lineChartView2.BottomAxisLabelBold = 0
lineChartView2.BottomAxisLabelItalic = 0
lineChartView2.BottomAxisLabelColor = [0.0, 0.0, 0.0]
lineChartView2.RightAxisTitle = ''
lineChartView2.ShowRightAxisGrid = 1
lineChartView2.RightAxisGridColor = [0.95, 0.95, 0.95]
lineChartView2.RightAxisColor = [0.0, 0.0, 0.0]
lineChartView2.RightAxisTitleFontFamily = 'Arial'
lineChartView2.RightAxisTitleFontFile = ''
lineChartView2.RightAxisTitleFontSize = 18
lineChartView2.RightAxisTitleBold = 1
lineChartView2.RightAxisTitleItalic = 0
lineChartView2.RightAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView2.RightAxisLogScale = 0
lineChartView2.RightAxisUseCustomRange = 0
lineChartView2.RightAxisRangeMinimum = 0.0
lineChartView2.RightAxisRangeMaximum = 1.0
lineChartView2.ShowRightAxisLabels = 1
lineChartView2.RightAxisLabelNotation = 'Mixed'
lineChartView2.RightAxisLabelPrecision = 2
lineChartView2.RightAxisUseCustomLabels = 0
lineChartView2.RightAxisLabels = []
lineChartView2.RightAxisLabelFontFamily = 'Arial'
lineChartView2.RightAxisLabelFontFile = ''
lineChartView2.RightAxisLabelFontSize = 12
lineChartView2.RightAxisLabelBold = 0
lineChartView2.RightAxisLabelItalic = 0
lineChartView2.RightAxisLabelColor = [0.0, 0.0, 0.0]
lineChartView2.TopAxisTitle = ''
lineChartView2.ShowTopAxisGrid = 1
lineChartView2.TopAxisGridColor = [0.95, 0.95, 0.95]
lineChartView2.TopAxisColor = [0.0, 0.0, 0.0]
lineChartView2.TopAxisTitleFontFamily = 'Arial'
lineChartView2.TopAxisTitleFontFile = ''
lineChartView2.TopAxisTitleFontSize = 18
lineChartView2.TopAxisTitleBold = 1
lineChartView2.TopAxisTitleItalic = 0
lineChartView2.TopAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView2.TopAxisLogScale = 0
lineChartView2.TopAxisUseCustomRange = 0
lineChartView2.TopAxisRangeMinimum = 0.0
lineChartView2.TopAxisRangeMaximum = 1.0
lineChartView2.ShowTopAxisLabels = 1
lineChartView2.TopAxisLabelNotation = 'Mixed'
lineChartView2.TopAxisLabelPrecision = 2
lineChartView2.TopAxisUseCustomLabels = 0
lineChartView2.TopAxisLabels = []
lineChartView2.TopAxisLabelFontFamily = 'Arial'
lineChartView2.TopAxisLabelFontFile = ''
lineChartView2.TopAxisLabelFontSize = 12
lineChartView2.TopAxisLabelBold = 0
lineChartView2.TopAxisLabelItalic = 0
lineChartView2.TopAxisLabelColor = [0.0, 0.0, 0.0]

# show data in view
plotData1Display = Show(plotData1, lineChartView2)

# trace defaults for the display properties.
plotData1Display.CompositeDataSetIndex = [0]
plotData1Display.AttributeType = 'Point Data'
plotData1Display.UseIndexForXAxis = 1
plotData1Display.XArrayName = 'Density'
plotData1Display.SeriesVisibility = ['Density', 'Energy', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']
plotData1Display.SeriesLabel = ['Density', 'Density', 'Energy', 'Energy', 'Mach', 'Mach', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', 'Pressure', 'Pressure', 'Pressure_Coefficient', 'Pressure_Coefficient', 'Temperature', 'Temperature', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotData1Display.SeriesColor = ['Density', '0', '0', '0', 'Energy', '0.89', '0.1', '0.11', 'Mach', '0.22', '0.49', '0.72', 'Momentum_X', '0.3', '0.69', '0.29', 'Momentum_Y', '0.6', '0.31', '0.64', 'Momentum_Z', '1', '0.5', '0', 'Momentum_Magnitude', '0.65', '0.34', '0.16', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.89', '0.1', '0.11', 'Temperature', '0.22', '0.49', '0.72', 'Points_X', '0.3', '0.69', '0.29', 'Points_Y', '0.6', '0.31', '0.64', 'Points_Z', '1', '0.5', '0', 'Points_Magnitude', '0.65', '0.34', '0.16']
plotData1Display.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotData1Display.SeriesLabelPrefix = ''
plotData1Display.SeriesLineStyle = ['Density', '1', 'Energy', '1', 'Mach', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Momentum_Magnitude', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotData1Display.SeriesLineThickness = ['Density', '2', 'Energy', '2', 'Mach', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Momentum_Magnitude', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotData1Display.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView2, layout=layout1, hint=1)

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Energy', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']
plotData1Display.SeriesColor = ['Density', '0', '0', '0', 'Energy', '0.889998', '0.100008', '0.110002', 'Mach', '0.220005', '0.489998', '0.719997', 'Momentum_X', '0.300008', '0.689998', '0.289998', 'Momentum_Y', '0.6', '0.310002', '0.639994', 'Momentum_Z', '1', '0.500008', '0', 'Momentum_Magnitude', '0.650004', '0.340002', '0.160006', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.889998', '0.100008', '0.110002', 'Temperature', '0.220005', '0.489998', '0.719997', 'Points_X', '0.300008', '0.689998', '0.289998', 'Points_Y', '0.6', '0.310002', '0.639994', 'Points_Z', '1', '0.500008', '0', 'Points_Magnitude', '0.650004', '0.340002', '0.160006']
plotData1Display.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']
plotData1Display.SeriesLineStyle = ['Density', '1', 'Energy', '1', 'Mach', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1']
plotData1Display.SeriesLineThickness = ['Density', '2', 'Energy', '2', 'Mach', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2']
plotData1Display.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Mach', 'Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Mach', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Mach', 'Temperature']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Mach']

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMinimum = 0.0

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMaximum = 1.0

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMaximum = 48.0

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMaximum = 47.0

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMaximum = 45.0

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMaximum = 44.0

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMaximum = 43.0

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMaximum = 42.0

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMaximum = 43.0

# Properties modified on plotData1Display
plotData1Display.UseIndexForXAxis = 0

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Points_X'

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMaximum = 1.0

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMaximum = 2.0

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMaximum = 1.0

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Points_Magnitude'

# Properties modified on plotData1Display
plotData1Display.UseIndexForXAxis = 1

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMaximum = 48.0

# Properties modified on plotData1Display
plotData1Display.UseIndexForXAxis = 0

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Points_X'

# Properties modified on lineChartView2
lineChartView2.BottomAxisRangeMaximum = 1.0

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=plotData1)
extractSurface1.PieceInvariant = 1
extractSurface1.NonlinearSubdivisionLevel = 1

# set active source
SetActiveSource(plotData1)

# destroy extractSurface1
Delete(extractSurface1)
del extractSurface1

# set active source
SetActiveSource(surface_flow2ndvtu)

# create a new 'Extract Region Surface'
extractRegionSurface1 = ExtractRegionSurface(Input=surface_flow2ndvtu)
extractRegionSurface1.PieceInvariant = 1
extractRegionSurface1.NonlinearSubdivisionLevel = 1
extractRegionSurface1.RegionArrayName = 'material'
extractRegionSurface1.SingleSided = 1
extractRegionSurface1.MaterialPropertiesName = 'material_properties'
extractRegionSurface1.MaterialIDsName = 'material_ids'
extractRegionSurface1.MaterialPIDsName = 'material_ancestors'
extractRegionSurface1.InterfaceIDsName = 'interface_ids'

# Properties modified on lineChartView2
lineChartView2.ChartTitle = 'upper'

# Properties modified on lineChartView2
lineChartView2.SortByXAxis = 1

# Properties modified on lineChartView2
lineChartView2.SortByXAxis = 0

# Properties modified on lineChartView2
lineChartView2.SortByXAxis = 1

# set active source
SetActiveSource(plotData1)

# set active source
SetActiveSource(surface_flow2ndvtu)

# hide data in view
Hide(plotData1, lineChartView2)

# destroy plotData1
Delete(plotData1)
del plotData1

# set active source
SetActiveSource(surface_flow2ndvtu)

# set active source
SetActiveSource(extractRegionSurface1)

# set active source
SetActiveSource(surface_flow2ndvtu)

# destroy extractRegionSurface1
Delete(extractRegionSurface1)
del extractRegionSurface1

# destroy lineChartView2
Delete(lineChartView2)
del lineChartView2

# close an empty frame
layout1.Collapse(4)

# set active view
SetActiveView(renderView1)

# create a new 'Clip'
clip1 = Clip(Input=surface_flow2ndvtu)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'Density']
clip1.Value = 1.1716042757034302
clip1.Invert = 1
clip1.Crinkleclip = 0
clip1.Exact = 0

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.5, 0.0, 0.0]
clip1.ClipType.Normal = [1.0, 0.0, 0.0]
clip1.ClipType.Offset = 0.0

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [0.0, 0.0, 0.0]
clip1.ClipType.Normal = [0.0, 1.0, 0.0]

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.AmbientColor = [1.0, 1.0, 1.0]
clip1Display.ColorArrayName = ['POINTS', 'Mach']
clip1Display.DiffuseColor = [1.0, 1.0, 1.0]
clip1Display.LookupTable = machLUT
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
clip1Display.OSPRayScaleArray = 'Density'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.OSPRayMaterial = 'None'
clip1Display.Orient = 0
clip1Display.OrientationMode = 'Direction'
clip1Display.SelectOrientationVectors = 'Density'
clip1Display.Scaling = 0
clip1Display.ScaleMode = 'No Data Scaling Off'
clip1Display.ScaleFactor = 0.1
clip1Display.SelectScaleArray = 'Density'
clip1Display.GlyphType = 'Arrow'
clip1Display.UseGlyphTable = 0
clip1Display.GlyphTableIndexArray = 'Density'
clip1Display.UseCompositeGlyphTable = 0
clip1Display.UseGlyphCullingAndLOD = 0
clip1Display.LODValues = []
clip1Display.ColorByLODIndex = 0
clip1Display.GaussianRadius = 0.005
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
clip1Display.SetScaleArray = ['POINTS', 'Density']
clip1Display.ScaleArrayComponent = ''
clip1Display.UseScaleFunction = 1
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityByArray = 0
clip1Display.OpacityArray = ['POINTS', 'Density']
clip1Display.OpacityArrayComponent = ''
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
clip1Display.ScalarOpacityFunction = machPWF
clip1Display.ScalarOpacityUnitDistance = 0.35866290357362607
clip1Display.ExtractedBlockIndex = 0
clip1Display.SelectMapper = 'Projected tetra'
clip1Display.SamplingDimensions = [128, 128, 128]
clip1Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
clip1Display.OSPRayScaleFunction.Points = [1.5819250345230103, 0.0, 0.5, 0.0, 2.035494327545166, 1.0, 0.5, 0.0]
clip1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
clip1Display.GlyphType.TipResolution = 6
clip1Display.GlyphType.TipRadius = 0.1
clip1Display.GlyphType.TipLength = 0.35
clip1Display.GlyphType.ShaftResolution = 6
clip1Display.GlyphType.ShaftRadius = 0.03
clip1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [0.6540390253067017, 0.0, 0.5, 0.0, 1.6593867540359497, 1.0, 0.5, 0.0]
clip1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [0.6540390253067017, 0.0, 0.5, 0.0, 1.6593867540359497, 1.0, 0.5, 0.0]
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
Hide(surface_flow2ndvtu, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# rename source object
RenameSource('Lower', clip1)

# create a new 'Plot Data'
plotData1 = PlotData(Input=clip1)

# Create a new 'Line Chart View'
lineChartView2 = CreateView('XYChartView')
lineChartView2.UseCache = 0
lineChartView2.ViewSize = [400, 400]
lineChartView2.ChartTitle = ''
lineChartView2.ChartTitleAlignment = 'Center'
lineChartView2.ChartTitleFontFamily = 'Arial'
lineChartView2.ChartTitleFontFile = ''
lineChartView2.ChartTitleFontSize = 18
lineChartView2.ChartTitleBold = 0
lineChartView2.ChartTitleItalic = 0
lineChartView2.ChartTitleColor = [0.0, 0.0, 0.0]
lineChartView2.ShowLegend = 1
lineChartView2.LegendLocation = 'TopRight'
lineChartView2.SortByXAxis = 0
lineChartView2.LegendPosition = [0, 0]
lineChartView2.LegendFontFamily = 'Arial'
lineChartView2.LegendFontFile = ''
lineChartView2.LegendFontSize = 12
lineChartView2.LegendBold = 0
lineChartView2.LegendItalic = 0
lineChartView2.TooltipNotation = 'Mixed'
lineChartView2.TooltipPrecision = 6
lineChartView2.HideTimeMarker = 0
lineChartView2.LeftAxisTitle = ''
lineChartView2.ShowLeftAxisGrid = 1
lineChartView2.LeftAxisGridColor = [0.95, 0.95, 0.95]
lineChartView2.LeftAxisColor = [0.0, 0.0, 0.0]
lineChartView2.LeftAxisTitleFontFamily = 'Arial'
lineChartView2.LeftAxisTitleFontFile = ''
lineChartView2.LeftAxisTitleFontSize = 18
lineChartView2.LeftAxisTitleBold = 1
lineChartView2.LeftAxisTitleItalic = 0
lineChartView2.LeftAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView2.LeftAxisLogScale = 0
lineChartView2.LeftAxisUseCustomRange = 0
lineChartView2.LeftAxisRangeMinimum = 0.0
lineChartView2.LeftAxisRangeMaximum = 1.0
lineChartView2.ShowLeftAxisLabels = 1
lineChartView2.LeftAxisLabelNotation = 'Mixed'
lineChartView2.LeftAxisLabelPrecision = 2
lineChartView2.LeftAxisUseCustomLabels = 0
lineChartView2.LeftAxisLabels = []
lineChartView2.LeftAxisLabelFontFamily = 'Arial'
lineChartView2.LeftAxisLabelFontFile = ''
lineChartView2.LeftAxisLabelFontSize = 12
lineChartView2.LeftAxisLabelBold = 0
lineChartView2.LeftAxisLabelItalic = 0
lineChartView2.LeftAxisLabelColor = [0.0, 0.0, 0.0]
lineChartView2.BottomAxisTitle = ''
lineChartView2.ShowBottomAxisGrid = 1
lineChartView2.BottomAxisGridColor = [0.95, 0.95, 0.95]
lineChartView2.BottomAxisColor = [0.0, 0.0, 0.0]
lineChartView2.BottomAxisTitleFontFamily = 'Arial'
lineChartView2.BottomAxisTitleFontFile = ''
lineChartView2.BottomAxisTitleFontSize = 18
lineChartView2.BottomAxisTitleBold = 1
lineChartView2.BottomAxisTitleItalic = 0
lineChartView2.BottomAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView2.BottomAxisLogScale = 0
lineChartView2.BottomAxisUseCustomRange = 0
lineChartView2.BottomAxisRangeMinimum = 0.0
lineChartView2.BottomAxisRangeMaximum = 1.0
lineChartView2.ShowBottomAxisLabels = 1
lineChartView2.BottomAxisLabelNotation = 'Mixed'
lineChartView2.BottomAxisLabelPrecision = 2
lineChartView2.BottomAxisUseCustomLabels = 0
lineChartView2.BottomAxisLabels = []
lineChartView2.BottomAxisLabelFontFamily = 'Arial'
lineChartView2.BottomAxisLabelFontFile = ''
lineChartView2.BottomAxisLabelFontSize = 12
lineChartView2.BottomAxisLabelBold = 0
lineChartView2.BottomAxisLabelItalic = 0
lineChartView2.BottomAxisLabelColor = [0.0, 0.0, 0.0]
lineChartView2.RightAxisTitle = ''
lineChartView2.ShowRightAxisGrid = 1
lineChartView2.RightAxisGridColor = [0.95, 0.95, 0.95]
lineChartView2.RightAxisColor = [0.0, 0.0, 0.0]
lineChartView2.RightAxisTitleFontFamily = 'Arial'
lineChartView2.RightAxisTitleFontFile = ''
lineChartView2.RightAxisTitleFontSize = 18
lineChartView2.RightAxisTitleBold = 1
lineChartView2.RightAxisTitleItalic = 0
lineChartView2.RightAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView2.RightAxisLogScale = 0
lineChartView2.RightAxisUseCustomRange = 0
lineChartView2.RightAxisRangeMinimum = 0.0
lineChartView2.RightAxisRangeMaximum = 1.0
lineChartView2.ShowRightAxisLabels = 1
lineChartView2.RightAxisLabelNotation = 'Mixed'
lineChartView2.RightAxisLabelPrecision = 2
lineChartView2.RightAxisUseCustomLabels = 0
lineChartView2.RightAxisLabels = []
lineChartView2.RightAxisLabelFontFamily = 'Arial'
lineChartView2.RightAxisLabelFontFile = ''
lineChartView2.RightAxisLabelFontSize = 12
lineChartView2.RightAxisLabelBold = 0
lineChartView2.RightAxisLabelItalic = 0
lineChartView2.RightAxisLabelColor = [0.0, 0.0, 0.0]
lineChartView2.TopAxisTitle = ''
lineChartView2.ShowTopAxisGrid = 1
lineChartView2.TopAxisGridColor = [0.95, 0.95, 0.95]
lineChartView2.TopAxisColor = [0.0, 0.0, 0.0]
lineChartView2.TopAxisTitleFontFamily = 'Arial'
lineChartView2.TopAxisTitleFontFile = ''
lineChartView2.TopAxisTitleFontSize = 18
lineChartView2.TopAxisTitleBold = 1
lineChartView2.TopAxisTitleItalic = 0
lineChartView2.TopAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView2.TopAxisLogScale = 0
lineChartView2.TopAxisUseCustomRange = 0
lineChartView2.TopAxisRangeMinimum = 0.0
lineChartView2.TopAxisRangeMaximum = 1.0
lineChartView2.ShowTopAxisLabels = 1
lineChartView2.TopAxisLabelNotation = 'Mixed'
lineChartView2.TopAxisLabelPrecision = 2
lineChartView2.TopAxisUseCustomLabels = 0
lineChartView2.TopAxisLabels = []
lineChartView2.TopAxisLabelFontFamily = 'Arial'
lineChartView2.TopAxisLabelFontFile = ''
lineChartView2.TopAxisLabelFontSize = 12
lineChartView2.TopAxisLabelBold = 0
lineChartView2.TopAxisLabelItalic = 0
lineChartView2.TopAxisLabelColor = [0.0, 0.0, 0.0]

# show data in view
plotData1Display = Show(plotData1, lineChartView2)

# trace defaults for the display properties.
plotData1Display.CompositeDataSetIndex = [0]
plotData1Display.AttributeType = 'Point Data'
plotData1Display.UseIndexForXAxis = 1
plotData1Display.XArrayName = 'Density'
plotData1Display.SeriesVisibility = ['Density', 'Energy', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']
plotData1Display.SeriesLabel = ['Density', 'Density', 'Energy', 'Energy', 'Mach', 'Mach', 'Momentum_X', 'Momentum_X', 'Momentum_Y', 'Momentum_Y', 'Momentum_Z', 'Momentum_Z', 'Momentum_Magnitude', 'Momentum_Magnitude', 'Pressure', 'Pressure', 'Pressure_Coefficient', 'Pressure_Coefficient', 'Temperature', 'Temperature', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotData1Display.SeriesColor = ['Density', '0', '0', '0', 'Energy', '0.89', '0.1', '0.11', 'Mach', '0.22', '0.49', '0.72', 'Momentum_X', '0.3', '0.69', '0.29', 'Momentum_Y', '0.6', '0.31', '0.64', 'Momentum_Z', '1', '0.5', '0', 'Momentum_Magnitude', '0.65', '0.34', '0.16', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.89', '0.1', '0.11', 'Temperature', '0.22', '0.49', '0.72', 'Points_X', '0.3', '0.69', '0.29', 'Points_Y', '0.6', '0.31', '0.64', 'Points_Z', '1', '0.5', '0', 'Points_Magnitude', '0.65', '0.34', '0.16']
plotData1Display.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotData1Display.SeriesLabelPrefix = ''
plotData1Display.SeriesLineStyle = ['Density', '1', 'Energy', '1', 'Mach', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Momentum_Magnitude', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotData1Display.SeriesLineThickness = ['Density', '2', 'Energy', '2', 'Mach', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Momentum_Magnitude', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotData1Display.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Momentum_Magnitude', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView2, layout=layout1, hint=1)

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Energy', 'Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']
plotData1Display.SeriesColor = ['Density', '0', '0', '0', 'Energy', '0.889998', '0.100008', '0.110002', 'Mach', '0.220005', '0.489998', '0.719997', 'Momentum_X', '0.300008', '0.689998', '0.289998', 'Momentum_Y', '0.6', '0.310002', '0.639994', 'Momentum_Z', '1', '0.500008', '0', 'Momentum_Magnitude', '0.650004', '0.340002', '0.160006', 'Pressure', '0', '0', '0', 'Pressure_Coefficient', '0.889998', '0.100008', '0.110002', 'Temperature', '0.220005', '0.489998', '0.719997', 'Points_X', '0.300008', '0.689998', '0.289998', 'Points_Y', '0.6', '0.310002', '0.639994', 'Points_Z', '1', '0.500008', '0', 'Points_Magnitude', '0.650004', '0.340002', '0.160006']
plotData1Display.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']
plotData1Display.SeriesLineStyle = ['Density', '1', 'Energy', '1', 'Mach', '1', 'Momentum_Magnitude', '1', 'Momentum_X', '1', 'Momentum_Y', '1', 'Momentum_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pressure', '1', 'Pressure_Coefficient', '1', 'Temperature', '1']
plotData1Display.SeriesLineThickness = ['Density', '2', 'Energy', '2', 'Mach', '2', 'Momentum_Magnitude', '2', 'Momentum_X', '2', 'Momentum_Y', '2', 'Momentum_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pressure', '2', 'Pressure_Coefficient', '2', 'Temperature', '2']
plotData1Display.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Mach', 'Momentum_Magnitude', 'Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Mach', 'Pressure', 'Pressure_Coefficient', 'Temperature']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Mach', 'Pressure', 'Pressure_Coefficient']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Mach', 'Pressure']

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Mach']

# Properties modified on plotData1Display
plotData1Display.UseIndexForXAxis = 0

# Properties modified on plotData1Display
plotData1Display.XArrayName = 'Points_X'

# Properties modified on lineChartView2
lineChartView2.LeftAxisUseCustomRange = 0

# Properties modified on lineChartView2
lineChartView2.LeftAxisUseCustomRange = 1

# Properties modified on lineChartView2
lineChartView2.BottomAxisUseCustomRange = 0

# Properties modified on lineChartView2
lineChartView2.LeftAxisUseCustomRange = 0

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.Play()

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = []

# Properties modified on plotData1Display
plotData1Display.SeriesVisibility = ['Mach']

# Properties modified on plotData1Display
plotData1Display.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '1', 'Pressure_Coefficient', '0', 'Temperature', '0']

# Properties modified on plotData1Display
plotData1Display.SeriesMarkerStyle = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']

# Properties modified on plotData1Display
plotData1Display.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '1', 'Pressure_Coefficient', '0', 'Temperature', '0']

# Properties modified on plotData1Display
plotData1Display.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '2', 'Pressure_Coefficient', '0', 'Temperature', '0']

# Properties modified on plotData1Display
plotData1Display.SeriesPlotCorner = ['Density', '0', 'Energy', '0', 'Mach', '0', 'Momentum_Magnitude', '0', 'Momentum_X', '0', 'Momentum_Y', '0', 'Momentum_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pressure', '0', 'Pressure_Coefficient', '0', 'Temperature', '0']

# Properties modified on lineChartView2
lineChartView2.ShowLegend = 0

# Properties modified on lineChartView2
lineChartView2.ShowLegend = 1

# Properties modified on lineChartView2
lineChartView2.SortByXAxis = 1

# Properties modified on lineChartView2
lineChartView2.SortByXAxis = 0

# Properties modified on lineChartView2
lineChartView2.SortByXAxis = 1

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(lineChartView2)

# create a new 'Python Calculator'
pythonCalculator1 = PythonCalculator(Input=plotData1)
pythonCalculator1.Expression = ''
pythonCalculator1.ArrayAssociation = 'Point Data'
pythonCalculator1.ArrayName = 'result'
pythonCalculator1.CopyArrays = 1

# set active source
SetActiveSource(plotData1)

# destroy pythonCalculator1
Delete(pythonCalculator1)
del pythonCalculator1

# set active source
SetActiveSource(clip1)

# hide data in view
Hide(plotData1, lineChartView2)

# destroy plotData1
Delete(plotData1)
del plotData1

# set active source
SetActiveSource(clip1)