# coding=utf-8
import pandas as pd
import codecs

xd = pd.ExcelFile(r"E:\data.xlsx")
df = xd.parse("Sheet1")
#with codecs.open(r"E:\data.html") as html_file:
with open(r"E:\data.html", 'w') as html_file:
    html_file.write(df.to_html(header = True,index = False))

