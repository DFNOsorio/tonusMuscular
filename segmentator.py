# -*- coding: utf-8 -*-

import h5py
import numpy as np
import matplotlib.pyplot as plt


filename1 = 'Testes_Egas_Moniz/patient_1_mvc_0007803B4638_2016-11-28_12-28-21.h5'
filename2 = 'Testes_Egas_Moniz/patient_1_plataforma_0007803B4638_2016-11-28_12-37-24.h5'
filename3 = 'Testes_Egas_Moniz/patient_1_plataforma_0007803B4638_2016-11-28_12-41-14.h5'
filename4 = 'Testes_Egas_Moniz/patient_1_plataforma_0007803B4638_2016-11-28_12-43-17.h5'
filename5 = 'Testes_Egas_Moniz/patient_1_plataforma_000780646DDA_0007803B4638_2016-11-28_12-31-22.h5'
filename6 = 'Testes_Egas_Moniz/patient_1_plataforma_000780646DDA_0007803B4638_2016-11-28_12-33-04.h5'
filename7 = 'Testes_Egas_Moniz/teste_000780646DDA_0007803B4638_2016-11-28_12-46-36.h5'
filename8 = 'Testes_Egas_Moniz/patient_1_repouso_0007803B4638_2016-11-28_12-27-00.h5'


filename_w='Egas_Moniz_Segments/Paciente1_MJ_Lupus.h5'


def load_data_h5(filename, platform = False):

    time = []

    file = h5py.File(filename, 'r')

    file_macs = file.keys()

    EMG_mac = '00:07:80:3B:46:38' #  Este e o mac addresss dos EMGS sempre

    if file_macs[0] == '00:07:80:3B:46:38' and platform: ## Se existir plataform e o primeiro mac for o dos EMGs

        platform_mac = file_macs[1]

    elif platform:  ## Se existir plataforma e o primeirpo mac nao é dos EMGs

        platform_mac =  file_macs[0]

    definitions = [file[EMG_mac].attrs["sampling rate"]*1.0, file[EMG_mac].attrs["resolution"]*1.0]

    ## Load EMGs data
    EMG_data_group = file[EMG_mac + "/raw"]

    time = np.linspace(0, len(EMG_data_group['nSeq'][:, 0])/1000.0, len(EMG_data_group['nSeq'][:, 0]))
    ## time = EMG_data_group['nSeq'][:, 0] / definitions[0]

    EMG_data = np.zeros((file[EMG_mac].attrs["nsamples"], len(EMG_data_group)-1))

    EMG_labels = []
    for i in range(0, len(EMG_data_group)-1):
        EMG_labels.append(EMG_data_group['channel_' + str(i+1)].attrs['label'])
        EMG_data[:, i] = EMG_data_group['channel_' + str(i+1)][:, 0]

    ## Load Platform data if any

    if platform:

        platform_data_group = file[platform_mac + "/raw"]

        platform_data = np.zeros((file[platform_mac].attrs["nsamples"], len(platform_data_group)-1))

        platform_labels = []

        for i in range(0, len(platform_data_group)-1):
            platform_labels.append(platform_data_group['channel_' + str(i+1)].attrs['label'])
            platform_data[:, i] = platform_data_group['channel_' + str(i+1)][:, 0]

        return time, EMG_data, EMG_labels, platform_data, platform_labels

    else:

        return time, EMG_data, EMG_labels

def segments(time, data, start, end):
    segment_data = []
    #SUBSTITUIR POR INDEX QUE É MAIS FACIL

    for idx,t in enumerate(time):
        if idx == (start*1000):
            time1=idx

    for idx2, t2 in enumerate(time):
        if idx2 == (end*1000):
            time2=idx2

    for index, value in enumerate(data):
        if index >= time1 and index <= time2:
            segment_data=data[time1:time2,:]

    return segment_data

def load_data(segment_data, segment):
    for x, y in enumerate(segment_data):
        if x<=7:
            channel=x+1
            f_new[segment].create_dataset('channel'+ str(channel), data=segment_data[:, x])
            x += 1



rest_time, rest_EMG_data, rest_EMG_lables       = load_data_h5(filename8)

MVC1_time, MVC1_EMG_data, MVC1_EMG_lables       = load_data_h5(filename1)

plat1_time, plat1_EMG_data, plat1_EMG_lables    = load_data_h5(filename2)
plat2_time, plat2_EMG_data, plat2_EMG_lables    = load_data_h5(filename3)
plat3_time, plat3_EMG_data, plat3_EMG_lables    = load_data_h5(filename4)
plat4_time, plat4_EMG_data, plat4_EMG_lables, plat4_data, plat4_lables    = load_data_h5(filename5)
plat5_time, plat5_EMG_data, plat5_EMG_lables, plat5_data, plat5_lables    = load_data_h5(filename6)
plat6_time, plat6_EMG_data, plat6_EMG_lables, plat6_data, plat6_lables    = load_data_h5(filename7)

plt.plot(plat2_EMG_data)
plt.show()

f_new = h5py.File(filename_w, 'w')

