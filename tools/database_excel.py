import h5py
import xlsxwriter
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from openpyxl.styles import PatternFill
import numpy as np
from tools import *
#from openpyxl.worksheet.table import Table, TableStyleInfo

file_excel = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/demo.xlsx'
patient = 'Patient1_Healthy'

def create_database():
    workbook = xlsxwriter.Workbook('C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/demo.xlsx')

def personal_data(file_name):
    file = h5py.File(file_name, 'r')

    wb2 = load_workbook(file_excel)
    sheet1 = wb2.create_sheet(patient)

    fill = PatternFill(start_color='000080', end_color='000080', fill_type='solid')

    A1 = sheet1.cell('A1')
    A1.value = "Gender"
    A1.font = A1.font.copy(bold=True)
    A1.fill = fill

    A2 = sheet1.cell('A2')
    A2.value = "Age"
    A2.font = A2.font.copy(bold=True)
    A2.fill = fill

    A3 = sheet1.cell('A3')
    A3.value = "Condition"
    A3.font = A3.font.copy(bold=True)
    A3.fill = fill

    A4 = sheet1.cell('A4')
    A4.value = "Director's Hand"
    A4.font = A4.font.copy(bold=True)
    A4.fill = fill



    B1 = sheet1.cell('B1')
    B1.value = file.attrs.values()[1]
    B1.alignment = Alignment(horizontal='center', vertical='center')

    B2 = sheet1.cell('B2')
    B2.value = file.attrs.values()[2]
    B2.alignment = Alignment(horizontal='center', vertical='center')

    B3 = sheet1.cell('B3')
    B3.value = file.attrs.values()[3]
    B3.alignment = Alignment(horizontal='center', vertical='center')

    B4 = sheet1.cell('B4')
    B4.value = "Right"
    B4.alignment = Alignment(horizontal='center', vertical='center')


    wb2.save(file_excel)


def parameters(EMG_values):
    wb2 = load_workbook(file_excel)
    sheet1 = wb2.get_sheet_by_name(patient)
    count = 6
    for i in EMG_values:
        title = sheet1.cell('B' + str(count))
        title.value = "Max values of each muscle - " + str(i)
        title.font = title.font.copy(bold=True)
        data = [['Rectus_A', EMG_values[i][0], EMG_values[i][1]],
                ['Obliques', EMG_values[i][2], EMG_values[i][3]],
                ['Ilicostalis', EMG_values[i][4], EMG_values[i][5]],
                ['Multifidus',  EMG_values[i][6], EMG_values[i][7]]
        ]
        first_row = sheet1.append([" ", "Left", "Right"])

        for row in data:
            sheet1.append(row)

        count = count + 13
    wb2.save(file_excel)

