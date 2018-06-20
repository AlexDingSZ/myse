import unittest
import csv
from ddt import ddt, data, unpack


def get_csv_data(filename):
    users = []
    with open(filename,'r',encoding='utf-8') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            users.append(row)
    return users


@ddt
class UserActionTest(unittest.TestCase):
    @data(*get_csv_data(r'../data/userinfo.csv'))
    @unpack
    def test_login(self,username,passwd,expect_result):
        print(username,' ' ,passwd,' ',expect_result)


if __name__ == "__main__":
    unittest.main()