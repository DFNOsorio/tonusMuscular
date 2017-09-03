import scipy.fftpack as fft
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import butter, lfilter, freqz
from scipy import integrate
import novainstrumentation as ni
import numpy as np
from tools import *

def append_arrays_healthy(male, female, over30):

    array ={}
    for task in male:
        muscle_array = {}
        for muscle in male[task]:
            merged_list = []
            merged_list.extend(male[task][muscle])
            merged_list.extend(female[task][muscle])
            merged_list.extend(over30[task][muscle])

            muscle_array[muscle] = merged_list

        array[task] = muscle_array

    return array

def append_arrays_freqEMG_healthy(male, female, over30):

    array = {}
    for task in male:
        muscle_array = {}
        for muscle in male[task]:
            freq_array = {}
            for freq in male[task][muscle]:
                merged_list = []
                merged_list.extend(male[task][muscle][freq])
                merged_list.extend(female[task][muscle][freq])
                merged_list.extend(over30[task][muscle][freq])

                freq_array[freq] = merged_list
            muscle_array[muscle] = freq_array

        array[task] = muscle_array

    return array

def append_arrays_EA(EA, EA_over):

    array ={}
    for task in EA:
        muscle_array = {}
        for muscle in EA[task]:
            merged_list = []
            merged_list.extend(EA[task][muscle])
            merged_list.extend(EA_over[task][muscle])

            muscle_array[muscle] = merged_list

        array[task] = muscle_array

    return array

def append_arrays_freqEMG_EA(EA, EA_over):

    array = {}
    for task in EA:
        muscle_array = {}
        for muscle in EA[task]:
            freq_array = {}
            for freq in EA[task][muscle]:
                merged_list = []
                merged_list.extend(EA[task][muscle][freq])
                merged_list.extend(EA_over[task][muscle][freq])

                freq_array[freq] = merged_list
            muscle_array[muscle] = freq_array

        array[task] = muscle_array

    return array

def append_arrays_healthy_rest(male, female, over30):

    array ={}

    for muscle in male:
        merged_list = []
        merged_list.extend(male[muscle])
        merged_list.extend(female[muscle])

        array[muscle] = merged_list

    return array

def mean_std_values_EMG(EMG_array):

    mean_values = {}
    std_values = {}
    median_values = {}

    for task in EMG_array:
        muscle_mean = {}
        muscle_std = {}
        muscle_median = {}
        for muscle in EMG_array[task]:
            muscle_mean[muscle] = np.mean(EMG_array[task][muscle])
            muscle_std[muscle] = np.std(EMG_array[task][muscle])
            muscle_median[muscle] = np.median(EMG_array[task][muscle])

        mean_values[task] = muscle_mean
        std_values[task] = muscle_std
        median_values[task] = muscle_median

    return mean_values, std_values, median_values

def mean_std_values_EMG_rest(EMG_array):

    mean_values = {}
    std_values = {}
    median_values = {}


    for muscle in EMG_array:
        mean_values[muscle] = np.mean(EMG_array[muscle])
        std_values[muscle] = np.std(EMG_array[muscle])
        median_values[muscle] = np.median(EMG_array[muscle])


    return mean_values, std_values, median_values


def EMG_values_boxplot_healthy_vs_EA(EMG_healthy, EMG_EA):
    l = 0
    pp = PdfPages('EMG_Mean-Healthy_vs_SA.pdf')

    for i in EMG_EA:

        fig = plt.figure(l)
        l = l + 1
        fig.suptitle(str(i) + " - Mean Value of normalized EMG", fontsize=21)

        plot1 = plt.subplot2grid((4, 2), (0, 0))
        data_rectus_l = [[EMG_healthy[i]["Rectus_L"]], [EMG_EA[i]["Rectus_L"]]]
        plt.boxplot(data_rectus_l, positions = [1,2], widths = 0.6)
        plt.xticks([1,2], ("Healthy", "SA"), fontsize=8)
        plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
        plt.ylim([0, 140])
        plot1.set_title("Rectus Left", fontsize=12)

        plot2 = plt.subplot2grid((4, 2), (0, 1))
        data_rectus_R = [[EMG_healthy[i]["Rectus_R"]], [EMG_EA[i]["Rectus_R"]]]
        plt.boxplot(data_rectus_R, positions = [1,2], widths=0.6)
        plt.xticks([1, 2], ("Healthy", "SA"),fontsize=8)
        plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
        plt.ylim([0, 140])
        plot2.set_title("Rectus Right", fontsize=12)

        plot3 = plt.subplot2grid((4, 2), (1, 0))
        data_obliques_l = [[EMG_healthy[i]["Obliques_L"]], [EMG_EA[i]["Obliques_L"]]]
        plt.boxplot(data_obliques_l, positions = [1,2], widths=0.6)
        plt.xticks([1, 2], ("Healthy", "SA"),fontsize=8)
        plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
        plt.ylim([0, 140])
        plot3.set_title("Obliques Left", fontsize=12)

        plot4 = plt.subplot2grid((4, 2), (1, 1))
        data_obliques_r = [[EMG_healthy[i]["Obliques_R"]], [EMG_EA[i]["Obliques_R"]]]
        plt.boxplot(data_obliques_r, positions = [1,2], widths=0.6)
        plt.xticks([1, 2], ("Healthy", "SA"),fontsize=8)
        plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
        plt.ylim([0, 140])
        plot4.set_title("Obliques Right", fontsize=12)

        plot5 = plt.subplot2grid((4, 2), (2, 0))
        data_ilicostalis_l = [[EMG_healthy[i]["Ilicostalis_L"]], [EMG_EA[i]["Ilicostalis_L"]]]
        plt.boxplot(data_ilicostalis_l, positions = [1,2], widths=0.6)
        plt.xticks([1, 2], ("Healthy", "SA"), fontsize=8)
        plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
        plt.ylim([0, 140])
        plot5.set_title("Iliocostalis Left", fontsize=12)

        plot6 = plt.subplot2grid((4, 2), (2, 1))
        data_ilicostalis_r = [[EMG_healthy[i]["Ilicostalis_R"]], [EMG_EA[i]["Ilicostalis_R"]]]
        plt.boxplot(data_ilicostalis_r, positions = [1,2], widths=0.6)
        plt.xticks([1, 2], ("Healthy", "SA"), fontsize=8)
        plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
        plt.ylim([0, 140])
        plot6.set_title("Iliocostalis Right", fontsize=12)

        plot7 = plt.subplot2grid((4, 2), (3, 0))
        data_multi_l = [[EMG_healthy[i]["Multifidus_L"]], [EMG_EA[i]["Multifidus_L"]]]
        plt.boxplot(data_multi_l, positions = [1,2], widths=0.6)
        plt.xticks([1, 2], ("Healthy", "SA"),fontsize=8)
        plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
        plt.ylim([0, 140])
        plot7.set_title("Multifidus Left", fontsize=12)

        plot8 = plt.subplot2grid((4, 2), (3, 1))
        data_multi_r = [[EMG_healthy[i]["Multifidus_R"]], [EMG_EA[i]["Multifidus_R"]]]
        plt.boxplot(data_multi_r, positions = [1,2], widths=0.6)
        plt.xticks([1, 2], ("Healthy", "SA"),fontsize=8)
        plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
        plt.ylim([0, 140])
        plot8.set_title("Multifidus Right", fontsize=12)

        plt.subplots_adjust(top=0.90, bottom=0.10, left=0.12, right=0.90, wspace=0.44, hspace=0.45)
        plt.show()
        pp.savefig(fig)
    pp.close()

def EMG_freq_front_boxplot_HealthyvsSA(freqEMG_healthy, freqEMG_SA):
    l = 0
    pp = PdfPages('EMG_Freqs_Front-Healthy_vs_SA.pdf')

    for i in freqEMG_healthy:
        fig = plt.figure(l)
        l = l + 1
        fig.suptitle(str(i) + " - EMG Frequencies Front Muscles", fontsize=21)

        row_peak_mean = 0
        col_peak_mean = 0
        row_80_median = 2
        col_80_median = 0

        colors = ['blue', 'green']
        color_index = 0
        plt.figtext(0.29, 0.91, "Peak Frequency", horizontalalignment='center', multialignment='center', size=18,
                    clip_on=True)
        plt.figtext(0.71, 0.91, "Mean Frequency", horizontalalignment='center', multialignment='center', size=18,
                    clip_on=True)
        plt.figtext(0.29, 0.46, "80% Frequency", horizontalalignment='center', multialignment='center', size=18,
                    clip_on=True)
        plt.figtext(0.71, 0.46, "Median Frequency", horizontalalignment='center', multialignment='center', size=18,
                    clip_on=True)

        for freq in freqEMG_healthy[i]["Rectus_L"]:
            if freq == "Peak" or freq == "Mean":
                row_l = row_peak_mean
                col_l = col_peak_mean
                row_r = row_peak_mean
                col_r = col_peak_mean + 1

                for muscle in freqEMG_healthy[i]:
                    if muscle == "Rectus_L" or muscle == "Obliques_L":
                        plot = plt.subplot2grid((4, 4), (row_l, col_l))
                        data = [[freqEMG_healthy[i][muscle][freq]], [freqEMG_SA[i][muscle][freq]]]
                        box = plt.boxplot(data, positions=[1, 2], widths=0.6)
                        plt.xticks([1, 2],
                                   ("Healthy", "SA"),
                                   fontsize=7)
                        plot.set_title(str(muscle), fontsize=12, style = 'italic')
                        row_l = row_l + 1

                    if muscle == "Rectus_R" or muscle == "Obliques_R":
                        plot = plt.subplot2grid((4, 4), (row_r, col_r))
                        data = [[freqEMG_healthy[i][muscle][freq]], [freqEMG_SA[i][muscle][freq]]]
                        box = plt.boxplot(data, positions=[1, 2], widths=0.6)
                        plt.xticks([1, 2],
                                   ("Healthy", "SA"),
                                   fontsize=7)
                        plot.set_title(str(muscle), fontsize=12, style='italic')
                        row_r = row_r + 1

                col_peak_mean = col_peak_mean + 2
                color_index = color_index + 1

            if freq == "Median" or freq == "80_freq":
                row_l = row_80_median
                col_l = col_80_median
                row_r = row_80_median
                col_r = col_80_median + 1

                for muscle in freqEMG_healthy[i]:
                    if muscle == "Rectus_L" or muscle == "Obliques_L":
                        plot = plt.subplot2grid((4, 4), (row_l, col_l))
                        data = [[freqEMG_healthy[i][muscle][freq]], [freqEMG_SA[i][muscle][freq]]]
                        box = plt.boxplot(data, positions=[1, 2], widths=0.6)
                        plt.xticks([1, 2],
                                   ("Healthy", "SA"),
                                   fontsize=7)
                        plot.set_title(str(muscle), fontsize=12, style='italic')
                        row_l = row_l + 1

                    if muscle == "Rectus_R" or muscle == "Obliques_R":
                        plot = plt.subplot2grid((4, 4), (row_r, col_r))
                        data = [[freqEMG_healthy[i][muscle][freq]], [freqEMG_SA[i][muscle][freq]]]
                        box = plt.boxplot(data, positions=[1, 2], widths=0.6)
                        plt.xticks([1, 2],
                                   ("Healthy", "SA"),
                                   fontsize=7)
                        plot.set_title(str(muscle), fontsize=12, style='italic')
                        row_r = row_r + 1

                col_80_median = col_80_median + 2
                color_index = color_index + 1

        plt.subplots_adjust(top=0.89, bottom=0.05, left=0.12, right=0.90, wspace=0.56, hspace=0.67)
        plt.show()
        pp.savefig(fig)
    pp.close()