def coherency(coherency_values):
    wb2 = load_workbook(file_excel)
    sheet1 = wb2.get_sheet_by_name(patient)

    fill = PatternFill(start_color='BCC2BC', end_color='BCC2BC', fill_type='solid')

    count = 6
    count1 = 7
    count2 = 8
    count_col = 8
    for i in coherency_values:
        title = sheet1.cell('H' + str(count))
        title.value = "Coherency values between each muscle and each COP direction - " + str(i)
        title.font = title.font.copy(bold=True)

        first_col = sheet1.cell('H' + str(count1))
        first_col.value = ''
        first_col.font = first_col.font.copy(bold=True)
        first_col.fill = fill

        second_col = sheet1.cell('I' + str(count1))
        second_col.value = 'COP X'
        second_col.font = second_col.font.copy(bold=True)
        second_col.fill = fill

        third_col = sheet1.cell('J' + str(count1))
        third_col.value = 'COP Y'
        third_col.font = third_col.font.copy(bold=True)
        third_col.fill = fill

        first_row = sheet1.cell('H' + str(count1+1))
        first_row.value = 'Rectus_A_L'
        first_row.font = first_row.font.copy(bold=True)
        first_row.fill = fill

        second_row = sheet1.cell('H' + str(count1 + 2))
        second_row.value = 'Obliques_L'
        second_row.font = second_row.font.copy(bold=True)
        second_row.fill = fill

        third_row = sheet1.cell('H' + str(count1 + 3))
        third_row.value = 'Ilicostalis_L'
        third_row.font = third_row.font.copy(bold=True)
        third_row.fill = fill

        fourth_row = sheet1.cell('H' + str(count1 + 4))
        fourth_row.value = 'Multifidus_L'
        fourth_row.font = fourth_row.font.copy(bold=True)
        fourth_row.fill = fill

        fifth_row = sheet1.cell('H' + str(count1 + 5))
        fifth_row.value = 'Rectus_A_R'
        fifth_row.font = fifth_row.font.copy(bold=True)
        fifth_row.fill = fill

        sixth_row = sheet1.cell('H' + str(count1 + 6))
        sixth_row.value = 'Obliques_R'
        sixth_row.font = sixth_row.font.copy(bold=True)
        sixth_row.fill = fill

        seventh_row = sheet1.cell('H' + str(count1 + 7))
        seventh_row.value = 'Ilicostalis_R'
        seventh_row.font = seventh_row.font.copy(bold=True)
        seventh_row.fill = fill

        eigth_row = sheet1.cell('H' + str(count1 + 8))
        eigth_row.value = 'Multifidus_R'
        eigth_row.font = eigth_row.font.copy(bold=True)
        eigth_row.fill = fill


        data = [[np.max(coherency_values[i]["coherency_x"][0:40, 0]),  np.max(coherency_values[i]["coherency_y"][0:40, 0])],
                [np.max(coherency_values[i]["coherency_x"][0:40, 2]),  np.max(coherency_values[i]["coherency_y"][0:40, 2])],
                [np.max(coherency_values[i]["coherency_x"][0:40, 4]),  np.max(coherency_values[i]["coherency_y"][0:40, 4])],
                [np.max(coherency_values[i]["coherency_x"][0:40, 6]),  np.max(coherency_values[i]["coherency_y"][0:40, 6])],
                [np.max(coherency_values[i]["coherency_x"][0:40, 1]),  np.max(coherency_values[i]["coherency_y"][0:40, 1])],
                [np.max(coherency_values[i]["coherency_x"][0:40, 3]),  np.max(coherency_values[i]["coherency_y"][0:40, 3])],
                [np.max(coherency_values[i]["coherency_x"][0:40, 5]),  np.max(coherency_values[i]["coherency_y"][0:40, 5])],
                [np.max(coherency_values[i]["coherency_x"][0:40, 7]),  np.max(coherency_values[i]["coherency_y"][0:40, 7])]
                ]

        for row in data:
            sheet1.cell(row= count2, column= count_col + 1, value= row[0])
            sheet1.cell(row= count2, column= count_col + 2, value= row[1])
            count2 = count2 + 1

        count = count + 13
        count1 = count1 + 13
        count2 = (count2-1) + 6
    wb2.save(file_excel)

def COP_parameters (mean_velocity, platform_COP):
    wb2 = load_workbook(file_excel)
    sheet1 = wb2.get_sheet_by_name(patient)

    fill = PatternFill(start_color='BCC2BC', end_color='BCC2BC', fill_type='solid')

    count = 6
    count1 = 7

    for i in mean_velocity:
        title = sheet1.cell('P' + str(count))
        title.value = "COP important values - " + str(i)
        title.font = title.font.copy(bold=True)

        first_col = sheet1.cell('P' + str(count1))
        first_col.value = ''
        first_col.font = first_col.font.copy(bold=True)
        first_col.fill = fill

        second_col = sheet1.cell('Q' + str(count1))
        second_col.value = 'COP X'
        second_col.font = second_col.font.copy(bold=True)
        second_col.fill = fill

        third_col = sheet1.cell('R' + str(count1))
        third_col.value = 'COP Y'
        third_col.font = third_col.font.copy(bold=True)
        third_col.fill = fill

        first_row = sheet1.cell('P' + str(count1 + 1))
        first_row.value = 'Mean Velocity'
        first_row.font = first_row.font.copy(bold=True)
        first_row.fill = fill

        velocity_x = sheet1.cell('Q' + str(count1+1))
        velocity_x.value = mean_velocity[i]["COP_X"]

        velocity_y = sheet1.cell('R' + str(count1+1))
        velocity_y.value = mean_velocity[i]["COP_Y"]

        area_traj = convex_hull(platform_COP[i]["COP_X"], platform_COP[i]["COP_Y"])
        area_value = area_calc(area_traj)

        area = sheet1.cell('P' + str(count1 + 3))
        area.value = "Area COP"
        area.font = area.font.copy(bold=True)
        area.fill = fill

        area_val = sheet1.cell(('Q' + str(count1 + 3)))
        area_val.value = area_value


        count = count + 13
        count1 = count1 + 13

    wb2.save(file_excel)


