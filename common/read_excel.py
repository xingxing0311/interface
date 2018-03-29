# coding:utf-8
import xlrd
from openpyxl import load_workbook

class ExcelUtil():
    def read_excel(self,file_path,index=0):
        wb=xlrd.open_workbook(file_path)
        sheet=wb.sheet_by_index(0)
        #获取行和高
        rows=sheet.nrows
        cols=sheet.ncols
        # print(rows,cols)
        key=sheet.row_values(0)
        data=[]
        if rows<2:
            print("行数小于两行，请检查数据")
        else:
            for i in range(rows-1):
                k={}
                for j in range(cols):
                    value=sheet.cell_value(i+1,j)
                    k[key[j]]=value
                data.append(k)
            return data

if __name__=="__main__":
    excel=ExcelUtil()
    file_path="e:\\python work\\interface_frame\\data\\kuaidi.xlsx"
    data=excel.read_excel(file_path,index=0)
    print(data)