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


## SO PARA UM FICEIRO
def RMS(signal, window_size=100, overlap=-1):

    if overlap>window_size or overlap==-1:

        overlap = window_size - 1

    delta = int(window_size - overlap)  ## Numero de pontos em que as janelas nao se sobrepoem. Por exemplo se a janela for 500 e o Overlap 499, entao todos os pontos vao ser considerados. Por outro lado se a janela for 500 e o overlap for 0, entao nao ha sobreposicao de janelas.

    indexes = []

    [[indexes.append(i)] for i in range(0, len(signal), delta)]

    RMS = np.zeros(len(indexes))

    c = 0
    for i in indexes:
        lower_bound = max([0, i-window_size/2])
        upper_bound = min([len(signal), i+window_size/2])
        RMS[c] = np.sqrt(np.mean(np.power(signal[lower_bound:upper_bound], 2)))
        c+=1

    return RMS

def RMS_whole_segment(segment, window_size=100, overlap=-1):

    RMS = np.zeros((1, len(segment[:, 0])))
    print len(segment[0, :])
    print RMS

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

#plt.plot(Reach_C_EMG_avr[:,0])
#plt.show()

## RMS

#EMG
## RMS

#EMG
window_size = 100
AE_EMG_RMS = RMS(AE_EMG_avr[:, 1], window_size)
RMS_whole_segment(AE_EMG_avr, window_size)

plt.plot(np.linspace(0, len(AE_EMG_avr[:,0]), len(AE_EMG_RMS)), AE_EMG_RMS)
plt.show()

