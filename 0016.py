# 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

import xlwt,json
from collections import OrderedDict

with open ('D:/python project/DIXXXY-V1/numbers.txt') as f:
    data = json.load(f,object_pairs_hook=OrderedDict)
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('numbers',cell_overwrite_ok=True)
    for row,i in enumerate(data):
        for col,j in enumerate(i):
            sheet1.write(row,col,j)
    workbook.save('numbers.xls')