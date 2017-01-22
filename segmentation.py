import h5py
import numpy as np
import copy
import matplotlib.pyplot as plt


filename = 'patient_1_mvc_0007803B4638_2016-11-28_12-28-21.h5'
filename_w='Paciente1.h5'
slice1=1
slice2=2

f = h5py.File(filename, 'r')

print("Keys: %s" % f.keys()[0])
EMG_Macs = f.keys()[0]
EMG_data_group = f[EMG_Macs + "/raw"]
print("Keys2: %s" % EMG_data_group)

EMG_def = [f[EMG_Macs].attrs["sampling rate"]*1.0, f[EMG_Macs].attrs["resolution"]*1.0]

EMG_data = np.zeros((f[EMG_Macs].attrs["nsamples"], len(EMG_data_group)-1))
EMG_time = EMG_data_group['nSeq'][:, 0] / EMG_def[0]

EMG_labels = []
for i in range(0, len(EMG_data_group)-1):

    EMG_labels.append(EMG_data_group['channel_' + str(i+1)].attrs['label'])
    d=EMG_data[:, i] = EMG_data_group['channel_' + str(i+1)][:, 0]


print("Vector tempo:")
print(EMG_time)

f_new = h5py.File(filename_w, 'w')

group1 = f_new.create_group('MVC1')
group2 = f_new.create_group('MVC2')
group3 = f_new.create_group('Relax')
group4 = f_new.create_group('Arms_extension')
group5 = f_new.create_group('Standing_EO')
group6 = f_new.create_group('Standing_EC')
group7 = f_new.create_group('OneFootStanding_R_EO')
group8 = f_new.create_group('OneFootStanding_R_EC')
group9 = f_new.create_group('OneFootStanding_L_EO')
group10 = f_new.create_group('OneFootStanding_L_EC')
group11 = f_new.create_group('Reach_Forward')
group12 = f_new.create_group('Reach_Ground')
group13 = f_new.create_group('Platform')
group14 = f_new.create_group('Platform/Arms_Extension')
group15 = f_new.create_group('Platform/Standing_EO')
group16 = f_new.create_group('Platform/Standing_EC')
group17 = f_new.create_group('Platform/OneFootStanding_R_EO')
group18 = f_new.create_group('Platform/OneFootStanding_R_EC')
group19 = f_new.create_group('Platform/OneFootStanding_L_EO')
group20 = f_new.create_group('Platform/OneFootStanding_L_EC')
group21 = f_new.create_group('Platform/Reach_Forward')
group22 = f_new.create_group('Platform/Reach_Ground')

for idx,t in enumerate(EMG_time):
    if t==slice1:
        s=idx

for idx2, t2 in enumerate(EMG_time):
    if t2 == slice2:
        d=idx2

for index, value in enumerate(EMG_data):
    if index >= s and index <= d:
        EMG_data_seg=EMG_data[s:d,:]

print(EMG_data_seg[:,0])

for index_t, value_t in enumerate(EMG_time):
    if index_t >= s and index_t <= d:
        EMG_time_seg=EMG_time[s:d]

print(EMG_time_seg)
print(len(EMG_time_seg))
print(len(EMG_data_seg))

for x, y in enumerate(EMG_data_seg):
    if x<=7:
        chanel=x+1
        f_new.create_dataset('MVC1/chanel'+'%d'%chanel, data=EMG_data_seg[:, x])
        x += 1