def EMG_freq_back_boxplot_HealthyvsSA(freqEMG_healthy, freqEMG_SA):
    l = 0
    pp = PdfPages('EMG_Freqs_Back-Healthy_vs_SA.pdf')

    for i in freqEMG_healthy:
        fig = plt.figure(l)
        l = l + 1
        fig.suptitle(str(i) + " - EMG Frequencies Back Muscles", fontsize=21)

        row_peak_mean = 0
        col_peak_mean = 0
        row_80_median = 2
        col_80_median = 0

        colors = ['blue', 'green']
        color_index = 0
        plt.figtext(0.29, 0.91, "Peak Frequency", horizontalalignment = 'center', multialignment = 'center', size = 18,
                    clip_on = True)
        plt.figtext(0.71, 0.91, "Mean Frequency", horizontalalignment='center', multialignment='center', size=18,
                    clip_on=True)
        plt.figtext(0.29, 0.46, "80% Frequency", horizontalalignment='center', multialignment='center', size=18,
                    clip_on=True)
        plt.figtext(0.71, 0.46, "Median Frequency", horizontalalignment='center', multialignment='center', size=18,
                    clip_on=True)

        for freq in freqEMG_healthy[i]["Rectus_L"]:
            if freq == "Peak" or freq == "Mean":
                row_l = row_peak_mean
                col_l = col_peak_mean
                row_r = row_peak_mean
                col_r = col_peak_mean + 1

                for muscle in freqEMG_healthy[i]:
                    if muscle == "Ilicostalis_L" or muscle == "Multi_L":
                        plot = plt.subplot2grid((4, 4), (row_l, col_l))
                        data = [[freqEMG_healthy[i][muscle][freq]], [freqEMG_SA[i][muscle][freq]]]
                        box = plt.boxplot(data, positions=[1, 2], widths=0.6)
                        plt.xticks([1, 2],
                                   ("Healthy", "SA"),
                                   fontsize=7)
                        plot.set_title(str(muscle), fontsize=12, style = 'italic')
                        row_l = row_l + 1

                    if muscle == "Ilicostalis_R" or muscle == "Multi_R":
                        plot = plt.subplot2grid((4, 4), (row_r, col_r))
                        data = [[freqEMG_healthy[i][muscle][freq]], [freqEMG_SA[i][muscle][freq]]]
                        box = plt.boxplot(data, positions=[1, 2], widths=0.6)
                        plt.xticks([1, 2],
                                   ("Healthy", "SA"),
                                   fontsize=7)
                        plot.set_title(str(muscle), fontsize=12, style='italic')
                        row_r = row_r + 1

                col_peak_mean = col_peak_mean + 2
                color_index = color_index + 1

            if freq == "Median" or freq == "80_freq":
                row_l = row_80_median
                col_l = col_80_median
                row_r = row_80_median
                col_r = col_80_median + 1

                for muscle in freqEMG_healthy[i]:
                    if muscle == "Ilicostalis_L" or muscle == "Multi_L":
                        plot = plt.subplot2grid((4, 4), (row_l, col_l))
                        data = [[freqEMG_healthy[i][muscle][freq]], [freqEMG_SA[i][muscle][freq]]]
                        box = plt.boxplot(data, positions=[1, 2], widths=0.6)
                        plt.xticks([1, 2],
                                   ("Healthy", "SA"),
                                   fontsize=7)
                        plot.set_title(str(muscle), fontsize=12, style='italic')
                        row_l = row_l + 1

                    if muscle == "Ilicostalis_R" or muscle == "Multi_R":
                        plot = plt.subplot2grid((4, 4), (row_r, col_r))
                        data = [[freqEMG_healthy[i][muscle][freq]], [freqEMG_SA[i][muscle][freq]]]
                        box = plt.boxplot(data, positions=[1, 2], widths=0.6)
                        plt.xticks([1, 2],
                                   ("Healthy", "SA"),
                                   fontsize=7)
                        plot.set_title(str(muscle), fontsize=12, style='italic')
                        row_r = row_r + 1

                col_80_median = col_80_median + 2
                color_index = color_index + 1

        plt.subplots_adjust(top=0.89, bottom=0.05, left=0.12, right=0.90, wspace=0.56, hspace=0.67)
        plt.show()
        pp.savefig(fig)
    pp.close()

def COP_freq_boxplot_HealthyvsSA(healthy_freqsCOP, SA_freqsCOP):
    l = 0
    pp = PdfPages('COP_Freqs-Healthy_vs_SA.pdf')

    for i in healthy_freqsCOP:
        fig = plt.figure(l)
        l = l + 1
        fig.suptitle(str(i) + " - COP Frequencies", fontsize=21)

        plot1 = plt.subplot2grid((2, 4), (0, 0))
        data_peak_x = [[healthy_freqsCOP[i]["Peak_X"]], [SA_freqsCOP[i]["Peak_X"]]]
        plt.boxplot(data_peak_x, positions=[1, 2], widths=0.6)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot1.set_title("Peak Frequency - COP X", fontsize=12)

        plot2 = plt.subplot2grid((2, 4), (0, 1))
        data_peak_y = [[healthy_freqsCOP[i]["Peak_Y"]], [SA_freqsCOP[i]["Peak_Y"]]]
        plt.boxplot(data_peak_y, positions=[1, 2], widths=0.6)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot2.set_title("Peak Frequency - COP Y", fontsize=12)

        plot3 = plt.subplot2grid((2, 4), (0, 2))
        data_mean_x = [[healthy_freqsCOP[i]["Mean_X"]], [SA_freqsCOP[i]["Mean_X"]]]
        plt.boxplot(data_mean_x, positions=[1, 2], widths=0.6)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot3.set_title("Mean Frequency - COP X", fontsize=12)

        plot4 = plt.subplot2grid((2, 4), (0, 3))
        data_mean_y = [[healthy_freqsCOP[i]["Mean_Y"]], [SA_freqsCOP[i]["Mean_Y"]]]
        plt.boxplot(data_mean_y, positions=[1, 2], widths=0.6)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot4.set_title("Mean Frequency - COP Y", fontsize=12)

        plot5 = plt.subplot2grid((2, 4), (1, 0))
        data_median_x = [[healthy_freqsCOP[i]["Median_X"]], [SA_freqsCOP[i]["Median_X"]]]
        plt.boxplot(data_median_x,positions=[1, 2], widths=0.6)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot5.set_title("Median Frequency - COP X", fontsize=12)

        plot6 = plt.subplot2grid((2, 4), (1, 1))
        data_median_y = [[healthy_freqsCOP[i]["Median_Y"]], [SA_freqsCOP[i]["Median_Y"]]]
        plt.boxplot(data_median_x, positions=[1, 2], widths=0.6)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot6.set_title("Median Frequency - COP Y", fontsize=12)

        plot7 = plt.subplot2grid((2, 4), (1, 2))
        data_80_X = [[healthy_freqsCOP[i]["80_X"]], [SA_freqsCOP[i]["80_X"]]]
        plt.boxplot(data_80_X, positions=[1, 2], widths=0.6)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot7.set_title("80% Frequency - COP X", fontsize=12)

        plot8 = plt.subplot2grid((2, 4), (1, 3))
        data_80_Y = [[healthy_freqsCOP[i]["80_Y"]], [SA_freqsCOP[i]["80_Y"]]]
        plt.boxplot(data_80_Y, positions=[1, 2], widths=0.6)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot8.set_title("80% Frequency - COP Y", fontsize=12)

        plt.subplots_adjust(top=0.90, bottom=0.10, left=0.12, right=0.90, wspace=0.31, hspace=0.27)
        plt.show()
        pp.savefig(fig)
    pp.close()

def COP_parameters_boxplot_HealthyvsSA(healthy_cop, SA_cop):
    l = 0
    pp = PdfPages('COP_Parameters-Healthy_vs_SA.pdf')

    for i in healthy_cop:
        fig = plt.figure(l)
        l = l + 1
        fig.suptitle(str(i) + " - COP Parameters", fontsize=21)

        plot1 = plt.subplot2grid((3, 3), (0, 0))
        data_velocity_x = [[healthy_cop[i]["Velocity_X"]], [SA_cop[i]["Velocity_X"]]]
        plt.boxplot(data_velocity_x, positions=[1, 2], widths=0.6)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot1.set_title("Velocity COP X", fontsize=12)

        plot2 = plt.subplot2grid((3, 3), (0, 1))
        data_velocity_y = [[healthy_cop[i]["Velocity_Y"]], [SA_cop[i]["Velocity_Y"]]]
        plt.boxplot(data_velocity_y, positions=[1, 2], widths=0.6)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot2.set_title("Velocity COP Y", fontsize=12)

        plot3 = plt.subplot2grid((3, 3), (1, 0))
        data_std_x = [[healthy_cop[i]["STD_X"]], [SA_cop[i]["STD_X"]]]
        plt.boxplot(data_std_x, positions=[1, 2], widths=0.6)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot3.set_title("STD COP X", fontsize=12)

        plot4 = plt.subplot2grid((3, 3), (1, 1))
        data_std_y = [[healthy_cop[i]["STD_Y"]], [SA_cop[i]["STD_Y"]]]
        plt.boxplot(data_std_y, positions=[1, 2], widths=0.6)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot4.set_title("STD COP Y", fontsize=12)

        plot5 = plt.subplot2grid((3, 3), (2, 0))
        data_amp_x = [[healthy_cop[i]["Amp_X"]], [SA_cop[i]["Amp_X"]]]
        plt.boxplot(data_amp_x, positions=[1, 2], widths=0.6)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot5.set_title("Amplitude COP X", fontsize=12)

        plot6 = plt.subplot2grid((3, 3), (2, 1))
        data_amp_y = [[healthy_cop[i]["Amp_Y"]], [SA_cop[i]["Amp_Y"]]]
        plt.boxplot(data_amp_y, positions=[1, 2], widths=0.6)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot6.set_title("Amplitude COP Y", fontsize=12)

        plot7 = plt.subplot2grid((3, 3), (1, 2))
        data_area = [[healthy_cop[i]["Area"]], [SA_cop[i]["Area"]]]
        plt.boxplot(data_area, positions=[1, 2], widths=0.6)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot7.set_title("Area", fontsize=12)

        plt.subplots_adjust(top=0.90, bottom=0.10, left=0.12, right=0.90, wspace=0.31, hspace=0.27)
        plt.show()
        pp.savefig(fig)
    pp.close()

