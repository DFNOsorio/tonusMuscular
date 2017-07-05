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


    count = 410
    value_final_over30 = {}
    value_final_male = {}
    value_final_female = {}
    value_final_EA = {}

    value_STDX_over30 = {}
    value_STDX_male = {}
    value_STDX_female = {}
    value_STDX_EA = {}

    value_STDY_over30 = {}
    value_STDY_male = {}
    value_STDY_female = {}
    value_STDY_EA = {}

    value_VX_over30 = {}
    value_VX_male = {}
    value_VX_female = {}
    value_VX_EA = {}

    value_VY_over30 = {}
    value_VY_male = {}
    value_VY_female = {}
    value_VY_EA = {}

    value_area_over30 = {}
    value_area_male = {}
    value_area_female = {}
    value_area_EA = {}


    for task in EMG_array:
        print ''
