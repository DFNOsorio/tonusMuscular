import numpy as np
import scipy.fftpack as fft
import matplotlib.pyplot as plt

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

def RAW_2_mass(platform_data):
    mass={}
    G = (100.0*1000.0+2013.83)/203.83
    Vi = 1000.0/G
    res = 16.0
    for i in platform_data:
        new_mass = np.zeros((len(platform_data[i][:,0]), 4))
        vOutput = [2.00030, 2.00011, 2.00029, 2.00056]
        for j in range(0, 4):
            S = (3.0 * vOutput[j]) / (Vi * 200.0)
            new_mass[:,j] = (platform_data[i][:,j]*3.0)/(S * np.power(2, (res-1)))
        mass[i] = new_mass
    return mass


def mass_2_COP(platform_mass):
    new = {}
    W = 225.0 + 12.0
    H = 225.0 + 12.0
    for i in platform_mass:
        Cop_x = []
        Cop_y = []
        TL = platform_mass[i][:, 0]
        TR = platform_mass[i][:, 1]
        BR = platform_mass[i][:, 2]
        BL = platform_mass[i][:, 3]

        Total_W = TL + TR + BR + BL + 0.001  # Prevents any division by 0
        Cop_x = (((TR+BR)-(TL+TR))/(Total_W))*W
        Cop_y = (((TR+TL)-(BR+BL))/(Total_W))*H

        new[i] = {"Total_W": Total_W, "COP_X": Cop_x, "COP_Y": Cop_y}
    return new

def fourier_EMG(array):
    FFT = {}
    freqs = {}
    IDX = {}
    time_step = 1.0 / 1000.0
    for i in array:
        feq = np.zeros((len(array[i][:,0]), len(array[i][0,:])))
        fft = np.zeros((len(array[i][:,0]), len(array[i][0,:])))
        idx = np.zeros((len(array[i][:,0]), len(array[i][0,:])))
        for j in range(0, np.shape(array[i])[1]):
            feq[:,j] = np.fft.fftfreq(len(array[i][:,0]), time_step)
            fft[:,j] = np.abs(np.fft.fft(array[i][:,j]))
            idx[:,j] = np.argsort(feq[:,j])
        FFT[i] = fft
        freqs[i] = feq
        IDX[i] = idx
        #spipy.signal.espectogram

    return  freqs, FFT, IDX

def fourier_COP(test_array):
    FFT_COP = {}
    freqs_COP = {}
    fft_COP = {}
    freqs = {}
    time_step = 1.0 / 1000.0
    for i in test_array:
        for j in test_array[i]:
            if j != "Total_W":
                #fft_COP = np.zeros((len(test_array[i][j])))
                #freqs = np.zeros((len(test_array[i][j])))
                fft_COP[j] = np.abs(np.fft.fft(test_array[i][j]))
                freqs[j] = np.fft.fftfreq(len(test_array[i][j]), time_step)
        FFT_COP[i] = {"FFT_COPX": fft_COP["COP_X"], "FFT_COPY": fft_COP["COP_Y"]}
        freqs_COP[i] = {"freqs_COPX": freqs["COP_X"], "freqs_COPY": freqs["COP_Y"]}
    return freqs_COP, FFT_COP

def velocity_COP(test_array):
    velocity_direction = {}
    velocity = {}
    mean_trajectory = {}
    velocity_mean = {}
    for i in test_array:
        for j in test_array[i]:
            if j == "COP_X" or j=="COP_Y":
                v = np.zeros((len(test_array[i][j])-1))
                time = len(test_array[i][j])/1000
                v = (np.abs(np.diff(test_array[i][j])))/0.001
                mean = np.mean(v)
                velocity_direction[j] = v
                mean_trajectory[j] = mean
        velocity[i] = {"velocity_COPX": velocity_direction["COP_X"], "velocity_COPY": velocity_direction["COP_Y"]}
        velocity_mean[i] = {"mean_COPX": mean_trajectory["COP_X"], "mean_COPY": mean_trajectory["COP_Y"]}
        #print "\n"
        #print i
        #print velocity_mean
    return velocity, velocity_mean

def trajectory(test_array):
    trajectory = {}
    for i in test_array:
        x = np.mean(test_array[i]["COP_X"])
        y = np.mean(test_array[i]["COP_Y"])
        trajectory[i] = {"X": x, "Y": y}
    return trajectory











def teste():
    data = np.random.rand(301) - 0.5
    ps = np.abs(np.fft.fft(data))**2
    print len(ps)
    time_step = 1.0 / 30.0
    freqs = np.fft.fftfreq(data.size, time_step)
    print len(freqs)
    idx = np.argsort(freqs)
    print len(idx)
    plt.plot(freqs[idx], ps[idx])
    plt.show()