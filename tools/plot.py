import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.image as mpimg
from matplotlib.backends.backend_pdf import PdfPages
from tools import *

def graph_platform(max_values, platform_COP, description, platform = False):

    ind = np.arange(2)
    margin = 0.01
    width = (1. - 2. * margin) / len(ind)
    #width = 0.35
    error_config = {'ecolor': '0.5', 'capthick': 0.5}
    pp = PdfPages('Platform_'+str(description)+'.pdf')

    l = 0
    for i in max_values:

        if max_values[i] != []:
            fig = plt.figure(l)
            l = l+1
            fig.suptitle(str(i) + "\n"+ str(description), fontsize=25)

        fig = plt.figure(l)
        l = l+1
        fig.suptitle(str(i) + "\n"+ str(description), fontsize=25)

        plot1 = plt.subplot2grid((3, 3), (0, 0))
        plt.bar(ind, [max_values[i][0],max_values[i][2]], width, error_kw=error_config, align= 'center')
        plt.xticks(ind, ("Rectus_A_L", "Obliques_L"), fontsize=10)
        plt.ylabel("Percentage from MVC maximum.(%)",fontsize=9)
        plt.ylim([0, 100])
        plot1.set_title("Maximum for for each muscle on the left side\n Front", fontsize=12)

        plot2 = plt.subplot2grid((3, 3), (0, 1))
        plt.bar(ind, [max_values[i][1], max_values[i][3]], width, error_kw=error_config, align= 'center')
        plt.xticks(ind, ("Rectus_A_R", "Obliques_R"), fontsize=10)
        plt.ylabel("Percentage from MVC maximum.(%)",fontsize=9)
        plt.ylim([0, 100])
        plot2.set_title("Maximum for for each muscle on the right side\n Front", fontsize=12)

        if platform == True:
            plot3 = plt.subplot2grid((3, 3), (1, 0), colspan=5, rowspan=5)
            img = mpimg.imread("tools/forcePlatform.png")
            plt.imshow(img, zorder=0, extent=[-225 - 12, +225 + 12, -225 - 12, +225 + 12])
            plt.plot(platform_COP[i]["COP_X"], platform_COP[i]["COP_Y"], color='yellow')
            plt.xlim([-225 - 12, 225 + 12])
            plt.ylim([-225 - 12, 225 + 12])
            plt.xlabel("Trajectory of COP on X axes", fontsize=12)
            plt.ylabel("Trajectory of COP on Y axes", fontsize=12)
            plot3.set_title("COP trajectory", fontsize=14)

        plot4 = plt.subplot2grid((3, 3), (2, 0))
        plt.bar(ind, [max_values[i][4], max_values[i][6]], width, error_kw=error_config, align= 'center')
        plt.xticks(ind, ("Ilicostalis_L", "Multifundus_L"), fontsize=10)
        plt.ylabel("Percentage from MVC maximum.(%)", fontsize=9)
        plt.ylim([0, 100])
        plot4.set_title("Maximum for for each muscle on the left side\n Back", fontsize=12)

        plot5 = plt.subplot2grid((3, 3), (2, 1))
        plt.bar(ind, [max_values[i][5], max_values[i][7]], width, error_kw=error_config, align= 'center')
        plt.xticks(ind, ("Ilicostalis_R", "Multifundus_R"), fontsize=10)
        plt.ylabel("Percentage from MVC maximum.(%)", fontsize=9)
        plt.ylim([0, 100])
        plot5.set_title("Maximum for for each muscle on the right side\n Back", fontsize=12)

        if platform == True:
            plt.subplots_adjust(top = 0.76, bottom = 0.08, left = 0.05,right=0.93, wspace=0.35, hspace=0.00)
        else:
            plt.subplots_adjust(top=0.75, bottom=0.11, left=0.30, right=0.98, wspace=0.47, hspace=0.01)


            plot1 = plt.subplot2grid((3, 3), (0, 0))
            plt.bar(ind, [max_values[i][0],max_values[i][2]], width, error_kw=error_config, align= 'center')
            plt.xticks(ind, ("Rectus_A_L", "Obliques_L"), fontsize=10)
            plt.ylabel("Percentage from MVC maximum.(%)",fontsize=9)
            plt.ylim([0, 100])
            plot1.set_title("Maximum for for each muscle on the left side\n Front", fontsize=12)

            plot2 = plt.subplot2grid((3, 3), (0, 1))
            plt.bar(ind, [max_values[i][1], max_values[i][3]], width, error_kw=error_config, align= 'center')
            plt.xticks(ind, ("Rectus_A_R", "Obliques_R"), fontsize=10)
            plt.ylabel("Percentage from MVC maximum.(%)",fontsize=9)
            plt.ylim([0, 100])
            plot2.set_title("Maximum for for each muscle on the right side\n Front", fontsize=12)

            if platform == True:
                plot3 = plt.subplot2grid((3, 3), (1, 2), colspan=5, rowspan=5)
                img = mpimg.imread("tools/forcePlatform.png")
                plt.imshow(img, zorder=0, extent=[-225 - 12, +225 + 12, -225 - 12, +225 + 12])
                plt.plot(platform_COP[i]["COP_X"], platform_COP[i]["COP_Y"], color='yellow')
                plt.xlim([-225 - 12, 225 + 12])
                plt.ylim([-225 - 12, 225 + 12])
                plt.xlabel("Trajectory of COP on X axes", fontsize=12)
                plt.ylabel("Trajectory of COP on Y axes", fontsize=12)
                plot3.set_title("COP trajectory", fontsize=14)

            plot4 = plt.subplot2grid((3, 3), (2, 0))
            plt.bar(ind, [max_values[i][4], max_values[i][6]], width, error_kw=error_config, align= 'center')
            plt.xticks(ind, ("Ilicostalis_L", "Multifundus_L"), fontsize=10)
            plt.ylabel("Percentage from MVC maximum.(%)", fontsize=9)
            plt.ylim([0, 100])
            plot4.set_title("Maximum for for each muscle on the left side\n Back", fontsize=12)

            plot5 = plt.subplot2grid((3, 3), (2, 1))
            plt.bar(ind, [max_values[i][5], max_values[i][7]], width, error_kw=error_config, align= 'center')
            plt.xticks(ind, ("Ilicostalis_R", "Multifundus_R"), fontsize=10)
            plt.ylabel("Percentage from MVC maximum.(%)", fontsize=9)
            plt.ylim([0, 100])
            plot5.set_title("Maximum for for each muscle on the right side\n Back", fontsize=12)

            if platform == True:
                plt.subplots_adjust(top = 0.76, bottom = 0.08, left = 0.05,right=0.93, wspace=0.35, hspace=0.00)
            else:
                plt.subplots_adjust(top=0.75, bottom=0.11, left=0.30, right=0.98, wspace=0.47, hspace=0.01)

            plt.show()
            pp.savefig(fig)
    pp.close()


