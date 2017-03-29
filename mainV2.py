from tools import *

import matplotlib.pyplot as plt
from scipy import signal



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

velocity, mean = velocity_COP(patient1.COP)

trajec = trajectory(patient1.COP)

f, Cxy = signal.coherence(patient1.EMG_normalization["Arms_extension"][:,1], patient1.COP["Standing_EO"]["COP_Y"], 1000, nperseg=1024)

#plt.plot(f, Cxy)
#plt.xlabel('frequency [Hz]')
#plt.ylabel('Coherence')
#plt.show()

c= coherence(patient1.COP, patient1.EMG_normalization)

#plt.plot(c["Arms_extension"]["freqs_y"][:,1], c["Arms_extension"]["coherency_y"][:,1])
#plt.show()
fig1_max_platform = graph(patient1.EMG_max_values, patient1.COP,"Emma", trajec, c, platform = True)






#fig1_max_platform = graph_platform(patient1.EMG_max_values, patient1.COP,"patient1_Lupus", platform = False)
#fig2_RMS = graph_RMS(patient1.EMG_RMS, "MJ_Lupus")
#fig3_normalization = graph_normalizedRMS(patient1.EMG_normalization, "MJ_Lupus")


