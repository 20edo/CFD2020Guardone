# This script runs simulations of a diamond airfoil with different mesh sizes

path = '/home/edo20/CFD2020_Guardone/Homework/DIAMOND_AIRFOIL'

# import necessary modules
import sys
import os
import numpy as np
import subprocess as sbp
import time
from statistics import stdev

# Simulations parameters

#profile_h= np.array(np.arange(start = 0.1, stop = 10, step = 1))		# Mesh size at the profile buondary
#freestream_H= np.array(np.arange( start = 5, stop = 50, step = 5))		# Mesh size at the freestream boundary
#nh = len(profile_h)
#nH = len(freestream_H)

nh = 5
nH = 2

profile_h= np.linspace(start = 0.1, stop = 10, num = nh)		# Mesh size at the profile buondary
freestream_H= np.linspace(start = 5, stop = 50, num = nH)		# Mesh size at the freestream boundary

print(profile_h)
print(freestream_H)
print(nh,nH)


# Change location to main folder
os.chdir(path)
print(os.getcwd())

# Initialize matrices 
Mach_rms = np.zeros((nh,nH))

# Start loops

for i in range(nh):
	for j in range(nH):
		print("//////////////////////////////////////////////////////////////////")
		print("Creating directory: h = ", profile_h[i] , "             H = " , freestream_H[j])
		# ================================ Folder operations
		# Move to the main folder
		os.chdir(path)
		# Copy CASE0 directory
		os.system("cp -r CASE0 Working_dir")
		os.chdir('Working_dir')

		# Edit lines 6 and 7 of the geo file
		meshgeo = open('MESH/mesh.geo')
		lines = meshgeo.readlines()
		lines[5] = 'h = ' + str(profile_h[i]) + '; \n'
		lines[6] = 'H = ' + str(freestream_H[j]) + '; \n'
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
		Data = np.genfromtxt('POST-PROCESSING/Data.csv', delimiter = ',', names = True, dtype = None, skip_header=0)
		Mach = Data['Mach']
		Mach_exact = Data['Exact_Mach0']
		Mach_error = Mach - Mach_exact
		Mach_rms[i,j] = stdev(Mach_error)
		
		
		# Return to the appropriate folder
		os.chdir(path)
		
		# Rename working directory
		dirname=("Case_h"+str(profile_h[i])+"H"+str(freestream_H[j]))
		os.system("mv Working_dir "+ dirname)
		
# End of the loop

# Global post-process
np.savetxt(path + 'Mach_rms.csv', Mach_rms)
plt.contour([h, H], Mach_rms, label = 'Mach rms')
plt.legend()
plt.show()
plt.savefig(path + 'Mach_rms.svg')
