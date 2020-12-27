np=4	# Number of processors (if you change this remember to change decomposeParDict)

mkdir log

# Mesh with gmsh
gmsh 	-3		../../MESH/mesh_1.geo 	2>&1	> log/gmsh.log

# Trasform mesh to openFoam format
gmshToFoam		../../MESH/mesh_1.msh	2>&1	> log/gmshToFoam.log

# Edit patches 
ex constant/polyMesh/boundary <<EOEX
  :20,25s/patch/empty/
  :28,32s/patch/wall/
  :41,47s/patch/empty/
  :x
EOEX

# Check mesh (look at the log for quality parameters)
checkMesh	2>&1	> log/checkMesh.log

# Renumber Mesh to reduce band and speed up the simulation
renumberMesh -overwrite 2>&1	>	log/renumberMesh.log

# Decompose
decomposePar	2>&1	>	log/decomposePar.log

# Run
mpirun -np $np 	simpleFoam 	-parallel	2>&1	>	log/simpleFoam.log	&

reconstructPar -latestTime	2>&1	> log/reconstructPar.log