def graph_normalizedRMS (test, description):
    pp = PdfPages('Normalized_RMS_' + str(description) + '.pdf')
    for j in range(0, 8):
        for i in test:
            fig = plt.figure(j)
            plt.plot(test[i][:, j], label=str(i))
            plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize = 10)

            plt.xlabel("Time in miliseconds", fontsize=7)
            plt.suptitle("Normalized RMS\n" + str(description), fontsize=24)
            if j == 0:
                plt.ylabel("Normalized RMS\n Rectus Abdominis_L")
            if j == 1:
                plt.ylabel("Normalized RMS\n Rectus Abdominis_R")
            if j == 2:
                plt.ylabel("Normalized RMS\n Obliques_L")
            if j == 3:
                plt.ylabel("Normalized RMS\n Obliques_R")
            if j == 4:
                plt.ylabel("Normalized RMS\n Ilicostalis_L")
            if j == 5:
                plt.ylabel("Normalized RMS\n Ilicostalis_R")
            if j == 6:
                plt.ylabel("Normalized RMS\n Multifundus_L")
            if j == 7:
                plt.ylabel("Normalized RMS\n Multifundus_R")
        fig.tight_layout(pad=5.0, w_pad=1.0, h_pad=1.0)
        plt.show()
        pp.savefig(fig)
    pp.close()

