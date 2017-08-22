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

def EMG_values_boxplot_healthy_vs_EA(EMG_healthy, EMG_EA):
    l = 0
    #pp = PdfPages('EMG_Peak_BoxPlot_Analysis_HealthyvsEA.pdf')

    for i in EMG_EA:

        fig = plt.figure(l)
        l = l + 1
        fig.suptitle(str(i) + " - Max Value of normalized EMG", fontsize=21)

        plot1 = plt.subplot2grid((4, 2), (0, 0))
        data_rectus_l = [[EMG_healthy[i]["Rectus_L"]], [EMG_EA[i]["Rectus_L"]]]
        plt.boxplot(data_rectus_l, positions = [1,2], widths = 0.6, showmeans= True)
        plt.xticks([1,2], ("Healthy", "SA"), fontsize=8)
        plt.ylim([0, 140])
        plot1.set_title("Rectus Left", fontsize=12)

        plot2 = plt.subplot2grid((4, 2), (0, 1))
        data_rectus_R = [[EMG_healthy[i]["Rectus_R"]], [EMG_EA[i]["Rectus_R"]]]
        plt.boxplot(data_rectus_R, positions = [1,2], widths=0.6, showmeans= True)
        plt.xticks([1, 2], ("Healthy", "SA"),fontsize=8)
        plt.ylim([0, 140])
        plot2.set_title("Rectus Right", fontsize=12)

        plot3 = plt.subplot2grid((4, 2), (1, 0))
        data_obliques_l = [[EMG_healthy[i]["Obliques_L"]], [EMG_EA[i]["Obliques_L"]]]
        plt.boxplot(data_obliques_l, positions = [1,2], widths=0.6, showmeans=True)
        plt.xticks([1, 2], ("Healthy", "SA"),fontsize=8)
        plt.ylim([0, 140])
        plot3.set_title("Obliques Left", fontsize=12)

        plot4 = plt.subplot2grid((4, 2), (1, 1))
        data_obliques_r = [[EMG_healthy[i]["Obliques_R"]], [EMG_EA[i]["Obliques_R"]]]
        plt.boxplot(data_obliques_r, positions = [1,2], widths=0.6, showmeans=True)
        plt.xticks([1, 2], ("Healthy", "SA"),fontsize=8)
        plt.ylim([0, 140])
        plot4.set_title("Obliques Right", fontsize=12)

        plot5 = plt.subplot2grid((4, 2), (2, 0))
        data_ilicostalis_l = [[EMG_healthy[i]["Ilicostalis_L"]], [EMG_EA[i]["Ilicostalis_L"]]]
        plt.boxplot(data_ilicostalis_l, positions = [1,2], widths=0.6, showmeans=True)
        plt.xticks([1, 2], ("Healthy", "SA"), fontsize=8)
        plt.ylim([0, 140])
        plot5.set_title("Iliocostalis Left", fontsize=12)

        plot6 = plt.subplot2grid((4, 2), (2, 1))
        data_ilicostalis_r = [[EMG_healthy[i]["Ilicostalis_R"]], [EMG_EA[i]["Ilicostalis_R"]]]
        plt.boxplot(data_ilicostalis_r, positions = [1,2], widths=0.6, showmeans=True)
        plt.xticks([1, 2], ("Healthy", "SA"), fontsize=8)
        plt.ylim([0, 140])
        plot6.set_title("Iliocostalis Right", fontsize=12)

        plot7 = plt.subplot2grid((4, 2), (3, 0))
        data_multi_l = [[EMG_healthy[i]["Multifidus_L"]], [EMG_EA[i]["Multifidus_L"]]]
        plt.boxplot(data_multi_l, positions = [1,2], widths=0.6, showmeans=True)
        plt.xticks([1, 2], ("Healthy", "SA"),fontsize=8)
        plt.ylim([0, 140])
        plot7.set_title("Multifidus Left", fontsize=12)

        plot8 = plt.subplot2grid((4, 2), (3, 1))
        data_multi_r = [[EMG_healthy[i]["Multifidus_R"]], [EMG_EA[i]["Multifidus_R"]]]
        plt.boxplot(data_multi_r, positions = [1,2], widths=0.6, showmeans=True)
        plt.xticks([1, 2], ("Healthy", "SA"),fontsize=8)
        plt.ylim([0, 140])
        plot8.set_title("Multifidus Right", fontsize=12)

        plt.subplots_adjust(top=0.90, bottom=0.10, left=0.12, right=0.90, wspace=0.44, hspace=0.45)
        plt.show()
        #pp.savefig(fig)
    #pp.close()

