import numpy as np
import CompDam_DGD
import viz

# logging
CompDam_DGD.dgd_mod.log_init(level=4, filename='pyextmod_run_output.txt')

# Load material properties from props file
m = CompDam_DGD.matprop_mod.loadmatprops('IM7-8552', False, 4, [100000, 0, 0.183, 0])

# Load parameters from the 'CompDam.parameters' file
p = CompDam_DGD.parameters_mod.loadparameters()

# State variables
svarray = [
	0.900000000000000E+00,     # SV1,  CDM_d2
	0.000000000000000E+00,     # SV2,  CDM_Fb1
	1.000000000000000E+00,     # SV3,  CDM_Fb2
	0.000000000000000E+00,     # SV4,  CDM_Fb3
	0.000000000000000E+00,     # SV5,  CDM_B
	0.200000000000000E+00,     # SV6,  CDM_Lc1
	0.200000000000000E+00,     # SV7,  CDM_Lc2
	0.183000000000000E+00,     # SV8,  CDM_Lc3
	0.000000000000000E+00,     # SV9,  CDM_FIm
	0.349000000000000E+00,     # SV10, CDM_alpha
	1.000000000000000E+00,     # SV11, CDM_STATUS
	0.000000000000000E+00,     # SV12, CDM_Plas12
	0.000000000000000E+00,     # SV13, CDM_Inel12
	0.000000000000000E+00,     # SV14, CDM_FIfT
	0.000000000000000E+00,     # SV15, CDM_slide1
	0.000000000000000E+00,     # SV16, CDM_slide2
	0.000000000000000E+00,     # SV17, CDM_FIfC
	0.000000000000000E+00,     # SV18, CDM_d1T
	0.000000000000000E+00      # SV19, CDM_d1C
]
sv = CompDam_DGD.statevar_mod.loadstatevars(len(svarray), svarray, m)
# print sv


# Other inputs
F = np.array([
	[1.000000000000000E+00, 0.000000000000000E+00, 0.000000000000000E+00],
	[0.000000000000000E+00, 1.200000000000000E+00, 0.000000000000000E+00],
	[0.000000000000000E+00, 0.100000000000000E+00, 1.000000000000000E+00]])

F_old = np.array([
	[1.000000000000000E+00, 0.000000000000000E+00, 0.000000000000000E+00],
	[0.000000000000000E+00, 1.000000000000000E+00, 0.000000000000000E+00],
	[0.000000000000000E+00, 0.000000000000000E+00, 1.000000000000000E+00]])

U = np.array([
	[1.000000000000000E+00, 0.000000000000000E+00, 0.000000000000000E+00],
	[0.000000000000000E+00, 1.000000000000000E+00, 0.000000000000000E+00],
	[0.000000000000000E+00, 0.000000000000000E+00, 1.000000000000000E+00]])

Cauchy = np.zeros((3,3), order='F')

CompDam_DGD.dgd_mod.dgdevolve(u=U, f=F, f_old=F_old, m=m, p=p, sv=sv, ndir=3, nshr=3, dt=0, cauchy=Cauchy)
# print Cauchy

CompDam_DGD.dgd_mod.log_close()


# Visualize
viz.visualize(lc=svarray[5:8], alpha=svarray[9], F=F, pathToLogFile='pyextmod_run_output.txt', initMD=1, initEQk=1)