def same_muscle_diferent_task_boxplot(EMG_healthy):
    l = 0
    #pp = PdfPages('EMG_Mean-Healthy_vs_SA.pdf')


    fig = plt.figure(l)

    fig.suptitle("Mean Value of normalized EMG", fontsize=21)

    plot1 = plt.subplot2grid((4, 2), (0, 0))
    data_rectus_l = [[EMG_healthy["Standing_EO"]["Rectus_L"]], [EMG_healthy["Standing_EC"]["Rectus_L"]],
                     [EMG_healthy["OneFootStanding_R_EO"]["Rectus_L"]], [EMG_healthy["OneFootStanding_R_EC"]["Rectus_L"]],
                     [EMG_healthy["OneFootStanding_L_EO"]["Rectus_L"]], [EMG_healthy["OneFootStanding_L_EC"]["Rectus_L"]],
                     [EMG_healthy["Reach_R"]["Rectus_L"]], [EMG_healthy["Reach_L"]["Rectus_L"]],
                     [EMG_healthy["Reach_C"]["Rectus_L"]]]
    plt.boxplot(data_rectus_l, positions = [1,2,3,4,5,6,7,8,9], widths = 0.6)
    plt.xticks([1,2,3,4,5,6,7,8,9], ('SEO', 'SEC', 'RFEO', 'RFEC', 'LFEO', 'LFEC', 'RR', 'RL', 'RC'), fontsize=8)
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 20])
    plot1.set_title("Rectus Left", fontsize=12)

    plot2 = plt.subplot2grid((4, 2), (0, 1))
    data_rectus_r = [[EMG_healthy["Standing_EO"]["Rectus_R"]], [EMG_healthy["Standing_EC"]["Rectus_R"]],
                     [EMG_healthy["OneFootStanding_R_EO"]["Rectus_R"]], [EMG_healthy["OneFootStanding_R_EC"]["Rectus_R"]],
                     [EMG_healthy["OneFootStanding_L_EO"]["Rectus_R"]], [EMG_healthy["OneFootStanding_L_EC"]["Rectus_R"]],
                     [EMG_healthy["Reach_R"]["Rectus_R"]], [EMG_healthy["Reach_L"]["Rectus_R"]],
                     [EMG_healthy["Reach_C"]["Rectus_R"]]]
    plt.boxplot(data_rectus_r, positions = [1,2,3,4,5,6,7,8,9], widths = 0.6)
    plt.xticks([1,2,3,4,5,6,7,8,9], ('SEO', 'SEC', 'RFEO', 'RFEC', 'LFEO', 'LFEC', 'RR', 'RL', 'RC'), fontsize=8)
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 20])
    plot2.set_title("Rectus Right", fontsize=12)

    plot3 = plt.subplot2grid((4, 2), (1, 0))
    data_obliques_l = [[EMG_healthy["Standing_EO"]["Obliques_L"]], [EMG_healthy["Standing_EC"]["Obliques_L"]],
                     [EMG_healthy["OneFootStanding_R_EO"]["Obliques_L"]], [EMG_healthy["OneFootStanding_R_EC"]["Obliques_L"]],
                     [EMG_healthy["OneFootStanding_L_EO"]["Obliques_L"]], [EMG_healthy["OneFootStanding_L_EC"]["Obliques_L"]],
                     [EMG_healthy["Reach_R"]["Obliques_L"]], [EMG_healthy["Reach_L"]["Obliques_L"]],
                     [EMG_healthy["Reach_C"]["Obliques_L"]]]
    plt.boxplot(data_obliques_l, positions = [1,2,3,4,5,6,7,8,9], widths = 0.6)
    plt.xticks([1,2,3,4,5,6,7,8,9], ('SEO', 'SEC', 'RFEO', 'RFEC', 'LFEO', 'LFEC', 'RR', 'RL', 'RC'), fontsize=8)
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 60])
    plot3.set_title("Obliques Left", fontsize=12)

    plot4 = plt.subplot2grid((4, 2), (1, 1))
    data_obliques_r = [[EMG_healthy["Standing_EO"]["Obliques_R"]], [EMG_healthy["Standing_EC"]["Obliques_R"]],
                     [EMG_healthy["OneFootStanding_R_EO"]["Obliques_R"]], [EMG_healthy["OneFootStanding_R_EC"]["Obliques_R"]],
                     [EMG_healthy["OneFootStanding_L_EO"]["Obliques_R"]], [EMG_healthy["OneFootStanding_L_EC"]["Obliques_R"]],
                     [EMG_healthy["Reach_R"]["Obliques_R"]], [EMG_healthy["Reach_L"]["Obliques_R"]],
                     [EMG_healthy["Reach_C"]["Obliques_R"]]]
    plt.boxplot(data_obliques_r, positions = [1,2,3,4,5,6,7,8,9], widths = 0.6)
    plt.xticks([1,2,3,4,5,6,7,8,9], ('SEO', 'SEC', 'RFEO', 'RFEC', 'LFEO', 'LFEC', 'RR', 'RL', 'RC'), fontsize=8)
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 60])
    plot4.set_title("Obliques Right", fontsize=12)

    plot5 = plt.subplot2grid((4, 2), (2, 0))
    data_ilicostalis_l = [[EMG_healthy["Standing_EO"]["Ilicostalis_L"]], [EMG_healthy["Standing_EC"]["Ilicostalis_L"]],
                     [EMG_healthy["OneFootStanding_R_EO"]["Ilicostalis_L"]], [EMG_healthy["OneFootStanding_R_EC"]["Ilicostalis_L"]],
                     [EMG_healthy["OneFootStanding_L_EO"]["Ilicostalis_L"]], [EMG_healthy["OneFootStanding_L_EC"]["Ilicostalis_L"]],
                     [EMG_healthy["Reach_R"]["Ilicostalis_L"]], [EMG_healthy["Reach_L"]["Ilicostalis_L"]],
                     [EMG_healthy["Reach_C"]["Ilicostalis_L"]]]
    plt.boxplot(data_ilicostalis_l, positions = [1,2,3,4,5,6,7,8,9], widths = 0.6)
    plt.xticks([1,2,3,4,5,6,7,8,9], ('SEO', 'SEC', 'RFEO', 'RFEC', 'LFEO', 'LFEC', 'RR', 'RL', 'RC'), fontsize=8)
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 40])
    plot5.set_title("Iliocostalis Left", fontsize=12)

    plot6 = plt.subplot2grid((4, 2), (2, 1))
    data_ilicostalis_r = [[EMG_healthy["Standing_EO"]["Ilicostalis_R"]], [EMG_healthy["Standing_EC"]["Ilicostalis_R"]],
                          [EMG_healthy["OneFootStanding_R_EO"]["Ilicostalis_R"]],
                          [EMG_healthy["OneFootStanding_R_EC"]["Ilicostalis_R"]],
                          [EMG_healthy["OneFootStanding_L_EO"]["Ilicostalis_R"]],
                          [EMG_healthy["OneFootStanding_L_EC"]["Ilicostalis_R"]],
                          [EMG_healthy["Reach_R"]["Ilicostalis_R"]], [EMG_healthy["Reach_L"]["Ilicostalis_R"]],
                          [EMG_healthy["Reach_C"]["Ilicostalis_R"]]]
    plt.boxplot(data_ilicostalis_r, positions=[1, 2, 3, 4, 5, 6, 7, 8, 9], widths=0.6)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9], ('SEO', 'SEC', 'RFEO', 'RFEC', 'LFEO', 'LFEC', 'RR', 'RL', 'RC'), fontsize=8)
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 40])
    plot6.set_title("Iliocostalis Right", fontsize=12)

    plot7 = plt.subplot2grid((4, 2), (3, 0))
    data_multi_l = [[EMG_healthy["Standing_EO"]["Multifidus_L"]], [EMG_healthy["Standing_EC"]["Multifidus_L"]],
                          [EMG_healthy["OneFootStanding_R_EO"]["Multifidus_L"]],
                          [EMG_healthy["OneFootStanding_R_EC"]["Multifidus_L"]],
                          [EMG_healthy["OneFootStanding_L_EO"]["Multifidus_L"]],
                          [EMG_healthy["OneFootStanding_L_EC"]["Multifidus_L"]],
                          [EMG_healthy["Reach_R"]["Multifidus_L"]], [EMG_healthy["Reach_L"]["Multifidus_L"]],
                          [EMG_healthy["Reach_C"]["Multifidus_L"]]]
    plt.boxplot(data_multi_l, positions=[1, 2, 3, 4, 5, 6, 7, 8, 9], widths=0.6)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9], ('SEO', 'SEC', 'RFEO', 'RFEC', 'LFEO', 'LFEC', 'RR', 'RL', 'RC'), fontsize=8)
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 20])
    plot7.set_title("Multifidus Left", fontsize=12)

    plot8 = plt.subplot2grid((4, 2), (3, 1))
    data_multi_r = [[EMG_healthy["Standing_EO"]["Multifidus_R"]], [EMG_healthy["Standing_EC"]["Multifidus_R"]],
                          [EMG_healthy["OneFootStanding_R_EO"]["Multifidus_R"]],
                          [EMG_healthy["OneFootStanding_R_EC"]["Multifidus_R"]],
                          [EMG_healthy["OneFootStanding_L_EO"]["Multifidus_R"]],
                          [EMG_healthy["OneFootStanding_L_EC"]["Multifidus_R"]],
                          [EMG_healthy["Reach_R"]["Multifidus_R"]], [EMG_healthy["Reach_L"]["Multifidus_R"]],
                          [EMG_healthy["Reach_C"]["Multifidus_R"]]]
    plt.boxplot(data_multi_r, positions=[1, 2, 3, 4, 5, 6, 7, 8, 9], widths=0.6)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9], ('SEO', 'SEC', 'RFEO', 'RFEC', 'LFEO', 'LFEC', 'RR', 'RL', 'RC'), fontsize=8)
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 20])
    plot8.set_title("Multifidus Right", fontsize=12)

    plt.subplots_adjust(top=0.90, bottom=0.10, left=0.12, right=0.90, wspace=0.44, hspace=0.45)
    plt.show()
    #pp.savefig(fig)
    #pp.close()

