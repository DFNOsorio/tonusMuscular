import scipy.fftpack as fft
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import butter, lfilter, freqz
from scipy import integrate
import novainstrumentation as ni
import numpy as np




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


def max_mvc(MVC1=[], MVC2=[], MVC3=[]):
    flag1, flag2, flag3 = True, True, True
    try:
        max_MVC1 = np.amax(MVC1, axis=0)
    except ValueError:
        flag1 = False

    try:
        max_MVC2 = np.amax(MVC2, axis=0)
    except ValueError:
        flag2 = False

    try:
        max_MVC3 = np.amax(MVC3, axis=0)
    except ValueError:
        flag3 = False

    if not flag1 and not flag2 and not flag3:
        return np.zeros(8)
    else:
        if not flag1:
            max_MVC1 = max_MVC2
        if not flag2:
            max_MVC2 = max_MVC1
        if not flag3:
            max_MVC3 = max_MVC1

        return np.mean(np.vstack((max_MVC1, max_MVC2, max_MVC3)), axis=0)


def norm_whole_segment(test, max_back, max_rectus, max_RO, max_LO):
    new_avg = {}
    new_max = {}
    new_mean = {}
    for i in test:
        try:
            new_new_avg = np.zeros(np.shape(test[i]))
            new_new_max = np.zeros(np.shape(test[i])[1])
            new_new_mean = np.zeros(np.shape(test[i])[1])

            new_new_avg[:, 0] = test[i][:, 0] / max_rectus[0]
            new_new_avg[:, 1] = test[i][:, 1] / max_rectus[1]

            new_new_avg[:, 2] = test[i][:, 2] / max_LO[3]
            new_new_avg[:, 3] = test[i][:, 3] / max_RO[2]

            new_new_avg[:, 4] = test[i][:, 4] / max_back[4]
            new_new_avg[:, 5] = test[i][:, 5] / max_back[5]
            new_new_avg[:, 6] = test[i][:, 6] / max_back[6]
            new_new_avg[:, 7] = test[i][:, 7] / max_back[7]

            for j in range(0, np.shape(test[i])[1]):
                new_new_max[j] = np.max(new_new_avg[:, j]) * 100
                new_new_mean[j] = np.mean(new_new_avg[:, j]) * 100

            new_avg[i] = np.array(new_new_avg)
            new_max[i] = np.array(new_new_max)
            new_mean[i] = np.array(new_new_mean)
        except IndexError:
            new_avg[i] = []
            new_max[i] = []
            new_mean[i] = []

    return new_avg, new_max, new_mean

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
        cop_x = Cop_x - np.mean(Cop_x)
        Cop_y = (((TR+TL)-(BR+BL))/(Total_W))*H
        cop_y = Cop_y - np.mean(Cop_y)

        new[i] = {"Total_W": Total_W, "COP_X": cop_x, "COP_Y": cop_y}
    return new

def fourier_EMG(array):
    Pxx = {}
    freqs = {}

    for i in array:
        feq = np.zeros((513, len(array[i][0,:])))
        pxx = np.zeros((513, len(array[i][0,:])))

        for j in range(0, np.shape(array[i])[1]):
            feq[:,j], pxx[:,j] = signal.welch(array[i][:,j], 1000, nperseg=1024)
        Pxx[i] = pxx
        freqs[i] = feq


    return freqs, Pxx

def fourier_COP(test_array):
    Pxx = {}
    freqs_COP = {}
    Pxx_den = {}
    freqs = {}

    for i in test_array:
        for j in test_array[i]:
            if j != "Total_W":
                freqs[j], Pxx_den[j] = signal.periodogram(test_array[i][j], fs = 1000)

        Pxx[i] = {"COP_X": Pxx_den["COP_X"], "COP_Y": Pxx_den["COP_Y"]}
        freqs_COP[i] = {"COP_X": freqs["COP_X"], "COP_Y": freqs["COP_Y"]}
    return freqs_COP, Pxx

def velocity_COP(test_array):
    velocity_direction = {}
    acelaration_direction = {}
    velocity = {}
    mean_trajectory = {}
    velocity_mean = {}
    acelaration = {}
    for i in test_array:
        for j in test_array[i]:
            if j == "COP_X" or j=="COP_Y":
                v = (np.diff(test_array[i][j]))/0.001
                a = (np.diff(v))/0.001
                mean = np.mean(v)
                velocity_direction[j] = v
                mean_trajectory[j] = mean
                acelaration_direction[j] = a
        velocity[i] = {"COP_X": velocity_direction["COP_X"], "COP_Y": velocity_direction["COP_Y"]}
        velocity_mean[i] = {"COP_X": mean_trajectory["COP_X"], "COP_Y": mean_trajectory["COP_Y"]}
        acelaration[i] = {"COP_X": acelaration_direction["COP_X"], "COP_Y": acelaration_direction["COP_Y"]}
    return velocity, velocity_mean, acelaration

def trajectory(test_array):
    trajectory = {}
    for i in test_array:
        x = np.mean(test_array[i]["COP_X"])
        y = np.mean(test_array[i]["COP_Y"])
        trajectory[i] = {"X": x, "Y": y}
    return trajectory

