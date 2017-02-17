import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
from matplotlib.backends.backend_pdf import PdfPages


def graph_platform(max_values, platform_COP,description, platform = False):
    ind = np.arange(2)
    margin = 0.01
    width = (1. - 2. * margin) / len(ind)
    #width = 0.35
    error_config = {'ecolor': '0.5', 'capthick': 0.5}
    pp = PdfPages('Platform_'+str(description)+'.pdf')

    l = 0
    for i in max_values:
        fig = plt.figure(l)
        l = l+1
        fig.suptitle(str(i) + "\n"+ str(description), fontsize=25)

        plot1 = plt.subplot2grid((3, 3), (0, 0))
        plt.bar(ind, [max_values[i][0],max_values[i][2]], width, error_kw=error_config, align= 'center')
        plt.xticks(ind, ("Rectus_A_L", "Obliques_L"), fontsize=7)
        plt.ylabel("Percentage from MVC maximum.(%)",fontsize=7)
        plt.ylim([0, 100])
        plot1.set_title("Maximum for for each muscle on the left side\n Front", fontsize=12)

        plot2 = plt.subplot2grid((3, 3), (0, 1))
        plt.bar(ind, [max_values[i][1], max_values[i][3]], width, error_kw=error_config, align= 'center')
        plt.xticks(ind, ("Rectus_A_R", "Obliques_R"), fontsize=7)
        plt.ylabel("Percentage from MVC maximum.(%)",fontsize=7)
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
        plt.xticks(ind, ("Ilicostalis_L", "Multifundus_L"), fontsize=7)
        plt.ylabel("Percentage from MVC maximum.(%)", fontsize=7)
        plt.ylim([0, 100])
        plot4.set_title("Maximum for for each muscle on the left side\n Back", fontsize=12)

        plot5 = plt.subplot2grid((3, 3), (2, 1))
        plt.bar(ind, [max_values[i][5], max_values[i][7]], width, error_kw=error_config, align= 'center')
        plt.xticks(ind, ("Ilicostalis_R", "Multifundus_R"), fontsize=7)
        plt.ylabel("Percentage from MVC maximum.(%)", fontsize=7)
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
