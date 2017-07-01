from tools import *
import xlsxwriter
import xlrd
from openpyxl import Workbook
from openpyxl import load_workbook
from xlrd import open_workbook
from openpyxl.styles import Alignment
from openpyxl.styles import PatternFill
import numpy as np



def get_value_tonus(EMG_array):
    file_excel_over30 = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_over30 _final.xlsx'
    file_excel_20 = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_20-30_final.xlsx'
    file_excel_EA = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_EA1_final.xlsx'

    wb_over30 = load_workbook(file_excel_over30)
    wb_20 = load_workbook(file_excel_20)
    wb_EA = load_workbook(file_excel_EA)


    count = 8
    value_final_over30 = {}
    value_final_male = {}
    value_final_female = {}
    value_final_EA = {}

    for task in EMG_array:

        value_rectus_l_over30 = []
        value_rectus_r_over30 = []
        value_obliques_l_over30 = []
        value_obliques_r_over30 = []
        value_ilicostalis_l_over30 = []
        value_ilicostalis_r_over30 = []
        value_multi_l_over30 = []
        value_multi_r_over30 = []

        value_rectus_l_female = []
        value_rectus_r_female = []
        value_obliques_l_female = []
        value_obliques_r_female = []
        value_ilicostalis_l_female = []
        value_ilicostalis_r_female = []
        value_multi_l_female = []
        value_multi_r_female = []

        value_rectus_l_male = []
        value_rectus_r_male = []
        value_obliques_l_male = []
        value_obliques_r_male = []
        value_ilicostalis_l_male = []
        value_ilicostalis_r_male = []
        value_multi_l_male = []
        value_multi_r_male = []

        value_rectus_l_EA = []
        value_rectus_r_EA = []
        value_obliques_l_EA = []
        value_obliques_r_EA = []
        value_ilicostalis_l_EA = []
        value_ilicostalis_r_EA = []
        value_multi_l_EA = []
        value_multi_r_EA = []

        for i in wb_over30.sheetnames:
            if i != 'Sheet1' and i != 'Statistical Analysis_20_Female' and i!= 'Statistical Analysis_20_Male'\
                    and i != 'Statistical Analysis over 30' and i != 'Folha1':

                ws_over30 = wb_over30.get_sheet_by_name(i)
                value_rectus_l_over30.append(ws_over30['B' + str(count)].value)
                value_rectus_r_over30.append(ws_over30['C' + str(count)].value)
                value_obliques_l_over30.append(ws_over30['B' + str(count+1)].value)
                value_obliques_r_over30.append(ws_over30['C' + str(count+1)].value)
                value_ilicostalis_l_over30.append(ws_over30['B' + str(count+2)].value)
                value_ilicostalis_r_over30.append(ws_over30['C' + str(count+2)].value)
                value_multi_l_over30.append(ws_over30['B' + str(count+3)].value)
                value_multi_r_over30.append(ws_over30['C' + str(count+3)].value)

        for i in wb_20.sheetnames:
            if i != 'Sheet1' and i != 'Statistical Analysis_20_Female' and i!= 'Statistical Analysis_20_Male'\
                    and i != 'Statistical Analysis over 30' and i != 'Folha1' and i != 'Patient5_Healthy'\
                    and i != 'Patient8_Healthy' and i != 'Patient10_Healthy' and i != 'Patient13_Healthy'\
                    and i != 'Patient17_Healthy' and i != 'Patient18_Healthy' and i != 'Patient23_Healthy'\
                    and i != 'Patient25_Healthy' and i != 'Patient27_Healthy' and i != 'Patient30_Healthy':

                ws_female = wb_20.get_sheet_by_name(i)
                value_rectus_l_female.append(ws_female['B' + str(count)].value)
                value_rectus_r_female.append(ws_female['C' + str(count)].value)
                value_obliques_l_female.append(ws_female['B' + str(count+1)].value)
                value_obliques_r_female.append(ws_female['C' + str(count+1)].value)
                value_ilicostalis_l_female.append(ws_female['B' + str(count+2)].value)
                value_ilicostalis_r_female.append(ws_female['C' + str(count+2)].value)
                value_multi_l_female.append(ws_female['B' + str(count+3)].value)
                value_multi_r_female.append(ws_female['C' + str(count+3)].value)

            if i == 'Patient8_Healthy' or i == 'Patient10_Healthy' or i == 'Patient13_Healthy'\
                    or i == 'Patient17_Healthy' or i == 'Patient18_Healthy' or i == 'Patient23_Healthy'\
                    or i == 'Patient25_Healthy' or i == 'Patient27_Healthy' or i == 'Patient30_Healthy' or i == 'Patient5_Healthy':

                ws_male = wb_20.get_sheet_by_name(i)
                value_rectus_l_male.append(ws_male['B' + str(count)].value)
                value_rectus_r_male.append(ws_male['C' + str(count)].value)
                value_obliques_l_male.append(ws_male['B' + str(count + 1)].value)
                value_obliques_r_male.append(ws_male['C' + str(count + 1)].value)
                value_ilicostalis_l_male.append(ws_male['B' + str(count + 2)].value)
                value_ilicostalis_r_male.append(ws_male['C' + str(count + 2)].value)
                value_multi_l_male.append(ws_male['B' + str(count + 3)].value)
                value_multi_r_male.append(ws_male['C' + str(count + 3)].value)


        for i in wb_EA.sheetnames:
            if i != 'Sheet1':

                ws_EA = wb_EA.get_sheet_by_name(i)
                value_rectus_l_EA.append(ws_EA['B' + str(count)].value)
                value_rectus_r_EA.append(ws_EA['C' + str(count)].value)
                value_obliques_l_EA.append(ws_EA['B' + str(count+1)].value)
                value_obliques_r_EA.append(ws_EA['C' + str(count+1)].value)
                value_ilicostalis_l_EA.append(ws_EA['B' + str(count+2)].value)
                value_ilicostalis_r_EA.append(ws_EA['C' + str(count+2)].value)
                value_multi_l_EA.append(ws_EA['B' + str(count+3)].value)
                value_multi_r_EA.append(ws_EA['C' + str(count+3)].value)

        count = count + 13

        value_final_over30[task] = {"Rectus_L": value_rectus_l_over30,"Rectus_R": value_rectus_r_over30, "Obliques_L": value_obliques_l_over30,
                             "Obliques_R": value_obliques_r_over30, "Ilicostalis_L": value_ilicostalis_l_over30, "Ilicostalis_R": value_ilicostalis_r_over30,
                             "Multifidus_L": value_multi_l_over30, "Multifidus_R": value_multi_r_over30}

        value_final_male[task] = {"Rectus_L": value_rectus_l_male, "Rectus_R": value_rectus_r_male,
                                    "Obliques_L": value_obliques_l_male,
                                    "Obliques_R": value_obliques_r_male, "Ilicostalis_L": value_ilicostalis_l_male,
                                    "Ilicostalis_R": value_ilicostalis_r_male,
                                    "Multifidus_L": value_multi_l_male, "Multifidus_R": value_multi_r_male}

        value_final_female[task] = {"Rectus_L": value_rectus_l_female, "Rectus_R": value_rectus_r_female,
                                    "Obliques_L": value_obliques_l_female,
                                    "Obliques_R": value_obliques_r_female, "Ilicostalis_L": value_ilicostalis_l_female,
                                    "Ilicostalis_R": value_ilicostalis_r_female,
                                    "Multifidus_L": value_multi_l_female, "Multifidus_R": value_multi_r_female}

        value_final_EA[task] = {"Rectus_L": value_rectus_l_EA, "Rectus_R": value_rectus_r_EA,
                                    "Obliques_L": value_obliques_l_EA,
                                    "Obliques_R": value_obliques_r_EA, "Ilicostalis_L": value_ilicostalis_l_EA,
                                    "Ilicostalis_R": value_ilicostalis_r_EA,
                                    "Multifidus_L": value_multi_l_EA, "Multifidus_R": value_multi_r_EA}

    return value_final_over30, value_final_male, value_final_female, value_final_EA




