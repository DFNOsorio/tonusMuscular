from tools import *

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

file = "Egas_Moniz_Segments/Paciente1_Ines_Healthy.h5"

patient1 = Patient(file, platform = True, verbose = True)

patient1.staticAVR = avg_out(patient1.static)
patient1.EMG_AVR = avg_out(patient1.EMG)
patient1.platform_AVR = avg_out(patient1.platform)
patient1.staticRMS = RMS_whole_segment(patient1.staticAVR)
patient1.EMG_RMS = RMS_whole_segment(patient1.EMG_AVR)  ##index ao contrario
patient1.platform_RMS = RMS_whole_segment(patient1.platform_AVR)
patient1.normalization_EMG = normalization(patient1)    ##index ao contrario
patient1.max_values = max_normalization(patient1)       ##index ao contrario
#patient1.correlation = correlation(patient1)

#plt.figure()
#plt.plot(patient1.EMG_RMS["Reach_L"][0,:])
#plt.plot(patient1.normalization_EMG["Reach_L"][0,:], linewidth=2.5)
#plt.show()
## FAZ ISTO PARA OS RESTAnTES INTERVALOS PARA TESTARES
# patient1.platform
# patient1.EMG

#plt.figure()
#plt.plot(patient1.static["MVC2"][:, 0])
#plt.plot(np.linspace(0, len(patient1.static["MVC2"][:, 0]), len(patient1.staticRMS["MVC2"][:, 0])), patient1.staticRMS["MVC2"][:, 0])
#plt.show()


## Max Values of normalized RMS
f=plt.figure()
values = {}
for i in range(0, 8):
    plt.subplot(2,4, i+1)
    y = np.zeros(len(patient1.max_values))
    ind = np.arange(11)
    width = 1
    error_config = {'ecolor': '0.3', 'capthick': 0.5}
    l=0
    for j in patient1.max_values:
        y[l] = patient1.max_values[j][i,:]
        l=l+1
    plt.bar(ind,y, width, error_kw=error_config)
    plt.xticks(ind + width/2.0, ("1","2", "3", "4", "5", "6", "7", "8", "9", "10", "11"), fontsize=7)
    plt.suptitle("Maximum for each test", fontsize=24)
    if i == 0:
        plt.ylabel("Percentage from MVC maximum.(%)\n Rectus Abdominis_L")
    if i == 1:
        plt.ylabel("Percentage from MVC maximum.(%)\n Rectus Abdominis_R")
    if i == 2:
        plt.ylabel("Percentage from MVC maximum.(%)\n Obliques_L")
    if i == 3:
        plt.ylabel("Percentage from MVC maximum.(%)\n Obliques_R")
    if i == 4:
        plt.ylabel("Percentage from MVC maximum.(%)\n Ilicostalis_L")
    if i == 5:
        plt.ylabel("Percentage from MVC maximum.(%)\n Ilicostalis_R")
    if i == 6:
        plt.ylabel("Percentage from MVC maximum.(%)\n Multifundus_L")
    if i == 7:
        plt.ylabel("Percentage from MVC maximum.(%)\n Multifundus_R")

data = ('1 - Arms_Extension\n'
        '2 - Standing_EO\n'
        '3 - Standing_EC\n'
        '4 - One Foot Standing_R_EO\n'
        '5 - One Foot Standing_R_EC\n'
        '6 - One Foot Standing_L_EO\n'
        '7 - One Foot Standing_L_EC\n'
        '8 - Reach_R\n'
        '9 - Reach_L\n'
        '10 - Reach_C\n'
        '11 - Reach_Ground\n')

plt.text(35,35,data)
plt.subplots_adjust(right=0.6,wspace=0.7, hspace=0.3)
plt.show()


