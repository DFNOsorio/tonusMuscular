import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg


def graph_platform(max_values, platform_COP, platform = False):
    ind = np.arange(2)
    width = 0.5
    error_config = {'ecolor': '0.3', 'capthick': 0.5}


    for i in max_values:
        fig = plt.figure()
        fig.suptitle(str(i), fontsize=20)

        plot1 = plt.subplot2grid((3, 3), (0, 0))
        plt.bar(ind, [max_values[i][0],max_values[i][2]], width, error_kw=error_config)
        plt.xticks(ind + width / 2.0, ("Rectus_A_L", "Obliques_L"), fontsize=7)
        plt.ylabel("Percentage from MVC maximum.(%)",fontsize=7)
        plot1.set_title("Maximum for for each muscle on the left side\n Front", fontsize=10)

        plot2 = plt.subplot2grid((3, 3), (0, 1))
        plt.bar(ind, [max_values[i][1], max_values[i][3]], width, error_kw=error_config)
        plt.xticks(ind + width / 2.0, ("Rectus_A_R", "Obliques_R"), fontsize=7)
        plt.ylabel("Percentage from MVC maximum.(%)",fontsize=7)
        plot2.set_title("Maximum for for each muscle on the right side\n Front", fontsize=10)

        if platform == True:
            plot3 = plt.subplot2grid((3, 3), (1, 2), colspan=2, rowspan=2)
            img = mpimg.imread("tools/forcePlatform.png")
            plt.imshow(img, zorder=0, extent=[-225 - 12, +225 + 12, -225 - 12, +225 + 12])
            plt.plot(platform_COP[i]["COP_X"], platform_COP[i]["COP_Y"], color='yellow')
            plt.xlim([-225 - 12, 225 + 12])
            plt.ylim([-225 - 12, 225 + 12])
            plt.xlabel("Trajectory of COP on X axes", fontsize=11)
            plt.ylabel("Trajectory of COP on Y axes", fontsize=11)
            plot3.set_title("COP trajectory", fontsize=15)

        plot4 = plt.subplot2grid((3, 3), (2, 0))
        plt.bar(ind, [max_values[i][4], max_values[i][6]], width, error_kw=error_config)
        plt.xticks(ind + width / 2.0, ("Ilicostalis_L", "Multifundus_L"), fontsize=7)
        plt.ylabel("Percentage from MVC maximum.(%)", fontsize=7)
        plot4.set_title("Maximum for for each muscle on the left side\n Back", fontsize=10)

        plot5 = plt.subplot2grid((3, 3), (2, 1))
        plt.bar(ind, [max_values[i][5], max_values[i][7]], width, error_kw=error_config)
        plt.xticks(ind + width / 2.0, ("Ilicostalis_R", "Multifundus_R"), fontsize=7)
        plt.ylabel("Percentage from MVC maximum.(%)", fontsize=7)
        plot5.set_title("Maximum for for each muscle on the right side\n Back", fontsize=10)

        if platform == True:
            plt.subplots_adjust(top = 0.72, bottom = 0.14, left = 0.15,right=0.91, wspace=0.56, hspace=0.03)
        else:
            plt.subplots_adjust(top=0.75, bottom=0.11, left=0.30, right=0.98, wspace=0.47, hspace=0.01)

        plt.show()

def graph_normalizedRMS (test):
    for j in range(0, 8):
        for i in test:
            plt.plot(test[i][:, j], label=str(i))
            plt.legend(bbox_to_anchor=(0.9, 1.1), loc=2, borderaxespad=0.)

            plt.xlabel("Time in miliseconds", fontsize=7)
            plt.suptitle("Normalized RMS", fontsize=24)
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
        plt.show()

def graph_RMS(test):
    for j in range(0, 8):
        for i in test:
            plt.plot(test[i][:,j], label= str(i))
            plt.legend(bbox_to_anchor=(0.9, 1.1), loc=2, borderaxespad=0.)

            #red_patch = mpatches.Patch(color='red', label='The red data')
            #plt.legend(handles=[red_patch])
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
            plt.suptitle("RMS", fontsize=24)
        plt.show()

