



import pytest
import openpyxl

def ReadExcel(path):
    book = openpyxl.load_workbook(path)
    sheet = book.active
    case = sheet['A1':'B1']
    for i,j in case:
        return [i.value,j.value]

@pytest.mark.parametrize('da,ta',ReadExcel(r"D:\python\pycase.xlsx"))
def test01(da,ta):
    print(da,ta)