def graph_RMS(test, description):
    pp = PdfPages('RMS_' + str(description) + '.pdf')
    for j in range(0, 8):
        for i in test:
            fig = plt.figure(j)
            plt.plot(test[i][:,j], label= str(i))
            plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize = 10)
            plt.xlabel("Time in miliseconds", fontsize=7)
            if j == 0:
                plt.ylabel("RMS of EMG\n Rectus Abdominis_L")
            if j == 1:
                plt.ylabel("RMS of EMG\n Rectus Abdominis_R")
            if j == 2:
                plt.ylabel("RMS of EMG\n Obliques_L")
            if j == 3:
                plt.ylabel("RMS of EMG\n Obliques_R")
            if j == 4:
                plt.ylabel("RMS of EMG\n Ilicostalis_L")
            if j == 5:
                plt.ylabel("RMS of EMG\n Ilicostalis_R")
            if j == 6:
                plt.ylabel("RMS of EMG\n Multifundus_L")
            if j == 7:
                plt.ylabel("RMS of EMG\n Multifundus_R")
            plt.suptitle("RMS\n" + str(description), fontsize=24)

        fig.tight_layout(pad=5.0, w_pad=1.0, h_pad=1.0)
        plt.show()
        pp.savefig(fig)
    pp.close()