def convex_hull(COPx, COPy):
    """Computes the convex hull of a set of 2D points.

    Input: an iterable sequence of (x, y) pairs representing the points.
    Output: a list of vertices of the convex hull in counter-clockwise order,
    starting from the vertex with the lexicographically smallest coordinates.
    Implements Andrew's monotone chain algorithm. O(n log n) complexity.
    """
    points = [(COPx[i], COPy[i]) for i in range(0, len(COPy))]

    # Sort the points lexicographically (tuples are compared lexicographically).
    # Remove duplicates to detect the case we have just one unique point.
    points = sorted(set(points))

    # Boring case: no points or a single point, possibly repeated multiple times.
    if len(points) <= 1:
        return points

    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
    # Returns a positive value, if OAB makes a counter-clockwise turn,
    # negative for clockwise turn, and zero if the points are collinear.
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list.
    contour = upper[:-1] + lower[:-1] + upper[0:1]

    #hull = [np.array(contour)[:, 0], np.array(contour)[:, 1]]

    return np.array(contour)


def area_calc(contour_array):

    """ This function uses the contour path to calculate the area, using Green's theorem.

    Parameters
    ----------
    contour_array: array
    contour path

    Returns
    -------
    area: float
    value for the area within the contour
    """

    x = contour_array[:, 0]
    y = contour_array[:, 1]
    if min(x)<0:
        x = np.array(x) - min(x)
    if min(y)<0:
        y = np.array(y) - min(y)

    area = 0
    for i in range(1, len(y) - 1):
        area += (y[i - 1] * x[i] - x[i - 1] * y[i])

    area = abs(area) / 2.0
    return area


def coherence(COP_array, EMG_array):
    frequency = dict()
    coherence = {}
    C_COP_EMG = dict()
    count = 0
    for i in EMG_array:
        C_COP_EMG.setdefault(i, {})
        frequency.setdefault(i, {})

        for j in ["COP_X", "COP_Y"]:
            f = np.zeros((513, 8))
            c = np.zeros((513, 8))

            for n in range(0, len(EMG_array[i][1])):
                f[:,n], c[:,n] =  signal.coherence(EMG_array[i][:,n],COP_array[i][j], 1000, nperseg=1024)
            C_COP_EMG[i][j] = c[:,:]
            frequency[i][j] = f[:,:]
        coherence[i] = {"freqs_x":frequency[i]["COP_X"], "freqs_y":frequency[i]["COP_Y"],
                        "coherency_x":C_COP_EMG[i]["COP_X"], "coherency_y":C_COP_EMG[i]["COP_Y"] }
    return coherence


def RMS_velocity_whole_segment(test, window_size=100, overlap=-1):
    new = {}
    for i in test:
        try:
            new_new = {}
            for j in test[i]:
                new_new[j] = RMS(test[i][j], window_size=window_size, overlap=overlap)
            new[i] = {"COP_X": new_new["COP_X"], "COP_Y": new_new["COP_Y"]}
        except IndexError:
            new[i] = {}

    return new


def normalization_COP(array):
    norm = {}
    for i in array:
        norm_COP = {}
        for j in array[i]:
            max = np.max(array[i][j])
            min = np.min(array[i][j])
            norm_COP[j] = ((array[i][j]) - min) / (max - min)
        norm[i] = {"COP_X": norm_COP["COP_X"], "COP_Y": norm_COP["COP_Y"]}
    return norm

def normalization_subEMG(EMG_array):
    max = np.max(EMG_array)
    min =  np.min(EMG_array)
    norm_EMG = (EMG_array - min) / (max - min)
    return norm_EMG

def normalization_subCOP(COP_array):
    max = np.max(COP_array)
    min =  np.min(COP_array)
    norm_COP = (COP_array - min) / (max - min)
    return norm_COP

def desviation(COP_array):
    dp = {}
    dp_array = {}

    for i in COP_array:
        for j in COP_array[i]:
            if j != "Total_W":
                dp[j] = np.std(COP_array[i][j])

        dp_array[i] = {"COP_X": dp["COP_X"], "COP_Y": dp["COP_Y"]}
    return dp_array

def amplitude(COP_array):
    dist = {}
    amplitude = {}
    for i in COP_array:
        for j in COP_array[i]:
            if j != "Total_W":
                dist[j] = np.max(COP_array[i][j]) - np.min(COP_array[i][j])

        amplitude[i] = {"COP_X": dist["COP_X"], "COP_Y": dist["COP_Y"]}
    return amplitude

def parameters_fourier_EMG(array_freqs, array_pxx):

    peaks_freqs = {}
    means_freqs = {}
    median_freqs = {}
    freqs_80 = {}

    for i in array_freqs:
        peak_freq = np.zeros((1,len(array_freqs[i][0,:])))
        mean_freq = np.zeros((1,len(array_freqs[i][0,:])))
        median_freq = np.zeros((1,len(array_freqs[i][0,:])))
        freq_80 = np.zeros((1,len(array_freqs[i][0,:])))

        for n in range(0, np.shape(array_freqs[i])[1]):

            area = integrate.cumtrapz(array_pxx[i][:,n],array_freqs[i][:,n], initial= 0)
            find80 = np.where(area >= 0.8 * area[len(area) - 1])
            find50 = np.where(area >= 0.5 * area[len(area) - 1])

            freq_80[:,n] = array_freqs[i][find80[0][0], n]
            median_freq[:, n] = array_freqs[i][find50[0][0], n]

            mean_freq[:,n] = np.trapz((array_freqs[i][:,n] * array_pxx[i][:,n]),array_freqs[i][:,n]) / np.trapz( array_pxx[i][:,n],array_freqs[i][:,n])

            for idx, value in enumerate(array_pxx[i][:,n]):

                if value == np.max(array_pxx[i][:,n]):
                    peak_freq[:,n] = array_freqs[i][:,n][idx]

        peaks_freqs[i] = peak_freq
        means_freqs[i] = mean_freq
        freqs_80[i] = freq_80
        median_freqs[i] = median_freq

    return peaks_freqs, means_freqs, freqs_80, median_freqs

