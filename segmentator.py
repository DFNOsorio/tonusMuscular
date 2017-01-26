import h5py
import numpy as np

filename1 = 'Testes_Egas_Moniz/patient_1_mvc_0007803B4638_2016-11-28_12-28-21.h5'
filename2 = 'Testes_Egas_Moniz/patient_1_mvc_0007803B4638_2016-11-28_12-28-48.h5'
filename3 = 'Testes_Egas_Moniz/patient_1_plataforma_0007803B4638_2016-11-28_12-37-24.h5'
filename4 = 'Testes_Egas_Moniz/patient_1_plataforma_0007803B4638_2016-11-28_12-41-14.h5'
filename5 = 'Testes_Egas_Moniz/patient_1_plataforma_0007803B4638_2016-11-28_12-43-17.h5'
filename6 = 'Testes_Egas_Moniz/patient_1_repouso_0007803B4638_2016-11-28_12-27-00.h5'

filename_w='Egas_Moniz_Segments/Paciente1_MJ_Lupus.h5'


def load_data_h5(filename, platform = False):

    time = []

    file = h5py.File(filename1, 'r')

    file_macs = file.keys()

    EMG_mac = "0007803B4638" ##  Este é o mac addresss dos EMGS sempre

    if file_macs[0] == "0007803B4638" && platform: ## Se existir plataform e o primeiro mac for o dos EMGs

        platform_mac = file_macs[1]

    elif platform:  ## Se existir plataforma e o primeirpo mac nao é dos EMGs

        platform_mac =  file_macs[0]

    definitions = [file[EMG_mac].attrs["sampling rate"]*1.0, file[EMG_mac].attrs["resolution"]*1.0]

    ## Load EMGs data
    EMG_data_group = file[EMG_mac + "/raw"]

    time = EMG_data_group['nSeq'][:, 0] / definitions[0]

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



rest_time, rest_EMG_data, rest_EMG_lables       =
MVC1_time, MVC1_EMG_data, MVC1_EMG_lables       =
MVC2_time, MVC2_EMG_data, MVC2_EMG_lables       =
plat1_time, plat1_EMG_data, plat1_EMG_lables    =
plat2_time, plat2_EMG_data, plat2_EMG_lables    =
plat3_time, plat3_EMG_data, plat3_EMG_lables    =
