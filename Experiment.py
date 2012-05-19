#! /usr/bin/python

from phil import *
from openpyxl.reader.excel import load_workbook
from alt_format_plate_wells_to_excel_sheet_mapping import plate_to_excel
import decimal

class Experiment:
        
    def __init__(self, name):
        self.name = name
        print "Initializing ",self.name
    
    def __open_worksheet(self):
        wb = load_workbook(self.name)
        ws = wb.worksheets[0]#uses only first worksheet
        return ws
    
    def total_timepoints(self):
        return self.__open_worksheet().get_highest_row()

    def total_timecourses(self):
        return self.__open_worksheet().get_highest_column()
    
    def extract_timecourse(self,well):
        ws = self.__open_worksheet()
        timecourse = []
        timepoints = self.total_timepoints()
        for i in range(1, timepoints + 1):
            try:
                cell_address = '%s%s'%(plate_to_excel[well],i)
            except KeyError:
                print "Out of bound well address hit. Exiting.."
                exit()
            cell_value = ws.cell(cell_address).value
            d = decimal.Decimal(cell_value) 
            timecourse.append(float('%1.4f'%d))
        return timecourse
        
