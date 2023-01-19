''' dlFlexToMultiXL.py
    Download a flexquery report 
    
    NOTE: I don't need a TWS or Gateway connection to do this!'''


from ib_insync import *
import pandas as pd
#from pandas import DataFrame as df
import datetime as dt
import openpyxl

import code.file as file

parms = file.read_json("parms/report.json")  # report parameters
space = " "

rpt = FlexReport(token=parms["token"], queryId=parms["rptID"])

x = dt.datetime.now()                                               # get current datetime
#now_str = x.strftime('%Y-%m-%d_%H-%M-%S')                          # format it to string and without milli seconds
now_str = x.strftime('%Y-%m-%d')                                    # format it to string and only date portion
output_folder = 'Output/flex/'   # set the main output folder to write reports to
out_folder = output_folder + now_str + space + parms["rptID"] + space        # create a path & base filename for the output

# Create an xlsx workbook
wb = pd.ExcelWriter(out_folder + 'Flex.xlsx', engine='openpyxl')

# Loop through Topics of Flex Report
for r in rpt.topics():
    report = rpt.df(r)
# Write each dataframe to a different worksheet.
    report.to_excel(wb, sheet_name=r,index=False)

wb.close()
