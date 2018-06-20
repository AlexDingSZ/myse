import xlrd

workbook = xlrd.open_workbook(r"E:\zl\auto\test.xlsx")
work_sheet = workbook.sheet_by_name("Sheet1")
rows = work_sheet.nrows
cols = work_sheet.ncols
for i in range(rows):
    for j in range(cols):
        print(work_sheet.cell_value(i,j)," ", end='')
    print()




