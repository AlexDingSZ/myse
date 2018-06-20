import unittest

from ddt import  ddt, data,unpack
from excel_util import excel_util




@ddt
class DataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('start')

    @classmethod
    def tearDownClass(cls):
        print('stop')
    excel = excel_util(r"E:\data.xlsx", 'Sheet1').next()
    @data({"aa":"valuea","bb":"valueab","cc":"valueac"},{"aa":"valuea","bb":"valueab","cc":"valueac"})

    #@data(*excel)
    @unpack
    def testLogin(self, **data):
        print(data['aa'])
        print(data['bb'])
        print(data['cc'])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(DataTest)
    unittest.TextTestRunner(verbosity=2).run(suite)