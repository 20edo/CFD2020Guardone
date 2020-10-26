echo /================================ Start Meshing ==========================/
gmsh -2 -nt 8  MESH/mesh.geo 2>&1 | tee MESH/log1.gmsh
gmsh -2 -nt 8 -format su2 MESH/mesh.msh 2>&1 | tee MESH/log2.gmsh
echo /================================ End of the meshing process =============/
