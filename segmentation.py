import h5py
import numpy as np
import copy
import matplotlib.pyplot as plt


filename1 = 'Testes_Egas_Moniz/patient_1_mvc_0007803B4638_2016-11-28_12-28-21.h5'
filename2 = 'Testes_Egas_Moniz/patient_1_mvc_0007803B4638_2016-11-28_12-28-48.h5'
filename3 = 'Testes_Egas_Moniz/patient_1_plataforma_0007803B4638_2016-11-28_12-37-24.h5'
filename4 = 'Testes_Egas_Moniz/patient_1_plataforma_0007803B4638_2016-11-28_12-41-14.h5'
filename5 = 'Testes_Egas_Moniz/patient_1_plataforma_0007803B4638_2016-11-28_12-43-17.h5'
filename6 = 'Testes_Egas_Moniz/patient_1_repouso_0007803B4638_2016-11-28_12-27-00.h5'

filename_w='Egas_Moniz_Segments/Paciente1_MJ_Lupus.h5'

def load_data_h5_MVC1(filename1):
    global EMG_data_MVC1
    global EMG_time_MVC1
    f1 = h5py.File(filename1, 'r')

    EMG_Macs = f1.keys()[0]
    EMG_data_group = f1[EMG_Macs + "/raw"]

    EMG_def = [f1[EMG_Macs].attrs["sampling rate"]*1.0, f1[EMG_Macs].attrs["resolution"]*1.0]

    EMG_data_MVC1 = np.zeros((f1[EMG_Macs].attrs["nsamples"], len(EMG_data_group)-1))
    EMG_time_MVC1 = EMG_data_group['nSeq'][:, 0] / EMG_def[0]

    EMG_labels = []
    for i in range(0, len(EMG_data_group)-1):
        EMG_labels.append(EMG_data_group['channel_' + str(i+1)].attrs['label'])
        EMG_data_MVC1[:, i] = EMG_data_group['channel_' + str(i+1)][:, 0]
    return (EMG_data_MVC1,EMG_time_MVC1)


def load_data_h5_MVC2(filename2):
    global EMG_data_MVC2
    global EMG_time_MVC2
    f2 = h5py.File(filename2, 'r')

    EMG_Macs = f2.keys()[0]
    EMG_data_group = f2[EMG_Macs + "/raw"]

    EMG_def = [f2[EMG_Macs].attrs["sampling rate"]*1.0, f2[EMG_Macs].attrs["resolution"]*1.0]

    EMG_data_MVC2 = np.zeros((f2[EMG_Macs].attrs["nsamples"], len(EMG_data_group)-1))
    EMG_time_MVC2 = EMG_data_group['nSeq'][:, 0] / EMG_def[0]

    EMG_labels = []
    for i in range(0, len(EMG_data_group)-1):
        EMG_labels.append(EMG_data_group['channel_' + str(i+1)].attrs['label'])
        EMG_data_MVC2[:, i] = EMG_data_group['channel_' + str(i+1)][:, 0]
    return (EMG_data_MVC2,EMG_time_MVC2)


def load_data_h5_plat1(filename3):
    global EMG_data_plat1
    global EMG_time_plat1
    f3 = h5py.File(filename3, 'r')

    EMG_Macs = f3.keys()[0]
    EMG_data_group = f3[EMG_Macs + "/raw"]

    EMG_def = [f3[EMG_Macs].attrs["sampling rate"]*1.0, f3[EMG_Macs].attrs["resolution"]*1.0]

    EMG_data_plat1 = np.zeros((f3[EMG_Macs].attrs["nsamples"], len(EMG_data_group)-1))
    EMG_time_plat1 = EMG_data_group['nSeq'][:, 0] / EMG_def[0]

    EMG_labels = []
    for i in range(0, len(EMG_data_group)-1):
        EMG_labels.append(EMG_data_group['channel_' + str(i+1)].attrs['label'])
        EMG_data_plat1[:, i] = EMG_data_group['channel_' + str(i+1)][:, 0]
    return (EMG_data_plat1,EMG_time_plat1)


