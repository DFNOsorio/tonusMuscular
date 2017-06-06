# -*- coding: utf-8 -*-

import h5py
import numpy as np
import matplotlib.pyplot as plt


filename1 = 'Testes_plat/Testes_FCT_dia1/patient_6_rest_EMGs_2017-06-01_18-04-06.h5'
filename2 = 'Testes_plat/Testes_FCT_dia1/patient_6_back_EMGs_2017-06-01_18-06-54.h5'
filename3 = 'Testes_plat/Testes_FCT_dia1/patient_6_front_EMGs_2017-06-01_18-04-57.h5'
filename4 = 'Testes_plat/Testes_FCT_dia1/patient_6_right_EMGs_2017-06-01_18-05-34.h5'
filename5 = 'Testes_plat/Testes_FCT_dia1/patient_6_left_EMGs_2017-06-01_18-06-11.h5'
filename6 = 'Testes_plat/Testes_FCT_dia1/patient_6_platform_Plataforma_EMGs_2017-06-01_18-08-00.h5'
#filename7 = 'Testes_plat/Testes_FCT_dia1/patient_4_platform_Plataforma_EMGs_2017-06-01_17-26-20.h5'




"""
if("plataforma in filename#):
    platform == True

"""
filename_w='Egas_Moniz_Segments/Patient13_Healthy.h5'


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

def load_data_plat(segment_data, segment):
    for x, y in enumerate(segment_data):
        if x<=3:
            channel=x+1
            f_new[segment].create_dataset('channel'+ str(channel), data=segment_data[:, x])
            x += 1

rest_time, rest_EMG_data, rest_EMG_lables       = load_data_h5(filename1)

MVC_back_time, MVC_back_EMG_data, MVC_back_EMG_lables       = load_data_h5(filename2)
MVC_rectus_time, MVC_rectus_EMG_data, MVC_rectus_EMG_lables = load_data_h5(filename3)
MVC_RO_time, MVC_RO_EMG_data, MVC_RO_EMG_lables             = load_data_h5(filename4)
MVC_LO_time, MVC_LO_EMG_data, MVC_LO_EMG_lables             = load_data_h5(filename5)

plat1_time, plat1_EMG_data, plat1_EMG_lables, plat1_data, plat1_lables    = load_data_h5(filename6, platform=True)
#plat2_time, plat2_EMG_data, plat2_EMG_lables, plat2_data, plat2_lables    = load_data_h5(filename7, platform=True)





f_new = h5py.File(filename_w, 'w')

atrib1 = f_new.attrs['Gender'] = 'M'
atrib2 = f_new.attrs['Age'] = 23
atrib3 = f_new.attrs['Condition'] = 'Healthy'
atrib4 = f_new.attrs['Dominant Hand'] = 'Right'
atrib5 = f_new.attrs['Height (cm)'] = 178
atrib6 = f_new.attrs['Weight (kg)'] = 86
atrib7 = f_new.attrs['Sports'] = 'Yes'

atrib8  = f_new.attrs ['Channel1'] = 'RA_L'
atrib9  = f_new.attrs ['Channel2'] = 'RA_R'
atrib10 = f_new.attrs ['Channel3'] = 'O_L'
atrib11 = f_new.attrs ['Channel4'] = 'O_R'
atrib12 = f_new.attrs ['Channel5'] = 'I_L'
atrib13 = f_new.attrs ['Channel6'] = 'I_R'
atrib14 = f_new.attrs ['Channel7'] = 'M_L'
atrib15 = f_new.attrs ['Channel8'] = 'M_R'


f_new.create_group('Static/MVC_back/MVC1')
f_new.create_group('Static/MVC_back/MVC2')
f_new.create_group('Static/MVC_back/MVC3')
f_new.create_group('Static/MVC_rectus/MVC1')
f_new.create_group('Static/MVC_rectus/MVC2')
f_new.create_group('Static/MVC_rectus/MVC3')
f_new.create_group('Static/MVC_RO/MVC1')
f_new.create_group('Static/MVC_RO/MVC2')
f_new.create_group('Static/MVC_RO/MVC3')
f_new.create_group('Static/MVC_LO/MVC1')
f_new.create_group('Static/MVC_LO/MVC2')
f_new.create_group('Static/MVC_LO/MVC3')
f_new.create_group('Static/Relax')