def parameters_fourrier_COP(freqs_array, pxx_array):

    peaks_freqs = {}
    means_freqs = {}
    median_freqs = {}
    freqs_80 = {}

    for i in freqs_array:

        freq_80 = {}
        median_freq = {}
        peak_freq = {}
        mean_freq = {}

        for j in freqs_array[i]:
            area = integrate.cumtrapz(pxx_array[i][j], freqs_array[i][j])
            find80 = np.where(area >= 0.8 * area[len(area) - 1])
            find50 = np.where(area >= 0.5 * area[len(area) - 1])


            freq_80[j] = freqs_array[i][j][find80[0][0]]
            median_freq[j] = freqs_array[i][j][find50[0][0]]

            mean_freq[j] = np.trapz((freqs_array[i][j] * pxx_array[i][j]),freqs_array[i][j]) / np.trapz(pxx_array[i][j],freqs_array[i][j])

            for idx, value in enumerate(pxx_array[i][j]):

                if value == np.max(pxx_array[i][j]):
                    peak_freq[j] = freqs_array[i][j][idx]


        peaks_freqs[i] =    {"COP_X": peak_freq["COP_X"], "COP_Y": peak_freq["COP_Y"]}
        means_freqs[i] =    {"COP_X": mean_freq["COP_X"], "COP_Y": mean_freq["COP_Y"]}
        freqs_80[i] =       {"COP_X": freq_80["COP_X"], "COP_Y": freq_80["COP_Y"]}
        median_freqs[i] =   {"COP_X": median_freq["COP_X"], "COP_Y": median_freq["COP_Y"]}

    return peaks_freqs, means_freqs, freqs_80, median_freqs


def alert(EMG):
    for i in EMG:
        for n in range(0,8):
            if EMG[i][n] > 95:
                print i
                print "\n"
                print n

def filter_EMG(array):
    EMG_filter = {}

    for i in array:
        EMG = np.zeros((len(array[i][:,0]), len(array[i][0,:])))

        for j in range(0, np.shape(array[i])[1]):
            EMG[:,j] = ni.filter.highpass(array[i][:,j],30,fs=1000)
        EMG_filter[i] = EMG


    return EMG_filter


def evolution_parameters(COP_array, COP_velocity):

    std = {}
    velocity = {}
    area = {}
    for i in COP_array:

        if i != "Reach_C" and i != "Reach_R" and i !="Reach_L":
            area_new = np.zeros((len(COP_array[i]["COP_X"]) / 2500.0))
            std_x_new = np.zeros((len(COP_array[i]["COP_X"]) / 2500.0))
            std_y_new = np.zeros((len(COP_array[i]["COP_Y"]) / 2500.0))
            velocity_x_new = np.zeros((len(COP_array[i]["COP_X"]) / 2500.0))
            velocity_y_new = np.zeros((len(COP_array[i]["COP_Y"]) / 2500.0))

            start = 0
            index = 0

            for count in range(2500, len(COP_array[i]["COP_X"]) + 1, 2500):

                area_traj = convex_hull(COP_array[i]["COP_X"][start:count], COP_array[i]["COP_Y"][start:count])
                area_new[index] = area_calc(area_traj)

                std_x_new[index] = np.std(COP_array[i]["COP_X"][start:count])
                std_y_new[index] = np.std(COP_array[i]["COP_Y"][start:count])
                velocity_x_new[index] = np.mean(COP_velocity[i]["COP_X"][start:count])
                velocity_y_new[index] = np.mean(COP_velocity[i]["COP_Y"][start:count])

                start = count
                index = index + 1

        else:
            area_new = np.zeros((len(COP_array[i]["COP_X"]) / 1000.0 ))
            std_x_new = np.zeros((len(COP_array[i]["COP_X"]) / 1000.0 ))
            std_y_new = np.zeros((len(COP_array[i]["COP_Y"]) / 1000.0 ))
            velocity_x_new = np.zeros((len(COP_array[i]["COP_X"]) / 1000.0))
            velocity_y_new = np.zeros((len(COP_array[i]["COP_Y"]) / 1000.0))

            start = 0
            index = 0

            for count in range(1000, len(COP_array[i]["COP_X"]) + 1, 1000):
                area_traj = convex_hull(COP_array[i]["COP_X"][start:count], COP_array[i]["COP_Y"][start:count])
                area_new[index] = area_calc(area_traj)

                std_x_new[index] = np.std(COP_array[i]["COP_X"][start:count])
                std_y_new[index] = np.std(COP_array[i]["COP_Y"][start:count])
                velocity_x_new[index] = np.mean(COP_velocity[i]["COP_X"][start:count])
                velocity_y_new[index] = np.mean(COP_velocity[i]["COP_Y"][start:count])

                start = count
                index = index + 1

        std[i] = {"COP_X": std_x_new, "COP_Y": std_y_new}
        velocity[i] = {"COP_X": velocity_x_new, "COP_Y": velocity_y_new}
        area[i] = area_new

    return std, velocity, area