def get_value_freq(freq_array):
    file_excel_over30 = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_over30 _final.xlsx'
    file_excel_20 = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_20-30_final.xlsx'
    file_excel_EA = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_EA1_final.xlsx'

    wb_over30 = load_workbook(file_excel_over30)
    wb_20 = load_workbook(file_excel_20)
    wb_EA = load_workbook(file_excel_EA)


    count = 260
    value_final_over30 = {}
    value_final_male = {}
    value_final_female = {}
    value_final_EA = {}

    for task in freq_array:
        over30 = {}
        female = {}
        male = {}
        EA = {}
        l = count

        for index in range(0, 8):
            peak_30 = []
            mean_30 = []
            median_30 = []
            eighty_value_30 = []

            peak_male = []
            mean_male = []
            median_male = []
            eighty_value_male = []

            peak_female = []
            mean_female = []
            median_female = []
            eighty_value_female = []

            peak_EA = []
            mean_EA = []
            median_EA = []
            eighty_value_EA = []

            for i in wb_over30.sheetnames:
                if i != 'Sheet1' and i != 'Statistical Analysis_20_Female' and i!= 'Statistical Analysis_20_Male'\
                        and i != 'Statistical Analysis over 30' and i != 'Folha1':

                    ws_over30 = wb_over30.get_sheet_by_name(i)

                    peak_30.append(ws_over30['B' + str(l)].value)
                    mean_30.append(ws_over30['C' + str(l)].value)
                    median_30.append(ws_over30['D' + str(l)].value)
                    eighty_value_30.append(ws_over30['E' + str(l)].value)

            for i in wb_20.sheetnames:
                if i != 'Sheet1' and i != 'Statistical Analysis_20_Female' and i != 'Statistical Analysis_20_Male' \
                        and i != 'Statistical Analysis over 30' and i != 'Folha1' and i != 'Patient5_Healthy' \
                        and i != 'Patient8_Healthy' and i != 'Patient10_Healthy' and i != 'Patient13_Healthy' \
                        and i != 'Patient17_Healthy' and i != 'Patient18_Healthy' and i != 'Patient23_Healthy' \
                        and i != 'Patient25_Healthy' and i != 'Patient27_Healthy' and i != 'Patient30_Healthy':
                    ws_20 = wb_20.get_sheet_by_name(i)

                    peak_female.append(ws_20['B' + str(l)].value)
                    mean_female.append(ws_20['C' + str(l)].value)
                    median_female.append(ws_20['D' + str(l)].value)
                    eighty_value_female.append(ws_20['E' + str(l)].value)

                if i == 'Patient8_Healthy' or i == 'Patient10_Healthy' or i == 'Patient13_Healthy' \
                        or i == 'Patient17_Healthy' or i == 'Patient18_Healthy' or i == 'Patient23_Healthy' \
                        or i == 'Patient25_Healthy' or i == 'Patient27_Healthy' or i == 'Patient30_Healthy' or i == 'Patient5_Healthy':

                    ws_20 = wb_20.get_sheet_by_name(i)

                    peak_male.append(ws_20['B' + str(l)].value)
                    mean_male.append(ws_20['C' + str(l)].value)
                    median_male.append(ws_20['D' + str(l)].value)
                    eighty_value_male.append(ws_20['E' + str(l)].value)

            for i in wb_EA.sheetnames:
                if i != 'Sheet1':
                    ws_EA = wb_EA.get_sheet_by_name(i)

                    peak_EA.append(ws_EA['B' + str(l)].value)
                    mean_EA.append(ws_EA['C' + str(l)].value)
                    median_EA.append(ws_EA['D' + str(l)].value)
                    eighty_value_EA.append(ws_EA['E' + str(l)].value)

            if index == 0:
                male["Rectus_L"] = {"Peak": peak_male, "Mean": mean_male, "Median": median_male,
                                          "80_freq": eighty_value_male}
                female["Rectus_L"] = {"Peak": peak_female, "Mean": mean_female, "Median": median_female,
                                          "80_freq": eighty_value_female}
                over30["Rectus_L"] = {"Peak": peak_30, "Mean": mean_30, "Median": median_30,
                                          "80_freq": eighty_value_30}
                EA["Rectus_L"] = {"Peak": peak_EA, "Mean": mean_EA, "Median": median_EA,
                                      "80_freq": eighty_value_EA}
            if index == 1:
                male["Rectus_R"] = {"Peak": peak_male, "Mean": mean_male, "Median": median_male,
                                          "80_freq": eighty_value_male}
                female["Rectus_R"] = {"Peak": peak_female, "Mean": mean_female, "Median": median_female,
                                          "80_freq": eighty_value_female}
                over30["Rectus_R"] = {"Peak": peak_30, "Mean": mean_30, "Median": median_30,
                                          "80_freq": eighty_value_30}
                EA["Rectus_R"] = {"Peak": peak_EA, "Mean": mean_EA, "Median": median_EA,
                                      "80_freq": eighty_value_EA}
            if index == 2:
                male["Obliques_L"] = {"Peak": peak_male, "Mean": mean_male, "Median": median_male,
                                            "80_freq": eighty_value_male}
                female["Obliques_L"] = {"Peak": peak_female, "Mean": mean_female, "Median": median_female,
                                            "80_freq": eighty_value_female}
                over30["Obliques_L"] = {"Peak": peak_30, "Mean": mean_30, "Median": median_30,
                                            "80_freq": eighty_value_30}
                EA["Obliques_L"] = {"Peak": peak_EA, "Mean": mean_EA, "Median": median_EA,
                                        "80_freq": eighty_value_EA}
            if index == 3:
                male["Obliques_R"] = {"Peak": peak_male, "Mean": mean_male, "Median": median_male,
                                            "80_freq": eighty_value_male}
                female["Obliques_R"] = {"Peak": peak_female, "Mean": mean_female, "Median": median_female,
                                          "80_freq": eighty_value_female}
                over30["Obliques_R"] = {"Peak": peak_30, "Mean": mean_30, "Median": median_30,
                                            "80_freq": eighty_value_30}
                EA["Obliques_R"] = {"Peak": peak_EA, "Mean": mean_EA, "Median": median_EA,
                                        "80_freq": eighty_value_EA}
            if index == 4:
                male["Ilicostalis_L"] = {"Peak": peak_male, "Mean": mean_male, "Median": median_male,
                                               "80_freq": eighty_value_male}
                female["Ilicostalis_L"] = {"Peak": peak_female, "Mean": mean_female, "Median": median_female,
                                             "80_freq": eighty_value_female}
                over30["Ilicostalis_L"] = {"Peak": peak_30, "Mean": mean_30, "Median": median_30,
                                               "80_freq": eighty_value_30}
                EA["Ilicostalis_L"] = {"Peak": peak_EA, "Mean": mean_EA, "Median": median_EA,
                                           "80_freq": eighty_value_EA}
            if index == 5:
                male["Ilicostalis_R"] = {"Peak": peak_male, "Mean": mean_male, "Median": median_male,
                                               "80_freq": eighty_value_male}
                female["Ilicostalis_R"] = {"Peak": peak_female, "Mean": mean_female, "Median": median_female,
                                             "80_freq": eighty_value_female}
                over30["Ilicostalis_R"] = {"Peak": peak_30, "Mean": mean_30, "Median": median_30,
                                               "80_freq": eighty_value_30}
                EA["Ilicostalis_R"] = {"Peak": peak_EA, "Mean": mean_EA, "Median": median_EA,
                                           "80_freq": eighty_value_EA}
            if index == 6:
                male["Multi_L"] = {"Peak": peak_male, "Mean": mean_male, "Median": median_male,
                                         "80_freq": eighty_value_male}
                female["Multi_L"] = {"Peak": peak_female, "Mean": mean_female, "Median": median_female,
                                       "80_freq": eighty_value_female}
                over30["Multi_L"] = {"Peak": peak_30, "Mean": mean_30, "Median": median_30,
                                         "80_freq": eighty_value_30}
                EA["Multi_L"] = {"Peak": peak_EA, "Mean": mean_EA, "Median": median_EA,
                                     "80_freq": eighty_value_EA}
            if index == 7:
                male["Multi_R"] = {"Peak": peak_male, "Mean": mean_male, "Median": median_male,
                                         "80_freq": eighty_value_male}
                female["Multi_R"] = {"Peak": peak_female, "Mean": mean_female, "Median": median_female,
                                       "80_freq": eighty_value_female}
                over30["Multi_R"] = {"Peak": peak_30, "Mean": mean_30, "Median": median_30,
                                         "80_freq": eighty_value_30}
                EA["Multi_R"] = {"Peak": peak_EA, "Mean": mean_EA, "Median": median_EA,
                                     "80_freq": eighty_value_EA}

            l = l + 1

        value_final_over30[task] = over30
        value_final_male[task] = male
        value_final_female[task] = female
        value_final_EA[task] = EA
        count = count + 12

    return value_final_over30, value_final_male, value_final_female, value_final_EA


