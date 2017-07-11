from tools import *
import xlsxwriter
import xlrd
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter, column_index_from_string
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

    count = 430
    value_final_over30 = {}
    value_final_male = {}
    value_final_female = {}
    value_final_EA_over30 = {}
    value_final_EA_evoluted = {}

    for task in EMG_array:
        over30 = {}
        female = {}
        male = {}
        EA_over30 = {}
        EA_evoluted = {}

        col_value = 18


        for index in range(0, 8):
            EMG_evolution_over30 = []
            EMG_evolution_male = []
            EMG_evolution_female = []
            EMG_evolution_EA_over30 = []
            EMG_evolution_EA_evol = []
            l = count


            ws_over30 = wb_over30.get_sheet_by_name('Statistical Analysis over 30')
            ws_20_male = wb_20.get_sheet_by_name('Statistical Analysis_20_Male')
            ws_20_female = wb_20.get_sheet_by_name('Statistical Analysis_20_Female')
            ws_EA_over30 = wb_EA.get_sheet_by_name('Statistical Analysis - EA over3')
            ws_EA_evoluted = wb_EA.get_sheet_by_name('Statistical Analysis - EA evol')


            for row in range(0,12):

                if ws_over30.cell(row= l, column= col_value).value != None:
                    EMG_evolution_over30.append(ws_over30.cell(row= l, column= col_value).value)
                if ws_20_male.cell(row= l, column= col_value).value != None:
                    EMG_evolution_male.append(ws_20_male.cell(row= l, column= col_value).value)
                if ws_20_female.cell(row= l, column= col_value).value != None:
                    EMG_evolution_female.append(ws_20_female.cell(row= l, column= col_value).value)
                if ws_EA_over30.cell(row= l, column= col_value).value != None:
                    EMG_evolution_EA_over30.append(ws_EA_over30.cell(row= l, column= col_value).value)
                if ws_EA_evoluted.cell(row= l, column= col_value).value != None:
                    EMG_evolution_EA_evol.append(ws_EA_evoluted.cell(row= l, column= col_value).value)
                l = l + 1

            if index == 0:
                male["Rectus_L"]        = EMG_evolution_male
                female["Rectus_L"]      = EMG_evolution_female
                over30["Rectus_L"]      = EMG_evolution_over30
                EA_over30["Rectus_L"]   = EMG_evolution_EA_over30
                EA_evoluted["Rectus_L"] = EMG_evolution_EA_evol

            if index == 1:
                male["Rectus_R"] = EMG_evolution_male
                female["Rectus_R"] = EMG_evolution_female
                over30["Rectus_R"] = EMG_evolution_over30
                EA_over30["Rectus_R"] = EMG_evolution_EA_over30
                EA_evoluted["Rectus_R"] = EMG_evolution_EA_evol

            if index == 2:
                male["Obliques_L"] = EMG_evolution_male
                female["Obliques_L"] = EMG_evolution_female
                over30["Obliques_L"] = EMG_evolution_over30
                EA_over30["Obliques_L"] = EMG_evolution_EA_over30
                EA_evoluted["Obliques_L"] = EMG_evolution_EA_evol

            if index == 3:
                male["Obliques_R"] = EMG_evolution_male
                female["Obliques_R"] = EMG_evolution_female
                over30["Obliques_R"] = EMG_evolution_over30
                EA_over30["Obliques_R"] = EMG_evolution_EA_over30
                EA_evoluted["Obliques_R"] = EMG_evolution_EA_evol

            if index == 4:
                male["Ilicostalis_L"] = EMG_evolution_male
                female["Ilicostalis_L"] = EMG_evolution_female
                over30["Ilicostalis_L"] = EMG_evolution_over30
                EA_over30["Ilicostalis_L"] = EMG_evolution_EA_over30
                EA_evoluted["Ilicostalis_L"] = EMG_evolution_EA_evol

            if index == 5:
                male["Ilicostalis_R"] = EMG_evolution_male
                female["Ilicostalis_R"] = EMG_evolution_female
                over30["Ilicostalis_R"] = EMG_evolution_over30
                EA_over30["Ilicostalis_R"] = EMG_evolution_EA_over30
                EA_evoluted["Ilicostalis_R"] = EMG_evolution_EA_evol

            if index == 6:
                male["Multi_L"] = EMG_evolution_male
                female["Multi_L"] = EMG_evolution_female
                over30["Multi_L"] = EMG_evolution_over30
                EA_over30["Multi_L"] = EMG_evolution_EA_over30
                EA_evoluted["Multi_L"] = EMG_evolution_EA_evol

            if index == 7:
                male["Multi_R"] = EMG_evolution_male
                female["Multi_R"] = EMG_evolution_female
                over30["Multi_R"] = EMG_evolution_over30
                EA_over30["Multi_R"] = EMG_evolution_EA_over30
                EA_evoluted["Multi_R"] = EMG_evolution_EA_evol

            col_value = col_value + 2

        value_final_over30[task] = over30
        value_final_male[task] = male
        value_final_female[task] = female
        value_final_EA_over30[task] = EA_over30
        value_final_EA_evoluted[task] = EA_evoluted
        count = count + 23

    return value_final_over30, value_final_male, value_final_female, value_final_EA_over30, value_final_EA_evoluted


