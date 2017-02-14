import numpy as np
import copy


def avg_out(test):

    new = {}

    for i in test:
        try:
            new_new = np.zeros(np.shape(test[i]))
            for j in range(0, np.shape(test[i])[1]):
                new_new[:, j] = test[i][:, j] - np.mean(test[i][:, j])
            print np.shape(new_new)
            new[i] = new_new

        except IndexError:
            new[i] = []
    return new


def RMS(signal, window_size=100, overlap=-1):

    if overlap > window_size or overlap == -1:

        overlap = window_size - 1

    # Numero de pontos em que as janelas nao se sobrepoem. Por exemplo se a
    # janela for 500 e o Overlap 499, entao todos os pontos vao ser
    # considerados. Por outro lado se a janela for 500 e o overlap for 0,
    # entao nao ha sobreposicao de janelas.
    delta = int(window_size - overlap)

    indexes = []

    [[indexes.append(i)] for i in range(0, len(signal), delta)]

    RMS = np.zeros(len(indexes))

    c = 0
    for i in indexes:
        lower_bound = max([0, i - window_size / 2])
        upper_bound = min([len(signal), i + window_size / 2])
        RMS[c] = np.sqrt(np.mean(np.power(signal[lower_bound:upper_bound], 2)))
        c += 1

    return RMS


def RMS_whole_segment(test, window_size=100, overlap=-1):

    new = {}
    for i in test:
        try:
            new_new = np.zeros(np.shape(test[i]))
            for j in range(0, np.shape(test[i])[1]):
                new_new[:, j] = RMS(test[i][:, j], window_size=window_size, overlap=overlap)
            new[i] = np.array(new_new)
        except IndexError:
            new[i] = []

    return new


def max_mvc(MVC1=[], MVC2=[]):
    flag1, flag2 = True, True
    try:
        max_MVC1 = np.amax(MVC1, axis=0)
    except ValueError:
        flag1 = False

    try:
        max_MVC2 = np.amax(MVC2, axis=0)
    except ValueError:
        flag2 = False

    if not flag1 and not flag2:
        return np.zeros(8)
    else:
        if not flag1:
            max_MVC1 = max_MVC2
        if not flag2:
            max_MVC2 = max_MVC1

        return np.mean(np.vstack((max_MVC1, max_MVC2)), axis=0)


def norm_whole_segment(test, max):
    new_avg = {}
    new_max = {}
    for i in test:
        try:
            new_new_avg = np.zeros(np.shape(test[i]))
            new_new_max = np.zeros(np.shape(test[i])[1])

            for j in range(0, np.shape(test[i])[1]):
                new_new_avg[:, j] = test[i][:, j] / max[j]
                new_new_max[j] = np.max(new_new_avg[:, j]) * 100

            new_avg[i] = np.array(new_new_avg)
            new_max[i] = np.array(new_new_max)
        except IndexError:
            new_avg[i] = []
            new_max[i] = []

    return new_avg, new_max

# def correlation(self):
 #   correlation = {}
  #  for i in self.EMG_RMS:
   #     print i
    #    platform_values = np.zeros((4,len(self.platform_RMS[i][1,:])))
    #   EMG_values = np.zeros((8, len(self.EMG_RMS[i][1, :])))
    #  correlation_values = []
    # for j in range(0,len(self.platform_RMS[i])):
    #    platform_values[j,:] = self.platform[i][j,:]
    #   for x in range(0,len(self.EMG_RMS[i])):
    #      EMG_values[x,:] = self.EMG_RMS[i][x,:]
    #     correlation_values[j,x] = np.correlate(EMG_values,platform_values)
    #correlation = correlation_values
    # return correlation
