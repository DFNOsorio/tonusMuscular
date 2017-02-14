import h5py
import numpy as np
from ops import *

dynamic_list = ["Arms_extension","Standing_EO", "Standing_EC", "OneFootStanding_R_EO", "OneFootStanding_R_EC", "OneFootStanding_L_EO", "OneFootStanding_L_EC", "Reach_R", "Reach_L", "Reach_C", "Reach_Ground"]

static_list = ["MVC1", "MVC2", "Relax"]



class Patient:

    def __init__(self, filename, platform = False, verbose = True):

        self.filename = filename

        self.platform = platform

        self.static         = {}

        self.EMG            = {}

        self.platform       = {}

        for i in static_list:

            self.static[i] = load_data_segment(filename, "Static", i, verbose = verbose)

        for i in dynamic_list:

            self.EMG[i] = load_data_segment(filename, "EMG", i, verbose = verbose)

            if platform: self.platform[i] = load_data_segment(filename, "Platform", i, verbose = verbose)

        avg_out(self.static)
        avg_out(self.EMG)

        if platform: avg_out(self.platform)





def load_data_segment(filename, place, segment, verbose="True"):

    file = h5py.File(filename, 'r')

    data_group = file[place + "/" + segment]

    try:
        data = np.zeros((len(data_group["channel1"]), len(data_group)))
        for t in range(0, len(data_group)):
            data[:, t] = data_group["channel" + str(t + 1)]
        if verbose:
            print "Segment", segment, "from", place, "loaded."
        return data

    except KeyError:
        if verbose:
            print "Segment", segment, "from", place, "failed to load (No data)."
            return []