def EMG_freq_front_boxplot_HealthyvsSA(freqEMG_healthy, freqEMG_SA):
    l = 0
    #pp = PdfPages('EMG_Freqs_BoxPlot_Analysis.pdf')

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
                        box = plt.boxplot(data, positions=[1, 2], widths=0.6, showmeans=True)
                        plt.xticks([1, 2],
                                   ("Healthy", "SA"),
                                   fontsize=7)
                        plot.set_title(str(muscle), fontsize=12, style = 'italic')
                        row_l = row_l + 1

                    if muscle == "Rectus_R" or muscle == "Obliques_R":
                        plot = plt.subplot2grid((4, 4), (row_r, col_r))
                        data = [[freqEMG_healthy[i][muscle][freq]], [freqEMG_SA[i][muscle][freq]]]
                        box = plt.boxplot(data, positions=[1, 2], widths=0.6, showmeans=True)
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
                        box = plt.boxplot(data, positions=[1, 2], widths=0.6, showmeans=True)
                        plt.xticks([1, 2],
                                   ("Healthy", "SA"),
                                   fontsize=7)
                        plot.set_title(str(muscle), fontsize=12, style='italic')
                        row_l = row_l + 1

                    if muscle == "Rectus_R" or muscle == "Obliques_R":
                        plot = plt.subplot2grid((4, 4), (row_r, col_r))
                        data = [[freqEMG_healthy[i][muscle][freq]], [freqEMG_SA[i][muscle][freq]]]
                        box = plt.boxplot(data, positions=[1, 2], widths=0.6, showmeans=True)
                        plt.xticks([1, 2],
                                   ("Healthy", "SA"),
                                   fontsize=7)
                        plot.set_title(str(muscle), fontsize=12, style='italic')
                        row_r = row_r + 1

                col_80_median = col_80_median + 2
                color_index = color_index + 1

        plt.subplots_adjust(top=0.89, bottom=0.05, left=0.12, right=0.90, wspace=0.56, hspace=0.67)
        plt.show()
        #pp.savefig(fig)
    #pp.close()

def EMG_freq_back_boxplot_HealthyvsSA(freqEMG_healthy, freqEMG_SA):
    l = 0
    #pp = PdfPages('EMG_Freqs_Back_BoxPlot_Analysis_Healthy_EA.pdf')

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
                        box = plt.boxplot(data, positions=[1, 2], widths=0.6, showmeans=True)
                        plt.xticks([1, 2],
                                   ("Healthy", "SA"),
                                   fontsize=7)
                        plot.set_title(str(muscle), fontsize=12, style = 'italic')
                        row_l = row_l + 1

                    if muscle == "Ilicostalis_R" or muscle == "Multi_R":
                        plot = plt.subplot2grid((4, 4), (row_r, col_r))
                        data = [[freqEMG_healthy[i][muscle][freq]], [freqEMG_SA[i][muscle][freq]]]
                        box = plt.boxplot(data, positions=[1, 2], widths=0.6, showmeans=True)
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
                        box = plt.boxplot(data, positions=[1, 2], widths=0.6, showmeans=True)
                        plt.xticks([1, 2],
                                   ("Healthy", "SA"),
                                   fontsize=7)
                        plot.set_title(str(muscle), fontsize=12, style='italic')
                        row_l = row_l + 1

                    if muscle == "Ilicostalis_R" or muscle == "Multi_R":
                        plot = plt.subplot2grid((4, 4), (row_r, col_r))
                        data = [[freqEMG_healthy[i][muscle][freq]], [freqEMG_SA[i][muscle][freq]]]
                        box = plt.boxplot(data, positions=[1, 2], widths=0.6, showmeans=True)
                        plt.xticks([1, 2],
                                   ("Healthy", "SA"),
                                   fontsize=7)
                        plot.set_title(str(muscle), fontsize=12, style='italic')
                        row_r = row_r + 1

                col_80_median = col_80_median + 2
                color_index = color_index + 1

        plt.subplots_adjust(top=0.89, bottom=0.05, left=0.12, right=0.90, wspace=0.56, hspace=0.67)
        plt.show()
        #pp.savefig(fig)
    #pp.close()

