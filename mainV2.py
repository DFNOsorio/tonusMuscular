from tools import *
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


file = "Egas_Moniz_Segments/Paciente2_Emma_Healthy.h5"

patient1 = Patient(file, platform=True, verbose=True)


patient1.static_avg = avg_out(patient1.static)
patient1.EMG_avg = avg_out(patient1.EMG)
print '\033[93m' + "AVG_END" + '\033[0m'

# patient1.static_RMS = RMS_whole_segment(patient1.static_avg)
# patient1.EMG_RMS = RMS_whole_segment(patient1.EMG_avg)
# print '\033[93m' + "RMS_END" + '\033[0m'
#
# patient1.max_MVC_back = max_mvc(patient1.static_RMS["MVC_back/MVC1"], patient1.static_RMS["MVC_back/MVC2"], patient1.static_RMS["MVC_back/MVC3"])
# print '\033[93m' + "MAX_back_END" + '\033[0m'
#
# patient1.max_MVC_rectus = max_mvc(patient1.static_RMS["MVC_rectus/MVC1"], patient1.static_RMS["MVC_rectus/MVC2"], patient1.static_RMS["MVC_rectus/MVC3"])
# print '\033[93m' + "MAX_rectus_END" + '\033[0m'
#
# patient1.max_MVC_RO = max_mvc(patient1.static_RMS["MVC_RO/MVC1"], patient1.static_RMS["MVC_RO/MVC2"], patient1.static_RMS["MVC_RO/MVC3"])
# print '\033[93m' + "MAX_RO_END" + '\033[0m'
#
# patient1.max_MVC_LO = max_mvc(patient1.static_RMS["MVC_LO/MVC1"], patient1.static_RMS["MVC_LO/MVC2"], patient1.static_RMS["MVC_LO/MVC3"])
# print '\033[93m' + "MAX_LO_END" + '\033[0m'
#
# patient1.static_normalization, patient1.static_max_values = norm_whole_segment(patient1.static_RMS, patient1.max_MVC_back, patient1.max_MVC_rectus, patient1.max_MVC_RO, patient1.max_MVC_LO)
# patient1.EMG_normalization, patient1.EMG_max_values = norm_whole_segment(patient1.EMG_RMS, patient1.max_MVC_back, patient1.max_MVC_rectus, patient1.max_MVC_RO, patient1.max_MVC_LO)
# print '\033[93m' + "NORM_END" + '\033[0m'


patient1.platformdata = RAW_2_mass(patient1.platform)
patient1.COP = mass_2_COP(patient1.platformdata)
# # #patient1.COP = []
print '\033[93m' + "COP_END" + '\033[0m'

# patient1.std = std(patient1.COP)
# print '\033[93m' + "STD_COP_END" + '\033[0m'
#
# patient1.amplitude = amplitude(patient1.COP)
# print '\033[93m' + "AMP_COP_END" + '\033[0m'
#
# patient1.velocity, patient1.mean, patient1.acelaration = velocity_COP(patient1.COP)
# print '\033[93m' + "VELOCITY_END" + '\033[0m'
#
# patient1.trajec = trajectory(patient1.COP)
# print '\033[93m' + "TRAJ_END" + '\033[0m'
#
# patient1.c= coherence(patient1.COP, patient1.EMG_normalization)
# print '\033[93m' + "COHERENCY_END" + '\033[0m'
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
#
# patient1.simple_corr = simple_correlation(patient1.EMG_normalization, patient1.COP)
# print '\033[93m' + "CORR_END" + '\033[0m'
#
patient1.fre_EMG, patient1.pxx_EMG = fourier_EMG(patient1.EMG_avg)
print '\033[93m' + "FOURRIER_EMG_END" + '\033[0m'

patient1.peak_EMG, patient1.meanf_EMG, patient1.f_80_EMG, patient1.f_50_EMG = parameters_fourier_EMG(patient1.fre_EMG, patient1.pxx_EMG)
print '\033[93m' + "FOURRIER_EMG_PARAMETERS_END" + '\033[0m'

patient1.freq_COP, patient1.pxx_COP = fourier_COP(patient1.COP)
print '\033[93m' + "FOURRIER_EMG_END" + '\033[0m'

patient1.peak_COP, patient1.meanf_COP, patient1.f_80_COP, patient1.f_50_COP = parameters_fourrier_COP(patient1.freq_COP, patient1.pxx_COP)
print '\033[93m' + "FOURRIER_COP_PARAMETERS_END" + '\033[0m'


##Creating database##

#create_database()

# personal_data(file)
# parameters(patient1.EMG_max_values)
# coherency(patient1.c)
# COP_parameters(patient1.mean, patient1.COP, patient1.std, patient1.amplitude)
# correlation_RL(patient1.corr_RL)
# correlation_FB(patient1.corr_FB)
# correlation_FB_cross(patient1.corr_FB_cross)
# correlation(patient1.simple_corr)
# fourrier_parameters_EMG(patient1.peak_EMG, patient1.meanf_EMG, patient1.f_80_EMG, patient1.f_50_EMG)
# fourrier_parameters_COP(patient1.peak_COP, patient1.meanf_COP, patient1.f_80_COP, patient1.f_50_COP)


##Plot figures##

#velocity_Muscle(patient1.EMG_normalization, patient1.v_norm)
#COP_Muscle(patient1.EMG_normalization, patient1.COP)
#group_LR_COP(patient1.COP_norm, patient1.EMG_normalization, patient1.v_norm, patient1.acel_norm, "Patient1 Healthy")
#group_FB_COP(patient1.COP_norm, patient1.EMG_normalization, patient1.v_norm, patient1.acel_norm, "Patient1 Healthy")
#groupmuscles_COP(patient1.COP_norm, patient1.EMG_normalization, "Patient1 Healthy")

#fig1_max_platform = graph(patient1.EMG_max_values, patient1.COP,"Patient6", patient1.trajec, patient1.c, patient1.mean, platform = True)



#http://www.scielo.br/pdf/bjmbr/v42n7/7329.pdf
#http://nwpii.com/ajbms/papers/AJBMS_2009_4_11.pdf


