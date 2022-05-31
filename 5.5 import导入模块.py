#导入模块：起到调用的作用，有两种导入方式
#1.导入所有，如：  a2文件导入a1，a1可以使用a2的所有类，属性，方法
#   import 文件名

import hs_demo

print(hs_demo.add(9, 9))


#2.只导入使用到的类或者方法
#from 模块名 import 类、属性、方法

from hs_demo import spu

print(spu(3, 4))

from l_demo import Students

s = Students()
s.name = '二傻子'
s.grade = 9
s.status = '睡觉'
s.study()

#通过包路径下导入文件
print(s)