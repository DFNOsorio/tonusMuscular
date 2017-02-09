import h5py
import numpy as np
import matplotlib.pyplot as plt

def load_data (filename, place, segment):

    file = h5py.File(filename, 'r')

    data_group = file[place + "/" + segment]
    for i in range(0, len(data_group)):
        data= np.zeros((len(data_group["channel" + str(i+1)]), i+1))

    for t in range(0, len(data_group)):
        data[:, t] = data_group["channel" + str(t + 1)]
    return data

file = "Egas_Moniz_Segments/Paciente1_Ines_Healthy.h5"


#EMG data
AE_EMG= load_data(file,"EMG", "Arms_extension")
S_EO_EMG= load_data(file, "EMG", "Standing_EO")
S_EC_EMG= load_data(file, "EMG", "Standing_EC")
OneF_R_EO_EMG= load_data(file, "EMG", "OneFootStanding_R_EO")
OneF_R_EC_EMG= load_data(file, "EMG", "OneFootStanding_R_EC")
OneF_L_EO_EMG= load_data(file, "EMG", "OneFootStanding_L_EO")
OneF_L_EC_EMG= load_data(file, "EMG", "OneFootStanding_L_EC")
Reach_R_EMG= load_data(file, "EMG","Reach_R")
Reach_L_EMG= load_data(file, "EMG","Reach_L")
Reach_C_EMG= load_data(file, "EMG","Reach_C")
Reach_G_EMG= load_data(file, "EMG", "Reach_Ground")

#Static data
#MVC1= load_data(file, "Static", "MVC1")
MVC2= load_data(file, "Static", "MVC2")
Relax= load_data(file, "Static", "Relax")

#Platform data
AE_plat= load_data(file,"Platform", "Arms_extension")
S_EO_plat= load_data(file, "Platform", "Standing_EO")
S_EC_plat= load_data(file, "Platform", "Standing_EC")
OneF_R_EO_plat= load_data(file, "Platform", "OneFootStanding_R_EO")
OneF_R_EC_plat= load_data(file, "Platform", "OneFootStanding_R_EC")
OneF_L_EO_plat= load_data(file, "Platform", "OneFootStanding_L_EO")
OneF_L_EC_plat= load_data(file, "Platform", "OneFootStanding_L_EC")
Reach_R_plat= load_data(file, "Platform","Reach_R")
Reach_L_plat= load_data(file, "Platform","Reach_L")
Reach_C_plat= load_data(file, "Platform","Reach_C")
Reach_G_EMG= load_data(file, "EMG", "Reach_Ground")

plt.plot(OneF_L_EC_plat[:,0])
plt.show()