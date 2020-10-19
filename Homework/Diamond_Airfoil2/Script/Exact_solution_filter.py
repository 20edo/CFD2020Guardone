import numpy as np
from math import mt

pdi = self.GetInput()
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
        V_exact.InsertNextTuple3(np.cos(mt.pi+x), 10, 0)
    else:
        V_exact.InsertNextTuple3(0, -10, 0)
    

pdo.GetPointData().AddArray(coords)
pdo.GetPointData().AddArray(V_exact)
