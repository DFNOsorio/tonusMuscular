from tools import *
import xlsxwriter
import xlrd
from openpyxl import Workbook
from openpyxl import load_workbook
from xlrd import open_workbook
from openpyxl.styles import Alignment
from openpyxl.styles import PatternFill
import numpy as np
from pylab import plot, show, savefig, xlim, figure,hold, ylim, legend, boxplot, setp, axes
import matplotlib.gridspec as gridspect





def get_EMG_evolution(EMG_array):
    file_excel_over30 = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_over30 _final.xlsx'
    file_excel_20 = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_20-30_final.xlsx'
    file_excel_EA = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_EA1_final.xlsx'

    wb_over30 = load_workbook(file_excel_over30)
    wb_20 = load_workbook(file_excel_20)
    wb_EA = load_workbook(file_excel_EA)


    count = 409
    value_final_over30 = {}
    value_final_male = {}
    value_final_female = {}
    value_final_EA = {}

    value_muscle_over30 = {}
    value_muscle_male = {}
    value_muscle_female = {}
    value_muscle_EA = {}


    for task in EMG_array:

        value_0_25 = []
        value_25_50 = []
        value_50_75 = []
        value_75_100 = []
        value_100_125 = []
        value_125_150 = []
        value_150_175 = []
        value_175_200 = []
        value_200_225 = []
        value_225_250 = []
        value_250_275 = []
        value_275_300 = []
        name = ''
        column = ''


        for i in wb_over30.sheetnames:
            if i != 'Sheet1' and i != 'Statistical Analysis_20_Female' and i!= 'Statistical Analysis_20_Male'\
                    and i != 'Statistical Analysis over 30' and i != 'Folha1':

                ws_over30 = wb_over30.get_sheet_by_name(i)

                if task == "Reach_L" and task == "Reach_R" and task == "Reach_C":
                    for muscle in EMG_array[task][1, :]:
                        if muscle == 0:
                            column = 'M'
                            name = "Rectus_L"
                        if muscle == 1:
                            column = 'N'
                            name = "Rectus_R"
                        if muscle == 2:
                            column = 'O'
                            name = "Obliques_L"
                        if muscle == 3:
                            column = 'P'
                            name = "Obliques_R"
                        if muscle == 4:
                            column = 'Q'
                            name = "Ilicostalis_L"
                        if muscle == 5:
                            column = 'R'
                            name = "Ilicostalis_R"
                        if muscle == 6:
                            column = 'S'
                            name = "Multi_L"
                        if muscle == 7:
                            column = 'T'
                            name = "Multi_R"

                        print name
                        print column


                        value_0_25.append(ws_over30[str(column) + str(count)].value)
                        value_25_50.append(ws_over30[str(column) + str(count + 1)].value)
                        value_50_75.append(ws_over30[str(column) + str(count + 2)].value)
                        value_75_100.append(ws_over30[str(column) + str(count + 3)].value)
                        value_100_125.append(ws_over30[str(column) + str(count + 4)].value)
                        value_125_150.append(ws_over30[str(column) + str(count + 5)].value)
                        value_150_175.append(ws_over30[str(column) + str(count + 6)].value)

                    value_muscle_over30[name] = {"[0 - 1]": value_0_25, "[1 - 2]": value_25_50, "[2 - 3]": value_50_75,
                                               "[3 - 4]": value_75_100, "[4 - 5]": value_100_125,
                                               "[5 - 6]": value_125_150, "[6 - 7]": value_150_175}

                if task != "Reach_L" and task != "Reach_R" and task != "Reach_C":
                    for muscle in EMG_array[task][1, :]:
                        if muscle == 0:
                            column = 'M'
                            name = "Rectus_L"
                        if muscle == 1:
                            column = 'N'
                            name = "Rectus_R"
                        if muscle == 2:
                            column = 'O'
                            name = "Obliques_L"
                        if muscle == 3:
                            column = 'P'
                            name = "Obliques_R"
                        if muscle == 4:
                            column = 'Q'
                            name = "Ilicostalis_L"
                        if muscle == 5:
                            column = 'R'
                            name = "Ilicostalis_R"
                        if muscle == 6:
                            column = 'S'
                            name = "Multi_L"
                        if muscle == 7:
                            column = 'T'
                            name = "Multi_R"
                        value_0_25.append(ws_over30[str(column) + str(count)].value)
                        value_25_50.append(ws_over30[str(column) + str(count + 1)].value)
                        value_50_75.append(ws_over30[str(column) + str(count + 2)].value)
                        value_75_100.append(ws_over30[str(column) + str(count + 3)].value)
                        value_100_125.append(ws_over30[str(column) + str(count + 4)].value)
                        value_125_150.append(ws_over30[str(column) + str(count + 5)].value)
                        value_150_175.append(ws_over30[str(column) + str(count + 6)].value)
                        value_175_200.append(ws_over30[str(column) + str(count + 7)].value)
                        value_200_225.append(ws_over30[str(column) + str(count + 8)].value)
                        value_225_250.append(ws_over30[str(column) + str(count + 9)].value)
                        value_250_275.append(ws_over30[str(column) + str(count + 10)].value)
                        value_275_300.append(ws_over30[str(column) + str(count + 11)].value)

                    value_muscle_over30[name] = {"[0 - 2.5]": value_0_25, "[2.5 - 5]": value_25_50, "[5 - 7.5]": value_50_75,
                                            "[7.5 - 10]": value_75_100, "[10 - 12.5]": value_100_125,
                                            "[12.5 - 15]": value_125_150, "[15 - 17.5]": value_150_175,
                                            "[17.5 - 20]": value_175_200, "[20 - 22.5]": value_200_225,
                                            "[22.5 - 25]": value_225_250, "[25 - 27.5]": value_250_275,
                                            "[27.5 - 30]": value_275_300}


    #     for i in wb_20.sheetnames:
    #         if i != 'Sheet1' and i != 'Statistical Analysis_20_Female' and i!= 'Statistical Analysis_20_Male'\
    #                 and i != 'Statistical Analysis over 30' and i != 'Folha1' and i != 'Patient5_Healthy'\
    #                 and i != 'Patient8_Healthy' and i != 'Patient10_Healthy' and i != 'Patient13_Healthy'\
    #                 and i != 'Patient17_Healthy' and i != 'Patient18_Healthy' and i != 'Patient23_Healthy'\
    #                 and i != 'Patient25_Healthy' and i != 'Patient27_Healthy' and i != 'Patient30_Healthy':
    #
    #             ws_male = wb_over30.get_sheet_by_name(i)
    #             if task == "Reach_L" and task == "Reach_R" and task == "Reach_C":
    #                 for muscle in EMG_array[task][1, :]:
    #                     if muscle == 0:
    #                         column = 'M'
    #                         name = "Rectus_L"
    #                     if muscle == 1:
    #                         column = 'N'
    #                         name = "Rectus_R"
    #                     if muscle == 2:
    #                         column = 'O'
    #                         name = "Obliques_L"
    #                     if muscle == 3:
    #                         column = 'P'
    #                         name = "Obliques_R"
    #                     if muscle == 4:
    #                         column = 'Q'
    #                         name = "Ilicostalis_L"
    #                     if muscle == 5:
    #                         column = 'R'
    #                         name = "Ilicostalis_R"
    #                     if muscle == 6:
    #                         column = 'S'
    #                         name = "Multi_L"
    #                     if muscle == 7:
    #                         column = 'T'
    #                         name = "Multi_R"
    #                     value_0_25.append(ws_male[str(column) + str(count)].value)
    #                     value_25_50.append(ws_male[str(column) + str(count + 1)].value)
    #                     value_50_75.append(ws_male[str(column) + str(count + 2)].value)
    #                     value_75_100.append(ws_male[str(column) + str(count + 3)].value)
    #                     value_100_125.append(ws_male[str(column) + str(count + 4)].value)
    #                     value_125_150.append(ws_male[str(column) + str(count + 5)].value)
    #                     value_150_175.append(ws_male[str(column) + str(count + 6)].value)
    #
    #                 value_muscle_male[name] = {"[0 - 1]": value_0_25, "[1 - 2]": value_25_50, "[2 - 3]": value_50_75,
    #                                            "[3 - 4]": value_75_100, "[4 - 5]": value_100_125,
    #                                            "[5 - 6]": value_125_150, "[6 - 7]": value_150_175}
    #
    #             if task != "Reach_L" and task != "Reach_R" and task != "Reach_C":
    #                 for muscle in EMG_array[task][1, :]:
    #                     if muscle == 0:
    #                         column = 'M'
    #                         name = "Rectus_L"
    #                     if muscle == 1:
    #                         column = 'N'
    #                         name = "Rectus_R"
    #                     if muscle == 2:
    #                         column = 'O'
    #                         name = "Obliques_L"
    #                     if muscle == 3:
    #                         column = 'P'
    #                         name = "Obliques_R"
    #                     if muscle == 4:
    #                         column = 'Q'
    #                         name = "Ilicostalis_L"
    #                     if muscle == 5:
    #                         column = 'R'
    #                         name = "Ilicostalis_R"
    #                     if muscle == 6:
    #                         column = 'S'
    #                         name = "Multi_L"
    #                     if muscle == 7:
    #                         column = 'T'
    #                         name = "Multi_R"
    #                     value_0_25.append(ws_male[str(column) + str(count)].value)
    #                     value_25_50.append(ws_male[str(column) + str(count + 1)].value)
    #                     value_50_75.append(ws_male[str(column) + str(count + 2)].value)
    #                     value_75_100.append(ws_male[str(column) + str(count + 3)].value)
    #                     value_100_125.append(ws_male[str(column) + str(count + 4)].value)
    #                     value_125_150.append(ws_male[str(column) + str(count + 5)].value)
    #                     value_150_175.append(ws_male[str(column) + str(count + 6)].value)
    #                     value_175_200.append(ws_male[str(column) + str(count + 7)].value)
    #                     value_200_225.append(ws_male[str(column) + str(count + 8)].value)
    #                     value_225_250.append(ws_male[str(column) + str(count + 9)].value)
    #                     value_250_275.append(ws_male[str(column) + str(count + 10)].value)
    #                     value_275_300.append(ws_male[str(column) + str(count + 11)].value)
    #
    #                 value_muscle_male[name] = {"[0 - 2.5]": value_0_25, "[2.5 - 5]": value_25_50, "[5 - 7.5]": value_50_75,
    #                                        "[7.5 - 10]": value_75_100, "[10 - 12.5]": value_100_125,
    #                                        "[12.5 - 15]": value_125_150, "[15 - 17.5]": value_150_175,
    #                                        "[17.5 - 20]": value_175_200, "[20 - 22.5]": value_200_225,
    #                                        "[22.5 - 25]": value_225_250, "[25 - 27.5]": value_250_275,
    #                                        "[27.5 - 30]": value_275_300}
    #
    #         if i == 'Patient8_Healthy' or i == 'Patient10_Healthy' or i == 'Patient13_Healthy'\
    #                 or i == 'Patient17_Healthy' or i == 'Patient18_Healthy' or i == 'Patient23_Healthy'\
    #                 or i == 'Patient25_Healthy' or i == 'Patient27_Healthy' or i == 'Patient30_Healthy' or i == 'Patient5_Healthy':
    #
    #             ws_female = wb_over30.get_sheet_by_name(i)
    #             if task == "Reach_L" and task == "Reach_R" and task == "Reach_C":
    #                 for muscle in EMG_array[task][1, :]:
    #                     if muscle == 0:
    #                         column = 'M'
    #                         name = "Rectus_L"
    #                     if muscle == 1:
    #                         column = 'N'
    #                         name = "Rectus_R"
    #                     if muscle == 2:
    #                         column = 'O'
    #                         name = "Obliques_L"
    #                     if muscle == 3:
    #                         column = 'P'
    #                         name = "Obliques_R"
    #                     if muscle == 4:
    #                         column = 'Q'
    #                         name = "Ilicostalis_L"
    #                     if muscle == 5:
    #                         column = 'R'
    #                         name = "Ilicostalis_R"
    #                     if muscle == 6:
    #                         column = 'S'
    #                         name = "Multi_L"
    #                     if muscle == 7:
    #                         column = 'T'
    #                         name = "Multi_R"
    #                     value_0_25.append(ws_female[str(column) + str(count)].value)
    #                     value_25_50.append(ws_female[str(column) + str(count + 1)].value)
    #                     value_50_75.append(ws_female[str(column) + str(count + 2)].value)
    #                     value_75_100.append(ws_female[str(column) + str(count + 3)].value)
    #                     value_100_125.append(ws_female[str(column) + str(count + 4)].value)
    #                     value_125_150.append(ws_female[str(column) + str(count + 5)].value)
    #                     value_150_175.append(ws_female[str(column) + str(count + 6)].value)
    #
    #                 value_muscle_female[name] = {"[0 - 1]": value_0_25, "[1 - 2]": value_25_50, "[2 - 3]": value_50_75,
    #                                          "[3 - 4]": value_75_100, "[4 - 5]": value_100_125,
    #                                          "[5 - 6]": value_125_150, "[6 - 7]": value_150_175}
    #
    #             if task != "Reach_L" and task != "Reach_R" and task != "Reach_C":
    #                 for muscle in EMG_array[task][1, :]:
    #                     if muscle == 0:
    #                         column = 'M'
    #                         name = "Rectus_L"
    #                     if muscle == 1:
    #                         column = 'N'
    #                         name = "Rectus_R"
    #                     if muscle == 2:
    #                         column = 'O'
    #                         name = "Obliques_L"
    #                     if muscle == 3:
    #                         column = 'P'
    #                         name = "Obliques_R"
    #                     if muscle == 4:
    #                         column = 'Q'
    #                         name = "Ilicostalis_L"
    #                     if muscle == 5:
    #                         column = 'R'
    #                         name = "Ilicostalis_R"
    #                     if muscle == 6:
    #                         column = 'S'
    #                         name = "Multi_L"
    #                     if muscle == 7:
    #                         column = 'T'
    #                         name = "Multi_R"
    #                     value_0_25.append(ws_female[str(column) + str(count)].value)
    #                     value_25_50.append(ws_female[str(column) + str(count + 1)].value)
    #                     value_50_75.append(ws_female[str(column) + str(count + 2)].value)
    #                     value_75_100.append(ws_female[str(column) + str(count + 3)].value)
    #                     value_100_125.append(ws_female[str(column) + str(count + 4)].value)
    #                     value_125_150.append(ws_female[str(column) + str(count + 5)].value)
    #                     value_150_175.append(ws_female[str(column) + str(count + 6)].value)
    #                     value_175_200.append(ws_female[str(column) + str(count + 7)].value)
    #                     value_200_225.append(ws_female[str(column) + str(count + 8)].value)
    #                     value_225_250.append(ws_female[str(column) + str(count + 9)].value)
    #                     value_250_275.append(ws_female[str(column) + str(count + 10)].value)
    #                     value_275_300.append(ws_female[str(column) + str(count + 11)].value)
    #
    #             value_muscle_female[name] = {"[0 - 2.5]": value_0_25, "[2.5 - 5]": value_25_50,
    #                                            "[5 - 7.5]": value_50_75,
    #                                            "[7.5 - 10]": value_75_100, "[10 - 12.5]": value_100_125,
    #                                            "[12.5 - 15]": value_125_150, "[15 - 17.5]": value_150_175,
    #                                            "[17.5 - 20]": value_175_200, "[20 - 22.5]": value_200_225,
    #                                            "[22.5 - 25]": value_225_250, "[25 - 27.5]": value_250_275,
    #                                            "[27.5 - 30]": value_275_300}
    #
    #
    #     for i in wb_EA.sheetnames:
    #         if i != 'Sheet1':
    #
    #             ws_EA = wb_over30.get_sheet_by_name(i)
    #             if task == "Reach_L" and task == "Reach_R" and task == "Reach_C":
    #                 for muscle in EMG_array[task][1, :]:
    #                     if muscle == 0:
    #                         column = 'M'
    #                         name = "Rectus_L"
    #                     if muscle == 1:
    #                         column = 'N'
    #                         name = "Rectus_R"
    #                     if muscle == 2:
    #                         column = 'O'
    #                         name = "Obliques_L"
    #                     if muscle == 3:
    #                         column = 'P'
    #                         name = "Obliques_R"
    #                     if muscle == 4:
    #                         column = 'Q'
    #                         name = "Ilicostalis_L"
    #                     if muscle == 5:
    #                         column = 'R'
    #                         name = "Ilicostalis_R"
    #                     if muscle == 6:
    #                         column = 'S'
    #                         name = "Multi_L"
    #                     if muscle == 7:
    #                         column = 'T'
    #                         name = "Multi_R"
    #                     value_0_25.append(ws_EA[str(column) + str(count)].value)
    #                     value_25_50.append(ws_EA[str(column) + str(count + 1)].value)
    #                     value_50_75.append(ws_EA[str(column) + str(count + 2)].value)
    #                     value_75_100.append(ws_EA[str(column) + str(count + 3)].value)
    #                     value_100_125.append(ws_EA[str(column) + str(count + 4)].value)
    #                     value_125_150.append(ws_EA[str(column) + str(count + 5)].value)
    #                     value_150_175.append(ws_EA[str(column) + str(count + 6)].value)
    #
    #                 value_muscle_EA[name] = {"[0 - 1]": value_0_25, "[1 - 2]": value_25_50, "[2 - 3]": value_50_75,
    #                                            "[3 - 4]": value_75_100, "[4 - 5]": value_100_125,
    #                                            "[5 - 6]": value_125_150, "[6 - 7]": value_150_175}
    #
    #             if task != "Reach_L" and task != "Reach_R" and task != "Reach_C":
    #                 for muscle in EMG_array[task][1, :]:
    #                     if muscle == 0:
    #                         column = 'M'
    #                         name = "Rectus_L"
    #                     if muscle == 1:
    #                         column = 'N'
    #                         name = "Rectus_R"
    #                     if muscle == 2:
    #                         column = 'O'
    #                         name = "Obliques_L"
    #                     if muscle == 3:
    #                         column = 'P'
    #                         name = "Obliques_R"
    #                     if muscle == 4:
    #                         column = 'Q'
    #                         name = "Ilicostalis_L"
    #                     if muscle == 5:
    #                         column = 'R'
    #                         name = "Ilicostalis_R"
    #                     if muscle == 6:
    #                         column = 'S'
    #                         name = "Multi_L"
    #                     if muscle == 7:
    #                         column = 'T'
    #                         name = "Multi_R"
    #                     value_0_25.append(ws_EA[str(column) + str(count)].value)
    #                     value_25_50.append(ws_EA[str(column) + str(count + 1)].value)
    #                     value_50_75.append(ws_EA[str(column) + str(count + 2)].value)
    #                     value_75_100.append(ws_EA[str(column) + str(count + 3)].value)
    #                     value_100_125.append(ws_EA[str(column) + str(count + 4)].value)
    #                     value_125_150.append(ws_EA[str(column) + str(count + 5)].value)
    #                     value_150_175.append(ws_EA[str(column) + str(count + 6)].value)
    #                     value_175_200.append(ws_EA[str(column) + str(count + 7)].value)
    #                     value_200_225.append(ws_EA[str(column) + str(count + 8)].value)
    #                     value_225_250.append(ws_EA[str(column) + str(count + 9)].value)
    #                     value_250_275.append(ws_EA[str(column) + str(count + 10)].value)
    #                     value_275_300.append(ws_EA[str(column) + str(count + 11)].value)
    #
    #                 value_muscle_EA[name] = {"[0 - 2.5]": value_0_25, "[2.5 - 5]": value_25_50,
    #                                                "[5 - 7.5]": value_50_75,
    #                                                "[7.5 - 10]": value_75_100, "[10 - 12.5]": value_100_125,
    #                                                "[12.5 - 15]": value_125_150, "[15 - 17.5]": value_150_175,
    #                                                "[17.5 - 20]": value_175_200, "[20 - 22.5]": value_200_225,
    #                                                "[22.5 - 25]": value_225_250, "[25 - 27.5]": value_250_275,
    #                                                "[27.5 - 30]": value_275_300}
    #
    #     count = count + 23
    #
    #     value_final_over30[task] = value_muscle_over30
    #
    #     value_final_male[task] = value_muscle_male
    #
    #     value_final_female[task] = value_muscle_female
    #
    #     value_final_EA[task] = value_muscle_EA
    #
    # return value_final_over30, value_final_male, value_final_female, value_final_EA
