import h5py
import xlsxwriter
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from openpyxl.styles import PatternFill
import numpy as np
#from openpyxl.worksheet.table import Table, TableStyleInfo


def create_database():
    workbook = xlsxwriter.Workbook('C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/demo.xlsx')

def personal_data(file_name):
    file = h5py.File(file_name, 'r')

    wb2 = load_workbook('C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/demo.xlsx')
    sheet1 = wb2.create_sheet('Patient1_Healthy')

    fill = PatternFill(start_color='BCC2BC', end_color='BCC2BC', fill_type='solid')

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


    wb2.save('C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/demo.xlsx')


def parameters(EMG_values):
    wb2 = load_workbook('C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/demo.xlsx')
    sheet1 = wb2.get_sheet_by_name('Patient1_Healthy')
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
    wb2.save('C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/demo.xlsx')

def coherency(coherency_values):
    wb2 = load_workbook('C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/demo.xlsx')
    sheet1 = wb2.get_sheet_by_name('Patient1_Healthy')
    count = 6
    for i in coherency_values:
        title = sheet1.cell('H' + str(count))
        title.value = "Coherency values between each muscle and each COP direction - " + str(i)
        title.font = title.font.copy(bold=True)
        data = [['Rectus_A_L', np.max(coherency_values[i]["coherency_x"][0:40, 0]),  np.max(coherency_values[i]["coherency_y"][0:40, 0])],
                ['Obliques_L', np.max(coherency_values[i]["coherency_x"][0:40, 0]),  np.max(coherency_values[i]["coherency_y"][0:40, 0])],
                ['Ilicostalis_L', np.max(coherency_values[i]["coherency_x"][0:40, 0]),  np.max(coherency_values[i]["coherency_y"][0:40, 0])],
                ['Multifidus_L', np.max(coherency_values[i]["coherency_x"][0:40, 0]),  np.max(coherency_values[i]["coherency_y"][0:40, 0])],
                ['Rectus_A_R', np.max(coherency_values[i]["coherency_x"][0:40, 0]),  np.max(coherency_values[i]["coherency_y"][0:40, 0])],
                ['Obliques_R', np.max(coherency_values[i]["coherency_x"][0:40, 0]),  np.max(coherency_values[i]["coherency_y"][0:40, 0])],
                ['Ilicostalis_R', np.max(coherency_values[i]["coherency_x"][0:40, 0]),  np.max(coherency_values[i]["coherency_y"][0:40, 0])],
                ['Multifidus_L', np.max(coherency_values[i]["coherency_x"][0:40, 0]),  np.max(coherency_values[i]["coherency_y"][0:40, 0])]
                ]
        first_row = sheet1.append([" ", "COP X", "COP Y"])

        for row in data:
            sheet1.append(row)
        count = count + 13
    wb2.save('C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/demo.xlsx')