def load_data_h5_plat2(filename4):
    global EMG_data_plat2
    global EMG_time_plat2
    f4 = h5py.File(filename4, 'r')

    EMG_Macs = f4.keys()[0]
    EMG_data_group = f4[EMG_Macs + "/raw"]

    EMG_def = [f4[EMG_Macs].attrs["sampling rate"]*1.0, f4[EMG_Macs].attrs["resolution"]*1.0]

    EMG_data_plat2 = np.zeros((f4[EMG_Macs].attrs["nsamples"], len(EMG_data_group)-1))
    EMG_time_plat2 = EMG_data_group['nSeq'][:, 0] / EMG_def[0]

    EMG_labels = []
    for i in range(0, len(EMG_data_group)-1):
        EMG_labels.append(EMG_data_group['channel_' + str(i+1)].attrs['label'])
        EMG_data_plat2[:, i] = EMG_data_group['channel_' + str(i+1)][:, 0]
    return (EMG_data_plat2,EMG_time_plat2)


def load_data_h5_plat3(filename5):
    global EMG_data_plat3
    global EMG_time_plat3
    f5 = h5py.File(filename5, 'r')

    EMG_Macs = f5.keys()[0]
    EMG_data_group = f5[EMG_Macs + "/raw"]

    EMG_def = [f5[EMG_Macs].attrs["sampling rate"]*1.0, f5[EMG_Macs].attrs["resolution"]*1.0]

    EMG_data_plat3 = np.zeros((f5[EMG_Macs].attrs["nsamples"], len(EMG_data_group)-1))
    EMG_time_plat3 = EMG_data_group['nSeq'][:, 0] / EMG_def[0]

    EMG_labels = []
    for i in range(0, len(EMG_data_group)-1):
        EMG_labels.append(EMG_data_group['channel_' + str(i+1)].attrs['label'])
        EMG_data_plat3[:, i] = EMG_data_group['channel_' + str(i+1)][:, 0]
    return (EMG_data_plat3,EMG_time_plat3)


def load_data_h5_repouso(filename3):
    global EMG_data_repouso
    global EMG_time_repouso
    f6 = h5py.File(filename6, 'r')

    EMG_Macs = f6.keys()[0]
    EMG_data_group = f6[EMG_Macs + "/raw"]

    EMG_def = [f6[EMG_Macs].attrs["sampling rate"]*1.0, f6[EMG_Macs].attrs["resolution"]*1.0]

    EMG_data_repouso = np.zeros((f6[EMG_Macs].attrs["nsamples"], len(EMG_data_group)-1))
    EMG_time_repouso = EMG_data_group['nSeq'][:, 0] / EMG_def[0]

    EMG_labels = []
    for i in range(0, len(EMG_data_group)-1):
        EMG_labels.append(EMG_data_group['channel_' + str(i+1)].attrs['label'])
        EMG_data_repouso[:, i] = EMG_data_group['channel_' + str(i+1)][:, 0]
    return (EMG_data_repouso,EMG_time_repouso)


load_data_h5_MVC1(filename1)
load_data_h5_MVC2(filename2)
load_data_h5_plat1(filename3)
load_data_h5_plat2(filename4)
load_data_h5_plat3(filename5)
load_data_h5_repouso(filename6)

f_new = h5py.File(filename_w, 'w')

atrib1 = f_new.attrs['Name'] = 'M.J'
atrib2 = f_new.attrs['Gender'] = 'F'
atrib3 = f_new.attrs['Age'] = 54
atrib4 = f_new.attrs['Condition'] = 'Lupus'


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

sliceMVC1=0
slice_2_MVC1=EMG_time_MVC1[len(EMG_time_MVC1)-3]
sliceMVC2=1
slice_2_MVC2=2