##Normalized RMS
for j in range (0,8):
    for i in patient1.normalization_EMG:
        plt.plot(patient1.normalization_EMG[i][j,:])
        plt.xlabel("Time in miliseconds", fontsize=7)
        plt.suptitle("Normalized RMS", fontsize=24)
        if j == 0:
            plt.ylabel("Normalized RMS\n Rectus Abdominis_L")
        if j == 1:
            plt.ylabel("Normalized RMS\n Rectus Abdominis_R")
        if j == 2:
            plt.ylabel("Normalized RMS\n Obliques_L")
        if j == 3:
            plt.ylabel("Normalized RMS\n Obliques_R")
        if j == 4:
            plt.ylabel("Normalized RMS\n Ilicostalis_L")
        if j == 5:
            plt.ylabel("Normalized RMS\n Ilicostalis_R")
        if j == 6:
            plt.ylabel("Normalized RMS\n Multifundus_L")
        if j == 7:
            plt.ylabel("Normalized RMS\n Multifundus_R")
    plt.show()



#Mean normalized RMS value for each data set for each muscule

plt.figure()
for i in range(0, 8):
    plt.subplot(2,4, i+1)
    y = np.zeros(len(patient1.normalization_EMG))
    ind = np.arange(11)
    width = 1
    error_config = {'ecolor': '0.3', 'capthick': 0.5}
    l=0
    for j in patient1.normalization_EMG:
        y[l] = np.mean(patient1.normalization_EMG[j][i,:])
        l=l+1
    plt.bar(ind,y, width, error_kw=error_config)
    plt.xticks(ind + width/2.0, ("1","2", "3", "4", "5", "6", "7", "8", "9", "10", "11"), fontsize=7)
    plt.suptitle("Mean Value for each test", fontsize=24)
    if i == 0:
        plt.ylabel("Mean Value of normalized RMS\n Rectus Abdominis_L")
    if i == 1:
        plt.ylabel("Mean Value of normalized RMS\n Rectus Abdominis_R")
    if i == 2:
        plt.ylabel("Mean Value of normalized RMS\n Obliques_L")
    if i == 3:
        plt.ylabel("Mean Value of normalized RMS\n Obliques_R")
    if i == 4:
        plt.ylabel("Mean Value of normalized RMS\n Ilicostalis_L")
    if i == 5:
        plt.ylabel("Mean Value of normalized RMS\n Ilicostalis_R")
    if i == 6:
        plt.ylabel("Mean Value of normalized RMS\n Multifundus_L")
    if i == 7:
        plt.ylabel("Mean Value of normalized RMS\n Multifundus_R")

description = ('1 - Arms Extension\n'
               '2 - Standing EO\n'
               '3 - Standing EC\n'
               '4 - One Foot Standing R EO\n'
               '5 - One Foot Standing R EC\n'
               '6 - One Foot Standing L EO\n'
               '7 - One Foot Standing L EC\n'
               '8 - Reach R\n'
               '9 - Reach L\n'
               '10 - Reach C\n'
               '11 - Reach Ground')

plt.text(0,0,description)
plt.subplots_adjust(right=0.6,wspace=0.7, hspace=0.3)
plt.show()

##EMG RMS
for j in range (0,8):
    for i in patient1.EMG_RMS:
        plt4=plt.plot(patient1.EMG_RMS[i][j,:])
        plt.xlabel("Time in miliseconds", fontsize=7)
        if j == 0:
            plt.ylabel("RMS of EMG\n Rectus Abdominis_L")
        if j == 1:
            plt.ylabel("RMS of EMG\n Rectus Abdominis_R")
        if j == 2:
            plt.ylabel("RMS of EMG\n Obliques_L")
        if j == 3:
            plt.ylabel("RMS of EMG\n Obliques_R")
        if j == 4:
            plt.ylabel("RMS of EMG\n Ilicostalis_L")
        if j == 5:
            plt.ylabel("RMS of EMG\n Ilicostalis_R")
        if j == 6:
            plt.ylabel("RMS of EMG\n Multifundus_L")
        if j == 7:
            plt.ylabel("RMS of EMG\n Multifundus_R")
        plt.suptitle("RMS", fontsize=24)
    plt.show()

#f.savefig("foo.pdf", bbox_inches='tight')