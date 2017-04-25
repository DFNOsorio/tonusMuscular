from tools import *
import numpy as np

def RL_muscles_COP(COP_array, velocity_array, aceleration_array, EMG_array):
    RA_corr = {}
    O_corr = {}
    I_corr = {}
    M_corr = {}
    correlation_values = {}
    for i in EMG_array:
        RA_RMS = RMS((EMG_array[i][:,1])-(EMG_array[i][:,0]))
        RA_array = normalization_subEMG(RA_RMS)

        O_RMS = RMS((EMG_array[i][:,3]) - (EMG_array[i][:,2]))
        O_array = normalization_subEMG(O_RMS)

        I_RMS = RMS((EMG_array[i][:,5]) - (EMG_array[i][:,4]))
        I_array = normalization_subEMG(I_RMS)

        M_RMS = RMS((EMG_array[i][:,7]) - (EMG_array[i][:,6]))
        M_array = normalization_subEMG(M_RMS)

        COP_X = normalization_subCOP(RMS(COP_array[i]["COP_X"]))

        RA_COP = np.corrcoef(RA_array,COP_X)
        RA_vel = np.corrcoef(RA_array[0:len(RA_array) - 1], velocity_array[i]["COP_X"])
        RA_acel = np.corrcoef(RA_array[0:len(RA_array) - 2], aceleration_array[i]["COP_X"])

        O_COP = np.corrcoef(O_array, COP_X)
        O_vel = np.corrcoef(O_array[0:len(O_array) - 1], velocity_array[i]["COP_X"])
        O_acel = np.corrcoef(O_array[0:len(O_array) - 2], aceleration_array[i]["COP_X"])

        I_COP = np.corrcoef(I_array, COP_X)
        I_vel = np.corrcoef(I_array[0:len(I_array) - 1], velocity_array[i]["COP_X"])
        I_acel = np.corrcoef(I_array[0:len(I_array) - 2], aceleration_array[i]["COP_X"])

        M_COP = np.corrcoef(M_array, COP_X)
        M_vel = np.corrcoef(M_array[0:len(M_array) - 1], velocity_array[i]["COP_X"])
        M_acel = np.corrcoef(M_array[0:len(M_array) - 2], aceleration_array[i]["COP_X"])

        RA_corr = {"RA_COP": RA_COP[0,1], "RA_vel": RA_vel[0,1], "RA_acel": RA_acel[0,1]}
        O_corr = {"O_COP": O_COP[0, 1], "O_vel": O_vel[0, 1], "O_acel": O_acel[0, 1]}
        I_corr = {"I_COP": I_COP[0, 1], "I_vel": I_vel[0, 1], "I_acel": I_acel[0, 1]}
        M_corr = {"M_COP": M_COP[0, 1], "M_vel": M_vel[0, 1], "M_acel": M_acel[0, 1]}

        correlation_values[i] = {"RA_corr": RA_corr, "O_corr": O_corr, "I_corr": I_corr, "M_corr": M_corr}
    return correlation_values

