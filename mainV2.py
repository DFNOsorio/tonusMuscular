from tools import *
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

file = "Egas_Moniz_Segments/Paciente1_Ines_Healthy.h5"

patient1 = Patient(file, platform=True, verbose=True)


patient1.static_avg = avg_out(patient1.static)
patient1.EMG_avg = avg_out(patient1.EMG)
print '\033[93m' + "AVG_END" + '\033[0m'

patient1.static_RMS = RMS_whole_segment(patient1.static_avg)
patient1.EMG_RMS = RMS_whole_segment(patient1.EMG_avg)
print '\033[93m' + "RMS_END" + '\033[0m'

patient1.RMS_max = max_mvc(patient1.static_RMS["MVC1"], patient1.static_RMS["MVC2"])
print '\033[93m' + "MAX_END" + '\033[0m'

patient1.static_normalization, patient1.static_max_values = norm_whole_segment(patient1.static_RMS, patient1.RMS_max)
patient1.EMG_normalization, patient1.EMG_max_values = norm_whole_segment(patient1.EMG_RMS, patient1.RMS_max)
print '\033[93m' + "NORM_END" + '\033[0m'

patient1.platformdata = RAW_2_mass(patient1.platform)
patient1.COP = mass_2_COP(patient1.platformdata)
# #patient1.COP = []
print '\033[93m' + "COP_END" + '\033[0m'

patient1.velocity, patient1.mean, patient1.acelaration = velocity_COP(patient1.COP)
print '\033[93m' + "VELOCITY_END" + '\033[0m'

patient1.trajec = trajectory(patient1.COP)
print '\033[93m' + "TRAJ_END" + '\033[0m'

patient1.c= coherence(patient1.COP, patient1.EMG_normalization)
print '\033[93m' + "COHERENCY_END" + '\033[0m'
#
# patient1.RMS_velocity = RMS_velocity_whole_segment(patient1.velocity)
# print '\033[93m' + "V_RMS_END" + '\033[0m'
#
# patient1.RMS_acel = RMS_velocity_whole_segment(patient1.acelaration)
# print '\033[93m' + "A_RMS_END" + '\033[0m'
#
# patient1.acel_norm = normalization_COP(patient1.RMS_acel)
# print '\033[93m' + "A_NORM_END" + '\033[0m'
#
# patient1.v_norm = normalization_COP(patient1.RMS_velocity)
# print '\033[93m' + "V_NORM_END" + '\033[0m'
#
# patient1.COP_norm = normalization_COP(patient1.COP)
# print '\033[93m' + "COP_NORM_END" + '\033[0m'
#
# patient1.corr_RL = RL_muscles_COP(patient1.COP, patient1.v_norm, patient1.acel_norm, patient1.EMG_normalization)
# print '\033[93m' + "RLCORR_END" + '\033[0m'
#
# patient1.corr_FB = FB_muscles_COP(patient1.COP, patient1.v_norm, patient1.acel_norm, patient1.EMG_normalization)
# print '\033[93m' + "FBCORR_END" + '\033[0m'
#
# patient1.corr_FB_cross = FB_muscles_COP_Cross(patient1.COP, patient1.EMG_normalization)
# print '\033[93m' + "FBCORR_CROSS_END" + '\033[0m'

##Creating database

create_database()
personal_data(file)
parameters(patient1.EMG_max_values)
coherency(patient1.c)



##Plot figures

#velocity_Muscle(patient1.EMG_normalization, patient1.v_norm)
#COP_Muscle(patient1.EMG_normalization, patient1.COP)
#group_LR_COP(patient1.COP_norm, patient1.EMG_normalization, patient1.v_norm, patient1.acel_norm, "Patient1 Healthy")
#group_FB_COP(patient1.COP_norm, patient1.EMG_normalization, patient1.v_norm, patient1.acel_norm, "Patient1 Healthy")
#groupmuscles_COP(patient1.COP_norm, patient1.EMG_normalization, "Patient1 Healthy")

#fig1_max_platform = graph(patient1.EMG_max_values, patient1.COP,"Patient2", patient1.trajec, patient1.c, patient1.mean, platform = True)