def get_COP_evolution(EMG_array):
    file_excel_over30 = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_over30 _final.xlsx'
    file_excel_20 = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_20-30_final.xlsx'
    file_excel_EA = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_EA1_final.xlsx'

    wb_over30 = load_workbook(file_excel_over30)
    wb_20 = load_workbook(file_excel_20)
    wb_EA = load_workbook(file_excel_EA)

    count = 431
    value_final_over30 = {}
    value_final_male = {}
    value_final_female = {}
    value_final_EA_over30 = {}
    value_final_EA_evoluted = {}

    for task in EMG_array:
        over30 = {}
        female = {}
        male = {}
        EA_over30 = {}
        EA_evoluted = {}

        col_value = 2

        for index in range(0, 4):
            EMG_evolution_over30 = []
            EMG_evolution_male = []
            EMG_evolution_female = []
            EMG_evolution_EA_over30 = []
            EMG_evolution_EA_evol = []
            l = count

            ws_over30 = wb_over30.get_sheet_by_name('Statistical Analysis over 30')
            ws_20_male = wb_20.get_sheet_by_name('Statistical Analysis_20_Male')
            ws_20_female = wb_20.get_sheet_by_name('Statistical Analysis_20_Female')
            ws_EA_over30 = wb_EA.get_sheet_by_name('Statistical Analysis - EA over3')
            ws_EA_evoluted = wb_EA.get_sheet_by_name('Statistical Analysis - EA evol')

            for row in range(0, 12):

                if ws_over30.cell(row=l, column=col_value).value != None:
                    EMG_evolution_over30.append(ws_over30.cell(row=l, column=col_value).value)
                if ws_20_male.cell(row=l, column=col_value).value != None:
                    EMG_evolution_male.append(ws_20_male.cell(row=l, column=col_value).value)
                if ws_20_female.cell(row=l, column=col_value).value != None:
                    EMG_evolution_female.append(ws_20_female.cell(row=l, column=col_value).value)
                if ws_EA_over30.cell(row=l, column=col_value).value != None:
                    EMG_evolution_EA_over30.append(ws_EA_over30.cell(row=l, column=col_value).value)
                if ws_EA_evoluted.cell(row=l, column=col_value).value != None:
                    EMG_evolution_EA_evol.append(ws_EA_evoluted.cell(row=l, column=col_value).value)
                l = l + 1


            if index == 0:
                male["STD_X"] = EMG_evolution_male
                female["STD_X"] = EMG_evolution_female
                over30["STD_X"] = EMG_evolution_over30
                EA_over30["STD_X"] = EMG_evolution_EA_over30
                EA_evoluted["STD_X"] = EMG_evolution_EA_evol

            if index == 1:
                male["Vel_X"] = EMG_evolution_male
                female["Vel_X"] = EMG_evolution_female
                over30["Vel_X"] = EMG_evolution_over30
                EA_over30["Vel_X"] = EMG_evolution_EA_over30
                EA_evoluted["Vel_X"] = EMG_evolution_EA_evol

            if index == 2:
                male["STD_Y"] = EMG_evolution_male
                female["STD_Y"] = EMG_evolution_female
                over30["STD_Y"] = EMG_evolution_over30
                EA_over30["STD_Y"] = EMG_evolution_EA_over30
                EA_evoluted["STD_Y"] = EMG_evolution_EA_evol

            if index == 3:
                male["Vel_Y"] = EMG_evolution_male
                female["Vel_Y"] = EMG_evolution_female
                over30["Vel_Y"] = EMG_evolution_over30
                EA_over30["Vel_Y"] = EMG_evolution_EA_over30
                EA_evoluted["Vel_Y"] = EMG_evolution_EA_evol

            col_value = col_value + 2

        value_final_over30[task] = over30
        value_final_male[task] = male
        value_final_female[task] = female
        value_final_EA_over30[task] = EA_over30
        value_final_EA_evoluted[task] = EA_evoluted
        count = count + 23

    return value_final_over30, value_final_male, value_final_female, value_final_EA_over30, value_final_EA_evoluted