def evolution_EMG(max_values, EMG_array):

    EMG_evolution = {}

    for i in EMG_array:
        if i != "Reach_C" and i != "Reach_R" and i != "Reach_L":

            EMG = np.zeros(((len(EMG_array[i][:,0]) / 2500.0), 8))

            for n in range(0, 8):

                start = 0
                count = 0
                for index in range(2500, len(EMG_array[i][:,n]) + 1,2500):

                    EMG[count, n] = (np.max(EMG_array[i][start:index, n])/max_values[i][n]) * 100.0


                    start = index
                    count = count + 1

        else:

            EMG = np.zeros(((len(EMG_array[i][:, 0]) / 1000.0), 8))



            for n in range(0, 8):

                start = 0
                count = 0
                for index in range(1000, len(EMG_array[i][:, n]) + 1, 1000):
                    EMG[count, n] = (np.max(EMG_array[i][start:index, n]) / max_values[i][n]) * 100.0



                    start = index
                    count = count + 1


        EMG_evolution[i] = EMG

    return EMG_evolution

def delete_EMG_values_freqs(over30, male, female, EA_over30, EA_evolved):

    for i in over30:
        EA_over30[i]["Ilicostalis_L"]["Peak"].pop(2)
        EA_over30[i]["Ilicostalis_L"]["Mean"].pop(2)
        EA_over30[i]["Ilicostalis_L"]["Median"].pop(2)
        EA_over30[i]["Ilicostalis_L"]["80_freq"].pop(2)

        EA_evolved[i]["Ilicostalis_R"]["Peak"].pop(0)
        EA_evolved[i]["Ilicostalis_R"]["Mean"].pop(0)
        EA_evolved[i]["Ilicostalis_R"]["Median"].pop(0)
        EA_evolved[i]["Ilicostalis_R"]["80_freq"].pop(0)

        over30[i]["Multi_L"]["Peak"].pop(3)
        over30[i]["Multi_L"]["Mean"].pop(3)
        over30[i]["Multi_L"]["Median"].pop(3)
        over30[i]["Multi_L"]["80_freq"].pop(3)

        female[i]["Ilicostalis_L"]["Peak"].pop(20)
        female[i]["Ilicostalis_L"]["Mean"].pop(20)
        female[i]["Ilicostalis_L"]["Median"].pop(20)
        female[i]["Ilicostalis_L"]["80_freq"].pop(20)

        male[i]["Ilicostalis_L"]["Peak"].pop(11)
        male[i]["Ilicostalis_L"]["Mean"].pop(11)
        male[i]["Ilicostalis_L"]["Median"].pop(11)
        male[i]["Ilicostalis_L"]["80_freq"].pop(11)

        male[i]["Obliques_L"]["Peak"].pop(11)
        male[i]["Obliques_L"]["Mean"].pop(11)
        male[i]["Obliques_L"]["Median"].pop(11)
        male[i]["Obliques_L"]["80_freq"].pop(11)

    for i in male["Reach_L"]:
        for n in male["Reach_L"][i]:
            male["OneFootStanding_R_EC"][i][n].pop(5)

    over30["Reach_L"]["Multi_L"]["Peak"].pop(3)
    over30["Reach_L"]["Multi_L"]["Mean"].pop(3)
    over30["Reach_L"]["Multi_L"]["Median"].pop(3)
    over30["Reach_L"]["Multi_L"]["80_freq"].pop(3)

    female["Standing_EO"]["Rectus_R"]["Peak"].pop(1)
    female["Standing_EO"]["Rectus_R"]["Mean"].pop(1)
    female["Standing_EO"]["Rectus_R"]["Median"].pop(1)
    female["Standing_EO"]["Rectus_R"]["80_freq"].pop(1)

    female["Standing_EC"]["Rectus_R"]["Peak"].pop(1)
    female["Standing_EC"]["Rectus_R"]["Mean"].pop(1)
    female["Standing_EC"]["Rectus_R"]["Median"].pop(1)
    female["Standing_EC"]["Rectus_R"]["80_freq"].pop(1)

    female["Reach_L"]["Rectus_R"]["Peak"].pop(1)
    female["Reach_L"]["Rectus_R"]["Mean"].pop(1)
    female["Reach_L"]["Rectus_R"]["Median"].pop(1)
    female["Reach_L"]["Rectus_R"]["80_freq"].pop(1)

    female["Reach_L"]["Ilicostalis_L"]["Peak"].pop(2)
    female["Reach_L"]["Ilicostalis_L"]["Mean"].pop(2)
    female["Reach_L"]["Ilicostalis_L"]["Median"].pop(2)
    female["Reach_L"]["Ilicostalis_L"]["80_freq"].pop(2)

    male["OneFootStanding_L_EO"]["Rectus_L"]["Peak"].pop(5)
    male["OneFootStanding_L_EO"]["Rectus_L"]["Mean"].pop(5)
    male["OneFootStanding_L_EO"]["Rectus_L"]["Median"].pop(5)
    male["OneFootStanding_L_EO"]["Rectus_L"]["80_freq"].pop(5)

    male["OneFootStanding_L_EO"]["Rectus_R"]["Peak"].pop(5)
    male["OneFootStanding_L_EO"]["Rectus_R"]["Mean"].pop(5)
    male["OneFootStanding_L_EO"]["Rectus_R"]["Median"].pop(5)
    male["OneFootStanding_L_EO"]["Rectus_R"]["80_freq"].pop(5)

    male["OneFootStanding_L_EO"]["Obliques_L"]["Peak"].pop(5)
    male["OneFootStanding_L_EO"]["Obliques_L"]["Mean"].pop(5)
    male["OneFootStanding_L_EO"]["Obliques_L"]["Median"].pop(5)
    male["OneFootStanding_L_EO"]["Obliques_L"]["80_freq"].pop(5)

    female["Reach_R"]["Multi_R"]["Peak"].pop(11)
    female["Reach_R"]["Multi_R"]["Mean"].pop(11)
    female["Reach_R"]["Multi_R"]["Median"].pop(11)
    female["Reach_R"]["Multi_R"]["80_freq"].pop(11)

    female["OneFootStanding_L_EC"]["Multi_R"]["Peak"].pop(17)
    female["OneFootStanding_L_EC"]["Multi_R"]["Mean"].pop(17)
    female["OneFootStanding_L_EC"]["Multi_R"]["Median"].pop(17)
    female["OneFootStanding_L_EC"]["Multi_R"]["80_freq"].pop(17)

    female["OneFootStanding_L_EO"]["Multi_R"]["Peak"].pop(17)
    female["OneFootStanding_L_EO"]["Multi_R"]["Mean"].pop(17)
    female["OneFootStanding_L_EO"]["Multi_R"]["Median"].pop(17)
    female["OneFootStanding_L_EO"]["Multi_R"]["80_freq"].pop(17)

    return over30, male, female, EA_over30, EA_evolved

