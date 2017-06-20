# 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：
# <?xmlversion="1.0" encoding="UTF-8"?>
# <root>
# <citys>
# <!--
	#城市信息
# -->
#{
	#"1" : "上海",
	#"2" : "北京",
	#"3" : "成都"
#}
#</citys>
#</root>

import json,xlwt
from collections import OrderedDict

with open('D:\py_exercise\exercise\city.txt','r') as f:
    L = []
    L.append(r"""
<?xmlversion="1.0" encoding="UTF-8"?>
<root>
<citys>
<!--
    城市信息
-->
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都",
}
   """)
   # L.append(f.read())
    L.append(r"""
</citys>
</root>
   """)
    with open ('D:\py_exercise\exercise\city.xml','w') as s:
        s.write(''.join(L))