def FB_muscles_COP(COP_array, velocity_array, aceleration_array, EMG_array):
    MR_L_corr = {}
    MR_R_corr = {}
    IO_L_corr = {}
    IO_R_corr = {}
    correlation_values = {}
    for i in EMG_array:
        MR_L_RMS = RMS((EMG_array[i][:, 0]) - (EMG_array[i][:, 6]))
        MR_L_array = normalization_subEMG(MR_L_RMS)

        MR_R_RMS = RMS((EMG_array[i][:, 1]) - (EMG_array[i][:, 7]))
        MR_R_array = normalization_subEMG(MR_R_RMS)

        IO_L_RMS = RMS((EMG_array[i][:, 2]) - (EMG_array[i][:, 4]))
        IO_L_array = normalization_subEMG(IO_L_RMS)

        IO_R_RMS = RMS((EMG_array[i][:, 3]) - (EMG_array[i][:, 5]))
        IO_R_array = normalization_subEMG(IO_R_RMS)

        COP_Y = normalization_subCOP(RMS(COP_array[i]["COP_Y"]))

        MR_L_COP = np.corrcoef(MR_L_array,COP_Y)
        MR_L_vel = np.corrcoef(MR_L_array[0:len(MR_L_array) - 1], velocity_array[i]["COP_Y"])
        MR_L_acel = np.corrcoef(MR_L_array[0:len(MR_L_array) - 2], aceleration_array[i]["COP_Y"])

        MR_R_COP = np.corrcoef(MR_R_array, COP_Y)
        MR_R_vel = np.corrcoef(MR_R_array[0:len(MR_R_array) - 1], velocity_array[i]["COP_Y"])
        MR_R_acel = np.corrcoef(MR_R_array[0:len(MR_R_array) - 2], aceleration_array[i]["COP_Y"])

        IO_L_COP = np.corrcoef(IO_L_array, COP_Y)
        IO_L_vel = np.corrcoef(IO_L_array[0:len(IO_L_array) - 1], velocity_array[i]["COP_Y"])
        IO_L_acel = np.corrcoef(IO_L_array[0:len(IO_L_array) - 2], aceleration_array[i]["COP_Y"])

        IO_R_COP = np.corrcoef(IO_R_array, COP_Y)
        IO_R_vel = np.corrcoef(IO_R_array[0:len(IO_R_array) - 1], velocity_array[i]["COP_Y"])
        IO_R_acel = np.corrcoef(IO_R_array[0:len(IO_R_array) - 2], aceleration_array[i]["COP_Y"])

        MR_L_corr = {"MR_L_COP": MR_L_COP[0,1], "MR_L_vel": MR_L_vel[0,1], "MR_L_acel": MR_L_acel[0,1]}
        MR_R_corr = {"MR_R_COP": MR_R_COP[0, 1], "MR_R_vel": MR_R_vel[0, 1], "MR_R_acel": MR_R_acel[0, 1]}
        IO_L_corr = {"IO_L_COP": IO_L_COP[0, 1], "IO_L_vel": IO_L_vel[0, 1], "IO_L_acel": IO_L_acel[0, 1]}
        IO_R_corr = {"IO_R_COP": IO_R_COP[0, 1], "IO_R_vel": IO_R_vel[0, 1], "IO_R_acel": IO_R_acel[0, 1]}

        correlation_values[i] = {"MR_L_corr": MR_L_corr, "MR_R_corr": MR_R_corr, "IO_L_corr": IO_L_corr, "IO_R_corr": IO_R_corr}
    return correlation_values

def FB_muscles_COP_Cross(COP_array, EMG_array):
    MR_LR_corr = {}
    MR_RL_corr = {}
    IO_LR_corr = {}
    IO_RL_corr = {}
    correlation_values = {}
    for i in EMG_array:
        MR_LR_RMS = RMS((EMG_array[i][:, 0]) - (EMG_array[i][:, 7]))
        MR_LR_array = normalization_subEMG(MR_LR_RMS)

        MR_RL_RMS = RMS((EMG_array[i][:, 1]) - (EMG_array[i][:, 6]))
        MR_RL_array = normalization_subEMG(MR_RL_RMS)

        IO_LR_RMS = RMS((EMG_array[i][:, 2]) - (EMG_array[i][:, 5]))
        IO_LR_array = normalization_subEMG(IO_LR_RMS)

        IO_RL_RMS = RMS((EMG_array[i][:, 3]) - (EMG_array[i][:, 4]))
        IO_RL_array = normalization_subEMG(IO_RL_RMS)

        COP_X = normalization_subCOP(RMS(COP_array[i]["COP_X"]))
        COP_Y = normalization_subCOP(RMS(COP_array[i]["COP_Y"]))

        MR_LR_COP_X = np.corrcoef(MR_LR_array, COP_X)
        MR_LR_COP_Y = np.corrcoef(MR_LR_array, COP_Y)

        MR_RL_COP_X = np.corrcoef(MR_RL_array, COP_X)
        MR_RL_COP_Y = np.corrcoef(MR_RL_array, COP_Y)

        IO_LR_COP_X = np.corrcoef(IO_LR_array, COP_X)
        IO_LR_COP_Y = np.corrcoef(IO_LR_array, COP_Y)

        IO_RL_COP_X = np.corrcoef(IO_RL_array, COP_X)
        IO_RL_COP_Y = np.corrcoef(IO_RL_array, COP_Y)

        MR_LR_corr = {"MR_LR_COP_X": MR_LR_COP_X[0, 1], "MR_LR_COP_Y": MR_LR_COP_Y[0, 1]}
        MR_RL_corr = {"MR_RL_COP_X": MR_RL_COP_X[0, 1], "MR_RL_COP_Y": MR_RL_COP_Y[0, 1]}
        IO_LR_corr = {"IO_LR_COP_X": IO_LR_COP_X[0, 1], "IO_LR_COP_Y": IO_LR_COP_Y[0, 1]}
        IO_RL_corr = {"IO_RL_COP_X": IO_RL_COP_X[0, 1], "IO_RL_COP_Y": IO_RL_COP_Y[0, 1]}

        correlation_values[i] = {"MR_LR_corr": MR_LR_corr, "MR_RL_corr": MR_RL_corr, "IO_LR_corr": IO_LR_corr,
                                 "IO_RL_corr": IO_RL_corr}
    return correlation_values