def delete_EMG_values_tonus(over30, male, female, EA_over30, EA_evolved):

    for i in over30:
        EA_over30[i]["Ilicostalis_L"].pop(2)

        EA_evolved[i]["Ilicostalis_R"].pop(0)

        over30[i]["Multifidus_L"].pop(3)

        male[i]["Ilicostalis_L"].pop(11)

        male[i]["Obliques_L"].pop(11)

        female[i]["Ilicostalis_L"].pop(20)

    for n in male["Reach_L"]:
        male["OneFootStanding_R_EC"][n].pop(5)

    over30["Reach_L"]["Multifidus_L"].pop(3)

    female["Standing_EO"]["Rectus_R"].pop(1)

    female["Standing_EC"]["Rectus_R"].pop(1)

    female["Reach_L"]["Rectus_R"].pop(1)

    female["Reach_L"]["Ilicostalis_L"].pop(2)

    male["OneFootStanding_L_EO"]["Rectus_L"].pop(5)

    male["OneFootStanding_L_EO"]["Rectus_R"].pop(5)

    male["OneFootStanding_L_EO"]["Obliques_L"].pop(5)

    female["Reach_R"]["Multifidus_R"].pop(11)

    female["OneFootStanding_L_EC"]["Multifidus_R"].pop(17)

    female["OneFootStanding_L_EO"]["Multifidus_R"].pop(17)

    female["Reach_R"]["Multifidus_L"].pop(11)

    over30["Reach_C"]["Ilicostalis_L"].pop(1)


    return over30, male, female, EA_over30, EA_evolved

def eliminate_none_freqs(over30, male, female, EA_over30, EA_more):
    for muscle in over30:
        for freq in over30[muscle]:
            for i in range(0, len(over30[muscle][freq])-1):
                if over30[muscle][freq][i] == None:
                    over30[muscle][freq].pop(i)

            for n in range(0, len(male[muscle][freq])-1):
                if male[muscle][freq][n] == None:
                    male[muscle][freq].pop(n)

            for x in range(0, len(female[muscle][freq])-1):
                if female[muscle][freq][x] == None:
                    female[muscle][freq].pop(x)

            for y in range(0, len(EA_over30[muscle][freq])-1):
                if EA_over30[muscle][freq][y] == None:
                    EA_over30[muscle][freq].pop(y)

            for z in range(0, len(EA_more[muscle][freq])-1):
                if EA_more[muscle][freq][z] == None:
                    EA_more[muscle][freq].pop(z)

    return over30, male, female, EA_over30, EA_more

def IMC_calculater(over30, male, female, EA_over30, EA_more):
    IMC_over30 =[]
    IMC_male = []
    IMC_female = []
    IMC_EA_over30 = []
    IMC_more = []

    for i in range (0, len(over30["Weight"])):
        height = (over30["Height"][i]) * 0.01
        weight = over30["Weight"][i]
        IMC = weight / (height * height)
        IMC_over30.append(IMC)

    for n in range (0, len(male["Weight"])):
        height = (male["Height"][n]) * 0.01
        weight = male["Weight"][n]
        IMC = weight / (height * height)
        IMC_male.append(IMC)

    for x in range(0, len(female["Weight"])):
        height = (female["Height"][x]) * 0.01
        weight = female["Weight"][x]
        IMC = weight / (height * height)
        IMC_female.append(IMC)

    for y in range(0, len(EA_over30["Weight"])):
        height = (EA_over30["Height"][y]) * 0.01
        weight = EA_over30["Weight"][y]
        IMC = weight / (height * height)
        IMC_EA_over30.append(IMC)

    for z in range(0, len(EA_more["Weight"])):
        height = (EA_more["Height"][z]) * 0.01
        weight = EA_more["Weight"][z]
        IMC = weight / (height * height)
        IMC_more.append(IMC)

    return IMC_over30, IMC_male, IMC_female, IMC_EA_over30, IMC_more

