from tools import *

import matplotlib.pyplot as plt


file = "Egas_Moniz_Segments/Paciente1_Ines_Healthy.h5"

patient1 = Patient(file, platform = False, verbose = True)

patient1.staticAVR = avg_out(patient1.static)
patient1.EMG_AVR = avg_out(patient1.EMG)
patient1.staticRMS = RMS_whole_segment(patient1.staticAVR)
patient1.EMG_RMS = RMS_whole_segment(patient1.EMG_AVR)  ##index ao contrario
patient1.normalization_EMG = normalization(patient1)    ##index ao contrario
patient1.max_values = max_normalization(patient1)       ##index ao contrario

## FAZ ISTO PARA OS RESTAnTES INTERVALOS PARA TESTARES
# patient1.platform
# patient1.EMG

#plt.figure()
#plt.plot(patient1.static["MVC2"][:, 0])
#plt.plot(np.linspace(0, len(patient1.static["MVC2"][:, 0]), len(patient1.staticRMS["MVC2"][:, 0])), patient1.staticRMS["MVC2"][:, 0])
#plt.show()



#print patient1.max_values["Arms_extension"]

#plt.plot(patient1.EMG_RMS["Arms_extension"][1,:])
#plt.show()

#plt.plot(patient1.normalization["Arms_extension"][1,:])
#plt.show()
#print(len(patient1.EMG_RMS))


