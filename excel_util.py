import  xlrd

class excel_util(object):
    def __init__(self,excel_path, sheet_name):
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheet_by_name(sheet_name)
        self.row = self.table.row_values(0)
        self.row_num = self.table.nrows
        self.col_num = self.table.ncols
        self.cur_row_no = 1

    def next(self):
        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.cur_row_no)
            i = self.col_num
            for x in range(i):
                s[self.row[x]]=col[x]
            r.append(s)
            self.cur_row_no += 1
        return r

    def hasNext(self):
        if self.row_num == 0 or self.row_num <= self.cur_row_no:
            return False
        else:
            return True
