from tools import *
from scipy import signal
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import novainstrumentation as ni
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model


file = "Egas_Moniz_Segments/Patient1_EA.h5"

patient1 = Patient(file, platform=True, verbose=True)

patient1.static_avg = avg_out(patient1.static)
patient1.EMG_avg = avg_out(patient1.EMG)
print '\033[93m' + "AVG_END" + '\033[0m'

patient1.static_RMS = RMS_whole_segment(patient1.static_avg)
patient1.EMG_RMS = RMS_whole_segment(patient1.EMG_avg)
print '\033[93m' + "RMS_END" + '\033[0m'

patient1.max_MVC_back = max_mvc(patient1.static_RMS["MVC_back/MVC1"], patient1.static_RMS["MVC_back/MVC2"], patient1.static_RMS["MVC_back/MVC3"])
print '\033[93m' + "MAX_back_END" + '\033[0m'

patient1.max_MVC_rectus = max_mvc(patient1.static_RMS["MVC_rectus/MVC1"], patient1.static_RMS["MVC_rectus/MVC2"], patient1.static_RMS["MVC_rectus/MVC3"])
print '\033[93m' + "MAX_rectus_END" + '\033[0m'

patient1.max_MVC_RO = max_mvc(patient1.static_RMS["MVC_RO/MVC1"], patient1.static_RMS["MVC_RO/MVC2"], patient1.static_RMS["MVC_RO/MVC3"])
print '\033[93m' + "MAX_RO_END" + '\033[0m'

patient1.max_MVC_LO = max_mvc(patient1.static_RMS["MVC_LO/MVC1"], patient1.static_RMS["MVC_LO/MVC2"], patient1.static_RMS["MVC_LO/MVC3"])
print '\033[93m' + "MAX_LO_END" + '\033[0m'

patient1.static_normalization, patient1.static_max_values, patient1.static_mean_values = norm_whole_segment(patient1.static_RMS, patient1.max_MVC_back, patient1.max_MVC_rectus, patient1.max_MVC_RO, patient1.max_MVC_LO)
patient1.EMG_normalization, patient1.EMG_max_values, patient1.EMG_mean_values = norm_whole_segment(patient1.EMG_RMS, patient1.max_MVC_back, patient1.max_MVC_rectus, patient1.max_MVC_RO, patient1.max_MVC_LO)
print '\033[93m' + "NORM_END" + '\033[0m'


# patient1.platformdata = RAW_2_mass(patient1.platform)
# patient1.COP = mass_2_COP(patient1.platformdata)
# print '\033[93m' + "COP_END" + '\033[0m'
#
# patient1.std = desviation(patient1.COP)
# print '\033[93m' + "STD_COP_END" + '\033[0m'
#
# patient1.amplitude = amplitude(patient1.COP)
# print '\033[93m' + "AMP_COP_END" + '\033[0m'
#
# patient1.velocity, patient1.mean, patient1.acelaration = velocity_COP(patient1.COP)
# print '\033[93m' + "VELOCITY_END" + '\033[0m'

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

# patient1.fre_EMG, patient1.pxx_EMG = fourier_EMG(patient1.EMG_avg)
# print '\033[93m' + "FOURRIER_EMG_END" + '\033[0m'
#
# patient1.peak_EMG, patient1.meanf_EMG, patient1.f_80_EMG, patient1.f_50_EMG = parameters_fourier_EMG(patient1.fre_EMG, patient1.pxx_EMG)
# print '\033[93m' + "FOURRIER_EMG_PARAMETERS_END" + '\033[0m'
#
# patient1.fre_EMG_rest, patient1.pxx_EMG_rest = fourier_EMG(patient1.static_normalization)
# print '\033[93m' + "FOURRIER_REST_END" + '\033[0m'
#
# patient1.peak_EMG_rest, patient1.meanf_EMG_rest, patient1.f_80_EMG_rest, patient1.f_50_EMG_rest = parameters_fourier_EMG(patient1.fre_EMG_rest, patient1.pxx_EMG_rest)
# print '\033[93m' + "FOURRIER_EMG_REST_PARAMETERS_END" + '\033[0m'
#
# patient1.freq_COP, patient1.pxx_COP = fourier_COP(patient1.COP)
# print '\033[93m' + "FOURRIER_EMG_END" + '\033[0m'
#
# patient1.peak_COP, patient1.meanf_COP, patient1.f_80_COP, patient1.f_50_COP = parameters_fourrier_COP(patient1.freq_COP, patient1.pxx_COP)
# print '\033[93m' + "FOURRIER_COP_PARAMETERS_END" + '\033[0m'
#
# patient1.std_evolution, patient1.velocity_evolution, patient1.area_e = evolution_parameters(patient1.COP, patient1.velocity)
# print '\033[93m' + "EVOLUTION_COP_PARAMETERS" + '\033[0m'
#
# patient1.EMG_evolution = evolution_EMG(patient1.EMG_max_values, patient1.EMG_normalization)
# print '\033[93m' + "EVOLUTION_EMG" + '\033[0m'




