echo /=============================== Start simulation ========================/
mpirun -np 4 SU2_CFD CFD/config.cfg 2>&1 | tee log.su2cfd
mv history.csv CFD
mv flow.vtu CFD
mv surface_flow.vtu CFD
mv restart_flow.dat CFD
mv log.su2cfd CFD
echo /=============================== End of the simulation ===================/

