echo /================================ Start Meshing ==========================/
gmsh -2 -nt 8  mesh.geo 2>&1 | tee log1.gmsh
gmsh -2 -nt 8 -format su2 mesh.geo 2>&1 | tee log2.gmsh
mv mesh.msh MESH
mv log1.gmsh MESH
mv log2.gmsh MESH
mv mesh.shu2 MESH
echo /================================ End of the meshing process =============/