def same_task_diferent_muscle_boxplot(EMG_healthy):
    l = 0
    #pp = PdfPages('EMG_Mean-Healthy_vs_SA.pdf')


    fig = plt.figure(l)

    fig.suptitle("Mean Value of normalized EMG", fontsize=21)

    plot1 = plt.subplot2grid((5, 2), (0, 0))
    data_standing_eo = [[EMG_healthy["Standing_EO"]["Rectus_L"]], [EMG_healthy["Standing_EO"]["Rectus_R"]],
                     [EMG_healthy["Standing_EO"]["Obliques_L"]], [EMG_healthy["Standing_EO"]["Obliques_R"]],
                     [EMG_healthy["Standing_EO"]["Ilicostalis_L"]], [EMG_healthy["Standing_EO"]["Ilicostalis_R"]],
                     [EMG_healthy["Standing_EO"]["Multifidus_L"]], [EMG_healthy["Standing_EO"]["Multifidus_R"]]]
    plt.boxplot(data_standing_eo, positions = [1,2,3,4,5,6,7,8], widths = 0.6)
    plt.xticks([1,2,3,4,5,6,7,8], ("Rectus_L", "Rectus_R", "", "Obliques_L",
                                     "Obliques_R", "Iliocostalis_L", "Iliocostalis_R",
                                     "Multifidus_L", "Multifidus_R"), fontsize=8)
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 20])
    plot1.set_title("Standing EO", fontsize=12)

    plot2 = plt.subplot2grid((5, 2), (0, 1))
    data_standing_ec = [[EMG_healthy["Standing_EC"]["Rectus_L"]], [EMG_healthy["Standing_EC"]["Rectus_R"]],
                        [EMG_healthy["Standing_EC"]["Obliques_L"]], [EMG_healthy["Standing_EC"]["Obliques_R"]],
                        [EMG_healthy["Standing_EC"]["Ilicostalis_L"]], [EMG_healthy["Standing_EC"]["Ilicostalis_R"]],
                        [EMG_healthy["Standing_EC"]["Multifidus_L"]], [EMG_healthy["Standing_EC"]["Multifidus_R"]]]
    plt.boxplot(data_standing_ec, positions=[1, 2, 3, 4, 5, 6, 7, 8], widths=0.6)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8], ("Rectus_L", "Rectus_R", "", "Obliques_L",
                                          "Obliques_R", "Iliocostalis_L", "Iliocostalis_R",
                                          "Multifidus_L", "Multifidus_R"), fontsize=8)
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 20])
    plot2.set_title("Standing EC", fontsize=12)

    plot3 = plt.subplot2grid((5, 2), (1, 0))
    data_right_eo = [[EMG_healthy["OneFootStanding_R_EO"]["Rectus_L"]], [EMG_healthy["OneFootStanding_R_EO"]["Rectus_R"]],
                        [EMG_healthy["OneFootStanding_R_EO"]["Obliques_L"]], [EMG_healthy["OneFootStanding_R_EO"]["Obliques_R"]],
                        [EMG_healthy["OneFootStanding_R_EO"]["Ilicostalis_L"]], [EMG_healthy["OneFootStanding_R_EO"]["Ilicostalis_R"]],
                        [EMG_healthy["OneFootStanding_R_EO"]["Multifidus_L"]], [EMG_healthy["OneFootStanding_R_EO"]["Multifidus_R"]]]
    plt.boxplot(data_right_eo, positions=[1, 2, 3, 4, 5, 6, 7, 8], widths=0.6)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8], ("Rectus_L", "Rectus_R", "", "Obliques_L",
                                          "Obliques_R", "Iliocostalis_L", "Iliocostalis_R",
                                          "Multifidus_L", "Multifidus_R"), fontsize=8)
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 60])
    plot3.set_title("Right Foot Standing EO", fontsize=12)

    plot4 = plt.subplot2grid((5, 2), (1, 1))
    data_right_ec = [[EMG_healthy["OneFootStanding_R_EC"]["Rectus_L"]],
                     [EMG_healthy["OneFootStanding_R_EC"]["Rectus_R"]],
                     [EMG_healthy["OneFootStanding_R_EC"]["Obliques_L"]],
                     [EMG_healthy["OneFootStanding_R_EC"]["Obliques_R"]],
                     [EMG_healthy["OneFootStanding_R_EC"]["Ilicostalis_L"]],
                     [EMG_healthy["OneFootStanding_R_EC"]["Ilicostalis_R"]],
                     [EMG_healthy["OneFootStanding_R_EC"]["Multifidus_L"]],
                     [EMG_healthy["OneFootStanding_R_EC"]["Multifidus_R"]]]
    plt.boxplot(data_right_ec, positions=[1, 2, 3, 4, 5, 6, 7, 8], widths=0.6)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8], ("Rectus_L", "Rectus_R", "", "Obliques_L",
                                          "Obliques_R", "Iliocostalis_L", "Iliocostalis_R",
                                          "Multifidus_L", "Multifidus_R"), fontsize=8)
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 60])
    plot4.set_title("Right Foot Standing EC", fontsize=12)

    plot5 = plt.subplot2grid((5, 2), (2, 0))
    data_left_eo = [[EMG_healthy["OneFootStanding_L_EO"]["Rectus_L"]],
                     [EMG_healthy["OneFootStanding_L_EO"]["Rectus_R"]],
                     [EMG_healthy["OneFootStanding_L_EO"]["Obliques_L"]],
                     [EMG_healthy["OneFootStanding_L_EO"]["Obliques_R"]],
                     [EMG_healthy["OneFootStanding_L_EO"]["Ilicostalis_L"]],
                     [EMG_healthy["OneFootStanding_L_EO"]["Ilicostalis_R"]],
                     [EMG_healthy["OneFootStanding_L_EO"]["Multifidus_L"]],
                     [EMG_healthy["OneFootStanding_L_EO"]["Multifidus_R"]]]
    plt.boxplot(data_left_eo, positions=[1, 2, 3, 4, 5, 6, 7, 8], widths=0.6)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8], ("Rectus_L", "Rectus_R", "", "Obliques_L",
                                          "Obliques_R", "Iliocostalis_L", "Iliocostalis_R",
                                          "Multifidus_L", "Multifidus_R"), fontsize=8)
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 40])
    plot5.set_title("Left Foot Standing EO", fontsize=12)

    plot6 = plt.subplot2grid((5, 2), (2, 1))
    data_left_ec = [[EMG_healthy["OneFootStanding_L_EC"]["Rectus_L"]],
                    [EMG_healthy["OneFootStanding_L_EC"]["Rectus_R"]],
                    [EMG_healthy["OneFootStanding_L_EC"]["Obliques_L"]],
                    [EMG_healthy["OneFootStanding_L_EC"]["Obliques_R"]],
                    [EMG_healthy["OneFootStanding_L_EC"]["Ilicostalis_L"]],
                    [EMG_healthy["OneFootStanding_L_EC"]["Ilicostalis_R"]],
                    [EMG_healthy["OneFootStanding_L_EC"]["Multifidus_L"]],
                    [EMG_healthy["OneFootStanding_L_EC"]["Multifidus_R"]]]
    plt.boxplot(data_left_ec, positions=[1, 2, 3, 4, 5, 6, 7, 8], widths=0.6)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8], ("Rectus_L", "Rectus_R", "", "Obliques_L",
                                          "Obliques_R", "Iliocostalis_L", "Iliocostalis_R",
                                          "Multifidus_L", "Multifidus_R"), fontsize=8)
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 40])
    plot6.set_title("Left Foot Standing EC", fontsize=12)

    plot7 = plt.subplot2grid((5, 2), (3, 0))
    data_reach_r = [[EMG_healthy["Reach_R"]["Rectus_L"]],
                    [EMG_healthy["Reach_R"]["Rectus_R"]],
                    [EMG_healthy["Reach_R"]["Obliques_L"]],
                    [EMG_healthy["Reach_R"]["Obliques_R"]],
                    [EMG_healthy["Reach_R"]["Ilicostalis_L"]],
                    [EMG_healthy["Reach_R"]["Ilicostalis_R"]],
                    [EMG_healthy["Reach_R"]["Multifidus_L"]],
                    [EMG_healthy["Reach_R"]["Multifidus_R"]]]
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.boxplot(data_reach_r, positions=[1, 2, 3, 4, 5, 6, 7, 8], widths=0.6)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8], ("Rectus_L", "Rectus_R", "", "Obliques_L",
                                          "Obliques_R", "Iliocostalis_L", "Iliocostalis_R",
                                          "Multifidus_L", "Multifidus_R"), fontsize=8)
    plt.ylim([0, 20])
    plot7.set_title("Reach Right", fontsize=12)

    plot8 = plt.subplot2grid((5, 2), (3, 1))
    data_reach_l = [[EMG_healthy["Reach_L"]["Rectus_L"]],
                    [EMG_healthy["Reach_L"]["Rectus_R"]],
                    [EMG_healthy["Reach_L"]["Obliques_L"]],
                    [EMG_healthy["Reach_L"]["Obliques_R"]],
                    [EMG_healthy["Reach_L"]["Ilicostalis_L"]],
                    [EMG_healthy["Reach_L"]["Ilicostalis_R"]],
                    [EMG_healthy["Reach_L"]["Multifidus_L"]],
                    [EMG_healthy["Reach_L"]["Multifidus_R"]]]
    plt.boxplot(data_reach_l, positions=[1, 2, 3, 4, 5, 6, 7, 8], widths=0.6)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8], ("Rectus_L", "Rectus_R", "", "Obliques_L",
                                          "Obliques_R", "Iliocostalis_L", "Iliocostalis_R",
                                          "Multifidus_L", "Multifidus_R"), fontsize=8)
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 20])
    plot8.set_title("Reach Left", fontsize=12)

    plot9 = plt.subplot2grid((5, 2), (4, 0))
    data_reach_c = [[EMG_healthy["Reach_C"]["Rectus_L"]],
                    [EMG_healthy["Reach_C"]["Rectus_R"]],
                    [EMG_healthy["Reach_C"]["Obliques_L"]],
                    [EMG_healthy["Reach_C"]["Obliques_R"]],
                    [EMG_healthy["Reach_C"]["Ilicostalis_L"]],
                    [EMG_healthy["Reach_C"]["Ilicostalis_R"]],
                    [EMG_healthy["Reach_C"]["Multifidus_L"]],
                    [EMG_healthy["Reach_C"]["Multifidus_R"]]]
    plt.boxplot(data_reach_c, positions=[1, 2, 3, 4, 5, 6, 7, 8], widths=0.6)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8], ("Rectus_L", "Rectus_R", "", "Obliques_L",
                                          "Obliques_R", "Iliocostalis_L", "Iliocostalis_R",
                                          "Multifidus_L", "Multifidus_R"), fontsize=8)
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 20])
    plot9.set_title("Reach Center", fontsize=12)

    plt.subplots_adjust(top=0.90, bottom=0.10, left=0.12, right=0.90, wspace=0.44, hspace=0.45)
    plt.show()
    #pp.savefig(fig)
    #pp.close()