def mean_muscles_correlation(over30, male, female, EA_over30, EA_more):
    mean_over30 = {}
    mean_male = {}
    mean_female = {}
    mean_EAover30 = {}
    mean_EAmore = {}


    for task in over30:
        muscle_mean_over30 = np.zeros((6, 8))
        muscle_mean_male = np.zeros((12, 8))
        muscle_mean_female = np.zeros((21, 8))
        muscle_mean_EAover30 = np.zeros((7, 8))
        muscle_mean_EAmore = np.zeros((3, 8))

        muscle_mean_over30[:, 0] = over30[task]["Rectus_L"]
        muscle_mean_over30[:, 1] = over30[task]["Rectus_R"]
        muscle_mean_over30[:, 2] = over30[task]["Obliques_L"]
        muscle_mean_over30[:, 3] = over30[task]["Obliques_R"]
        muscle_mean_over30[:, 4] = over30[task]["Ilicostalis_L"]
        muscle_mean_over30[:, 5] = over30[task]["Ilicostalis_R"]
        muscle_mean_over30[:, 6] = over30[task]["Multifidus_L"]
        muscle_mean_over30[:, 7] = over30[task]["Multifidus_R"]

        muscle_mean_male[:, 0] = male[task]["Rectus_L"]
        muscle_mean_male[:, 1] = male[task]["Rectus_R"]
        muscle_mean_male[:, 2] = male[task]["Obliques_L"]
        muscle_mean_male[:, 3] = male[task]["Obliques_R"]
        muscle_mean_male[:, 4] = male[task]["Ilicostalis_L"]
        muscle_mean_male[:, 5] = male[task]["Ilicostalis_R"]
        muscle_mean_male[:, 6] = male[task]["Multifidus_L"]
        muscle_mean_male[:, 7] = male[task]["Multifidus_R"]

        muscle_mean_female[:, 0] = female[task]["Rectus_L"]
        muscle_mean_female[:, 1] = female[task]["Rectus_R"]
        muscle_mean_female[:, 2] = female[task]["Obliques_L"]
        muscle_mean_female[:, 3] = female[task]["Obliques_R"]
        muscle_mean_female[:, 4] = female[task]["Ilicostalis_L"]
        muscle_mean_female[:, 5] = female[task]["Ilicostalis_R"]
        muscle_mean_female[:, 6] = female[task]["Multifidus_L"]
        muscle_mean_female[:, 7] = female[task]["Multifidus_R"]

        muscle_mean_EAover30[:, 0] = EA_over30[task]["Rectus_L"]
        muscle_mean_EAover30[:, 1] = EA_over30[task]["Rectus_R"]
        muscle_mean_EAover30[:, 2] = EA_over30[task]["Obliques_L"]
        muscle_mean_EAover30[:, 3] = EA_over30[task]["Obliques_R"]
        muscle_mean_EAover30[:, 4] = EA_over30[task]["Ilicostalis_L"]
        muscle_mean_EAover30[:, 5] = EA_over30[task]["Ilicostalis_R"]
        muscle_mean_EAover30[:, 6] = EA_over30[task]["Multifidus_L"]
        muscle_mean_EAover30[:, 7] = EA_over30[task]["Multifidus_R"]

        muscle_mean_EAmore[:, 0] = EA_more[task]["Rectus_L"]
        muscle_mean_EAmore[:, 1] = EA_more[task]["Rectus_R"]
        muscle_mean_EAmore[:, 2] = EA_more[task]["Obliques_L"]
        muscle_mean_EAmore[:, 3] = EA_more[task]["Obliques_R"]
        muscle_mean_EAmore[:, 4] = EA_more[task]["Ilicostalis_L"]
        muscle_mean_EAmore[:, 5] = EA_more[task]["Ilicostalis_R"]
        muscle_mean_EAmore[:, 6] = EA_more[task]["Multifidus_L"]
        muscle_mean_EAmore[:, 7] = EA_more[task]["Multifidus_R"]

        mean_over30[task] = muscle_mean_over30
        mean_male[task] = muscle_mean_male
        mean_female[task] = muscle_mean_female
        mean_EAover30[task] = muscle_mean_EAover30
        mean_EAmore[task] = muscle_mean_EAmore

    return mean_over30, mean_male, mean_female, mean_EAover30, mean_EAmore