def get_evolution_area(area_array):
    file_excel_over30 = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_over30 _final.xlsx'
    file_excel_20 = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_20-30_final.xlsx'
    file_excel_EA = 'C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/database_posturography_EA1_final.xlsx'

    wb_over30 = load_workbook(file_excel_over30)
    wb_20 = load_workbook(file_excel_20)
    wb_EA = load_workbook(file_excel_EA)

    count = 430
    value_final_over30 = {}
    value_final_male = {}
    value_final_female = {}
    value_final_EA_over30 = {}
    value_final_EA_evoluted = {}

    for task in area_array:


        col_value = 13


        area_evolution_over30 = []
        area_evolution_male = []
        area_evolution_female = []
        area_evolution_EA_over30 = []
        area_evolution_EA_evol = []
        l = count

        ws_over30 = wb_over30.get_sheet_by_name('Statistical Analysis over 30')
        ws_20_male = wb_20.get_sheet_by_name('Statistical Analysis_20_Male')
        ws_20_female = wb_20.get_sheet_by_name('Statistical Analysis_20_Female')
        ws_EA_over30 = wb_EA.get_sheet_by_name('Statistical Analysis - EA over3')
        ws_EA_evoluted = wb_EA.get_sheet_by_name('Statistical Analysis - EA evol')

        for row in range(0, 12):

            if ws_over30.cell(row=l, column=col_value).value != None:
                area_evolution_over30.append(ws_over30.cell(row=l, column=col_value).value)
            if ws_20_male.cell(row=l, column=col_value).value != None:
                area_evolution_male.append(ws_20_male.cell(row=l, column=col_value).value)
            if ws_20_female.cell(row=l, column=col_value).value != None:
                area_evolution_female.append(ws_20_female.cell(row=l, column=col_value).value)
            if ws_EA_over30.cell(row=l, column=col_value).value != None:
                area_evolution_EA_over30.append(ws_EA_over30.cell(row=l, column=col_value).value)
            if ws_EA_evoluted.cell(row=l, column=col_value).value != None:
                area_evolution_EA_evol.append(ws_EA_evoluted.cell(row=l, column=col_value).value)
            l = l + 1

        value_final_over30[task] = area_evolution_over30
        value_final_male[task] = area_evolution_male
        value_final_female[task] = area_evolution_female
        value_final_EA_over30[task] = area_evolution_EA_over30
        value_final_EA_evoluted[task] = area_evolution_EA_evol
        count = count + 23

    return value_final_over30, value_final_male, value_final_female, value_final_EA_over30, value_final_EA_evoluted