def same_muscle_diferent_task_barerror(EMG_mean, EMG_std, EMG_median):
    l = 0
    #pp = PdfPages('EMG_Mean-Healthy_vs_SA.pdf')

    n_groups = 9

    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    fig = plt.figure(l)

    fig.suptitle("Mean Value of normalized EMG", fontsize=21)

    plot1 = plt.subplot2grid((4, 2), (0, 0))
    mean_rectus_l = [EMG_mean["Standing_EO"]["Rectus_L"], EMG_mean["Standing_EC"]["Rectus_L"],
                     EMG_mean["OneFootStanding_R_EO"]["Rectus_L"], EMG_mean["OneFootStanding_R_EC"]["Rectus_L"],
                     EMG_mean["OneFootStanding_L_EO"]["Rectus_L"],EMG_mean["OneFootStanding_L_EC"]["Rectus_L"],
                     EMG_mean["Reach_R"]["Rectus_L"],EMG_mean["Reach_L"]["Rectus_L"],
                     EMG_mean["Reach_C"]["Rectus_L"]]

    std_rectus_l = [EMG_std["Standing_EO"]["Rectus_L"], EMG_std["Standing_EC"]["Rectus_L"],
                     EMG_std["OneFootStanding_R_EO"]["Rectus_L"], EMG_std["OneFootStanding_R_EC"]["Rectus_L"],
                     EMG_std["OneFootStanding_L_EO"]["Rectus_L"], EMG_std["OneFootStanding_L_EC"]["Rectus_L"],
                     EMG_std["Reach_R"]["Rectus_L"], EMG_std["Reach_L"]["Rectus_L"],
                     EMG_std["Reach_C"]["Rectus_L"]]

    median_rectus_l = [EMG_median["Standing_EO"]["Rectus_L"], EMG_median["Standing_EC"]["Rectus_L"],
                       EMG_median["OneFootStanding_R_EO"]["Rectus_L"], EMG_median["OneFootStanding_R_EC"]["Rectus_L"],
                       EMG_median["OneFootStanding_L_EO"]["Rectus_L"], EMG_median["OneFootStanding_L_EC"]["Rectus_L"],
                       EMG_median["Reach_R"]["Rectus_L"], EMG_median["Reach_L"]["Rectus_L"],
                       EMG_median["Reach_C"]["Rectus_L"]]

    rects1 = plt.bar(index,mean_rectus_l, bar_width,
                     alpha=opacity,
                     color='b',
                     yerr=std_rectus_l,
                     error_kw=error_config)

    plt.plot(index + 0.18, median_rectus_l, 'ro', color='b', label='Median Value')

    plt.xticks(index + bar_width / 2, ('SEO', 'SEC', 'RFEO', 'RFEC', 'LFEO', 'LFEC', 'RR', 'RL', 'RC'))
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 25])
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
    plot1.set_title("Rectus Left", fontsize=12)

    plot2 = plt.subplot2grid((4, 2), (0, 1))
    mean_rectus_r = [EMG_mean["Standing_EO"]["Rectus_R"], EMG_mean["Standing_EC"]["Rectus_R"],
                     EMG_mean["OneFootStanding_R_EO"]["Rectus_R"], EMG_mean["OneFootStanding_R_EC"]["Rectus_R"],
                     EMG_mean["OneFootStanding_L_EO"]["Rectus_R"], EMG_mean["OneFootStanding_L_EC"]["Rectus_R"],
                     EMG_mean["Reach_R"]["Rectus_R"], EMG_mean["Reach_L"]["Rectus_R"],
                     EMG_mean["Reach_C"]["Rectus_R"]]

    std_rectus_r = [EMG_std["Standing_EO"]["Rectus_R"], EMG_std["Standing_EC"]["Rectus_R"],
                    EMG_std["OneFootStanding_R_EO"]["Rectus_R"], EMG_std["OneFootStanding_R_EC"]["Rectus_R"],
                    EMG_std["OneFootStanding_L_EO"]["Rectus_R"], EMG_std["OneFootStanding_L_EC"]["Rectus_R"],
                    EMG_std["Reach_R"]["Rectus_R"], EMG_std["Reach_L"]["Rectus_R"],
                    EMG_std["Reach_C"]["Rectus_R"]]

    median_rectus_r = [EMG_median["Standing_EO"]["Rectus_R"], EMG_median["Standing_EC"]["Rectus_R"],
                       EMG_median["OneFootStanding_R_EO"]["Rectus_R"], EMG_median["OneFootStanding_R_EC"]["Rectus_R"],
                       EMG_median["OneFootStanding_L_EO"]["Rectus_R"], EMG_median["OneFootStanding_L_EC"]["Rectus_R"],
                       EMG_median["Reach_R"]["Rectus_R"], EMG_median["Reach_L"]["Rectus_R"],
                       EMG_median["Reach_C"]["Rectus_R"]]

    rects1 = plt.bar(index, mean_rectus_r, bar_width,
                     alpha=opacity,
                     color='r',
                     yerr=std_rectus_r,
                     error_kw=error_config)

    plt.plot(index + 0.18, median_rectus_r, 'ro', color='r', label='Median Value')

    plt.xticks(index + bar_width / 2, ('SEO', 'SEC', 'RFEO', 'RFEC', 'LFEO', 'LFEC', 'RR', 'RL', 'RC'))
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 25])
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
    plot2.set_title("Rectus Right", fontsize=12)

    plot3 = plt.subplot2grid((4, 2), (1, 0))
    mean_obliques_l = [EMG_mean["Standing_EO"]["Obliques_L"], EMG_mean["Standing_EC"]["Obliques_L"],
                     EMG_mean["OneFootStanding_R_EO"]["Obliques_L"], EMG_mean["OneFootStanding_R_EC"]["Obliques_L"],
                     EMG_mean["OneFootStanding_L_EO"]["Obliques_L"], EMG_mean["OneFootStanding_L_EC"]["Obliques_L"],
                     EMG_mean["Reach_R"]["Obliques_L"], EMG_mean["Reach_L"]["Obliques_L"],
                     EMG_mean["Reach_C"]["Obliques_L"]]

    std_obliques_l = [EMG_std["Standing_EO"]["Obliques_L"], EMG_std["Standing_EC"]["Obliques_L"],
                    EMG_std["OneFootStanding_R_EO"]["Obliques_L"], EMG_std["OneFootStanding_R_EC"]["Obliques_L"],
                    EMG_std["OneFootStanding_L_EO"]["Obliques_L"], EMG_std["OneFootStanding_L_EC"]["Obliques_L"],
                    EMG_std["Reach_R"]["Obliques_L"], EMG_std["Reach_L"]["Obliques_L"],
                    EMG_std["Reach_C"]["Obliques_L"]]

    median_obliques_l = [EMG_median["Standing_EO"]["Obliques_L"], EMG_median["Standing_EC"]["Obliques_L"],
                         EMG_median["OneFootStanding_R_EO"]["Obliques_L"], EMG_median["OneFootStanding_R_EC"]["Obliques_L"],
                         EMG_median["OneFootStanding_L_EO"]["Obliques_L"], EMG_median["OneFootStanding_L_EC"]["Obliques_L"],
                         EMG_median["Reach_R"]["Obliques_L"], EMG_median["Reach_L"]["Obliques_L"],
                         EMG_median["Reach_C"]["Obliques_L"]]

    rects1 = plt.bar(index, mean_obliques_l, bar_width,
                     alpha=opacity,
                     color='g',
                     yerr=std_obliques_l,
                     error_kw=error_config)

    plt.plot(index + 0.18, median_obliques_l, 'ro', color='g', label='Median Value')

    plt.xticks(index + bar_width / 2, ('SEO', 'SEC', 'RFEO', 'RFEC', 'LFEO', 'LFEC', 'RR', 'RL', 'RC'))
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 40])
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
    plot3.set_title("Obliques Left", fontsize=12)

    plot4 = plt.subplot2grid((4, 2), (1, 1))
    mean_obliques_r = [EMG_mean["Standing_EO"]["Obliques_R"], EMG_mean["Standing_EC"]["Obliques_R"],
                       EMG_mean["OneFootStanding_R_EO"]["Obliques_R"], EMG_mean["OneFootStanding_R_EC"]["Obliques_R"],
                       EMG_mean["OneFootStanding_L_EO"]["Obliques_R"], EMG_mean["OneFootStanding_L_EC"]["Obliques_R"],
                       EMG_mean["Reach_R"]["Obliques_R"], EMG_mean["Reach_L"]["Obliques_R"],
                       EMG_mean["Reach_C"]["Obliques_R"]]

    std_obliques_r = [EMG_std["Standing_EO"]["Obliques_R"], EMG_std["Standing_EC"]["Obliques_R"],
                      EMG_std["OneFootStanding_R_EO"]["Obliques_R"], EMG_std["OneFootStanding_R_EC"]["Obliques_R"],
                      EMG_std["OneFootStanding_L_EO"]["Obliques_R"], EMG_std["OneFootStanding_L_EC"]["Obliques_R"],
                      EMG_std["Reach_R"]["Obliques_R"], EMG_std["Reach_L"]["Obliques_R"],
                      EMG_std["Reach_C"]["Obliques_R"]]

    median_obliques_r = [EMG_median["Standing_EO"]["Obliques_R"], EMG_median["Standing_EC"]["Obliques_R"],
                         EMG_median["OneFootStanding_R_EO"]["Obliques_R"], EMG_median["OneFootStanding_R_EC"]["Obliques_R"],
                         EMG_median["OneFootStanding_L_EO"]["Obliques_R"], EMG_median["OneFootStanding_L_EC"]["Obliques_R"],
                         EMG_median["Reach_R"]["Obliques_R"], EMG_median["Reach_L"]["Obliques_R"],
                         EMG_median["Reach_C"]["Obliques_R"]]

    rects1 = plt.bar(index, mean_obliques_r, bar_width,
                     alpha=opacity,
                     color='c',
                     yerr=std_obliques_r,
                     error_kw=error_config)
    plt.plot(index + 0.18, median_obliques_r, 'ro', color='g', label='Median Value')

    plt.xticks(index + bar_width / 2, ('SEO', 'SEC', 'RFEO', 'RFEC', 'LFEO', 'LFEC', 'RR', 'RL', 'RC'))
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 40])
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
    plot4.set_title("Obliques Right", fontsize=12)

    plot5 = plt.subplot2grid((4, 2), (2, 0))
    mean_ilicostalis_l = [EMG_mean["Standing_EO"]["Ilicostalis_L"], EMG_mean["Standing_EC"]["Ilicostalis_L"],
                       EMG_mean["OneFootStanding_R_EO"]["Ilicostalis_L"], EMG_mean["OneFootStanding_R_EC"]["Ilicostalis_L"],
                       EMG_mean["OneFootStanding_L_EO"]["Ilicostalis_L"], EMG_mean["OneFootStanding_L_EC"]["Ilicostalis_L"],
                       EMG_mean["Reach_R"]["Ilicostalis_L"], EMG_mean["Reach_L"]["Ilicostalis_L"],
                       EMG_mean["Reach_C"]["Ilicostalis_L"]]

    std_ilicostalis_l = [EMG_std["Standing_EO"]["Ilicostalis_L"], EMG_std["Standing_EC"]["Ilicostalis_L"],
                      EMG_std["OneFootStanding_R_EO"]["Ilicostalis_L"], EMG_std["OneFootStanding_R_EC"]["Ilicostalis_L"],
                      EMG_std["OneFootStanding_L_EO"]["Ilicostalis_L"], EMG_std["OneFootStanding_L_EC"]["Ilicostalis_L"],
                      EMG_std["Reach_R"]["Ilicostalis_L"], EMG_std["Reach_L"]["Ilicostalis_L"],
                      EMG_std["Reach_C"]["Ilicostalis_L"]]

    median_ilicostalis_l = [EMG_median["Standing_EO"]["Ilicostalis_L"], EMG_median["Standing_EC"]["Ilicostalis_L"],
                            EMG_median["OneFootStanding_R_EO"]["Ilicostalis_L"],
                            EMG_median["OneFootStanding_R_EC"]["Ilicostalis_L"],
                            EMG_median["OneFootStanding_L_EO"]["Ilicostalis_L"],
                            EMG_median["OneFootStanding_L_EC"]["Ilicostalis_L"],
                            EMG_median["Reach_R"]["Ilicostalis_L"], EMG_median["Reach_L"]["Ilicostalis_L"],
                            EMG_median["Reach_C"]["Ilicostalis_L"]]

    rects1 = plt.bar(index, mean_ilicostalis_l, bar_width,
                     alpha=opacity,
                     color='m',
                     yerr=std_ilicostalis_l,
                     error_kw=error_config)

    plt.plot(index + 0.18, median_ilicostalis_l, 'ro', color='m', label='Median Value')

    plt.xticks(index + bar_width / 2, ('SEO', 'SEC', 'RFEO', 'RFEC', 'LFEO', 'LFEC', 'RR', 'RL', 'RC'))
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 50])
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
    plot5.set_title("Iliocostalis Left", fontsize=12)

    plot6 = plt.subplot2grid((4, 2), (2, 1))
    mean_ilicostalis_r = [EMG_mean["Standing_EO"]["Ilicostalis_R"], EMG_mean["Standing_EC"]["Ilicostalis_R"],
                          EMG_mean["OneFootStanding_R_EO"]["Ilicostalis_R"],
                          EMG_mean["OneFootStanding_R_EC"]["Ilicostalis_R"],
                          EMG_mean["OneFootStanding_L_EO"]["Ilicostalis_R"],
                          EMG_mean["OneFootStanding_L_EC"]["Ilicostalis_R"],
                          EMG_mean["Reach_R"]["Ilicostalis_R"], EMG_mean["Reach_L"]["Ilicostalis_R"],
                          EMG_mean["Reach_C"]["Ilicostalis_R"]]

    std_ilicostalis_r = [EMG_std["Standing_EO"]["Ilicostalis_R"], EMG_std["Standing_EC"]["Ilicostalis_R"],
                         EMG_std["OneFootStanding_R_EO"]["Ilicostalis_R"],
                         EMG_std["OneFootStanding_R_EC"]["Ilicostalis_R"],
                         EMG_std["OneFootStanding_L_EO"]["Ilicostalis_R"],
                         EMG_std["OneFootStanding_L_EC"]["Ilicostalis_R"],
                         EMG_std["Reach_R"]["Ilicostalis_R"], EMG_std["Reach_L"]["Ilicostalis_R"],
                         EMG_std["Reach_C"]["Ilicostalis_R"]]

    median_ilicostalis_r = [EMG_median["Standing_EO"]["Ilicostalis_R"], EMG_median["Standing_EC"]["Ilicostalis_R"],
                            EMG_median["OneFootStanding_R_EO"]["Ilicostalis_R"],
                            EMG_median["OneFootStanding_R_EC"]["Ilicostalis_R"],
                            EMG_median["OneFootStanding_L_EO"]["Ilicostalis_R"],
                            EMG_median["OneFootStanding_L_EC"]["Ilicostalis_R"],
                            EMG_median["Reach_R"]["Ilicostalis_R"], EMG_median["Reach_L"]["Ilicostalis_R"],
                            EMG_median["Reach_C"]["Ilicostalis_R"]]

    rects1 = plt.bar(index, mean_ilicostalis_r, bar_width,
                     alpha=opacity,
                     color='y',
                     yerr=std_ilicostalis_r,
                     error_kw=error_config)

    plt.plot(index + 0.18, median_ilicostalis_r, 'ro', color='y', label='Median Value')

    plt.xticks(index + bar_width / 2, ('SEO', 'SEC', 'RFEO', 'RFEC', 'LFEO', 'LFEC', 'RR', 'RL', 'RC'))
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 25])
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
    plot6.set_title("Iliocostalis Right", fontsize=12)

    plot7 = plt.subplot2grid((4, 2), (3, 0))
    mean_multi_l = [EMG_mean["Standing_EO"]["Multifidus_L"], EMG_mean["Standing_EC"]["Multifidus_L"],
                          EMG_mean["OneFootStanding_R_EO"]["Multifidus_L"],
                          EMG_mean["OneFootStanding_R_EC"]["Multifidus_L"],
                          EMG_mean["OneFootStanding_L_EO"]["Multifidus_L"],
                          EMG_mean["OneFootStanding_L_EC"]["Multifidus_L"],
                          EMG_mean["Reach_R"]["Multifidus_L"], EMG_mean["Reach_L"]["Multifidus_L"],
                          EMG_mean["Reach_C"]["Multifidus_L"]]

    std_multi_l = [EMG_std["Standing_EO"]["Multifidus_L"], EMG_std["Standing_EC"]["Multifidus_L"],
                         EMG_std["OneFootStanding_R_EO"]["Multifidus_L"],
                         EMG_std["OneFootStanding_R_EC"]["Multifidus_L"],
                         EMG_std["OneFootStanding_L_EO"]["Multifidus_L"],
                         EMG_std["OneFootStanding_L_EC"]["Multifidus_L"],
                         EMG_std["Reach_R"]["Multifidus_L"], EMG_std["Reach_L"]["Multifidus_L"],
                         EMG_std["Reach_C"]["Multifidus_L"]]

    median_multi_l = [EMG_median["Standing_EO"]["Multifidus_L"], EMG_median["Standing_EC"]["Multifidus_L"],
                      EMG_median["OneFootStanding_R_EO"]["Multifidus_L"],
                      EMG_median["OneFootStanding_R_EC"]["Multifidus_L"],
                      EMG_median["OneFootStanding_L_EO"]["Multifidus_L"],
                      EMG_median["OneFootStanding_L_EC"]["Multifidus_L"],
                      EMG_median["Reach_R"]["Multifidus_L"], EMG_median["Reach_L"]["Multifidus_L"],
                      EMG_median["Reach_C"]["Multifidus_L"]]

    rects1 = plt.bar(index, mean_multi_l, bar_width,
                     alpha=opacity,
                     color='teal',
                     yerr=std_multi_l,
                     error_kw=error_config)

    plt.plot(index + 0.18, median_multi_l, 'ro', color='teal', label='Median Value')

    plt.xticks(index + bar_width / 2, ('SEO', 'SEC', 'RFEO', 'RFEC', 'LFEO', 'LFEC', 'RR', 'RL', 'RC'))
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 40])
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
    plot7.set_title("Multifidus Left", fontsize=12)

    plot8 = plt.subplot2grid((4, 2), (3, 1))
    mean_multi_r = [EMG_mean["Standing_EO"]["Multifidus_R"], EMG_mean["Standing_EC"]["Multifidus_R"],
                    EMG_mean["OneFootStanding_R_EO"]["Multifidus_R"],
                    EMG_mean["OneFootStanding_R_EC"]["Multifidus_R"],
                    EMG_mean["OneFootStanding_L_EO"]["Multifidus_R"],
                    EMG_mean["OneFootStanding_L_EC"]["Multifidus_R"],
                    EMG_mean["Reach_R"]["Multifidus_R"], EMG_mean["Reach_L"]["Multifidus_R"],
                    EMG_mean["Reach_C"]["Multifidus_R"]]

    std_multi_r = [EMG_std["Standing_EO"]["Multifidus_R"], EMG_std["Standing_EC"]["Multifidus_R"],
                   EMG_std["OneFootStanding_R_EO"]["Multifidus_R"],
                   EMG_std["OneFootStanding_R_EC"]["Multifidus_R"],
                   EMG_std["OneFootStanding_L_EO"]["Multifidus_R"],
                   EMG_std["OneFootStanding_L_EC"]["Multifidus_R"],
                   EMG_std["Reach_R"]["Multifidus_R"], EMG_std["Reach_L"]["Multifidus_R"],
                   EMG_std["Reach_C"]["Multifidus_R"]]

    median_multi_r = [EMG_median["Standing_EO"]["Multifidus_R"], EMG_median["Standing_EC"]["Multifidus_R"],
                      EMG_median["OneFootStanding_R_EO"]["Multifidus_R"],
                      EMG_median["OneFootStanding_R_EC"]["Multifidus_R"],
                      EMG_median["OneFootStanding_L_EO"]["Multifidus_R"],
                      EMG_median["OneFootStanding_L_EC"]["Multifidus_R"],
                      EMG_median["Reach_R"]["Multifidus_R"], EMG_median["Reach_L"]["Multifidus_R"],
                      EMG_median["Reach_C"]["Multifidus_R"]]

    rects1 = plt.bar(index, mean_multi_r, bar_width,
                     alpha=opacity,
                     color='skyblue',
                     yerr=std_multi_r,
                     error_kw=error_config)

    plt.plot(index + 0.18, median_multi_r, 'ro', color='skyblue', label='Median Value')

    plt.xticks(index + bar_width / 2, ('SEO', 'SEC', 'RFEO', 'RFEC', 'LFEO', 'LFEC', 'RR', 'RL', 'RC'))
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 40])
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
    plot8.set_title("Multifidus Right", fontsize=12)

    plt.subplots_adjust(top=0.90, bottom=0.10, left=0.12, right=0.90, wspace=0.44, hspace=0.45)
    plt.show()
    #pp.savefig(fig)
    #pp.close()

