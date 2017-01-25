from pasta import *
import h5py
import numpy as np
import copy
import matplotlib.pyplot as plt


filename = 'Testes_Egas_Moniz/patient_1_repouso_0007803B4638_2016-11-28_12-27-00.h5'

def load_data_h5(filename):
    f = h5py.File(filename, 'r')
    global EMG_data
    global EMG_time
    EMG_Macs = f.keys()[0]
    EMG_data_group = f[EMG_Macs + "/raw"]

    EMG_def = [f[EMG_Macs].attrs["sampling rate"]*1.0, f[EMG_Macs].attrs["resolution"]*1.0]

    EMG_data = np.zeros((f[EMG_Macs].attrs["nsamples"], len(EMG_data_group)-1))
    EMG_time = EMG_data_group['nSeq'][:, 0] / EMG_def[0]

    EMG_labels = []
    for i in range(0, len(EMG_data_group)-1):
        EMG_labels.append(EMG_data_group['channel_' + str(i+1)].attrs['label'])
        EMG_data[:, i] = EMG_data_group['channel_' + str(i+1)][:, 0]
    return [EMG_data, EMG_time, EMG_labels, EMG_def]

load_data_h5(filename)

slice1=4
slice2=6


for idx,t in enumerate(EMG_time):
    if t==slice1:
        s=idx



for idx2, t2 in enumerate(EMG_time):
    if t2 == slice2:
        d=idx2



for index, value in enumerate(EMG_data):
    if index >= s and index <= d:
        EMG_data_seg=EMG_data[s:d,:]


def segmentation(EMG_data_seg):
    global data_set
    for x, y in enumerate(EMG_data_seg):
        if x<=7:
            channel=x+1
            data_set=f_new.create_dataset('MVC1/channel'+ str(channel), data=EMG_data_seg[:, x])
            x += 1
    return data_set


print(d)
print(s)
print(EMG_data[:,1])
print(EMG_data_seg[:,1])
segmentation(EMG_data_seg)
