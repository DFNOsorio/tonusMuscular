from tools import *
import xlsxwriter
import openpyxl
import xlrd, xlwt

def create_database():
    workbook = xlsxwriter.Workbook('C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/demo.xlsx')

def fill_parameters():
    wb = xlrd.open_workbook('C:/Users/Rita/PycharmProjects/tonusMuscular/Excel_database/demo.xlsx')
    worksheet = wb.add_sheet('Patient1_Healthy')
