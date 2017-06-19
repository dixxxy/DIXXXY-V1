# 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

import xlwt,json
from collections import OrderedDict

with open ('D:\python project\DIXXXY-V1\city.txt') as f:
    data = json.load(f,object_pairs_hook=OrderedDict)
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('city', cell_overwrite_ok=True)
    for row,i in enumerate(data):
        sheet1.write(row,0,i)
        sheet1.write(row,1,data[i])
    workbook.save('city.xls')