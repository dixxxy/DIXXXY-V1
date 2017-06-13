import xlwt,json
from collections import OrderedDict

with open('D:\python project\DIXXXY-V1\student.txt') as f:
    data = json.load(f,object_pairs_hook=OrderedDict)
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('student',cell_overwrite_ok=True)
    for row, i in enumerate(list(data)):
        sheet1.write(row,0,i)
        for col,j in enumerate(data[i]):
            sheet1.write(row,col+1,j)
    workbook.save('D:\python project\DIXXXY-V1\student.xls')