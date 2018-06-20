import unittest

class my_unittest_case(unittest.TestCase):
    class_var= 1
    @classmethod
    def setUpClass(cls):
        print("from setupclass")
        #print(cls.class_var)

    def setUp(self):
        print()
        print("from setup")

    def tearDown(self):
        print("from teardown")

    @classmethod
    def tearDownClass(cls):
        #print(cls.class_var)
        print("from teardownclass")

    def test_equal01(self):
        self.assertEqual(1, 1)
        #self.assertEquals("aa","aa")
        print("case1 ")

    def test_equal02(self):
        self.assertEqual(1, 1)
        print("case2 ")


if __name__ == "__main__":
    unittest.main()
    print("end")