def correlation_RL(correlation_RL):
    wb2 = load_workbook(file_excel)
    sheet1 = wb2.get_sheet_by_name(patient)

    fill = PatternFill(start_color='FF6600', end_color='FF6600', fill_type='solid')
    header = sheet1.cell('A151')
    header.value = "Correlation values between EMG, COP, velocity and accelaration"
    header.font = header.font.copy(bold=True)

    RL_description1 = sheet1.cell('A154')
    RL_description1.value = "**EMG data - Right muscle minus left muscle. Correlation between EMG data,"

    RL_description1 = sheet1.cell('A155')
    RL_description1.value = " COP in X direction, velocity in X direction and accelaration in X direction."

    count = 158
    count1 = 160
    count_col = 2

    for i in correlation_RL:
        title = sheet1.cell('A' + str(count))
        title.value = "Correlation values - " + str(i)
        title.font = title.font.copy(bold=True)

        first_col = sheet1.cell('A' + str(count + 1))
        first_col.value = ''
        first_col.font = first_col.font.copy(bold=True)
        first_col.fill = fill

        second_col = sheet1.cell('B' + str(count + 1))
        second_col.value = 'COP X'
        second_col.font = second_col.font.copy(bold=True)
        second_col.fill = fill

        third_col = sheet1.cell('C' + str(count + 1))
        third_col.value = 'Velocity X'
        third_col.font = third_col.font.copy(bold=True)
        third_col.fill = fill

        fourth_col = sheet1.cell('D' + str(count + 1))
        fourth_col.value = 'Acelaration X'
        fourth_col.font = fourth_col.font.copy(bold=True)
        fourth_col.fill = fill

        first_row = sheet1.cell('A' + str(count + 2))
        first_row.value = 'Rectus_A'
        first_row.font = first_row.font.copy(bold=True)
        first_row.fill = fill

        second_row = sheet1.cell('A' + str(count + 3))
        second_row.value = 'Obliques'
        second_row.font = second_row.font.copy(bold=True)
        second_row.fill = fill

        third_row = sheet1.cell('A' + str(count + 4))
        third_row.value = 'Ilicostalis'
        third_row.font = third_row.font.copy(bold=True)
        third_row.fill = fill

        fourth_row = sheet1.cell('A' + str(count + 5))
        fourth_row.value = 'Multifidus'
        fourth_row.font = fourth_row.font.copy(bold=True)
        fourth_row.fill = fill

        data = [[correlation_RL[i]["RA_corr"]["RA_COP"], correlation_RL[i]["RA_corr"]["RA_vel"], correlation_RL[i]["RA_corr"]["RA_acel"]],
                [correlation_RL[i]["O_corr"]["O_COP"], correlation_RL[i]["O_corr"]["O_vel"], correlation_RL[i]["O_corr"]["O_acel"]],
                [correlation_RL[i]["I_corr"]["I_COP"], correlation_RL[i]["I_corr"]["I_vel"], correlation_RL[i]["I_corr"]["I_acel"]],
                [correlation_RL[i]["M_corr"]["M_COP"], correlation_RL[i]["M_corr"]["M_vel"], correlation_RL[i]["M_corr"]["M_acel"]]
                ]

        for row in data:
            sheet1.cell(row = count1, column = count_col, value = row[0])
            sheet1.cell(row = count1, column = count_col + 1, value = row[1])
            sheet1.cell(row = count1, column = count_col + 2, value = row[2])
            count1 = count1 + 1

        count = count + 8
        count1 = (count1 - 1) + 5

    wb2.save(file_excel)

def correlation_FB(correlation_FB):
    wb2 = load_workbook(file_excel)
    sheet1 = wb2.get_sheet_by_name(patient)

    fill = PatternFill(start_color='FF6600', end_color='FF6600', fill_type='solid')

    FB_description1 = sheet1.cell('H154')
    FB_description1.value = "**EMG data - Front muscle minus back muscle. Correlation between EMG data,"

    FB_description1 = sheet1.cell('H155')
    FB_description1.value = " COP in Y direction, velocity in Y direction and accelaration in Y direction."

    count = 158
    count1 = 160
    count_col = 9

    for i in correlation_FB:
        title = sheet1.cell('H' + str(count))
        title.value = "Correlation values - " + str(i)
        title.font = title.font.copy(bold=True)

        first_col = sheet1.cell('H' + str(count + 1))
        first_col.value = ''
        first_col.font = first_col.font.copy(bold=True)
        first_col.fill = fill

        second_col = sheet1.cell('I' + str(count + 1))
        second_col.value = 'COP Y'
        second_col.font = second_col.font.copy(bold=True)
        second_col.fill = fill

        third_col = sheet1.cell('J' + str(count + 1))
        third_col.value = 'Velocity Y'
        third_col.font = third_col.font.copy(bold=True)
        third_col.fill = fill

        fourth_col = sheet1.cell('K' + str(count + 1))
        fourth_col.value = 'Acelaration Y'
        fourth_col.font = fourth_col.font.copy(bold=True)
        fourth_col.fill = fill

        first_row = sheet1.cell('H' + str(count + 2))
        first_row.value = 'R-M_L'
        first_row.font = first_row.font.copy(bold=True)
        first_row.fill = fill

        second_row = sheet1.cell('H' + str(count + 3))
        second_row.value = 'R-M_R'
        second_row.font = second_row.font.copy(bold=True)
        second_row.fill = fill

        third_row = sheet1.cell('H' + str(count + 4))
        third_row.value = 'O-I_L'
        third_row.font = third_row.font.copy(bold=True)
        third_row.fill = fill

        fourth_row = sheet1.cell('H' + str(count + 5))
        fourth_row.value = 'O-I_R'
        fourth_row.font = fourth_row.font.copy(bold=True)
        fourth_row.fill = fill

        data = [[correlation_FB[i]["MR_L_corr"]["MR_L_COP"], correlation_FB[i]["MR_L_corr"]["MR_L_vel"], correlation_FB[i]["MR_L_corr"]["MR_L_acel"]],
                [correlation_FB[i]["MR_R_corr"]["MR_R_COP"], correlation_FB[i]["MR_R_corr"]["MR_R_vel"], correlation_FB[i]["MR_R_corr"]["MR_R_acel"]],
                [correlation_FB[i]["IO_L_corr"]["IO_L_COP"], correlation_FB[i]["IO_L_corr"]["IO_L_vel"], correlation_FB[i]["IO_L_corr"]["IO_L_acel"]],
                [correlation_FB[i]["IO_R_corr"]["IO_R_COP"], correlation_FB[i]["IO_R_corr"]["IO_R_vel"], correlation_FB[i]["IO_R_corr"]["IO_R_acel"]]
                ]

        for row in data:
            sheet1.cell(row = count1, column = count_col, value = row[0])
            sheet1.cell(row = count1, column = count_col + 1, value = row[1])
            sheet1.cell(row = count1, column = count_col + 2, value = row[2])

            count1 = count1 + 1

        count = count + 8
        count1 = count1 + 4

    wb2.save(file_excel)

