import unittest
from ddt import ddt,data,unpack


@ddt
class my_case(unittest.TestCase):
    test_data1 = (1,2,3,5)
    test_data2 = ((3, 2), (4, 3), (5, 3))
    test_data3 = [(3, 2), (4, 3), (5, 3)]

    @data(1, 2, 3, 3, 5)
    @data(*test_data1)
    def test_ddt_fun1(self, para): #单个参数
        print(para)

    @data((3, 2), (4, 3), (5, 3))
    @data(*test_data2)
    @unpack
    def test_ddt_fun2(self, para1,para2): #多个参数
        print(para1,para2)

    @data(*test_data3)
    @unpack
    def test_ddt_fun3(self,para1,para2):
        print(para1,para2)

if __name__ == "__main__":
    unittest.main()