f_new.create_group('EMG/Standing_EO')
f_new.create_group('EMG/Standing_EC')
f_new.create_group('EMG/OneFootStanding_R_EO')
f_new.create_group('EMG/OneFootStanding_R_EC')
f_new.create_group('EMG/OneFootStanding_L_EO')
f_new.create_group('EMG/OneFootStanding_L_EC')
f_new.create_group('EMG/Reach_R')
f_new.create_group('EMG/Reach_L')
f_new.create_group('EMG/Reach_C')



f_new.create_group('Platform/Standing_EO')
f_new.create_group('Platform/Standing_EC')
f_new.create_group('Platform/OneFootStanding_R_EO')
f_new.create_group('Platform/OneFootStanding_R_EC')
f_new.create_group('Platform/OneFootStanding_L_EO')
f_new.create_group('Platform/OneFootStanding_L_EC')
f_new.create_group('Platform/Reach_R')
f_new.create_group('Platform/Reach_L')
f_new.create_group('Platform/Reach_C')


sliceMVC1_back  = 15
sliceMVC1_back2 = 19
sliceMVC2_back  = 20
sliceMVC2_back2 = 24
sliceMVC3_back  = 25
sliceMVC3_back2 = 29

sliceMVC1_rectus  = 8
sliceMVC1_rectus2 = 11
sliceMVC2_rectus  = 12
sliceMVC2_rectus2 = 16
sliceMVC3_rectus  = 17
sliceMVC3_rectus2 = 20

sliceMVC1_RO  = 7
sliceMVC1_RO2 = 11
sliceMVC2_RO  = 12
sliceMVC2_RO2 = 14
sliceMVC3_RO  = 15
sliceMVC3_RO2 = 19

sliceMVC1_LO  = 11
sliceMVC1_LO2 = 14
sliceMVC2_LO  = 15
sliceMVC2_LO2 = 18
sliceMVC3_LO  = 19
sliceMVC3_LO2 = 23


slice_2FS       = 18
slice_2_2FS     = 48
slice_2FS_EC    = 55
slice_2_2FS_EC  = 85
slice_RF_EO     = 104
slice_2_RF_EO   = 134
slice_RF_EC     = 149
slice_2_RF_EC   = 179
slice_LF_EO     = 196
slice_2_LF_EO   = 226
slice_LF_EC     = 240
slice_LF2_EC    = 265
slice_reach_R   = 303
slice_reach2_R  = 310
slice_reach_L   = 317
slice_reach2_L  = 324
slice_reach_C   = 337
slice_reach2_C  = 343


slice_repouso = 23
slice_2_repouso = 35



rest_segment = segments(rest_time, rest_EMG_data, slice_repouso, slice_2_repouso)

MVC1_back_segment = segments(MVC_back_time, MVC_back_EMG_data, sliceMVC1_back, sliceMVC1_back2)
MVC2_back_segment = segments(MVC_back_time, MVC_back_EMG_data, sliceMVC2_back, sliceMVC2_back2)
MVC3_back_segment = segments(MVC_back_time, MVC_back_EMG_data, sliceMVC3_back, sliceMVC3_back2)

MVC1_rectus_segment = segments(MVC_rectus_time, MVC_rectus_EMG_data,sliceMVC1_rectus, sliceMVC1_rectus2)
MVC2_rectus_segment = segments(MVC_rectus_time, MVC_rectus_EMG_data,sliceMVC2_rectus, sliceMVC2_rectus2)
MVC3_rectus_segment = segments(MVC_rectus_time, MVC_rectus_EMG_data,sliceMVC3_rectus, sliceMVC3_rectus2)

MVC1_RO_segment = segments(MVC_RO_time, MVC_RO_EMG_data, sliceMVC1_RO, sliceMVC1_RO2)
MVC2_RO_segment = segments(MVC_RO_time, MVC_RO_EMG_data, sliceMVC2_RO, sliceMVC2_RO2)
MVC3_RO_segment = segments(MVC_RO_time, MVC_RO_EMG_data, sliceMVC3_RO, sliceMVC3_RO2)

MVC1_LO_segment = segments(MVC_LO_time, MVC_LO_EMG_data, sliceMVC1_LO, sliceMVC1_LO2)
MVC2_LO_segment = segments(MVC_LO_time, MVC_LO_EMG_data, sliceMVC2_LO, sliceMVC2_LO2)
MVC3_LO_segment = segments(MVC_LO_time, MVC_LO_EMG_data, sliceMVC3_LO, sliceMVC3_LO2)