slice_AE=0
slice_2_AE=1
slice_2FS=1.1
slice_2_2FS=2
slice_2FS_EC=2.1
slice_2_2FS_EC=2.5
slice_RF_EO=2.6
slice_2_RF_EO=3
slice_RF_EC=3.1
slice_2_RF_EC=10

slice_plat2=0
slice_2_plat2=1
slice_plat3=0
slice_2_plat3=1
slice_repouso=0
slice_2_repouso=1


def array_MVC1(EMG_time_MVC1,EMG_data_MVC1,sliceMVC1,slice_2_MVC1):
    global EMG_data_seg_MVC1

    for idx,t in enumerate(EMG_time_MVC1):
        if t==sliceMVC1:
            time1=idx

    for idx2, t2 in enumerate(EMG_time_MVC1):
        if t2 == slice_2_MVC1:
            time2=idx2

    for index, value in enumerate(EMG_data_MVC1):
        if index >= time1 and index <= time2:
            EMG_data_seg_MVC1=EMG_data_MVC1[time1:time2,:]
    return EMG_data_seg_MVC1



def array_MVC2(EMG_time_MVC2,EMG_data_MVC2,sliceMVC2,slice_2_MVC2):
    global EMG_data_seg_MVC2

    for idx,t in enumerate(EMG_time_MVC2):
        if t==sliceMVC2:
            time1=idx

    for idx2, t2 in enumerate(EMG_time_MVC2):
        if t2 == slice_2_MVC2:
            time2=idx2

    for index, value in enumerate(EMG_data_MVC2):
        if index >= time1 and index <= time2:
            EMG_data_seg_MVC2=EMG_data_MVC2[time1:time2,:]
    return EMG_data_seg_MVC2

def array_plat1(EMG_time_plat1,EMG_data_plat1,slice_AE,slice_2_AE,slice_2FS,slice_2_2FS,slice_2FS_EC,slice_2_2FS_EC,slice_RF_EO,slice_2_RF_EO,slice_RF_EC,slice_2_RF_EC):

    global EMG_data_AE,EMG_data_2FS,EMG_data_2FS_EC,EMG_data_RF_EO,EMG_data_RF_EC

    for idx,t in enumerate(EMG_time_plat1):
        if t==slice_AE:
            time1=idx
        if t==slice_2_AE:
            time2=idx
        if t==slice_2FS:
            time3=idx
        if t==slice_2_2FS:
            time4=idx
        if t==slice_2FS_EC:
            time5=idx
        if t==slice_2_2FS_EC:
            time6=idx
        if t==slice_RF_EO:
            time7=idx
        if t==slice_2_RF_EO:
            time8=idx
        if t==slice_RF_EC:
            time9=idx
        if t==slice_2_RF_EC:
            time10=idx

    for index, value in enumerate(EMG_data_plat1):
        if index >= time1 and index <= time2:
            EMG_data_AE=EMG_data_plat1[time1:time2,:]
        if index >= time3 and index <= time4:
            EMG_data_2FS=EMG_data_plat1[time3:time4,:]
        if index >= time5 and index <= time6:
            EMG_data_2FS_EC=EMG_data_plat1[time5:time6,:]
        if index >= time7 and index <= time8:
            EMG_data_RF_EO=EMG_data_plat1[time7:time8,:]
        if index >= time9 and index <= time10:
            EMG_data_RF_EC=EMG_data_plat1[time9:time10,:]
    return (EMG_data_AE,EMG_data_2FS,EMG_data_2FS_EC,EMG_data_RF_EO,EMG_data_RF_EC)

