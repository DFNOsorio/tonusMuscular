import h5py
import numpy as np
import copy
import matplotlib.pyplot as plt


filename1 = 'Testes_Egas_Moniz/patient_2_mvc_0007803B4638_2016-11-28_15-04-03.h5'
filename2 = 'Testes_Egas_Moniz/patient_1_mvc_0007803B4638_2016-11-28_12-28-48.h5'
filename3 = 'Testes_Egas_Moniz/patient_1_plataforma_0007803B4638_2016-11-28_12-37-24.h5'
filename4 = 'Testes_Egas_Moniz/patient_3_plataforma_0007803B4638_2016-11-28_15-33-02.h5'
filename5 = 'Testes_Egas_Moniz/patient_3_mvc_0007803B4638_2016-11-28_15-30-30.h5'
filename6 = 'Testes_Egas_Moniz/teste_000780646DDA_0007803B4638_2016-11-28_12-46-36.h5'

filename_w='Egas_Moniz_Segments/Paciente1_MJ_Lupus.h5'

def load_data_h5(filename, platform = False):

    time = []

    file = h5py.File(filename, 'r')

    file_macs = file.keys()

    EMG_mac = '00:07:80:3B:46:38'

    if file_macs[0] == "00:07:80:3B:46:38" and platform:

        platform_mac = file_macs[1]

    elif platform:

        platform_mac =  file_macs[0]

    definitions = [file[EMG_mac].attrs["sampling rate"]*1.0, file[EMG_mac].attrs["resolution"]*1.0]

    ## Load EMGs data
    EMG_data_group = file[EMG_mac + "/raw"]

    time = np.linspace(0, len(EMG_data_group['nSeq'][:, 0]) / 1000.0, len(EMG_data_group['nSeq'][:, 0]))

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

        return EMG_data,time, EMG_labels


data_MVC1, time_MVC1, MVC1_labels = load_data_h5(filename1)
data_MVC2, time_MVC2, MVC2_labels = load_data_h5(filename2)
data_plat1, time_plat1, plat1_labels = load_data_h5(filename3)
data_plat2, time_plat2, plat2_labels = load_data_h5(filename4)
data_plat3, time_plat3, plat3_labels = load_data_h5(filename5)
data_relax, time_relax, relax_labels = load_data_h5(filename6)

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
slice_2_MVC1=time_MVC1[len(time_MVC1)-1]
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
slice_2_repouso=time_relax[len(time_relax)-1]

def segments(time, data, start, end):
    segment_data = []
    global t, t2
    for idx,t in enumerate(time):
        if t == start:
            time1=idx

    for idx2, t2 in enumerate(time):
        if t2 == end:
            time2=idx2

    for index, value in enumerate(data):
        if index >= time1 and index <= time2:
            segment_data=data[time1:time2,:]

    return segment_data

rest_segment = segments(time_relax, data_relax, slice_repouso, slice_2_repouso)

MVC1_segment = segments(time_MVC1, data_MVC1, sliceMVC1, slice_2_MVC1)
MVC2_segment = segments(time_MVC2, data_MVC2, sliceMVC2, slice_2_MVC2)

AE_segment     = segments(time_plat1, data_plat1, slice_AE, slice_2_AE)
TFS_segment    = segments(time_plat1, data_plat1, slice_2FS, slice_2_2FS)
TFS_EC_segment = segments(time_plat1, data_plat1, slice_2FS_EC, slice_2_2FS_EC)
RF_EO_segment  = segments(time_plat1, data_plat1, slice_RF_EO, slice_2_RF_EO)
RF_EC_segment  = segments(time_plat1, data_plat1, slice_RF_EC, slice_2_RF_EC)

plat2_segment = segments(time_plat2, data_plat2, slice_plat2, slice_2_plat2)
plat3_segment = segments(time_plat3, data_plat3, slice_plat3, slice_2_plat3)

def load_data(segment_data, segment):
    for x, y in enumerate(data):
        if x<=7:
            channel=x+1
            f_new[segment].create_dataset('channel'+ str(channel), data=segment_data[:, x])
            x += 1

load_data(rest_segment, 'Static/Relax')
load_data(MVC1_segment, "Static/MVC1")
load_data(MVC2_segment, "Static/MVC2")

load_data(AE_segment, "EMG/Arms_extension")
load_data(TFS_segment, "EMG/Standing_EO")
load_data(TFS_EC_segment, "EMG/Standing_EC")
load_data(RF_EO_segment, "EMG/OneFootStanding_R_EO")
load_data(RF_EC_segment, "EMG/OneFootStanding_R_EC")

print time_plat1[len(time_plat1)-1]
print time_plat2[len(time_plat2)-1]
print time_plat3[len(time_plat3)-1]
print time_relax[len(time_relax)-1]

