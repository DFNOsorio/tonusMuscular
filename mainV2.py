from tools import *

import matplotlib.pyplot as plt


file = "Egas_Moniz_Segments/Paciente1_Ines_Healthy.h5"

patient1 = Patient(file, platform = False, verbose = True)

patient1.staticRMS = RMS_whole_segment(patient1.static)

## FAZ ISTO PARA OS RESTAnTES INTERVALOS PARA TESTARES
# patient1.platform
# patient1.EMG

plt.figure()
plt.plot(patient1.static["MVC2"][:, 0])
plt.plot(np.linspace(0, len(patient1.static["MVC2"][:, 0]), len(patient1.staticRMS["MVC2"][:, 0])), patient1.staticRMS["MVC2"][:, 0])
plt.show()