def graph(max_values, platform_COP,description,mean_trajectory, coherence, velocity, platform = False):
    ind = np.arange(4)
    margin = 0.01
    #width = (1. - 1. * margin) / len(ind)
    width = 0.5
    error_config = {'ecolor': '0.5', 'capthick': 0.5}
    pp = PdfPages('Platform_'+str(description)+'.pdf')

    l = 0
    for i in max_values:
        if max_values[i] != []:
            fig = plt.figure(l)
            l = l+1
            fig.suptitle(str(i) + "\n"+ str(description), fontsize=25)

            plot1 = plt.subplot2grid((3, 3), (0, 0))
            plt.bar(ind, [max_values[i][0],max_values[i][2], max_values[i][4], max_values[i][6]], width, error_kw=error_config, align= 'center')
            plt.xticks(ind, ("Rectus_A_L", "Obliques_L", "Ilicostalis_L", "Multifundus_L"), fontsize=10)
            plt.ylabel("Percentage from MVC \n maximum.(%)",fontsize=9)
            plt.ylim([0, 100])
            plot1.set_title("Maximum for for each muscle \n on the left side", fontsize=12)

            plot2 = plt.subplot2grid((3, 3), (0, 1))
            plt.bar(ind, [max_values[i][1], max_values[i][3], max_values[i][5], max_values[i][7]], width, error_kw=error_config, align= 'center')
            plt.xticks(ind, ("Rectus_A_R", "Obliques_R", "Ilicostalis_R", "Multifundus_R"), fontsize=10)
            plt.ylabel("Percentage from MVC \n maximum.(%)",fontsize=9)
            plt.ylim([0, 100])
            plot2.set_title("Maximum for for each muscle \n on the right side", fontsize=12)


            if platform == True:
                with sns.axes_style("white"):
                    area_traj = convex_hull(platform_COP[i]["COP_X"], platform_COP[i]["COP_Y"])
                    area_value = area_calc(area_traj)
                    plot3 = plt.subplot2grid((3, 3), (0, 2), colspan= 2, rowspan=2)
                    img = mpimg.imread("tools/forcePlatform.png")
                    plt.imshow(img, zorder=0, extent=[-225 - 12, +225 + 12, -225 - 12, +225 + 12])
                    plt.plot(platform_COP[i]["COP_X"], platform_COP[i]["COP_Y"], color='yellow')
                    plt.plot(area_traj[:,0], area_traj[:,1], label = str(area_value) + "\n"+"mm2")
                    plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
                    plt.xlim([-225 - 12, 225 + 12])
                    plt.ylim([-225 - 12, 225 + 12])
                    plt.xlabel("Trajectory of COP on X axes", fontsize=12)
                    plt.ylabel("Trajectory of COP on Y axes", fontsize=12)
                    plt.scatter(mean_trajectory[i]["X"], mean_trajectory[i]["Y"], s=100, color='r')
                    plot3.set_title("COP trajectory", fontsize=14)

            plot4 = plt.subplot2grid((3, 3), (2, 0))
            plt.axis('off')
            col_labels = ['Left Side', 'Right Side']
            row_labels = ['Rectus_A', 'Obliques', 'Ilicostalis', 'Multifidus']
            table_vals = [[max_values[i][0], max_values[i][1]],
                          [max_values[i][2], max_values[i][3]],
                          [max_values[i][4], max_values[i][5]],
                          [max_values[i][6], max_values[i][7]]]
            the_table = plt.table(cellText=table_vals,
                                    colWidths=[0.4] * 2,
                                    rowLabels=row_labels,
                                    colLabels=col_labels,
                                    loc='center')
            the_table.auto_set_font_size(False)
            the_table.set_fontsize(11)
            the_table.scale(1.1, 1.1)
            plot4.set_title("Table 1 - Values of maximum of each muscle in percentage (%)", fontsize=11)
            plt.text(30, 25, 'Table Title', size=30)

            plot5 = plt.subplot2grid((3, 3), (2, 1))
            plt.axis('off')
            col_labels = ['COP X', 'COP Y']
            row_labels = ['Rectus_A_L', 'Obliques_L', 'Ilicostalis_L', 'Multifidus_L',
                          'Rectus_A_R', 'Obliques_R', 'Ilicostalis_R', 'Multifidus_R']
            table_values = [[np.max(coherence[i]["coherency_x"][0:40, 0]),  np.max(coherence[i]["coherency_y"][0:40, 0])],
                            [np.max(coherence[i]["coherency_x"][0:40, 2]), np.max(coherence[i]["coherency_y"][0:40, 2])],
                            [np.max(coherence[i]["coherency_x"][0:40, 4]), np.max(coherence[i]["coherency_y"][0:40, 4])],
                            [np.max(coherence[i]["coherency_x"][0:40, 6]), np.max(coherence[i]["coherency_y"][0:40, 6])],
                            [np.max(coherence[i]["coherency_x"][0:40, 1]), np.max(coherence[i]["coherency_y"][0:40, 1])],
                            [np.max(coherence[i]["coherency_x"][0:40, 3]), np.max(coherence[i]["coherency_y"][0:40, 3])],
                            [np.max(coherence[i]["coherency_x"][0:40, 5]), np.max(coherence[i]["coherency_y"][0:40, 5])],
                            [np.max(coherence[i]["coherency_x"][0:40, 7]), np.max(coherence[i]["coherency_y"][0:40, 7])]]

            freqs_table = plt.table(cellText=table_values,
                                  colWidths=[0.4] * 2,
                                  rowLabels=row_labels,
                                  colLabels=col_labels,
                                  loc='upper center')
            freqs_table.auto_set_font_size(False)
            freqs_table.set_fontsize(11)
            freqs_table.scale(1.1, 1.1)
            plot5.set_title("Table 2 - Coherence of frequency signals between frequencys of 0 Hz to 40 Hz", fontsize=11)
            plt.text(30, 25, 'Table Title', size=30)

            plot6 = plt.subplot2grid((3, 3), (2, 2))
            plt.axis('off')
            col_labels = ['COP X', 'COP Y']
            row_labels = ['Velocity', 'Mean Point']
            COP_values = [[velocity[i]["mean_COPX"], velocity[i]["mean_COPY"]], [mean_trajectory[i]["X"], mean_trajectory[i]["Y"]]]
            COP_table = plt.table(cellText=COP_values,
                                    colWidths=[0.4] * 2,
                                    rowLabels=row_labels,
                                    colLabels=col_labels,
                                    loc='center')
            COP_table.auto_set_font_size(False)
            COP_table.set_fontsize(11)
            COP_table.scale(1.1, 1.1)
            plot6.set_title("Table 3 - Relevante COP values", fontsize=11)
            plt.text(30, 25, 'Table Title', size=30)

            plot7 = plt.subplot2grid((3, 3), (1, 0))
            ind1 = [1, 2, 3, 4]
            plt.plot(ind1, [np.max(coherence[i]["coherency_x"][0:40, 0]),
                            np.max(coherence[i]["coherency_x"][0:40, 2]),
                            np.max(coherence[i]["coherency_x"][0:40, 4]),
                            np.max(coherence[i]["coherency_x"][0:40, 6])],'ro', color = 'blue', label = "COP X")
            plt.plot(ind1, [np.max(coherence[i]["coherency_y"][0:40, 0]),
                            np.max(coherence[i]["coherency_y"][0:40, 2]),
                            np.max(coherence[i]["coherency_y"][0:40, 4]),
                            np.max(coherence[i]["coherency_y"][0:40, 6])], 'ro', label = "COP Y")
            plt.legend(bbox_to_anchor=(1.0, 1.0), loc=2, borderaxespad=0., fontsize=10)
            plt.xticks(ind1, ("Rectus_A_L", "Obliques_L", "Ilicostalis_L", "Multifidus_L"), fontsize=10)
            plt.xlim([0, 5])
            plt.ylim([0, 0.8])
            plt.ylabel("Coherence between COP \n and each muscle.", fontsize=9)
            plot7.set_title("Coherence", fontsize=12)

            plot8 = plt.subplot2grid((3, 3), (1, 1))
            plt.plot(ind1, [np.max(coherence[i]["coherency_x"][0:40, 1]),
                            np.max(coherence[i]["coherency_x"][0:40, 3]),
                            np.max(coherence[i]["coherency_x"][0:40, 5]),
                            np.max(coherence[i]["coherency_x"][0:40, 7])], 'ro', color='blue')
            plt.plot(ind1, [np.max(coherence[i]["coherency_y"][0:40, 1]),
                            np.max(coherence[i]["coherency_y"][0:40, 3]),
                            np.max(coherence[i]["coherency_y"][0:40, 5]),
                            np.max(coherence[i]["coherency_y"][0:40, 7])], 'ro')
            plt.xticks(ind1, ("Rectus_A_R", "Obliques_R", "Ilicostalis_R", "Multifidus_R"), fontsize=10)
            plt.xlim([0, 5])
            plt.ylim([0, 0.8])
            plt.ylabel("Coherence between COP \n and each muscle.", fontsize=9)
            plot8.set_title("Coherence", fontsize=12)


            if platform == True:
                plt.subplots_adjust(top = 0.76, bottom = 0.08, left = 0.05,right=0.93, wspace=0.43, hspace=0.62)
            else:
                plt.subplots_adjust(top=0.75, bottom=0.11, left=0.30, right=0.98, wspace=0.47, hspace=0.01)

            plt.show()