FS_segment      = segments(plat1_time, plat1_EMG_data, slice_2FS, slice_2_2FS)
FS_EC_segment   = segments(plat1_time, plat1_EMG_data, slice_2FS_EC, slice_2_2FS_EC)
RF_EO_segment   = segments(plat1_time, plat1_EMG_data, slice_RF_EO, slice_2_RF_EO)
RF_EC_segment   = segments(plat1_time, plat1_EMG_data, slice_RF_EC, slice_2_RF_EC)
LF_EO_segment   = segments(plat1_time, plat1_EMG_data, slice_LF_EO, slice_2_LF_EO)
LF_EC_segment   = segments(plat1_time, plat1_EMG_data, slice_LF_EC, slice_LF2_EC)
reach_R_segment = segments(plat1_time, plat1_EMG_data, slice_reach_R, slice_reach2_R)
reach_L_segment = segments(plat1_time, plat1_EMG_data, slice_reach_L, slice_reach2_L)
reach_C_segment = segments(plat1_time, plat1_EMG_data, slice_reach_C, slice_reach2_C)



FS_plat_segment      = segments(plat1_time, plat1_data, slice_2FS, slice_2_2FS)
FS_EC_plat_segment   = segments(plat1_time, plat1_data, slice_2FS_EC, slice_2_2FS_EC)
RF_EO_plat_segment   = segments(plat1_time, plat1_data, slice_RF_EO, slice_2_RF_EO)
RF_EC_plat_segment   = segments(plat1_time, plat1_data, slice_RF_EC, slice_2_RF_EC)
LF_EO_plat_segment   = segments(plat1_time, plat1_data, slice_LF_EO, slice_2_LF_EO)
LF_EC_plat_segment   = segments(plat1_time, plat1_data, slice_LF_EC, slice_LF2_EC)
reach_R_plat_segment = segments(plat1_time, plat1_data, slice_reach_R, slice_reach2_R)
reach_L_plat_segment = segments(plat1_time, plat1_data, slice_reach_L, slice_reach2_L)
reach_C_plat_segment = segments(plat1_time, plat1_data, slice_reach_C, slice_reach2_C)



load_data(rest_segment, 'Static/Relax')

load_data(MVC1_back_segment, "Static/MVC_back/MVC1")
load_data(MVC2_back_segment, "Static/MVC_back/MVC2")
load_data(MVC3_back_segment, "Static/MVC_back/MVC3")

load_data(MVC1_rectus_segment, "Static/MVC_rectus/MVC1")
load_data(MVC2_rectus_segment, "Static/MVC_rectus/MVC2")
load_data(MVC3_rectus_segment, "Static/MVC_rectus/MVC3")

load_data(MVC1_RO_segment, "Static/MVC_RO/MVC1")
load_data(MVC2_RO_segment, "Static/MVC_RO/MVC2")
load_data(MVC3_RO_segment, "Static/MVC_RO/MVC3")

load_data(MVC1_LO_segment, "Static/MVC_LO/MVC1")
load_data(MVC2_LO_segment, "Static/MVC_LO/MVC2")
load_data(MVC3_LO_segment, "Static/MVC_LO/MVC3")


load_data(FS_segment, "EMG/Standing_EO")
load_data(FS_EC_segment, "EMG/Standing_EC")
load_data(RF_EO_segment, "EMG/OneFootStanding_R_EO")
load_data(RF_EC_segment, "EMG/OneFootStanding_R_EC")
load_data(LF_EO_segment, "EMG/OneFootStanding_L_EO")
load_data(LF_EC_segment, "EMG/OneFootStanding_L_EC")
load_data(reach_R_segment, "EMG/Reach_R")
load_data(reach_L_segment, "EMG/Reach_L")
load_data(reach_C_segment, "EMG/Reach_C")


load_data_plat(FS_plat_segment, "Platform/Standing_EO")
load_data_plat(FS_EC_plat_segment, "Platform/Standing_EC")
load_data_plat(RF_EO_plat_segment, "Platform/OneFootStanding_R_EO")
load_data_plat(RF_EC_plat_segment, "Platform/OneFootStanding_R_EC")
load_data_plat(LF_EO_plat_segment, "Platform/OneFootStanding_L_EO")
load_data_plat(LF_EC_plat_segment, "Platform/OneFootStanding_L_EC")
load_data_plat(reach_R_plat_segment, "Platform/Reach_R")
load_data_plat(reach_L_plat_segment, "Platform/Reach_L")
load_data_plat(reach_C_plat_segment, "Platform/Reach_C")


