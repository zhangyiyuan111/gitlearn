# import time
# import tkinter
# from tkinter import *
# import openpyxl
# from openpyxl import load_workbook
# import os
# file = os.listdir()
# for i in file:
#     if "xlsx" in i or "xls" in i:
#         name = i
# work_space = load_workbook(name)
# sheet = work_space.worksheets[0]
# a = []
# for row in sheet.rows:
#     value_imei = str(row[0].value)
#     a.append(value_imei)
# b = str(tuple(a[1:42]))
# b_str = str(b)
# b_str = b_str.replace(" ","")
# with open("IMEI.txt",mode="w") as f:
#     f.write(b_str)
# os.system("pause")
import random
import string

str_8 = ''
for i in range(8):
    str_8 = str_8+random.choice(string.ascii_lowercase)
print(str_8)