def same_task_diferent_muscle_barerror(EMG_mean, EMG_std, EMG_median):
    l = 0
    #pp = PdfPages('EMG_Mean-Healthy_vs_SA.pdf')

    n_groups = 8

    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    fig = plt.figure(l)

    fig.suptitle("Mean Value of normalized EMG", fontsize=21)

    plot1 = plt.subplot2grid((5, 2), (0, 0))
    mean_standing_eo = [EMG_mean["Standing_EO"]["Rectus_L"], EMG_mean["Standing_EO"]["Rectus_R"],
                     EMG_mean["Standing_EO"]["Obliques_L"], EMG_mean["Standing_EO"]["Obliques_R"],
                     EMG_mean["Standing_EO"]["Ilicostalis_L"], EMG_mean["Standing_EO"]["Ilicostalis_R"],
                     EMG_mean["Standing_EO"]["Multifidus_L"], EMG_mean["Standing_EO"]["Multifidus_R"]]

    std_standing_eo = [EMG_std["Standing_EO"]["Rectus_L"], EMG_std["Standing_EO"]["Rectus_R"],
                       EMG_std["Standing_EO"]["Obliques_L"], EMG_std["Standing_EO"]["Obliques_R"],
                       EMG_std["Standing_EO"]["Ilicostalis_L"], EMG_std["Standing_EO"]["Ilicostalis_R"],
                       EMG_std["Standing_EO"]["Multifidus_L"], EMG_std["Standing_EO"]["Multifidus_R"]]

    median_standing_eo = [EMG_median["Standing_EO"]["Rectus_L"], EMG_median["Standing_EO"]["Rectus_R"],
                       EMG_median["Standing_EO"]["Obliques_L"], EMG_median["Standing_EO"]["Obliques_R"],
                       EMG_median["Standing_EO"]["Ilicostalis_L"], EMG_median["Standing_EO"]["Ilicostalis_R"],
                       EMG_median["Standing_EO"]["Multifidus_L"], EMG_median["Standing_EO"]["Multifidus_R"]]

    rects1 = plt.bar(index,mean_standing_eo, bar_width,
                     alpha=opacity,
                     color='b',
                     yerr=std_standing_eo,
                     error_kw=error_config)

    plt.plot(index + 0.18, median_standing_eo,'ro', color = 'b', label = 'Median Value')

    plt.xticks(index + bar_width / 2, ('RL', 'RR', 'OL', 'OR', 'IL', 'IR', 'ML', 'MR'))
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 20])
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
    plot1.set_title("Standing Eyes Open", fontsize=12)

    plot2 = plt.subplot2grid((5, 2), (0, 1))
    mean_standing_ec = [EMG_mean["Standing_EC"]["Rectus_L"], EMG_mean["Standing_EC"]["Rectus_R"],
                        EMG_mean["Standing_EC"]["Obliques_L"], EMG_mean["Standing_EC"]["Obliques_R"],
                        EMG_mean["Standing_EC"]["Ilicostalis_L"], EMG_mean["Standing_EC"]["Ilicostalis_R"],
                        EMG_mean["Standing_EC"]["Multifidus_L"], EMG_mean["Standing_EC"]["Multifidus_R"]]

    std_standing_ec = [EMG_std["Standing_EC"]["Rectus_L"], EMG_std["Standing_EC"]["Rectus_R"],
                       EMG_std["Standing_EC"]["Obliques_L"], EMG_std["Standing_EC"]["Obliques_R"],
                       EMG_std["Standing_EC"]["Ilicostalis_L"], EMG_std["Standing_EC"]["Ilicostalis_R"],
                       EMG_std["Standing_EC"]["Multifidus_L"], EMG_std["Standing_EC"]["Multifidus_R"]]

    median_standing_ec = [EMG_median["Standing_EC"]["Rectus_L"], EMG_median["Standing_EC"]["Rectus_R"],
                          EMG_median["Standing_EC"]["Obliques_L"], EMG_median["Standing_EC"]["Obliques_R"],
                          EMG_median["Standing_EC"]["Ilicostalis_L"], EMG_median["Standing_EC"]["Ilicostalis_R"],
                          EMG_median["Standing_EC"]["Multifidus_L"], EMG_median["Standing_EC"]["Multifidus_R"]]

    rects1 = plt.bar(index, mean_standing_ec, bar_width,
                     alpha=opacity,
                     color='r',
                     yerr=std_standing_ec,
                     error_kw=error_config)

    plt.plot(index + 0.18, median_standing_ec, 'ro', color='r', label = 'Median Value')

    plt.xticks(index + bar_width / 2, ('RL', 'RR', 'OL', 'OR', 'IL', 'IR', 'ML', 'MR'))
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 20])
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
    plot2.set_title("Standing Eyes Close", fontsize=12)

    plot3 = plt.subplot2grid((5, 2), (1, 0))
    mean_rf_eo = [EMG_mean["OneFootStanding_R_EO"]["Rectus_L"], EMG_mean["OneFootStanding_R_EO"]["Rectus_R"],
                        EMG_mean["OneFootStanding_R_EO"]["Obliques_L"], EMG_mean["OneFootStanding_R_EO"]["Obliques_R"],
                        EMG_mean["OneFootStanding_R_EO"]["Ilicostalis_L"], EMG_mean["OneFootStanding_R_EO"]["Ilicostalis_R"],
                        EMG_mean["OneFootStanding_R_EO"]["Multifidus_L"], EMG_mean["OneFootStanding_R_EO"]["Multifidus_R"]]

    std_rf_eo = [EMG_std["OneFootStanding_R_EO"]["Rectus_L"], EMG_std["OneFootStanding_R_EO"]["Rectus_R"],
                       EMG_std["OneFootStanding_R_EO"]["Obliques_L"], EMG_std["OneFootStanding_R_EO"]["Obliques_R"],
                       EMG_std["OneFootStanding_R_EO"]["Ilicostalis_L"], EMG_std["OneFootStanding_R_EO"]["Ilicostalis_R"],
                       EMG_std["OneFootStanding_R_EO"]["Multifidus_L"], EMG_std["OneFootStanding_R_EO"]["Multifidus_R"]]

    median_rf_eo = [EMG_median["OneFootStanding_R_EO"]["Rectus_L"], EMG_median["OneFootStanding_R_EO"]["Rectus_R"],
                    EMG_median["OneFootStanding_R_EO"]["Obliques_L"], EMG_median["OneFootStanding_R_EO"]["Obliques_R"],
                    EMG_median["OneFootStanding_R_EO"]["Ilicostalis_L"], EMG_median["OneFootStanding_R_EO"]["Ilicostalis_R"],
                    EMG_median["OneFootStanding_R_EO"]["Multifidus_L"], EMG_median["OneFootStanding_R_EO"]["Multifidus_R"]]

    rects1 = plt.bar(index, mean_rf_eo, bar_width,
                     alpha=opacity,
                     color='g',
                     yerr=std_rf_eo,
                     error_kw=error_config)

    plt.plot(index + 0.18, median_rf_eo, 'ro', color='g', label = 'Median Value')

    plt.xticks(index + bar_width / 2, ('RL', 'RR', 'OL', 'OR', 'IL', 'IR', 'ML', 'MR'))
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 40])
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
    plot3.set_title("Right Foot Standind Eyes Open", fontsize=12)

    plot4 = plt.subplot2grid((5, 2), (1, 1))
    mean_rf_ec = [EMG_mean["OneFootStanding_R_EC"]["Rectus_L"], EMG_mean["OneFootStanding_R_EC"]["Rectus_R"],
                        EMG_mean["OneFootStanding_R_EC"]["Obliques_L"], EMG_mean["OneFootStanding_R_EC"]["Obliques_R"],
                        EMG_mean["OneFootStanding_R_EC"]["Ilicostalis_L"], EMG_mean["OneFootStanding_R_EC"]["Ilicostalis_R"],
                        EMG_mean["OneFootStanding_R_EC"]["Multifidus_L"], EMG_mean["OneFootStanding_R_EC"]["Multifidus_R"]]

    std_rf_ec = [EMG_std["OneFootStanding_R_EC"]["Rectus_L"], EMG_std["OneFootStanding_R_EC"]["Rectus_R"],
                       EMG_std["OneFootStanding_R_EC"]["Obliques_L"], EMG_std["OneFootStanding_R_EC"]["Obliques_R"],
                       EMG_std["OneFootStanding_R_EC"]["Ilicostalis_L"], EMG_std["OneFootStanding_R_EC"]["Ilicostalis_R"],
                       EMG_std["OneFootStanding_R_EC"]["Multifidus_L"], EMG_std["OneFootStanding_R_EC"]["Multifidus_R"]]

    median_rf_ec = [EMG_median["OneFootStanding_R_EC"]["Rectus_L"], EMG_median["OneFootStanding_R_EC"]["Rectus_R"],
                    EMG_median["OneFootStanding_R_EC"]["Obliques_L"], EMG_median["OneFootStanding_R_EC"]["Obliques_R"],
                    EMG_median["OneFootStanding_R_EC"]["Ilicostalis_L"], EMG_median["OneFootStanding_R_EC"]["Ilicostalis_R"],
                    EMG_median["OneFootStanding_R_EC"]["Multifidus_L"], EMG_median["OneFootStanding_R_EC"]["Multifidus_R"]]

    rects1 = plt.bar(index, mean_rf_ec, bar_width,
                     alpha=opacity,
                     color='c',
                     yerr=std_rf_ec,
                     error_kw=error_config)

    plt.plot(index + 0.18, median_rf_ec, 'ro', color='c', label = 'Median Value')

    plt.xticks(index + bar_width / 2, ('RL', 'RR', 'OL', 'OR', 'IL', 'IR', 'ML', 'MR'))
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 40])
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
    plot4.set_title("Right Foot Standing Eyes Close", fontsize=12)

    plot5 = plt.subplot2grid((5, 2), (2, 0))
    mean_lf_eo = [EMG_mean["OneFootStanding_L_EO"]["Rectus_L"], EMG_mean["OneFootStanding_L_EO"]["Rectus_R"],
                  EMG_mean["OneFootStanding_L_EO"]["Obliques_L"], EMG_mean["OneFootStanding_L_EO"]["Obliques_R"],
                  EMG_mean["OneFootStanding_L_EO"]["Ilicostalis_L"], EMG_mean["OneFootStanding_L_EO"]["Ilicostalis_R"],
                  EMG_mean["OneFootStanding_L_EO"]["Multifidus_L"], EMG_mean["OneFootStanding_L_EO"]["Multifidus_R"]]

    std_lf_eo = [EMG_std["OneFootStanding_L_EO"]["Rectus_L"], EMG_std["OneFootStanding_L_EO"]["Rectus_R"],
                 EMG_std["OneFootStanding_L_EO"]["Obliques_L"], EMG_std["OneFootStanding_L_EO"]["Obliques_R"],
                 EMG_std["OneFootStanding_L_EO"]["Ilicostalis_L"], EMG_std["OneFootStanding_L_EO"]["Ilicostalis_R"],
                 EMG_std["OneFootStanding_L_EO"]["Multifidus_L"], EMG_std["OneFootStanding_L_EO"]["Multifidus_R"]]

    median_lf_eo = [EMG_median["OneFootStanding_L_EO"]["Rectus_L"], EMG_median["OneFootStanding_L_EO"]["Rectus_R"],
                 EMG_median["OneFootStanding_L_EO"]["Obliques_L"], EMG_median["OneFootStanding_L_EO"]["Obliques_R"],
                 EMG_median["OneFootStanding_L_EO"]["Ilicostalis_L"], EMG_median["OneFootStanding_L_EO"]["Ilicostalis_R"],
                 EMG_median["OneFootStanding_L_EO"]["Multifidus_L"], EMG_median["OneFootStanding_L_EO"]["Multifidus_R"]]

    rects1 = plt.bar(index, mean_lf_eo, bar_width,
                     alpha=opacity,
                     color='m',
                     yerr=std_lf_eo,
                     error_kw=error_config)

    plt.plot(index + 0.18, median_lf_eo, 'ro', color='m', label = 'Median Value')

    plt.xticks(index + bar_width / 2, ('RL', 'RR', 'OL', 'OR', 'IL', 'IR', 'ML', 'MR'))
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 40])
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
    plot5.set_title("Left Foot Eyes Open", fontsize=12)

    plot6 = plt.subplot2grid((5, 2), (2, 1))

    mean_lf_ec = [EMG_mean["OneFootStanding_L_EC"]["Rectus_L"],
                    EMG_mean["OneFootStanding_L_EC"]["Rectus_R"],
                    EMG_mean["OneFootStanding_L_EC"]["Obliques_L"],
                    EMG_mean["OneFootStanding_L_EC"]["Obliques_R"],
                    EMG_mean["OneFootStanding_L_EC"]["Ilicostalis_L"],
                    EMG_mean["OneFootStanding_L_EC"]["Ilicostalis_R"],
                    EMG_mean["OneFootStanding_L_EC"]["Multifidus_L"],
                    EMG_mean["OneFootStanding_L_EC"]["Multifidus_R"]]

    std_lf_ec = [EMG_std["OneFootStanding_L_EC"]["Rectus_L"], EMG_std["OneFootStanding_L_EC"]["Rectus_R"],
                 EMG_std["OneFootStanding_L_EC"]["Obliques_L"], EMG_std["OneFootStanding_L_EC"]["Obliques_R"],
                 EMG_std["OneFootStanding_L_EC"]["Ilicostalis_L"], EMG_std["OneFootStanding_L_EC"]["Ilicostalis_R"],
                 EMG_std["OneFootStanding_L_EC"]["Multifidus_L"], EMG_std["OneFootStanding_L_EC"]["Multifidus_R"]]

    median_lf_ec = [EMG_median["OneFootStanding_L_EC"]["Rectus_L"], EMG_median["OneFootStanding_L_EC"]["Rectus_R"],
                    EMG_median["OneFootStanding_L_EC"]["Obliques_L"], EMG_median["OneFootStanding_L_EC"]["Obliques_R"],
                    EMG_median["OneFootStanding_L_EC"]["Ilicostalis_L"], EMG_median["OneFootStanding_L_EC"]["Ilicostalis_R"],
                    EMG_median["OneFootStanding_L_EC"]["Multifidus_L"], EMG_median["OneFootStanding_L_EC"]["Multifidus_R"]]

    rects1 = plt.bar(index, mean_lf_ec, bar_width,
                     alpha=opacity,
                     color='y',
                     yerr=std_lf_ec,
                     error_kw=error_config)

    plt.plot(index + 0.18, median_lf_ec, 'ro', color='y', label = 'Median Value')

    plt.xticks(index + bar_width / 2, ('RL', 'RR', 'OL', 'OR', 'IL', 'IR', 'ML', 'MR'))
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 40])
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
    plot6.set_title("Left Foot Eyes Close", fontsize=12)

    plot7 = plt.subplot2grid((5, 2), (3, 0))
    mean_reach_r = [EMG_mean["Reach_R"]["Rectus_L"],
                  EMG_mean["Reach_R"]["Rectus_R"],
                  EMG_mean["Reach_R"]["Obliques_L"],
                  EMG_mean["Reach_R"]["Obliques_R"],
                  EMG_mean["Reach_R"]["Ilicostalis_L"],
                  EMG_mean["Reach_R"]["Ilicostalis_R"],
                  EMG_mean["Reach_R"]["Multifidus_L"],
                  EMG_mean["Reach_R"]["Multifidus_R"]]

    std_reach_r = [EMG_std["Reach_R"]["Rectus_L"], EMG_std["Reach_R"]["Rectus_R"],
                 EMG_std["Reach_R"]["Obliques_L"], EMG_std["Reach_R"]["Obliques_R"],
                 EMG_std["Reach_R"]["Ilicostalis_L"], EMG_std["Reach_R"]["Ilicostalis_R"],
                 EMG_std["Reach_R"]["Multifidus_L"], EMG_std["Reach_R"]["Multifidus_R"]]

    median_reach_r = [EMG_median["Reach_R"]["Rectus_L"], EMG_median["Reach_R"]["Rectus_R"],
                      EMG_median["Reach_R"]["Obliques_L"], EMG_median["Reach_R"]["Obliques_R"],
                      EMG_median["Reach_R"]["Ilicostalis_L"], EMG_median["Reach_R"]["Ilicostalis_R"],
                      EMG_median["Reach_R"]["Multifidus_L"], EMG_median["Reach_R"]["Multifidus_R"]]

    rects1 = plt.bar(index, mean_reach_r, bar_width,
                     alpha=opacity,
                     color='teal',
                     yerr=std_reach_r,
                     error_kw=error_config)

    plt.plot(index + 0.18, median_reach_r, 'ro', color='teal', label = 'Median Value')

    plt.xticks(index + bar_width / 2, ('RL', 'RR', 'OL', 'OR', 'IL', 'IR', 'ML', 'MR'))
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 60])
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
    plot7.set_title("Reach Right", fontsize=12)

    plot8 = plt.subplot2grid((5, 2), (3, 1))
    mean_reach_l = [EMG_mean["Reach_L"]["Rectus_L"],
                    EMG_mean["Reach_L"]["Rectus_R"],
                    EMG_mean["Reach_L"]["Obliques_L"],
                    EMG_mean["Reach_L"]["Obliques_R"],
                    EMG_mean["Reach_L"]["Ilicostalis_L"],
                    EMG_mean["Reach_L"]["Ilicostalis_R"],
                    EMG_mean["Reach_L"]["Multifidus_L"],
                    EMG_mean["Reach_L"]["Multifidus_R"]]

    std_reach_l = [EMG_std["Reach_L"]["Rectus_L"], EMG_std["Reach_L"]["Rectus_R"],
                   EMG_std["Reach_L"]["Obliques_L"], EMG_std["Reach_L"]["Obliques_R"],
                   EMG_std["Reach_L"]["Ilicostalis_L"], EMG_std["Reach_L"]["Ilicostalis_R"],
                   EMG_std["Reach_L"]["Multifidus_L"], EMG_std["Reach_L"]["Multifidus_R"]]

    median_reach_l = [EMG_std["Reach_L"]["Rectus_L"], EMG_std["Reach_L"]["Rectus_R"],
                   EMG_std["Reach_L"]["Obliques_L"], EMG_std["Reach_L"]["Obliques_R"],
                   EMG_std["Reach_L"]["Ilicostalis_L"], EMG_std["Reach_L"]["Ilicostalis_R"],
                   EMG_std["Reach_L"]["Multifidus_L"], EMG_std["Reach_L"]["Multifidus_R"]]

    rects1 = plt.bar(index, median_reach_l, bar_width,
                     alpha=opacity,
                     color='skyblue',
                     yerr=std_reach_l,
                     error_kw=error_config)

    plt.plot(index + 0.18, median_reach_l, 'ro', color='skyblue', label = 'Median Value')

    plt.xticks(index + bar_width / 2, ('RL', 'RR', 'OL', 'OR', 'IL', 'IR', 'ML', 'MR'))
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 25])
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
    plot8.set_title("Reach Left", fontsize=12)

    plot9 = plt.subplot2grid((5, 2), (4, 0))
    mean_reach_c = [EMG_mean["Reach_C"]["Rectus_L"],
                    EMG_mean["Reach_C"]["Rectus_R"],
                    EMG_mean["Reach_C"]["Obliques_L"],
                    EMG_mean["Reach_C"]["Obliques_R"],
                    EMG_mean["Reach_C"]["Ilicostalis_L"],
                    EMG_mean["Reach_C"]["Ilicostalis_R"],
                    EMG_mean["Reach_C"]["Multifidus_L"],
                    EMG_mean["Reach_C"]["Multifidus_R"]]

    std_reach_c = [EMG_std["Reach_C"]["Rectus_L"], EMG_std["Reach_C"]["Rectus_R"],
                   EMG_std["Reach_C"]["Obliques_L"], EMG_std["Reach_C"]["Obliques_R"],
                   EMG_std["Reach_C"]["Ilicostalis_L"], EMG_std["Reach_C"]["Ilicostalis_R"],
                   EMG_std["Reach_C"]["Multifidus_L"], EMG_std["Reach_C"]["Multifidus_R"]]

    median_reach_c = [EMG_median["Reach_C"]["Rectus_L"], EMG_median["Reach_C"]["Rectus_R"],
                      EMG_median["Reach_C"]["Obliques_L"], EMG_median["Reach_C"]["Obliques_R"],
                      EMG_median["Reach_C"]["Ilicostalis_L"], EMG_median["Reach_C"]["Ilicostalis_R"],
                      EMG_median["Reach_C"]["Multifidus_L"], EMG_median["Reach_C"]["Multifidus_R"]]

    rects1 = plt.bar(index, mean_reach_c, bar_width,
                     alpha=opacity,
                     color='darkmagenta',
                     yerr=std_reach_c,
                     error_kw=error_config)
    plt.plot(index + 0.18, median_reach_c, 'ro', color='darkmagenta', label = 'Median Value')

    plt.xticks(index + bar_width / 2, ('RL', 'RR', 'OL', 'OR', 'IL', 'IR', 'ML', 'MR'))
    plt.ylabel("Percentage from\n MVC maximum.(%)", fontsize=8)
    plt.ylim([0, 50])
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
    plot9.set_title("Reach Center", fontsize=12)

    plt.subplots_adjust(top=0.90, bottom=0.10, left=0.12, right=0.90, wspace=0.44, hspace=0.45)
    plt.show()
    #pp.savefig(fig)
    #pp.close()