def get_values_COP(mean_velocity):
    file_excel_over30 = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_over30 _final.xlsx'
    file_excel_20 = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_20-30_final.xlsx'
    file_excel_EA = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_EA1_final.xlsx'

    wb_over30 = load_workbook(file_excel_over30)
    wb_20 = load_workbook(file_excel_20)
    wb_EA = load_workbook(file_excel_EA)

    count = 8

    cop_parameters_over30 = {}
    cop_parameters_male = {}
    cop_parameters_female = {}
    cop_parameters_EA = {}

    for task in mean_velocity:

        mean_v_x_over30 = []
        mean_v_y_over30 = []
        std_x_over30 = []
        std_y_over30 = []
        amp_x_over30 = []
        amp_y_over30 = []
        area_value_over30 = []

        mean_v_x_male = []
        mean_v_y_male = []
        std_x_male = []
        std_y_male = []
        amp_x_male = []
        amp_y_male = []
        area_value_male = []

        mean_v_x_female = []
        mean_v_y_female = []
        std_x_female = []
        std_y_female = []
        amp_x_female = []
        amp_y_female = []
        area_value_female = []

        mean_v_x_EA = []
        mean_v_y_EA = []
        std_x_EA = []
        std_y_EA = []
        amp_x_EA = []
        amp_y_EA = []
        area_value_EA = []

        for i in wb_over30.sheetnames:
            if i != 'Sheet1' and i != 'Statistical Analysis_20_Female' and i != 'Statistical Analysis_20_Male' \
                    and i != 'Statistical Analysis over 30' and i != 'Folha1':
                ws_over30 = wb_over30.get_sheet_by_name(i)

                mean_v_x_over30.append(ws_over30['Q' + str(count)].value)
                mean_v_y_over30.append(ws_over30['R' + str(count)].value)
                std_x_over30.append(ws_over30['Q' + str(count + 1)].value)
                std_y_over30.append(ws_over30['R' + str(count + 1)].value)
                amp_x_over30.append(ws_over30['Q' + str(count + 2)].value)
                amp_y_over30.append(ws_over30['R' + str(count + 2)].value)
                area_value_over30.append(ws_over30['Q' + str(count + 5)].value)

        for i in wb_20.sheetnames:
            if i != 'Sheet1' and i != 'Statistical Analysis_20_Female' and i != 'Statistical Analysis_20_Male' \
                    and i != 'Statistical Analysis over 30' and i != 'Folha1' and i != 'Patient5_Healthy' \
                    and i != 'Patient8_Healthy' and i != 'Patient10_Healthy' and i != 'Patient13_Healthy' \
                    and i != 'Patient17_Healthy' and i != 'Patient18_Healthy' and i != 'Patient23_Healthy' \
                    and i != 'Patient25_Healthy' and i != 'Patient27_Healthy' and i != 'Patient30_Healthy':
                ws_20 = wb_20.get_sheet_by_name(i)

                mean_v_x_female.append(ws_20['Q' + str(count)].value)
                mean_v_y_female.append(ws_20['R' + str(count)].value)
                std_x_female.append(ws_20['Q' + str(count + 1)].value)
                std_y_female.append(ws_20['R' + str(count + 1)].value)
                amp_x_female.append(ws_20['Q' + str(count + 2)].value)
                amp_y_female.append(ws_20['R' + str(count + 2)].value)
                area_value_female.append(ws_20['Q' + str(count + 5)].value)

            if i == 'Patient8_Healthy' or i == 'Patient10_Healthy' or i == 'Patient13_Healthy' \
                    or i == 'Patient17_Healthy' or i == 'Patient18_Healthy' or i == 'Patient23_Healthy' \
                    or i == 'Patient25_Healthy' or i == 'Patient27_Healthy' or i == 'Patient30_Healthy' or i == 'Patient5_Healthy':
                ws_20 = wb_20.get_sheet_by_name(i)

                mean_v_x_male.append(ws_20['Q' + str(count)].value)
                mean_v_y_male.append(ws_20['R' + str(count)].value)
                std_x_male.append(ws_20['Q' + str(count + 1)].value)
                std_y_male.append(ws_20['R' + str(count + 1)].value)
                amp_x_male.append(ws_20['Q' + str(count + 2)].value)
                amp_y_male.append(ws_20['R' + str(count + 2)].value)
                area_value_male.append(ws_20['Q' + str(count + 5)].value)

        for i in wb_EA.sheetnames:
            if i != 'Sheet1':
                ws_EA = wb_EA.get_sheet_by_name(i)

                mean_v_x_EA.append(ws_EA['Q' + str(count)].value)
                mean_v_y_EA.append(ws_EA['R' + str(count)].value)
                std_x_EA.append(ws_EA['Q' + str(count + 1)].value)
                std_y_EA.append(ws_EA['R' + str(count + 1)].value)
                amp_x_EA.append(ws_EA['Q' + str(count + 2)].value)
                amp_y_EA.append(ws_EA['R' + str(count + 2)].value)
                area_value_EA.append(ws_EA['Q' + str(count + 5)].value)


        cop_parameters_over30[task] = {"Velocity_X": mean_v_x_over30, "Velocity_Y": mean_v_y_over30,
                                 "STD_X": std_x_over30, "STD_Y": std_y_over30,
                                 "Amp_X": amp_x_over30, "Amp_Y": amp_y_over30,
                                 "Area": area_value_over30}

        cop_parameters_male[task] = {"Velocity_X": mean_v_x_male, "Velocity_Y": mean_v_y_male,
                                       "STD_X": std_x_male, "STD_Y": std_y_male,
                                       "Amp_X": amp_x_male, "Amp_Y": amp_y_male,
                                       "Area": area_value_male}

        cop_parameters_female[task] = {"Velocity_X": mean_v_x_female, "Velocity_Y": mean_v_y_female,
                                       "STD_X": std_x_female, "STD_Y": std_y_female,
                                       "Amp_X": amp_x_female, "Amp_Y": amp_y_female,
                                       "Area": area_value_female}

        cop_parameters_EA[task] = {"Velocity_X": mean_v_x_EA, "Velocity_Y": mean_v_y_EA,
                                       "STD_X": std_x_EA, "STD_Y": std_y_EA,
                                       "Amp_X": amp_x_EA, "Amp_Y": amp_y_EA,
                                       "Area": area_value_EA}

        count = count + 13

    return cop_parameters_over30, cop_parameters_male, cop_parameters_female, cop_parameters_EA


