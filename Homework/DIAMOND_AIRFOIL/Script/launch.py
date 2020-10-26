# This script runs simulations of a diamond airfoil with different mesh sizes

path = '/home/edo20/CFD2020_Guardone/Homework/DIAMOND_AIRFOIL'

# import necessary modules
import sys
import os
import numpy as np
import subprocess as sbp
import time

# Simulations parameters
profile_h=0.1*np.arange(1,100,10)	# Mesh size at the profile buondary
freestream_H=5*np.arange(1,10)		# Mesh size at the freestream boundary

# Change location to main folder
os.chdir(path)
print(os.getcwd())

# Start loops

for i in profile_h:
	for j in freestream_H:
		print("//////////////////////////////////////////////////////////////////")
		print("Creating directory: h = ", i , "             H = " , j)
		# ================================ Folder operations
		# Move to the main folder
		os.chdir(path)
		# Copy CASE0 directory
		os.system("cp -r CASE0 Working_dir")
		os.chdir('Working_dir')

		# Edit lines 6 and 7 of the geo file
		meshgeo = open('MESH/mesh.geo')
		lines = meshgeo.readlines()
		lines[5] = 'h = ' + str(i) + '; \n'
		lines[6] = 'H = ' + str(j) + '; \n'
		mgeo=open('m.geo','w')
		newfile="".join(lines)
		mgeo.write(newfile)
		mgeo.close()
		os.system("rm MESH/mesh.geo")
		os.system("mv m.geo MESH/mesh.geo")
		
		# ================================= Mesh and solve
		# Mesh
		os.system('chmod 777 MESH/mesh.sh')
		os.system('./MESH/mesh.sh')

		# Solve
		os.system('chmod 777 CFD/solve.sh')
		os.system('./CFD/solve.sh')


		# Post-process
		os.system('pvpython POST-PROCESSING/post-processing.py')
		
		
		# Return to the appropriate folder
		os.chdir(path)
		
		# Rename working directory
		dirname=("Case_h"+str(i)+"H"+str(j))
		os.system("mv Working_dir "+ dirname)
		
# End of the loop

# Global post-process
