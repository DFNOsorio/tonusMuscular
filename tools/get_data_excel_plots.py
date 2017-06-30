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