def COP_freq_boxplot_HealthyvsSA(healthy_freqsCOP, SA_freqsCOP):
    l = 0
    #pp = PdfPages('COP_Freqs_BoxPlot_Analysis_Healthy_EA.pdf')

    for i in healthy_freqsCOP:
        fig = plt.figure(l)
        l = l + 1
        fig.suptitle(str(i) + " - COP Frequencies", fontsize=21)

        plot1 = plt.subplot2grid((2, 4), (0, 0))
        data_peak_x = [[healthy_freqsCOP[i]["Peak_X"]], [SA_freqsCOP[i]["Peak_X"]]]
        plt.boxplot(data_peak_x, positions=[1, 2], widths=0.6, showmeans=True)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot1.set_title("Peak Frequency - COP X", fontsize=12)

        plot2 = plt.subplot2grid((2, 4), (0, 1))
        data_peak_y = [[healthy_freqsCOP[i]["Peak_Y"]], [SA_freqsCOP[i]["Peak_Y"]]]
        plt.boxplot(data_peak_y, positions=[1, 2], widths=0.6, showmeans=True)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot2.set_title("Peak Frequency - COP Y", fontsize=12)

        plot3 = plt.subplot2grid((2, 4), (0, 2))
        data_mean_x = [[healthy_freqsCOP[i]["Mean_X"]], [SA_freqsCOP[i]["Mean_X"]]]
        plt.boxplot(data_mean_x, positions=[1, 2], widths=0.6, showmeans=True)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot3.set_title("Mean Frequency - COP X", fontsize=12)

        plot4 = plt.subplot2grid((2, 4), (0, 3))
        data_mean_y = [[healthy_freqsCOP[i]["Mean_Y"]], [SA_freqsCOP[i]["Mean_Y"]]]
        plt.boxplot(data_mean_y, positions=[1, 2], widths=0.6, showmeans=True)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot4.set_title("Mean Frequency - COP Y", fontsize=12)

        plot5 = plt.subplot2grid((2, 4), (1, 0))
        data_median_x = [[healthy_freqsCOP[i]["Median_X"]], [SA_freqsCOP[i]["Median_X"]]]
        plt.boxplot(data_median_x,positions=[1, 2], widths=0.6, showmeans=True)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot5.set_title("Median Frequency - COP X", fontsize=12)

        plot6 = plt.subplot2grid((2, 4), (1, 1))
        data_median_y = [[healthy_freqsCOP[i]["Median_Y"]], [SA_freqsCOP[i]["Median_Y"]]]
        plt.boxplot(data_median_x, positions=[1, 2], widths=0.6, showmeans=True)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot6.set_title("Median Frequency - COP Y", fontsize=12)

        plot7 = plt.subplot2grid((2, 4), (1, 2))
        data_80_X = [[healthy_freqsCOP[i]["80_X"]], [SA_freqsCOP[i]["80_X"]]]
        plt.boxplot(data_80_X, positions=[1, 2], widths=0.6, showmeans=True)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot7.set_title("80% Frequency - COP X", fontsize=12)

        plot8 = plt.subplot2grid((2, 4), (1, 3))
        data_80_Y = [[healthy_freqsCOP[i]["80_Y"]], [SA_freqsCOP[i]["80_Y"]]]
        plt.boxplot(data_80_Y, positions=[1, 2], widths=0.6, showmeans=True)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot8.set_title("80% Frequency - COP Y", fontsize=12)

        plt.subplots_adjust(top=0.90, bottom=0.10, left=0.12, right=0.90, wspace=0.31, hspace=0.27)
        plt.show()
        #pp.savefig(fig)
    #pp.close()

