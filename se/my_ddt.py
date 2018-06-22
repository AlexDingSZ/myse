import unittest
from ddt import ddt,data,unpack

@ddt
class my_case_ddt(unittest.TestCase):
    test_data1 = (1,2,3,5)
    test_data2 = ((13, 2), (14, 3), (15, 3))
    test_data3 = [(23, 2), (24, 3), (25, 3)]
    test_data4 = [(33, 2), (34, 3), (35, 3)]

   # @data(1, 2, 3, 3, 5)
    @data(*test_data1)
    def test_ddt_fun1(self, para): #单个参数
        print(para)

    #@data((3, 2), (4, 3), (5, 3))
    @data(*test_data2)
    @unpack
    def test_ddt_fun2(self, para1,para2): #多个参数
        print(para1,para2)

    @data(*test_data3)
    @unpack
    def test_ddt_fun3(self,para1,para2):
        print(para1,para2)

    @data(*test_data4)
    @unpack
    def test_ddt_fun4(self,para1,para2):
        print(para1,para2)


if __name__ == "__main__":
    unittest.main()