def array_plat2(EMG_time_plat2,EMG_data_plat2,slice_plat2,slice_2_plat2):
    global EMG_data_seg_plat2

    for idx,t in enumerate(EMG_time_plat2):
        if t==slice_plat2:
            time1=idx

    for idx2, t2 in enumerate(EMG_time_plat2):
        if t2 == slice_2_plat2:
            time2=idx2

    for index, value in enumerate(EMG_data_plat2):
        if index >= time1 and index <= time2:
            EMG_data_seg_plat2=EMG_data_plat2[time1:time2,:]
    return EMG_data_seg_plat2

def array_plat3(EMG_time_plat3,EMG_data_plat3,slice_plat3,slice_2_plat3):
    global EMG_data_seg_plat3

    for idx,t in enumerate(EMG_time_plat3):
        if t==slice_plat3:
            time1=idx

    for idx2, t2 in enumerate(EMG_time_plat3):
        if t2 == slice_2_plat3:
            time2=idx2

    for index, value in enumerate(EMG_data_plat3):
        if index >= time1 and index <= time2:
            EMG_data_seg_plat3=EMG_data_plat3[time1:time2,:]
    return EMG_data_seg_plat3

def array_repouso(EMG_time_repouso,EMG_data_repouso,slice_repouso,slice_2_repouso):
    global EMG_data_seg_repouso

    for idx,t in enumerate(EMG_time_repouso):
        if t==slice_repouso:
            time1=idx

    for idx2, t2 in enumerate(EMG_time_repouso):
        if t2 == slice_2_repouso:
            time2=idx2

    for index, value in enumerate(EMG_data_repouso):
        if index >= time1 and index <= time2:
            EMG_data_seg_repouso=EMG_data_repouso[time1:time2,:]
    return EMG_data_seg_repouso

array_MVC1(EMG_time_MVC1,EMG_data_MVC1,sliceMVC1,slice_2_MVC1)
array_MVC2(EMG_time_MVC2,EMG_data_MVC2,sliceMVC2,slice_2_MVC2)
array_plat1(EMG_time_plat1,EMG_data_plat1,slice_AE,slice_2_AE,slice_2FS,slice_2_2FS,slice_2FS_EC,slice_2_2FS_EC,slice_RF_EO,slice_2_RF_EO,slice_RF_EC,slice_2_RF_EC)
array_plat2(EMG_time_plat2,EMG_data_plat2,slice_plat2,slice_2_plat2)
array_plat3(EMG_time_plat3,EMG_data_plat3,slice_plat3,slice_2_plat3)
array_repouso(EMG_time_repouso,EMG_data_repouso,slice_repouso,slice_2_repouso)

def segmentation_MVC1(EMG_data_seg_MVC1, segment):
    for x, y in enumerate(EMG_data_seg_MVC1):
        if x<=7:
            channel=x+1
            f_new["Static/MVC1"] #chama este grupo ou nao fazes o create antes e fazes so f_new.create_dataset("Static/MVC1/channel"+ str(channel), data=EMG_data_seg[:, x]) que criate tudo.
            data_set_MVC1=f_new[segment].create_dataset('channel'+ str(channel), data=EMG_data_seg_MVC1[:, x])
            x += 1
    return data_set_MVC1

def segmentation_MVC2(EMG_data_seg_MVC2, segment):
    for x, y in enumerate(EMG_data_seg_MVC2):
        if x<=7:
            channel=x+1
            f_new["Static/MVC2"] #chama este grupo ou nao fazes o create antes e fazes so f_new.create_dataset("Static/MVC1/channel"+ str(channel), data=EMG_data_seg[:, x]) que criate tudo.
            data_set_MVC2=f_new[segment].create_dataset('channel'+ str(channel), data=EMG_data_seg_MVC2[:, x])
            x += 1
    return data_set_MVC2

def segmentation_repouso(EMG_data_seg_repouso, segment):
    for x, y in enumerate(EMG_data_seg_repouso):
        if x<=7:
            channel=x+1
            f_new["Static/Relax"] #chama este grupo ou nao fazes o create antes e fazes so f_new.create_dataset("Static/MVC1/channel"+ str(channel), data=EMG_data_seg[:, x]) que criate tudo.
            data_set_repouso=f_new[segment].create_dataset('channel'+ str(channel), data=EMG_data_seg_repouso[:, x])
            x += 1
    return data_set_repouso