def get_values_COP_freq(COP_freq):
    file_excel_over30 = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_over30 _final.xlsx'
    file_excel_20 = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_20-30_final.xlsx'
    file_excel_EA = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_EA1_final.xlsx'

    wb_over30 = load_workbook(file_excel_over30)
    wb_20 = load_workbook(file_excel_20)
    wb_EA = load_workbook(file_excel_EA)

    count = 260

    cop_freqs_over30 = {}
    cop_freqs_male = {}
    cop_freqs_female = {}
    cop_freqs_EA = {}

    for task in COP_freq:

        peak_over30_copx = []
        mean_over30_copx = []
        median_over30_copx = []
        eighty_over30_copx = []

        peak_over30_copy = []
        mean_over30_copy = []
        median_over30_copy = []
        eighty_over30_copy = []

        peak_male_copx = []
        mean_male_copx = []
        median_male_copx = []
        eighty_male_copx = []

        peak_male_copy = []
        mean_male_copy = []
        median_male_copy = []
        eighty_male_copy = []

        peak_female_copx = []
        mean_female_copx = []
        median_female_copx = []
        eighty_female_copx = []

        peak_female_copy = []
        mean_female_copy = []
        median_female_copy = []
        eighty_female_copy = []

        peak_EA_copx = []
        mean_EA_copx = []
        median_EA_copx = []
        eighty_EA_copx = []

        peak_EA_copy = []
        mean_EA_copy = []
        median_EA_copy = []
        eighty_EA_copy = []



        for i in wb_over30.sheetnames:
            if i != 'Sheet1' and i != 'Statistical Analysis_20_Female' and i != 'Statistical Analysis_20_Male' \
                    and i != 'Statistical Analysis over 30' and i != 'Folha1':
                ws_over30 = wb_over30.get_sheet_by_name(i)

                peak_over30_copx.append(ws_over30['K' + str(count)].value)
                peak_over30_copy.append(ws_over30['K' + str(count + 1)].value)
                mean_over30_copx.append(ws_over30['L' + str(count)].value)
                mean_over30_copy.append(ws_over30['L' + str(count + 1)].value)
                median_over30_copx.append(ws_over30['M' + str(count)].value)
                median_over30_copy.append(ws_over30['M' + str(count + 1)].value)
                eighty_over30_copx.append(ws_over30['N' + str(count)].value)
                eighty_over30_copy.append(ws_over30['N' + str(count + 1)].value)

        for i in wb_20.sheetnames:
            if i != 'Sheet1' and i != 'Statistical Analysis_20_Female' and i != 'Statistical Analysis_20_Male' \
                    and i != 'Statistical Analysis over 30' and i != 'Folha1' and i != 'Patient5_Healthy' \
                    and i != 'Patient8_Healthy' and i != 'Patient10_Healthy' and i != 'Patient13_Healthy' \
                    and i != 'Patient17_Healthy' and i != 'Patient18_Healthy' and i != 'Patient23_Healthy' \
                    and i != 'Patient25_Healthy' and i != 'Patient27_Healthy' and i != 'Patient30_Healthy':
                ws_20 = wb_20.get_sheet_by_name(i)

                peak_female_copx.append(ws_20['K' + str(count)].value)
                peak_female_copy.append(ws_20['K' + str(count + 1)].value)
                mean_female_copx.append(ws_20['L' + str(count)].value)
                mean_female_copy.append(ws_20['L' + str(count + 1)].value)
                median_female_copx.append(ws_20['M' + str(count)].value)
                median_female_copy.append(ws_20['M' + str(count + 1)].value)
                eighty_female_copx.append(ws_20['N' + str(count)].value)
                eighty_female_copy.append(ws_20['N' + str(count + 1)].value)

            if i == 'Patient8_Healthy' or i == 'Patient10_Healthy' or i == 'Patient13_Healthy' \
                    or i == 'Patient17_Healthy' or i == 'Patient18_Healthy' or i == 'Patient23_Healthy' \
                    or i == 'Patient25_Healthy' or i == 'Patient27_Healthy' or i == 'Patient30_Healthy' or i == 'Patient5_Healthy':
                ws_20 = wb_20.get_sheet_by_name(i)

                peak_male_copx.append(ws_20['K' + str(count)].value)
                peak_male_copy.append(ws_20['K' + str(count + 1)].value)
                mean_male_copx.append(ws_20['L' + str(count)].value)
                mean_male_copy.append(ws_20['L' + str(count + 1)].value)
                median_male_copx.append(ws_20['M' + str(count)].value)
                median_male_copy.append(ws_20['M' + str(count + 1)].value)
                eighty_male_copx.append(ws_20['N' + str(count)].value)
                eighty_male_copy.append(ws_20['N' + str(count + 1)].value)

        for i in wb_EA.sheetnames:
            if i != 'Sheet1':
                ws_EA = wb_EA.get_sheet_by_name(i)

                peak_EA_copx.append(ws_EA['K' + str(count)].value)
                peak_EA_copy.append(ws_EA['K' + str(count + 1)].value)
                mean_EA_copx.append(ws_EA['L' + str(count)].value)
                mean_EA_copy.append(ws_EA['L' + str(count + 1)].value)
                median_EA_copx.append(ws_EA['M' + str(count)].value)
                median_EA_copy.append(ws_EA['M' + str(count + 1)].value)
                eighty_EA_copx.append(ws_EA['N' + str(count)].value)
                eighty_EA_copy.append(ws_EA['N' + str(count + 1)].value)


        cop_freqs_over30[task] = {"Peak_X": peak_over30_copx, "Peak_Y": peak_over30_copy,
                                 "Mean_X": mean_over30_copx, "Mean_Y": mean_female_copy,
                                 "Median_X": median_over30_copx, "Median_Y": median_over30_copy,
                                 "80_X": eighty_over30_copx, "80_Y": eighty_over30_copy}

        cop_freqs_male[task] = {"Peak_X": peak_male_copx, "Peak_Y": peak_male_copy,
                                 "Mean_X": mean_male_copx, "Mean_Y": mean_male_copy,
                                 "Median_X": median_male_copx, "Median_Y": median_male_copy,
                                 "80_X": eighty_male_copx, "80_Y": eighty_male_copy}

        cop_freqs_female[task] = {"Peak_X": peak_female_copx, "Peak_Y": peak_female_copy,
                                 "Mean_X": mean_female_copx, "Mean_Y": mean_female_copy,
                                 "Median_X": median_female_copx, "Median_Y": median_female_copy,
                                 "80_X": eighty_female_copx, "80_Y": eighty_female_copy}

        cop_freqs_EA[task] = {"Peak_X": peak_EA_copx, "Peak_Y": peak_EA_copy,
                                 "Mean_X": mean_EA_copx, "Mean_Y": mean_EA_copy,
                                 "Median_X": median_EA_copx, "Median_Y": median_EA_copy,
                                 "80_X": eighty_EA_copx, "80_Y": eighty_EA_copy}

        count = count + 12

    return cop_freqs_over30, cop_freqs_male, cop_freqs_female, cop_freqs_EA