def EMG_values_hitogram(EMG):
    l = 0
    #pp = PdfPages('EMG_Mean-Healthy_vs_SA.pdf')

    for i in EMG:

        fig = plt.figure(l)
        l = l + 1
        fig.suptitle(str(i) + " - Mean Value of normalized EMG", fontsize=21)

        plot1 = plt.subplot2grid((4, 2), (0, 0))
        plt.hist(EMG[i]["Rectus_L"], bins = 30)
        plt.ylabel("Frequency", fontsize=8)
        plt.xlabel("Percentage from MVC (%)", fontsize=8)
        plot1.set_title("Rectus Left", fontsize=12)

        plot2 = plt.subplot2grid((4, 2), (0, 1))
        plt.hist(EMG[i]["Rectus_R"], bins = 30)
        plt.ylabel("Frequency", fontsize=8)
        plt.xlabel("Percentage from MVC (%)", fontsize=8)
        plot2.set_title("Rectus Right", fontsize=12)

        plot3 = plt.subplot2grid((4, 2), (1, 0))
        plt.hist(EMG[i]["Obliques_L"], bins = 30)
        plt.ylabel("Frequency", fontsize=8)
        plt.xlabel("Percentage from MVC (%)", fontsize=8)
        plot3.set_title("Obliques Left", fontsize=12)

        plot4 = plt.subplot2grid((4, 2), (1, 1))
        plt.hist(EMG[i]["Obliques_R"], bins = 30)
        plt.ylabel("Frequency", fontsize=8)
        plt.xlabel("Percentage from MVC (%)", fontsize=8)
        plot4.set_title("Obliques Right", fontsize=12)

        plot5 = plt.subplot2grid((4, 2), (2, 0))
        plt.hist(EMG[i]["Ilicostalis_L"], bins = 30)
        plt.ylabel("Frequency", fontsize=8)
        plt.xlabel("Percentage from MVC (%)", fontsize=8)
        plot5.set_title("Iliocostalis Left", fontsize=12)

        plot6 = plt.subplot2grid((4, 2), (2, 1))
        plt.hist(EMG[i]["Ilicostalis_R"], bins = 30)
        plt.ylabel("Frequency", fontsize=8)
        plt.xlabel("Percentage from MVC (%)", fontsize=8)
        plot6.set_title("Iliocostalis Right", fontsize=12)

        plot7 = plt.subplot2grid((4, 2), (3, 0))
        plt.hist(EMG[i]["Multifidus_L"], bins = 30)
        plt.ylabel("Frequency", fontsize=8)
        plt.xlabel("Percentage from MVC (%)", fontsize=8)
        plot7.set_title("Multifidus Left", fontsize=12)

        plot8 = plt.subplot2grid((4, 2), (3, 1))
        plt.hist(EMG[i]["Multifidus_R"], bins = 30)
        plt.ylabel("Frequency", fontsize=8)
        plt.xlabel("Percentage from MVC (%)", fontsize=8)
        plot8.set_title("Multifidus Right", fontsize=12)

        plt.subplots_adjust(top=0.90, bottom=0.10, left=0.12, right=0.90, wspace=0.44, hspace=0.59)
        plt.show()
        #pp.savefig(fig)
    #pp.close()