def correlation_FB_cross(correlation_FB_cross):
    wb2 = load_workbook(file_excel)
    sheet1 = wb2.get_sheet_by_name(patient)

    fill = PatternFill(start_color='FF6600', end_color='FF6600', fill_type='solid')

    FB_description1 = sheet1.cell('O154')
    FB_description1.value = "**EMG data - Front muscle minus back muscle in cross direction. Correlation between EMG data,"

    FB_description1 = sheet1.cell('O155')
    FB_description1.value = " COP in Y direction, velocity in Y direction and accelaration in Y direction."

    count = 158
    count1 = 160
    count_col = 16

    for i in correlation_FB_cross:
        title = sheet1.cell('O' + str(count))
        title.value = "Correlation values - " + str(i)
        title.font = title.font.copy(bold=True)

        first_col = sheet1.cell('O' + str(count + 1))
        first_col.value = ''
        first_col.font = first_col.font.copy(bold=True)
        first_col.fill = fill

        second_col = sheet1.cell('P' + str(count + 1))
        second_col.value = 'COP X'
        second_col.font = second_col.font.copy(bold=True)
        second_col.fill = fill

        third_col = sheet1.cell('Q' + str(count + 1))
        third_col.value = 'COP Y'
        third_col.font = third_col.font.copy(bold=True)
        third_col.fill = fill

        first_row = sheet1.cell('O' + str(count + 2))
        first_row.value = 'RL-MR'
        first_row.font = first_row.font.copy(bold=True)
        first_row.fill = fill

        second_row = sheet1.cell('O' + str(count + 3))
        second_row.value = 'RR-LM'
        second_row.font = second_row.font.copy(bold=True)
        second_row.fill = fill

        third_row = sheet1.cell('O' + str(count + 4))
        third_row.value = 'OL-IR'
        third_row.font = third_row.font.copy(bold=True)
        third_row.fill = fill

        fourth_row = sheet1.cell('O' + str(count + 5))
        fourth_row.value = 'OR-IL'
        fourth_row.font = fourth_row.font.copy(bold=True)
        fourth_row.fill = fill

        data = [[correlation_FB_cross[i]["MR_LR_corr"]["MR_LR_COP_X"], correlation_FB_cross[i]["MR_LR_corr"]["MR_LR_COP_Y"]],
                [correlation_FB_cross[i]["MR_RL_corr"]["MR_RL_COP_X"], correlation_FB_cross[i]["MR_RL_corr"]["MR_RL_COP_Y"]],
                [correlation_FB_cross[i]["IO_LR_corr"]["IO_LR_COP_X"], correlation_FB_cross[i]["IO_LR_corr"]["IO_LR_COP_Y"]],
                [correlation_FB_cross[i]["IO_RL_corr"]["IO_RL_COP_X"], correlation_FB_cross[i]["IO_RL_corr"]["IO_RL_COP_Y"]]
                ]

        for row in data:
            sheet1.cell(row = count1, column = count_col, value = row[0])
            sheet1.cell(row = count1, column = count_col + 1, value = row[1])

            count1 = count1 + 1

        count = count + 8
        count1 = count1 + 4

    wb2.save(file_excel)