def get_value_freq_rest():
    file_excel_over30 = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_over30 _final.xlsx'
    file_excel_20 = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_20-30_final.xlsx'
    file_excel_EA = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_EA1_final.xlsx'

    wb_over30 = load_workbook(file_excel_over30)
    wb_20 = load_workbook(file_excel_20)
    wb_EA = load_workbook(file_excel_EA)

    count = 392
    over30 = {}
    male = {}
    female = {}
    EA = {}


    for index in range(0, 8):
        peak_30 = []
        mean_30 = []
        median_30 = []
        eighty_value_30 = []

        peak_male = []
        mean_male = []
        median_male = []
        eighty_value_male = []

        peak_female = []
        mean_female = []
        median_female = []
        eighty_value_female = []

        peak_EA = []
        mean_EA = []
        median_EA = []
        eighty_value_EA = []

        for i in wb_over30.sheetnames:
            if i != 'Sheet1' and i != 'Statistical Analysis_20_Female' and i!= 'Statistical Analysis_20_Male'\
                        and i != 'Statistical Analysis over 30' and i != 'Folha1':

                ws_over30 = wb_over30.get_sheet_by_name(i)
                if ws_over30['B' + str(count)].value != 'None':

                    peak_30.append(ws_over30['B' + str(count)].value)
                    mean_30.append(ws_over30['C' + str(count)].value)
                    median_30.append(ws_over30['D' + str(count)].value)
                    eighty_value_30.append(ws_over30['E' + str(count)].value)

        for i in wb_20.sheetnames:
            if i != 'Sheet1' and i != 'Statistical Analysis_20_Female' and i != 'Statistical Analysis_20_Male' \
                        and i != 'Statistical Analysis over 30' and i != 'Folha1' and i != 'Patient5_Healthy' \
                        and i != 'Patient8_Healthy' and i != 'Patient10_Healthy' and i != 'Patient13_Healthy' \
                        and i != 'Patient17_Healthy' and i != 'Patient18_Healthy' and i != 'Patient23_Healthy' \
                        and i != 'Patient25_Healthy' and i != 'Patient27_Healthy' and i != 'Patient30_Healthy':
                ws_20 = wb_20.get_sheet_by_name(i)
                if ws_20['B' + str(count)].value != 'None':

                    peak_female.append(ws_20['B' + str(count)].value)
                    mean_female.append(ws_20['C' + str(count)].value)
                    median_female.append(ws_20['D' + str(count)].value)
                    eighty_value_female.append(ws_20['E' + str(count)].value)

            if i == 'Patient8_Healthy' or i == 'Patient10_Healthy' or i == 'Patient13_Healthy' \
                        or i == 'Patient17_Healthy' or i == 'Patient18_Healthy' or i == 'Patient23_Healthy' \
                        or i == 'Patient25_Healthy' or i == 'Patient27_Healthy' or i == 'Patient30_Healthy' or i == 'Patient5_Healthy':

                ws_20 = wb_20.get_sheet_by_name(i)
                if ws_20['B' + str(count)].value != 'None':

                    peak_male.append(ws_20['B' + str(count)].value)
                    mean_male.append(ws_20['C' + str(count)].value)
                    median_male.append(ws_20['D' + str(count)].value)
                    eighty_value_male.append(ws_20['E' + str(count)].value)

        for i in wb_EA.sheetnames:
            if i != 'Sheet1':
                ws_EA = wb_EA.get_sheet_by_name(i)
                if ws_EA['B' + str(count)].value != 'None':

                    peak_EA.append(ws_EA['B' + str(count)].value)
                    mean_EA.append(ws_EA['C' + str(count)].value)
                    median_EA.append(ws_EA['D' + str(count)].value)
                    eighty_value_EA.append(ws_EA['E' + str(count)].value)

        if index == 0:
            male["Rectus_L"] = {"Peak": peak_male, "Mean": mean_male, "Median": median_male,
                                          "80_freq": eighty_value_male}
            female["Rectus_L"] = {"Peak": peak_female, "Mean": mean_female, "Median": median_female,
                                          "80_freq": eighty_value_female}
            over30["Rectus_L"] = {"Peak": peak_30, "Mean": mean_30, "Median": median_30,
                                          "80_freq": eighty_value_30}
            EA["Rectus_L"] = {"Peak": peak_EA, "Mean": mean_EA, "Median": median_EA,
                                      "80_freq": eighty_value_EA}
        if index == 1:
            male["Rectus_R"] = {"Peak": peak_male, "Mean": mean_male, "Median": median_male,
                                          "80_freq": eighty_value_male}
            female["Rectus_R"] = {"Peak": peak_female, "Mean": mean_female, "Median": median_female,
                                          "80_freq": eighty_value_female}
            over30["Rectus_R"] = {"Peak": peak_30, "Mean": mean_30, "Median": median_30,
                                          "80_freq": eighty_value_30}
            EA["Rectus_R"] = {"Peak": peak_EA, "Mean": mean_EA, "Median": median_EA,
                                      "80_freq": eighty_value_EA}
        if index == 2:
            male["Obliques_L"] = {"Peak": peak_male, "Mean": mean_male, "Median": median_male,
                                            "80_freq": eighty_value_male}
            female["Obliques_L"] = {"Peak": peak_female, "Mean": mean_female, "Median": median_female,
                                            "80_freq": eighty_value_female}
            over30["Obliques_L"] = {"Peak": peak_30, "Mean": mean_30, "Median": median_30,
                                            "80_freq": eighty_value_30}
            EA["Obliques_L"] = {"Peak": peak_EA, "Mean": mean_EA, "Median": median_EA,
                                        "80_freq": eighty_value_EA}
        if index == 3:
            male["Obliques_R"] = {"Peak": peak_male, "Mean": mean_male, "Median": median_male,
                                            "80_freq": eighty_value_male}
            female["Obliques_R"] = {"Peak": peak_female, "Mean": mean_female, "Median": median_female,
                                          "80_freq": eighty_value_female}
            over30["Obliques_R"] = {"Peak": peak_30, "Mean": mean_30, "Median": median_30,
                                            "80_freq": eighty_value_30}
            EA["Obliques_R"] = {"Peak": peak_EA, "Mean": mean_EA, "Median": median_EA,
                                        "80_freq": eighty_value_EA}
        if index == 4:
            male["Ilicostalis_L"] = {"Peak": peak_male, "Mean": mean_male, "Median": median_male,
                                               "80_freq": eighty_value_male}
            female["Ilicostalis_L"] = {"Peak": peak_female, "Mean": mean_female, "Median": median_female,
                                             "80_freq": eighty_value_female}
            over30["Ilicostalis_L"] = {"Peak": peak_30, "Mean": mean_30, "Median": median_30,
                                               "80_freq": eighty_value_30}
            EA["Ilicostalis_L"] = {"Peak": peak_EA, "Mean": mean_EA, "Median": median_EA,
                                           "80_freq": eighty_value_EA}
        if index == 5:
            male["Ilicostalis_R"] = {"Peak": peak_male, "Mean": mean_male, "Median": median_male,
                                               "80_freq": eighty_value_male}
            female["Ilicostalis_R"] = {"Peak": peak_female, "Mean": mean_female, "Median": median_female,
                                             "80_freq": eighty_value_female}
            over30["Ilicostalis_R"] = {"Peak": peak_30, "Mean": mean_30, "Median": median_30,
                                               "80_freq": eighty_value_30}
            EA["Ilicostalis_R"] = {"Peak": peak_EA, "Mean": mean_EA, "Median": median_EA,
                                           "80_freq": eighty_value_EA}
        if index == 6:
            male["Multi_L"] = {"Peak": peak_male, "Mean": mean_male, "Median": median_male,
                                         "80_freq": eighty_value_male}
            female["Multi_L"] = {"Peak": peak_female, "Mean": mean_female, "Median": median_female,
                                       "80_freq": eighty_value_female}
            over30["Multi_L"] = {"Peak": peak_30, "Mean": mean_30, "Median": median_30,
                                         "80_freq": eighty_value_30}
            EA["Multi_L"] = {"Peak": peak_EA, "Mean": mean_EA, "Median": median_EA,
                                     "80_freq": eighty_value_EA}
        if index == 7:
            male["Multi_R"] = {"Peak": peak_male, "Mean": mean_male, "Median": median_male,
                                         "80_freq": eighty_value_male}
            female["Multi_R"] = {"Peak": peak_female, "Mean": mean_female, "Median": median_female,
                                       "80_freq": eighty_value_female}
            over30["Multi_R"] = {"Peak": peak_30, "Mean": mean_30, "Median": median_30,
                                         "80_freq": eighty_value_30}
            EA["Multi_R"] = {"Peak": peak_EA, "Mean": mean_EA, "Median": median_EA,
                                     "80_freq": eighty_value_EA}

        count = count + 1


    return over30, male, female, EA


