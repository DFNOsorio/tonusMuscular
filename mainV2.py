from tools import *
from scipy import signal
from scipy.signal import butter, lfilter, freqz
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
#patient1.COP = []
print '\033[93m' + "COP_END" + '\033[0m'

velocity, mean = velocity_COP(patient1.COP)
print '\033[93m' + "VELOCITY_END" + '\033[0m'

trajec = trajectory(patient1.COP)
print '\033[93m' + "TRAJ_END" + '\033[0m'

c= coherence(patient1.COP, patient1.EMG_normalization)
print '\033[93m' + "COHERENCY_END" + '\033[0m'

#COP_Muscle(patient1.EMG_normalization, patient1.COP)

fig1_max_platform = graph(patient1.EMG_max_values, patient1.COP,"Ines", trajec, c, mean, platform = True)



#fig1_max_platform = graph_platform(patient1.EMG_max_values, patient1.COP,"patient1_Lupus", platform = False)
#fig2_RMS = graph_RMS(patient1.EMG_RMS, "MJ_Lupus")
#fig3_normalization = graph_normalizedRMS(patient1.EMG_normalization, "MJ_Lupus")


