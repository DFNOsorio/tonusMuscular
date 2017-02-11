import numpy as np
import copy

def avg_out(test):

    new = {}

    for i in test:
        try:
            new_new = np.zeros(np.shape(test[i]))
            for j in range(0, np.shape(test[i])[1]):
                new_new[:, j] = test[i][:, j] - np.mean(test[i][:, j])
            new[i] = new_new

        except IndexError:
            new[i] = []

    return new


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


def RMS_whole_segment(test, window_size=100, overlap=-1):

    new = {}
    for i in test:
        try:
            new_new = []
            for j in range(0, np.shape(test[i])[1]):
                new_new.append(RMS(test[i][:, j], window_size = window_size, overlap = overlap))
            new[i] = np.array(new_new)

        except IndexError:
            new[i] = []

    return new

def normalization (self):
    max = np.zeros((8, 1))
    max1 = np.zeros((8, 1))
    max2 = np.zeros((8, 1))

    if self.static["MVC2"] == []:
        for i in range(0, len(self.staticRMS["MVC1"][:,0])):
            max[i] = np.max(self.staticRMS["MVC1"][i,:])

    if self.static["MVC1"] == []:
        for i in range(0, len(self.staticRMS["MVC2"][:,0])):
            max[i] = np.max(self.staticRMS["MVC2"][i,:])

    else:
        for i in range(0, len(self.staticRMS["MVC1"][:,0])):
            max[i] = np.max(self.staticRMS["MVC1"][i,:])

        for i in range(0, len(self.staticRMS["MVC1"][:,0])):
            max[i] = np.max(self.staticRMS["MVC1"][i,:])

        for i in range (0, len(max1[:,1])-1):
            max[i] = (max1[i] + max2 [i]) / 2

    nor_all = {}
    for i in self.EMG_RMS:
        try:
            normalized = np.zeros(np.shape(self.EMG_RMS[i]))
            for j in range(0, np.shape(self.EMG_RMS[i])[1]):
                normalized[j,:] = self.EMG_RMS[i][j,:]/ max[j]

            nor_all[i] = normalized

        except IndexError:
            nor_all[i] = normalized

    return nor_all

def max_normalization (self):
    values = {}
    max_values = np.zeros((8,1))
    for i in self.normalization_EMG:
        for j in range(0, len(self.normalization_EMG[i])):
            max_values[j] = np.max(self.normalization_EMG[i][j,:])

        values[i] = max_values
    return values