def cop_parameters_same_parameter(COP_mean, COP_std, COP_median):
    n_groups = 9

    fig = plt.figure()
    fig.suptitle("Bar Error represention for COP's amplitude - X direction", fontsize=21)

    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    mean = [COP_mean["Standing_EO"]["Area"], COP_mean["Standing_EC"]["Area"],
                          COP_mean["OneFootStanding_R_EO"]["Area"],
                          COP_mean["OneFootStanding_R_EC"]["Area"],
                          COP_mean["OneFootStanding_L_EO"]["Area"],
                          COP_mean["OneFootStanding_L_EC"]["Area"],
                          COP_mean["Reach_R"]["Area"], COP_mean["Reach_L"]["Area"],
                          COP_mean["Reach_C"]["Area"]]

    std = [COP_std["Standing_EO"]["Area"], COP_std["Standing_EC"]["Area"],
           COP_std["OneFootStanding_R_EO"]["Area"],
           COP_std["OneFootStanding_R_EC"]["Area"],
           COP_std["OneFootStanding_L_EO"]["Area"],
           COP_std["OneFootStanding_L_EC"]["Area"],
           COP_std["Reach_R"]["Area"], COP_std["Reach_L"]["Area"],
           COP_std["Reach_C"]["Area"]]

    median = [COP_median["Standing_EO"]["Area"], COP_median["Standing_EC"]["Area"],
              COP_median["OneFootStanding_R_EO"]["Area"],
              COP_median["OneFootStanding_R_EC"]["Area"],
              COP_median["OneFootStanding_L_EO"]["Area"],
              COP_median["OneFootStanding_L_EC"]["Area"],
              COP_median["Reach_R"]["Area"], COP_median["Reach_L"]["Area"],
              COP_median["Reach_C"]["Area"]]

    rects1 = plt.bar(index, mean, bar_width,
                     alpha=opacity,
                     color='r',
                     yerr=std,
                     error_kw=error_config)

    plt.plot(index + bar_width / 2, median, 'ro', color='r', label='Median Value')
    plt.xticks(index + bar_width / 2, ('SEO', 'SEC', 'RFEO', 'RFEC', 'LFEO', 'LFEC', 'RR', 'RL', 'RC'), fontsize = 13)
    plt.ylabel("Amplitude x direction (mm)", fontsize=15)
    #plt.ylim([0, 40])
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=20)
    plt.show()