def segmentation_AE(EMG_data_AE, segment):
    for x, y in enumerate(EMG_data_AE):
        if x<=7:
            channel=x+1
            f_new["EMG/Arms_extension"] #chama este grupo ou nao fazes o create antes e fazes so f_new.create_dataset("Static/MVC1/channel"+ str(channel), data=EMG_data_seg[:, x]) que criate tudo.
            data_set_AE=f_new[segment].create_dataset('channel'+ str(channel), data=EMG_data_AE[:, x])
            x += 1
    return data_set_AE

def segmentation_2FS(EMG_data_2FS, segment):
    for x, y in enumerate(EMG_data_2FS):
        if x<=7:
            channel=x+1
            f_new["EMG/Standing_EO"] #chama este grupo ou nao fazes o create antes e fazes so f_new.create_dataset("Static/MVC1/channel"+ str(channel), data=EMG_data_seg[:, x]) que criate tudo.
            data_set_2FS=f_new[segment].create_dataset('channel'+ str(channel), data=EMG_data_2FS[:, x])
            x += 1
    return data_set_2FS

def segmentation_2FS_EC(EMG_data_2FS_EC, segment):
    for x, y in enumerate(EMG_data_2FS_EC):
        if x<=7:
            channel=x+1
            f_new["EMG/Standing_EC"] #chama este grupo ou nao fazes o create antes e fazes so f_new.create_dataset("Static/MVC1/channel"+ str(channel), data=EMG_data_seg[:, x]) que criate tudo.
            data_set_2FS_EC=f_new[segment].create_dataset('channel'+ str(channel), data=EMG_data_2FS_EC[:, x])
            x += 1
    return data_set_2FS_EC

def segmentation_RF_EO(EMG_data_RF_EO, segment):
    for x, y in enumerate(EMG_data_RF_EO):
        if x<=7:
            channel=x+1
            f_new["EMG/OneFootStanding_R_EO"] #chama este grupo ou nao fazes o create antes e fazes so f_new.create_dataset("Static/MVC1/channel"+ str(channel), data=EMG_data_seg[:, x]) que criate tudo.
            data_set_RF_EO=f_new[segment].create_dataset('channel'+ str(channel), data=EMG_data_RF_EO[:, x])
            x += 1
    return data_set_RF_EO

def segmentation_RF_EC(EMG_data_RF_EC, segment):
    for x, y in enumerate(EMG_data_RF_EC):
        if x<=7:
            channel=x+1
            f_new["EMG/OneFootStanding_R_EC"] #chama este grupo ou nao fazes o create antes e fazes so f_new.create_dataset("Static/MVC1/channel"+ str(channel), data=EMG_data_seg[:, x]) que criate tudo.
            data_set_RF_EC=f_new[segment].create_dataset('channel'+ str(channel), data=EMG_data_RF_EC[:, x])
            x += 1
    return data_set_RF_EC

segmentation_MVC1(EMG_data_seg_MVC1, "Static/MVC1")
segmentation_MVC2(EMG_data_seg_MVC2, "Static/MVC2")
segmentation_repouso(EMG_data_seg_repouso, "Static/Relax")
segmentation_AE(EMG_data_AE, "EMG/Arms_extension")
segmentation_2FS(EMG_data_2FS, "EMG/Standing_EO")
segmentation_2FS_EC(EMG_data_2FS_EC, "EMG/Standing_EC")
segmentation_RF_EO(EMG_data_RF_EO, "EMG/OneFootStanding_R_EO")
segmentation_RF_EC(EMG_data_RF_EC, "EMG/OneFootStanding_R_EO")
## segmentation(EMG_data_seg, "ECG/Arms_extension")

f_new.close()


