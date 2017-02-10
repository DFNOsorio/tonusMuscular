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


def avarage_out(array):

    for t in range(0, len(array[1,:]-1)):
        array_avarage_out = np.zeros((len(array),t+1))

    for i in range(0, len(array[1,:])):
        array_avarage_out[:,i] = array[:,i] - np.mean(array[:,i])

    return array_avarage_out


def RMS(array):
    ms = 0
    for t in range(0, len(array[1,:]-1)):
        array_RMS = np.zeros((len(array),t+1))

    for i in range(0, len(array[1,:])-1):
        for x in range(0, len(array)):
            current_value = ms + np.power(array[x,i],2)
            array_RMS[x,i] = np.square(current_value / len(array))
            ms = current_value

    return array_RMS


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
#MVC1= load_data(file, "Static", "MVC1") ?????
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
Reach_G_plat= load_data(file, "EMG", "Reach_Ground")

#plt.plot(AE_EMG[:,7])
#plt.show()

##Avarage Out

#EMG
AE_EMG_avr = avarage_out(AE_EMG)
S_EO_EMG_avr = avarage_out(S_EO_EMG)
S_EC_EMG_avr = avarage_out(S_EC_EMG)
OneF_R_EO_EMG_avr = avarage_out(OneF_R_EO_EMG)
OneF_R_EC_EMG_avr = avarage_out(OneF_R_EC_EMG)
OneF_L_EO_EMG_avr = avarage_out(OneF_L_EO_EMG)
OneF_L_EC_EMG_avr = avarage_out(OneF_L_EC_EMG)
Reach_R_EMG_avr = avarage_out(Reach_R_EMG)
Reach_L_EMG_avr = avarage_out(Reach_L_EMG)
Reach_C_EMG_avr = avarage_out(Reach_C_EMG)
Reach_G_EMG_avr = avarage_out(Reach_G_EMG)

#Static
#MVC1_avr = avarage_out(MVC1) ????????
MVC2_avr = avarage_out(MVC2)
Relax_avr = avarage_out(Relax)

plt.plot(Reach_C_EMG_avr[:,0])
plt.show()

## RMS

#EMG
AE_EMG_RMS = RMS(Reach_C_EMG_avr)
plt.plot(AE_EMG_RMS[:,0])
plt.show()