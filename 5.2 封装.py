#封装
#为了数据或功能的安全考虑，可以将部分数据或功能设置隐藏，外部接口无法访问
#封装主要使用的奇数是_或__，在变量或功能的前面加上__，如：__name ，__set_name()

class Students():

    name = '张三'
    __score = '76'


    def __set_score(self,score):
        self.__score = score


    def get_score(self):
        return self.__score


print(Students.name)
# print(Students.__score)
s = Students()
print(s.get_score())