def COP_parameters_boxplot_HealthyvsSA(healthy_cop, SA_cop):
    l = 0
    #pp = PdfPages('COP_Parameters_BoxPlot_Analysis_Healthy_EA.pdf')

    for i in healthy_cop:
        fig = plt.figure(l)
        l = l + 1
        fig.suptitle(str(i) + " - COP Parameters", fontsize=21)

        plot1 = plt.subplot2grid((3, 3), (0, 0))
        data_velocity_x = [[healthy_cop[i]["Velocity_X"]], [SA_cop[i]["Velocity_X"]]]
        plt.boxplot(data_velocity_x, positions=[1, 2], widths=0.6, showmeans=True)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot1.set_title("Velocity COP X", fontsize=12)

        plot2 = plt.subplot2grid((3, 3), (0, 1))
        data_velocity_y = [[healthy_cop[i]["Velocity_Y"]], [SA_cop[i]["Velocity_Y"]]]
        plt.boxplot(data_velocity_y, positions=[1, 2], widths=0.6, showmeans=True)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot2.set_title("Velocity COP Y", fontsize=12)

        plot3 = plt.subplot2grid((3, 3), (1, 0))
        data_std_x = [[healthy_cop[i]["STD_X"]], [SA_cop[i]["STD_X"]]]
        plt.boxplot(data_std_x, positions=[1, 2], widths=0.6, showmeans=True)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot3.set_title("STD COP X", fontsize=12)

        plot4 = plt.subplot2grid((3, 3), (1, 1))
        data_std_y = [[healthy_cop[i]["STD_Y"]], [SA_cop[i]["STD_Y"]]]
        plt.boxplot(data_std_y, positions=[1, 2], widths=0.6, showmeans=True)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot4.set_title("STD COP Y", fontsize=12)

        plot5 = plt.subplot2grid((3, 3), (2, 0))
        data_amp_x = [[healthy_cop[i]["Amp_X"]], [SA_cop[i]["Amp_X"]]]
        plt.boxplot(data_amp_x, positions=[1, 2], widths=0.6, showmeans=True)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot5.set_title("Amplitude COP X", fontsize=12)

        plot6 = plt.subplot2grid((3, 3), (2, 1))
        data_amp_y = [[healthy_cop[i]["Amp_Y"]], [SA_cop[i]["Amp_Y"]]]
        plt.boxplot(data_amp_y, positions=[1, 2], widths=0.6, showmeans=True)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot6.set_title("Amplitude COP Y", fontsize=12)

        plot7 = plt.subplot2grid((3, 3), (1, 2))
        data_area = [[healthy_cop[i]["Area"]], [SA_cop[i]["Area"]]]
        plt.boxplot(data_area, positions=[1, 2], widths=0.6, showmeans=True)
        plt.xticks([1, 2],
                   ("Healthy", "SA"),
                   fontsize=7)
        plot7.set_title("Area", fontsize=12)

        plt.subplots_adjust(top=0.90, bottom=0.10, left=0.12, right=0.90, wspace=0.31, hspace=0.27)
        plt.show()
        #pp.savefig(fig)
    #pp.close()
