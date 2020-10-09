# This script runs simulations of a diamond airfoil with different mesh sizes

path = '/home/edo20/CFD2020_Guardone/Homework/Diamond_Airfoil'

# import necessary modules
import sys
import os
import numpy as np
import subprocess as sbp
import time

# Simulations parameters
profile_h=0.01*np.arange(1,100,10)	# Mesh size at the profile buondary
freestream_H=np.arange(1,10)		# Mesh size at the freestream boundary

# Inizialize timers
meshTime=time.time()
simTime=time.time()
totTime=time.time()

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
		os.chdir(dirname + "/MESH")

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

		# Start timers
		totTime = time.time()
		meshTime = time.time()

		# Mesh with gmsh
		os.system("gmsh -2 -nt 8  mesh.geo 2>&1 | tee log1.gmsh")
		os.system("gmsh -2 -nt 8 -format su2 mesh.msh 2>&1 | tee log2.gmsh")
		meshTIME = time.time()-meshTime	# Stop mesh timer

		# Copy config file
		os.chdir(path)
		os.system('cp CASE0/config.cfg ' + dirname)

		# RUN
		os.chdir(dirname)
		simTime = time.time()			# Start simulation timer
		os.system('mpirun -np 4 SU2_CFD config.cfg 2>&1 | tee log.su2cfd')
		simTIME = time.time() - simTime	# Stop simulation timer

		# Case post-process
		totTIME = time.time() - totTime	# Stop total timer
		original_stdout=sys.stdout
		# Save time elapsed in a file
		with open('log.time','w') as logtime:
			sys.stdout = logtime
			print('mesh time:	' + str(meshTIME) ,'/n simulation time:	' + str(simTIME), '/n total time:	' + str(totTIME))  
		sys.stdout = original_stdout
		
		# Return to the appropriate folder
		os.chdir(path)

# End of the loop

# Global post-process