def correlation_samemuscle_tasks(over30, male, female, EA_over30, EA_more):
    over30_corr = {}
    male_corr = {}
    female_corr = {}
    EA_over30_corr ={}
    EA_more_corr = {}


    for muscle in over30["Standing_EO"]:
        task_over30 = np.zeros((6, 9))
        task_male = np.zeros((12, 9))
        task_female = np.zeros((21, 9))
        task_EAover30 = np.zeros((7, 9))
        task_EAmore = np.zeros((3, 9))

        task_over30[:, 0] = over30["Standing_EO"][muscle]
        task_over30[:, 1] = over30["Standing_EC"][muscle]
        task_over30[:, 2] = over30["OneFootStanding_R_EO"][muscle]
        task_over30[:, 3] = over30["OneFootStanding_R_EC"][muscle]
        task_over30[:, 4] = over30["OneFootStanding_L_EO"][muscle]
        task_over30[:, 5] = over30["OneFootStanding_L_EC"][muscle]
        task_over30[:, 6] = over30["Reach_R"][muscle]
        task_over30[:, 7] = over30["Reach_L"][muscle]
        task_over30[:, 8] = over30["Reach_C"][muscle]

        task_male[:, 0] = male["Standing_EO"][muscle]
        task_male[:, 1] = male["Standing_EC"][muscle]
        task_male[:, 2] = male["OneFootStanding_R_EO"][muscle]
        task_male[:, 3] = male["OneFootStanding_R_EC"][muscle]
        task_male[:, 4] = male["OneFootStanding_L_EO"][muscle]
        task_male[:, 5] = male["OneFootStanding_L_EC"][muscle]
        task_male[:, 6] = male["Reach_R"][muscle]
        task_male[:, 7] = male["Reach_L"][muscle]
        task_male[:, 8] = male["Reach_C"][muscle]

        task_female[:, 0] = female["Standing_EO"][muscle]
        task_female[:, 1] = female["Standing_EC"][muscle]
        task_female[:, 2] = female["OneFootStanding_R_EO"][muscle]
        task_female[:, 3] = female["OneFootStanding_R_EC"][muscle]
        task_female[:, 4] = female["OneFootStanding_L_EO"][muscle]
        task_female[:, 5] = female["OneFootStanding_L_EC"][muscle]
        task_female[:, 6] = female["Reach_R"][muscle]
        task_female[:, 7] = female["Reach_L"][muscle]
        task_female[:, 8] = female["Reach_C"][muscle]

        task_EAover30[:, 0] = EA_over30["Standing_EO"][muscle]
        task_EAover30[:, 1] = EA_over30["Standing_EC"][muscle]
        task_EAover30[:, 2] = EA_over30["OneFootStanding_R_EO"][muscle]
        task_EAover30[:, 3] = EA_over30["OneFootStanding_R_EC"][muscle]
        task_EAover30[:, 4] = EA_over30["OneFootStanding_L_EO"][muscle]
        task_EAover30[:, 5] = EA_over30["OneFootStanding_L_EC"][muscle]
        task_EAover30[:, 6] = EA_over30["Reach_R"][muscle]
        task_EAover30[:, 7] = EA_over30["Reach_L"][muscle]
        task_EAover30[:, 8] = EA_over30["Reach_C"][muscle]

        task_EAmore[:, 0] = EA_more["Standing_EO"][muscle]
        task_EAmore[:, 1] = EA_more["Standing_EC"][muscle]
        task_EAmore[:, 2] = EA_more["OneFootStanding_R_EO"][muscle]
        task_EAmore[:, 3] = EA_more["OneFootStanding_R_EC"][muscle]
        task_EAmore[:, 4] = EA_more["OneFootStanding_L_EO"][muscle]
        task_EAmore[:, 5] = EA_more["OneFootStanding_L_EC"][muscle]
        task_EAmore[:, 6] = EA_more["Reach_R"][muscle]
        task_EAmore[:, 7] = EA_more["Reach_L"][muscle]
        task_EAmore[:, 8] = EA_more["Reach_C"][muscle]

        over30_corr[muscle] = task_over30
        male_corr[muscle] = task_male
        female_corr[muscle] = task_female
        EA_over30_corr[muscle] = task_EAover30
        EA_more_corr[muscle] = task_EAmore

    return over30_corr, male_corr, female_corr, EA_over30_corr, EA_more_corr

def eliminate_rest_values(over30, male, female, EAover30, EAmore):

    over30["Multifidus_L"].pop(3)
    EAover30["Ilicostalis_L"].pop(2)
    EAmore["Ilicostalis_R"].pop(0)
    male["Ilicostalis_R"].pop(6)
    male["Multifidus_R"].pop(6)
    male["Multifidus_L"].pop(11)
    male["Ilicostalis_L"].pop(11)
    male["Obliques_L"].pop(11)

    for muscle in female:
        female[muscle].pop(15)

    female["Obliques_L"].pop(15)
    female["Ilicostalis_L"].pop(15)

    female["Obliques_R"].pop(17)
    female["Rectus_L"].pop(17)
    female["Obliques_L"].pop(16)

    female["Obliques_L"].pop(17)
    female["Ilicostalis_L"].pop(18)
    female["Obliques_R"].pop(18)
    female["Multifidus_R"].pop(19)

    return over30, male, female, EAover30, EAmore