def get_value_tonus_rest():
    file_excel_over30 = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_over30 _final.xlsx'
    file_excel_20 = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_20-30_final.xlsx'
    file_excel_EA = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_EA1_final.xlsx'

    wb_over30 = load_workbook(file_excel_over30)
    wb_20 = load_workbook(file_excel_20)
    wb_EA = load_workbook(file_excel_EA)


    count = 146
    value_final_over30 = {}
    value_final_male = {}
    value_final_female = {}
    value_final_EA = {}

    value_rectus_l_over30 = []
    value_rectus_r_over30 = []
    value_obliques_l_over30 = []
    value_obliques_r_over30 = []
    value_ilicostalis_l_over30 = []
    value_ilicostalis_r_over30 = []
    value_multi_l_over30 = []
    value_multi_r_over30 = []

    value_rectus_l_female = []
    value_rectus_r_female = []
    value_obliques_l_female = []
    value_obliques_r_female = []
    value_ilicostalis_l_female = []
    value_ilicostalis_r_female = []
    value_multi_l_female = []
    value_multi_r_female = []

    value_rectus_l_male = []
    value_rectus_r_male = []
    value_obliques_l_male = []
    value_obliques_r_male = []
    value_ilicostalis_l_male = []
    value_ilicostalis_r_male = []
    value_multi_l_male = []
    value_multi_r_male = []

    value_rectus_l_EA = []
    value_rectus_r_EA = []
    value_obliques_l_EA = []
    value_obliques_r_EA = []
    value_ilicostalis_l_EA = []
    value_ilicostalis_r_EA = []
    value_multi_l_EA = []
    value_multi_r_EA = []

    for i in wb_over30.sheetnames:
        if i != 'Sheet1' and i != 'Statistical Analysis_20_Female' and i != 'Statistical Analysis_20_Male' \
                and i != 'Statistical Analysis over 30' and i != 'Folha1':
            ws_over30 = wb_over30.get_sheet_by_name(i)
            value_rectus_l_over30.append(ws_over30['B' + str(count)].value)
            value_rectus_r_over30.append(ws_over30['C' + str(count)].value)
            value_obliques_l_over30.append(ws_over30['B' + str(count + 1)].value)
            value_obliques_r_over30.append(ws_over30['C' + str(count + 1)].value)
            value_ilicostalis_l_over30.append(ws_over30['B' + str(count + 2)].value)
            value_ilicostalis_r_over30.append(ws_over30['C' + str(count + 2)].value)
            value_multi_l_over30.append(ws_over30['B' + str(count + 3)].value)
            value_multi_r_over30.append(ws_over30['C' + str(count + 3)].value)

    for i in wb_20.sheetnames:
        if i != 'Sheet1' and i != 'Statistical Analysis_20_Female' and i != 'Statistical Analysis_20_Male' \
                and i != 'Statistical Analysis over 30' and i != 'Folha1' and i != 'Patient5_Healthy' \
                and i != 'Patient8_Healthy' and i != 'Patient10_Healthy' and i != 'Patient13_Healthy' \
                and i != 'Patient17_Healthy' and i != 'Patient18_Healthy' and i != 'Patient23_Healthy' \
                and i != 'Patient25_Healthy' and i != 'Patient27_Healthy' and i != 'Patient30_Healthy':
            ws_female = wb_20.get_sheet_by_name(i)
            value_rectus_l_female.append(ws_female['B' + str(count)].value)
            value_rectus_r_female.append(ws_female['C' + str(count)].value)
            value_obliques_l_female.append(ws_female['B' + str(count + 1)].value)
            value_obliques_r_female.append(ws_female['C' + str(count + 1)].value)
            value_ilicostalis_l_female.append(ws_female['B' + str(count + 2)].value)
            value_ilicostalis_r_female.append(ws_female['C' + str(count + 2)].value)
            value_multi_l_female.append(ws_female['B' + str(count + 3)].value)
            value_multi_r_female.append(ws_female['C' + str(count + 3)].value)

        if i == 'Patient8_Healthy' or i == 'Patient10_Healthy' or i == 'Patient13_Healthy' \
                or i == 'Patient17_Healthy' or i == 'Patient18_Healthy' or i == 'Patient23_Healthy' \
                or i == 'Patient25_Healthy' or i == 'Patient27_Healthy' or i == 'Patient30_Healthy' or i == 'Patient5_Healthy':
            ws_male = wb_20.get_sheet_by_name(i)
            value_rectus_l_male.append(ws_male['B' + str(count)].value)
            value_rectus_r_male.append(ws_male['C' + str(count)].value)
            value_obliques_l_male.append(ws_male['B' + str(count + 1)].value)
            value_obliques_r_male.append(ws_male['C' + str(count + 1)].value)
            value_ilicostalis_l_male.append(ws_male['B' + str(count + 2)].value)
            value_ilicostalis_r_male.append(ws_male['C' + str(count + 2)].value)
            value_multi_l_male.append(ws_male['B' + str(count + 3)].value)
            value_multi_r_male.append(ws_male['C' + str(count + 3)].value)

    for i in wb_EA.sheetnames:
        if i != 'Sheet1':
            ws_EA = wb_EA.get_sheet_by_name(i)
            value_rectus_l_EA.append(ws_EA['B' + str(count)].value)
            value_rectus_r_EA.append(ws_EA['C' + str(count)].value)
            value_obliques_l_EA.append(ws_EA['B' + str(count + 1)].value)
            value_obliques_r_EA.append(ws_EA['C' + str(count + 1)].value)
            value_ilicostalis_l_EA.append(ws_EA['B' + str(count + 2)].value)
            value_ilicostalis_r_EA.append(ws_EA['C' + str(count + 2)].value)
            value_multi_l_EA.append(ws_EA['B' + str(count + 3)].value)
            value_multi_r_EA.append(ws_EA['C' + str(count + 3)].value)


    value_final_over30 = {"Rectus_L": value_rectus_l_over30, "Rectus_R": value_rectus_r_over30,
                                "Obliques_L": value_obliques_l_over30,
                                "Obliques_R": value_obliques_r_over30, "Ilicostalis_L": value_ilicostalis_l_over30,
                                "Ilicostalis_R": value_ilicostalis_r_over30,
                                "Multifidus_L": value_multi_l_over30, "Multifidus_R": value_multi_r_over30}

    value_final_male = {"Rectus_L": value_rectus_l_male, "Rectus_R": value_rectus_r_male,
                              "Obliques_L": value_obliques_l_male,
                              "Obliques_R": value_obliques_r_male, "Ilicostalis_L": value_ilicostalis_l_male,
                              "Ilicostalis_R": value_ilicostalis_r_male,
                              "Multifidus_L": value_multi_l_male, "Multifidus_R": value_multi_r_male}

    value_final_female = {"Rectus_L": value_rectus_l_female, "Rectus_R": value_rectus_r_female,
                                "Obliques_L": value_obliques_l_female,
                                "Obliques_R": value_obliques_r_female, "Ilicostalis_L": value_ilicostalis_l_female,
                                "Ilicostalis_R": value_ilicostalis_r_female,
                                "Multifidus_L": value_multi_l_female, "Multifidus_R": value_multi_r_female}

    value_final_EA = {"Rectus_L": value_rectus_l_EA, "Rectus_R": value_rectus_r_EA,
                            "Obliques_L": value_obliques_l_EA,
                            "Obliques_R": value_obliques_r_EA, "Ilicostalis_L": value_ilicostalis_l_EA,
                            "Ilicostalis_R": value_ilicostalis_r_EA,
                            "Multifidus_L": value_multi_l_EA, "Multifidus_R": value_multi_r_EA}


    return value_final_over30, value_final_male, value_final_female, value_final_EA