def COP_Muscle (EMG_array, COP_array):
    l = 0
    for i in EMG_array:
        fig = plt.figure(l)
        l = l + 1
        fig.suptitle(str(i), fontsize=25)
        plot1 = plt.subplot2grid((4, 2), (0, 0))
        plt.plot((EMG_array[i][:,0])*5.0+5.0, label = "Rectus_A_L")
        plt.plot(COP_array[i]["COP_X"]/15.0, label = "COP X")
        plt.plot((EMG_array[i][:,1])*5.0-5.0, label = "Rectus_A_R")
        plt.legend(bbox_to_anchor=(0, 0), loc=3, borderaxespad=0., fontsize=10)

        plot2 = plt.subplot2grid((4, 2), (0, 1))
        plt.plot((EMG_array[i][:, 0]) * 5.0 + 5.0, label = "Rectus_A_L")
        plt.plot(COP_array[i]["COP_Y"] / 15.0, label = "COP_Y")
        plt.plot((EMG_array[i][:, 1]) * 5.0 - 5.0, label = "Rectus_A_L")
        plt.legend(bbox_to_anchor=(0, 0), loc=3, borderaxespad=0., fontsize=10)

        plot3 = plt.subplot2grid((4, 2), (1, 0))
        plt.plot((EMG_array[i][:, 2]) * 5.0 + 5.0, label = "Obliques_L")
        plt.plot(COP_array[i]["COP_X"] / 15.0, label = "COP X")
        plt.plot((EMG_array[i][:, 3]) * 5.0 - 5.0, label = "Obliques_R")
        plt.legend(bbox_to_anchor=(0, 0), loc=3, borderaxespad=0., fontsize=10)

        plot4 = plt.subplot2grid((4, 2), (1, 1))
        plt.plot((EMG_array[i][:, 2]) * 5.0 + 5.0, label = "Obliques_L")
        plt.plot(COP_array[i]["COP_Y"] / 15.0, label = "COP_Y")
        plt.plot((EMG_array[i][:, 3]) * 5.0 - 5.0, label = "Obliques_R")
        plt.legend(bbox_to_anchor=(0, 0), loc=3, borderaxespad=0., fontsize=10)

        plot5 = plt.subplot2grid((4, 2), (2, 0))
        plt.plot((EMG_array[i][:, 4]) * 5.0 + 5.0, label = "Ilicostalis_L")
        plt.plot(COP_array[i]["COP_X"] / 15.0, label = "COP X")
        plt.plot((EMG_array[i][:, 5]) * 5.0 - 5.0, label = "Ilicostalis_R")
        plt.legend(bbox_to_anchor=(0, 0), loc=3, borderaxespad=0., fontsize=10)

        plot6 = plt.subplot2grid((4, 2), (2, 1))
        plt.plot((EMG_array[i][:, 4]) * 5.0 + 5.0, label = "Ilicostalis_L")
        plt.plot(COP_array[i]["COP_Y"] / 15.0, label = "COP Y")
        plt.plot((EMG_array[i][:, 5]) * 5.0 - 5.0, label = "Ilicostalis_R")
        plt.legend(bbox_to_anchor=(0, 0), loc=3, borderaxespad=0., fontsize=10)

        plot7 = plt.subplot2grid((4, 2), (3, 0))
        plt.plot((EMG_array[i][:, 6]) * 5.0 + 5.0, label = "Multifidus_L")
        plt.plot(COP_array[i]["COP_X"] / 15.0, label = "COP X")
        plt.plot((EMG_array[i][:, 7]) * 5.0 - 5.0, label = "Multifidus_R")
        plt.legend(bbox_to_anchor=(0, 0), loc=3, borderaxespad=0., fontsize=10)

        plot8 = plt.subplot2grid((4, 2), (3, 1))
        plt.plot((EMG_array[i][:, 6]) * 5.0 + 5.0, label = "Multifidus_L")
        plt.plot(COP_array[i]["COP_Y"] / 15.0, label = "COP Y")
        plt.plot((EMG_array[i][:, 7]) * 5.0 - 5.0, label = "Multifidus_R")
        plt.legend(bbox_to_anchor=(0, 0), loc=3, borderaxespad=0., fontsize=10)

        plt.show()




