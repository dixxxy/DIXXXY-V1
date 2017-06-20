# 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下所示：
# <?xml version="1.0" encoding="UTF-8"?>
# <root>
# <numbers>
# <!--
	#数字信息
# -->

#[
	#[1, 82, 65535],
	#[20, 90, 13],
	#[26, 809, 1024]
#]

#</numbers>
#</root>

import json,xlwt
from collections import OrderedDict

with open ('D:/py_exercise/exercise/numbers.txt','r') as f:
    L = []
    L.append(r"""
<?xml version="1.0" encoding="UTF-8"?>
<root>
<numbers>
<!-- 
    数字信息
-->
[
   [1, 82, 65535],
   [20, 90, 13],
   [26, 809, 1024]
]
    """)
   # L.append(f.read())
    L.append(r"""
</numbers>
</root>
      """)
    with open('D:/py_exercise/exercise/numbers.xml','w') as s:
        s.write(''.join(L))