#Creating database##

# # create_database()

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
# rest_parameters(patient1.static_max_values,patient1.peak_EMG_rest, patient1.meanf_EMG_rest, patient1.f_50_EMG_rest, patient1.f_80_EMG_rest)
# mean_values_EMG(patient1.EMG_mean_values)
# rest_mean_values(patient1.static_mean_values)
# evolution_parameters_COP(patient1.std_evolution, patient1.velocity_evolution, patient1.area_e, patient1.COP)
# EMG_evolution(patient1.EMG_evolution)

# patient1.max_MVC_back = max_mvc(patient1.static_RMS["MVC1"], patient1.static_RMS["MVC2"], [])
# print '\033[93m' + "MAX_back_END" + '\033[0m'
#
# patient1.max_MVC_rectus = max_mvc(patient1.static_RMS["MVC1"], patient1.static_RMS["MVC2"], [])
# print '\033[93m' + "MAX_rectus_END" + '\033[0m'
#
# patient1.max_MVC_RO = max_mvc(patient1.static_RMS["MVC1"], patient1.static_RMS["MVC2"], [])
# print '\033[93m' + "MAX_RO_END" + '\033[0m'
#
# patient1.max_MVC_LO = max_mvc(patient1.static_RMS["MVC1"], patient1.static_RMS["MVC2"], [])
# print '\033[93m' + "MAX_LO_END" + '\033[0m'

#####################################################################################################

# over30_EMG_value, male_EMG_value, female_EMG_value, EA_over30_EMG_value, EA_more_EMG_value = get_value_tonus(patient1.EMG_normalization)

# over30_freq, male_freq, female_freq, EA_over30_freq, EA_more_freq = get_value_freq(patient1.peak_EMG)

# over30_cop, male_cop, female_cop, EA_over30_cop, EA_more_cop = get_values_COP(patient1.mean)

# over30_cop_freq, male_cop_freq, female_cop_freq, EA_over30_cop_freq, EA_more_cop_freq = get_values_COP_freq(patient1.peak_COP)

# over30_freq_rest, male_freq_rest, female_freq_rest, EA_over30_freq_rest, EA_more_freq_rest = get_value_freq_rest()

over30_tonus_rest, male_tonus_rest, female_tonus_rest, EA_over30_tonus_rest, EA_more_tonus_rest = get_value_tonus_rest()

# over30_freq_new, male_freq_new, female_freq_new, EA_over30_freq_new, EA_more_freq_new = delete_EMG_values_freqs(over30_freq, male_freq, female_freq, EA_over30_freq, EA_more_freq)

# over30_tonus_new, male_tonus_new, female_tonus_new, EA_over30_tonus_new, EA_more_tonus_new = delete_EMG_values_tonus(over30_EMG_value, male_EMG_value, female_EMG_value, EA_over30_EMG_value, EA_more_EMG_value)

# over30_tonus_mean, male_tonus_mean, female_tonus_mean, EA_over30_tonus_mean, EA_more_tonus_mean = get_value_mean_tonus(patient1.EMG_normalization)

# over30_mean_tonus_new, male_mean_tonus_new, female_mean_tonus_new, EA_over30_mean_tonus_new, EA_more_mean_tonus_new = delete_EMG_values_tonus(over30_tonus_mean, male_tonus_mean, female_tonus_mean, EA_over30_tonus_mean, EA_more_tonus_mean)

over30_rest_mean, male_rest_mean, female_rest_mean, EA_over30_rest_mean, EA_more_rest_mean = get_value_mean_tonus_rest()

# over30_EMG, male_EMG, female_EMG, EA_over30_EMG, EA_more_EMG = get_EMG_evolution(patient1.EMG_evolution)

# over30_COP, male_COP, female_COP, EA_over30_COP, EA_more_COP = get_COP_evolution(patient1.area_e)

# over30_area, male_area, female_area, EA_over30_area, EA_more_area = get_evolution_area(patient1.area_e)

# over30_freqs_rest_e, male_freqs_rest_e, female_freqs_rest_e, EAover30_freqs_rest_e, EAmore_freqs_rest_e = eliminate_rest_freqs(over30_freq_rest, male_freq_rest, female_freq_rest, EA_over30_freq_rest, EA_more_freq_rest)

