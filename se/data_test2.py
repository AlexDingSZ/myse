import unittest

from ddt import  ddt, data,unpack
from excel_util import excel_util

excel = excel_util(r"E:\data.xlsx", 'Sheet1')

@ddt
class DataTest(unittest.TestCase):


    @data({"key1":"value1","key2":"value2","key3":"value3"},{"key1":"value11","key2":"value21","key3":"value31"})
    @unpack
    def testLogin(self, **data):
        print(data['key1'])
        print(data['key2'])
        print(data['key3'])

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(DataTest)
    unittest.TextTestRunner(verbosity=2).run(suite)