atrib1 = f_new.attrs['Name'] = 'M.J.'
atrib2 = f_new.attrs['Gender'] = 'F'
atrib3 = f_new.attrs['Age'] = 54
atrib4 = f_new.attrs['Condition'] = 'Lupus'
atrib5 = f_new.attrs ['Channel1'] = 'RA_L'
atrib6 = f_new.attrs ['Channel2'] = 'RA_R'
atrib7 = f_new.attrs ['Channel3'] = 'O_L'
atrib8 = f_new.attrs ['Channel4'] = 'O_R'
atrib9 = f_new.attrs ['Channel5'] = 'I_L'
atrib10 = f_new.attrs ['Channel6'] = 'I_R'
atrib11 = f_new.attrs ['Channel7'] = 'M_L'
atrib12 = f_new.attrs ['Channel8'] = 'M_R'


f_new.create_group('Static/MVC1')
f_new.create_group('Static/MVC2')
f_new.create_group('Static/Relax')

f_new.create_group('EMG/Arms_extension')
f_new.create_group('EMG/Standing_EO')
f_new.create_group('EMG/Standing_EC')
f_new.create_group('EMG/OneFootStanding_R_EO')
f_new.create_group('EMG/OneFootStanding_R_EC')
f_new.create_group('EMG/OneFootStanding_L_EO')
f_new.create_group('EMG/OneFootStanding_L_EC')
f_new.create_group('EMG/Reach_R')
f_new.create_group('EMG/Reach_L')
f_new.create_group('EMG/Reach_C')
f_new.create_group('EMG/Reach_Ground')

f_new.create_group('Platform/Arms_extension')
f_new.create_group('Platform/Standing_EO')
f_new.create_group('Platform/Standing_EC')
f_new.create_group('Platform/OneFootStanding_R_EO')
f_new.create_group('Platform/OneFootStanding_R_EC')
f_new.create_group('Platform/OneFootStanding_L_EO')
f_new.create_group('Platform/OneFootStanding_L_EC')
f_new.create_group('Platform/Reach_R')
f_new.create_group('Platform/Reach_L')
f_new.create_group('Platform/Reach_C')
f_new.create_group('Platform/Reach_Ground')

sliceMVC1=10.0
slice_2_MVC1= 19.0
sliceMVC2=20.0
slice_2_MVC2= 30.149

slice_AE=16.0
slice_2_AE=31.0
slice_2FS=41.0
slice_2_2FS=71.0

slice_2FS_EC=0
slice_2_2FS_EC=28.0
#slice_RF_EO=0.0
#slice_2_RF_EO=30.0
#slice_RF_EC=49.0
#slice_2_RF_EC=79.0
slice_LF_EO = 77.0
slice_2_LF_EO= 107.0
#slice_LF_EC = 136.0
#slice_LF2_EC = 173
slice_reach_R = 139.0
slice_reach2_R = 145.0
slice_reach_L = 150.0
slice_reach2_L = 156.0
slice_reach_C =160
slice_reach2_C = 166.0
slice_reach_G = 177.0
slice_reach2_G = 215.399

slice_repouso=0
slice_2_repouso = 16.198

rest_segment = segments(rest_time, rest_EMG_data, slice_repouso, slice_2_repouso)

MVC1_segment = segments(MVC1_time, MVC1_EMG_data, sliceMVC1, slice_2_MVC1)
MVC2_segment = segments(MVC1_time, MVC1_EMG_data, sliceMVC2, slice_2_MVC2)

AE_segment     = segments(plat1_time, plat1_EMG_data, slice_AE, slice_2_AE)
FS_segment    = segments(plat1_time, plat1_EMG_data, slice_2FS, slice_2_2FS)
FS_EC_segment = segments(plat2_time, plat2_EMG_data, slice_2FS_EC, slice_2_2FS_EC)
#RF_EO_segment  = segments(plat2_time, plat2_EMG_data, slice_RF_EO, slice_2_RF_EO)
#RF_EC_segment  = segments(plat3_time, plat3_EMG_data, slice_RF_EC, slice_2_RF_EC)
LF_EO_segment = segments(plat2_time, plat2_EMG_data, slice_LF_EO, slice_2_LF_EO)
#LF_EC_segment = segments(plat3_time, plat3_EMG_data, slice_LF_EC, slice_LF2_EC)
reach_R_segment = segments(plat2_time, plat2_EMG_data, slice_reach_R, slice_reach2_R)
reach_L_segment = segments(plat2_time, plat2_EMG_data, slice_reach_L, slice_reach2_L)
reach_C_segment = segments(plat2_time, plat2_EMG_data, slice_reach_C, slice_reach2_C)
reach_G_segment = segments(plat2_time, plat2_EMG_data, slice_reach_G, slice_reach2_G)


load_data(rest_segment, 'Static/Relax')
load_data(MVC1_segment, "Static/MVC1")
load_data(MVC2_segment, "Static/MVC2")

load_data(AE_segment, "EMG/Arms_extension")
load_data(FS_segment, "EMG/Standing_EO")
load_data(FS_EC_segment, "EMG/Standing_EC")
#load_data(RF_EO_segment, "EMG/OneFootStanding_R_EO")
#load_data(RF_EC_segment, "EMG/OneFootStanding_R_EC")
load_data(LF_EO_segment, "EMG/OneFootStanding_L_EO")
#load_data(LF_EC_segment, "EMG/OneFootStanding_L_EC")
load_data(reach_R_segment, "EMG/Reach_R")
load_data(reach_L_segment, "EMG/Reach_L")
load_data(reach_G_segment, "EMG/Reach_Ground")
load_data(reach_C_segment, "EMG/Reach_C")
### Faltam os outros
