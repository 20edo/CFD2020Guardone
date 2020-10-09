# This script runs simulations of a diamond airfoil with different mesh sizes

path = '/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil/Script'

# import necessary modules
import os
import numpy as np
import subprocess as sbp

# Simulations parameters
profile_h=0.01*np.arange(1,100,10)	# Mesh size at the profile buondary
freestream_H=np.arange(1,10)		# Mesh size at the freestream boundary


# Change location to main folder
os.chdir(path)
print(os.getcwd())

# Start loops

for i in profile_h:
	for j in freestream_H:
		print("Creating directory h ", i, "H" , j)
		dirname=("Case_h"+str(i)+"H"+str(j))
		os.system("mkdir -p " + dirname + "/MESH")
		# Create geo file
		os.system("cp CASE0/MESH/mesh.geo " + dirname + "/MESH")
		print(' Current work directory 1:', os.getcwd())
		os.chdir(dirname + "/MESH")
		print(' Current work directory 2:', os.getcwd())
		print('Files in the directory:', sbp.check_output('ls'))

		# Edit lines 6 and 7
		meshgeo = open('mesh.geo')
		lines = meshgeo.readlines()
		lines[5] = 'h = ' + str(i) + '; \n'
		lines[6] = 'H = ' + str(j) + '; \n'
		mgeo=open('m.geo','w')
		newfile="".join(lines)
		mgeo.write(newfile)
		mgeo.close()
		os.system("rm mesh.geo")
		os.system("mv m.geo mesh.geo")

		# Mesh with gmsh
		os.system("gmsh -2 mesh.geo")
		os.system("gmsh -2 -format su2 mesh.msh > log.gmsh")

		# Copy config file
		os.chdir(path)
		os.system('cp CASE0/config.cfg ' + dirname)

		# RUN
		os.chdir(dirname)
		os.system('mpirun -np 4 SU2_CFD config.cfg > log.su2cfd')
		
		# Case post-process

		# Return to the appropriate folder
		os.chdir(path)

# End of the loop

# Global post-process