# over30_freqs_rest_new, male_freqs_rest_new, female_freqs_rest_new, EAover30_freqs_rest_new, EAmore_freqs_rest_new = eliminate_none_freqs(over30_freqs_rest_e, male_freqs_rest_e, female_freqs_rest_e, EAover30_freqs_rest_e, EAmore_freqs_rest_e)

# over30_pdata, male_pdata, female_pdata, EA_over30_pdata, EA_more_pdata = get_IMC()

# over30_IMC, male_IMC, IMC_female, IMC_over30_EA, IMC_moreEA = IMC_calculater(over30_pdata, male_pdata, female_pdata, EA_over30_pdata, EA_more_pdata)

# over30_muscle_peakEMG, male_muscle_peakEMG, female_muscle_peakEMG, EAover30_mucle_peakEMG, EAmore_mucle_peakEMG = mean_muscles_correlation(over30_EMG_value, male_EMG_value, female_EMG_value, EA_over30_EMG_value, EA_more_EMG_value)

# over30_task_peakEMG, male_task_peakEMG, female_task_peakEMG, EAover30_task_peakEMG, EAmore_task_peakEMG = correlation_samemuscle_tasks(over30_EMG_value, male_EMG_value, female_EMG_value, EA_over30_EMG_value, EA_more_EMG_value)

over30_rest_peakEMG_new, male_rest_peakEMG_new, female_rest_peakEMG_new, EAover30_rest_peakEMG_new, EAmore_rest_peakEMG_new = eliminate_rest_values(over30_tonus_rest, male_tonus_rest, female_tonus_rest, EA_over30_tonus_rest, EA_more_tonus_rest)

over30_rest_meanEMG_new, male_rest_meanEMG_new, female_rest_meanEMG_new, EAover30_rest_meanEMG_new, EAmore_rest_meanEMG_new = eliminate_rest_values(over30_rest_mean, male_rest_mean, female_rest_mean, EA_over30_rest_mean, EA_more_rest_mean)


# EMG_values_boxplot(over30_tonus_new, male_tonus_new, female_tonus_new, EA_over30_tonus_new, EA_more_tonus_new)
# EMG_freq_front_boxplot(over30_freq_new, male_freq_new, female_freq_new, EA_over30_freq_new, EA_more_freq_new)
# EMG_freq_back_boxplot(over30_freq_new, male_freq_new, female_freq_new, EA_over30_freq_new, EA_more_freq_new)
# COP_parameters_boxplot(over30_cop, male_cop, female_cop, EA_over30_cop, EA_more_cop)
# COP_freq_boxplot(over30_cop_freq, male_cop_freq, female_cop_freq, EA_over30_cop_freq, EA_more_cop_freq)
# task_vs_relax(over30_EMG_value, male_EMG_value, female_EMG_value, EA_over30_EMG_value, EA_more_EMG_value,
#               over30_tonus_rest, male_tonus_rest, female_tonus_rest, EA_over30_tonus_rest, EA_more_tonus_rest)
# plot_evalution_graphs(over30_EMG, male_EMG, female_EMG, EA_over30_EMG, EA_more_EMG,
#                        over30_COP, male_COP, female_COP, EA_over30_COP, EA_more_COP,
#                        over30_area, male_area, female_area, EA_over30_area, EA_more_area)
# EMG_mean_values_boxplot(over30_mean_tonus_new, male_mean_tonus_new, female_mean_tonus_new,
#                         EA_over30_mean_tonus_new, EA_more_mean_tonus_new)
# mean_task_vs_relax(over30_tonus_mean, male_tonus_mean, female_tonus_mean, EA_over30_tonus_mean, EA_more_tonus_mean,
              #over30_rest_mean, male_rest_mean, female_rest_mean, EA_over30_rest_mean, EA_more_rest_mean)
# EMG_freq_rest_back_boxplot(over30_freqs_rest_new, male_freqs_rest_new, female_freqs_rest_new, EAover30_freqs_rest_new, EAmore_freqs_rest_new)
# EMG_freq_rest_front_boxplot(over30_freqs_rest_new, male_freqs_rest_new, female_freqs_rest_new, EAover30_freqs_rest_new, EAmore_freqs_rest_new)
EMG_rest_values_boxplot(over30_rest_peakEMG_new, male_rest_peakEMG_new, female_rest_peakEMG_new, EAover30_rest_peakEMG_new, EAmore_rest_peakEMG_new)
EMG_rest_meanvalues_boxplot(over30_rest_mean, male_rest_mean, female_rest_mean, EA_over30_rest_mean, EA_more_rest_mean)


#correlation_muscles(over30_muscle_peakEMG)
#correlation_tasks(EAover30_task_peakEMG)