def eliminate_rest_freqs(over30, male, female, EAover30, EAmore):

    over30["Multi_L"]["80_freq"].pop(3)
    over30["Multi_L"]["Median"].pop(3)
    over30["Multi_L"]["Mean"].pop(3)
    over30["Multi_L"]["Peak"].pop(3)

    EAover30["Ilicostalis_L"]["80_freq"].pop(2)
    EAover30["Ilicostalis_L"]["Median"].pop(2)
    EAover30["Ilicostalis_L"]["Mean"].pop(2)
    EAover30["Ilicostalis_L"]["Peak"].pop(2)

    EAmore["Ilicostalis_R"]["80_freq"].pop(0)
    EAmore["Ilicostalis_R"]["Median"].pop(0)
    EAmore["Ilicostalis_R"]["Mean"].pop(0)
    EAmore["Ilicostalis_R"]["Peak"].pop(0)

    male["Ilicostalis_R"]["80_freq"].pop(6)
    male["Ilicostalis_R"]["Median"].pop(6)
    male["Ilicostalis_R"]["Mean"].pop(6)
    male["Ilicostalis_R"]["Peak"].pop(6)
    male["Multi_R"]["80_freq"].pop(6)
    male["Multi_R"]["Median"].pop(6)
    male["Multi_R"]["Mean"].pop(6)
    male["Multi_R"]["Peak"].pop(6)

    male["Multi_L"]["80_freq"].pop(11)
    male["Multi_L"]["Median"].pop(11)
    male["Multi_L"]["Mean"].pop(11)
    male["Multi_L"]["Peak"].pop(11)
    male["Ilicostalis_L"]["80_freq"].pop(11)
    male["Ilicostalis_L"]["Median"].pop(11)
    male["Ilicostalis_L"]["Mean"].pop(11)
    male["Ilicostalis_L"]["Peak"].pop(11)
    male["Obliques_L"]["80_freq"].pop(11)
    male["Obliques_L"]["Median"].pop(11)
    male["Obliques_L"]["Mean"].pop(11)
    male["Obliques_L"]["Peak"].pop(11)

    for muscle in female:
        female[muscle]["80_freq"].pop(15)
        female[muscle]["Median"].pop(15)
        female[muscle]["Mean"].pop(15)
        female[muscle]["Peak"].pop(15)

    female["Obliques_L"]["80_freq"].pop(15)
    female["Obliques_L"]["Median"].pop(15)
    female["Obliques_L"]["Mean"].pop(15)
    female["Obliques_L"]["Peak"].pop(15)
    female["Ilicostalis_L"]["80_freq"].pop(15)
    female["Ilicostalis_L"]["Median"].pop(15)
    female["Ilicostalis_L"]["Mean"].pop(15)
    female["Ilicostalis_L"]["Peak"].pop(15)

    female["Obliques_R"]["80_freq"].pop(17)
    female["Obliques_R"]["Median"].pop(17)
    female["Obliques_R"]["Mean"].pop(17)
    female["Obliques_R"]["Peak"].pop(17)
    female["Rectus_L"]["80_freq"].pop(17)
    female["Rectus_L"]["Median"].pop(17)
    female["Rectus_L"]["Mean"].pop(17)
    female["Rectus_L"]["Peak"].pop(17)
    female["Obliques_L"]["80_freq"].pop(16)
    female["Obliques_L"]["Median"].pop(16)
    female["Obliques_L"]["Mean"].pop(16)
    female["Obliques_L"]["Peak"].pop(16)

    female["Obliques_L"]["80_freq"].pop(14)
    female["Obliques_L"]["Median"].pop(14)
    female["Obliques_L"]["Mean"].pop(14)
    female["Obliques_L"]["Peak"].pop(14)
    female["Ilicostalis_L"]["80_freq"].pop(16)
    female["Ilicostalis_L"]["Median"].pop(16)
    female["Ilicostalis_L"]["Mean"].pop(16)
    female["Ilicostalis_L"]["Peak"].pop(16)
    female["Obliques_R"]["80_freq"].pop(16)
    female["Obliques_R"]["Median"].pop(16)
    female["Obliques_R"]["Mean"].pop(16)
    female["Obliques_R"]["Peak"].pop(16)
    female["Multi_R"]["80_freq"].pop(17)
    female["Multi_R"]["Median"].pop(17)
    female["Multi_R"]["Mean"].pop(17)
    female["Multi_R"]["Peak"].pop(17)

    return over30, male, female, EAover30, EAmore

def mean_muscles_correlation_single(EMG):
    array = {}

    for task in EMG:
        muscle = np.zeros((39,8))

        muscle[:, 0] = EMG[task]["Rectus_L"]
        muscle[:, 1] = EMG[task]["Rectus_R"]
        muscle[:, 2] = EMG[task]["Obliques_L"]
        muscle[:, 3] = EMG[task]["Obliques_R"]
        muscle[:, 4] = EMG[task]["Ilicostalis_L"]
        muscle[:, 5] = EMG[task]["Ilicostalis_R"]
        muscle[:, 6] = EMG[task]["Multifidus_L"]
        muscle[:, 7] = EMG[task]["Multifidus_R"]

        array[task] = muscle

    return array

def correlation_samemuscle_tasks_single(EMG):
    array = {}


    for muscle in EMG["Standing_EO"]:
        task_matrix = np.zeros((39, 9))

        task_matrix[:, 0] = EMG["Standing_EO"][muscle]
        task_matrix[:, 1] = EMG["Standing_EC"][muscle]
        task_matrix[:, 2] = EMG["OneFootStanding_R_EO"][muscle]
        task_matrix[:, 3] = EMG["OneFootStanding_R_EC"][muscle]
        task_matrix[:, 4] = EMG["OneFootStanding_L_EO"][muscle]
        task_matrix[:, 5] = EMG["OneFootStanding_L_EC"][muscle]
        task_matrix[:, 6] = EMG["Reach_R"][muscle]
        task_matrix[:, 7] = EMG["Reach_L"][muscle]
        task_matrix[:, 8] = EMG["Reach_C"][muscle]



        array[muscle] = task_matrix


    return array


