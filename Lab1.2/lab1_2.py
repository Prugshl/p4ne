#Import pyplot and openpyxl
import openpyxl
from matplotlib import pyplot
from openpyxl import load_workbook
wb = (openpyxl.load_workbook("C:\\Users\\aa.markelov\\Desktop\\WORD\\PY\\1.2\\data_analysis_lab.xlsx"))
#print(type(wb))
sheet = wb['Data'] #Get data from list "Data"
colA = sheet['A'][1:] #Get data from column A except header
colC = sheet['C'][1:] #Get data from column C except header
colD = sheet['D'][1:] #Get data from column D except header

def getvalue(x):
    return x.value

year_x = list(map(getvalue, colA)) #get data from colA and make a list
sun_temp_y = list(map(getvalue, colC)) #get data from colA and make a list
sun_activ_y = list(map(getvalue, colD)) #get data from colA and make a list

pyplot.plot(year_x, sun_temp_y)  #create a graf, x goes first
pyplot.plot(year_x, sun_activ_y)  #create a graf, x goes first
pyplot.show()
