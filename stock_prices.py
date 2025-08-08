import xlsxwriter as xw
 # creating a workbook
"""wb = xw.Workbook('stock_prices.xlsx')
wb_sheet = wb.add_worksheet('Prices')

stock_prices = {'A' :[357, 457, 187, 831, 779, 338, 129, 508, 407, 748, 511, 609], \
    
                'B': [14908, 13408, 17103, 18886, 19828, 12098, 17080, 16850, 15023, 12405, 15469, 13800 ],\
                'C': [60, 64, 54, 93, 87, 74, 96, 92, 83, 85, 70, 88],\
                'D': [1667, 1962, 1845, 1535, 1753, 1767, 1551, 1893, 1715, 1707, 1627, 1532], \
                'E': [2181, 2333, 2265, 2274, 2739, 2601, 2569, 2520, 2744, 2234, 2230, 2836],\
    }

months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

stock_list = ['A', 'B', 'C', 'D', 'E']

wb_format_1 = wb.add_format({'border':1})
wb_format_2 = wb.add_format({'border':2})

wb_sheet.write_column('A2', stock_list, wb_format_2)
wb_sheet.write_row('B1', months, wb_format_2)
row = 1
for stock in stock_prices:
    stocks = stock_prices[stock]
    wb_sheet.write_row(row, 1, stocks, wb_format_1)
    row += 1
wb.close()"""


# Perfoming calculations using excel formulas (media of stock prices throughout the year
import xlwings as xlw
"""obj_excel = xlw.App(visible=False)
obj_workbook = xlw.Book('stock_prices.xlsx')
obj_worksheet = obj_workbook.sheets[0]
formula = '=ROUND(AVERAGE(B2:M2),0)'
obj_worksheet.range("N2,N3,N4,N5,N6").formula = formula
obj_workbook.save()
obj_workbook.close()
obj_excel.kill()"""
#context manager
with xlw.App() as app:
    obj_excel = xlw.App(visible=False)
    obj_workbook = xlw.Book('stock_prices.xlsx')
    obj_worksheet = obj_workbook.sheets[0]
    formula = '=ROUND(AVERAGE(B2:M2),0)'
    obj_worksheet.range("N2,N3,N4,N5,N6").formula = formula
    obj_workbook.save()
    obj_workbook.close()
    obj_excel.kill()

# app password gmail = aqbr gutj itvk morc

# ploting a pie chart of the averave stock values     
    



