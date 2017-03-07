import xlrd

row_val = []

def ReadStockXls(xls):
    workbook = xlrd.open_workbook(xls)
    worksheet = workbook.sheet_by_index(0)
    nrows = worksheet.nrows

    for i in range(1, nrows):
        row_val.append(worksheet.row_values(i)[0])

ReadStockXls('kospi.xls')
ReadStockXls('kosdaq.xls')

out_file = open('code.txt', 'w')
for code in row_val:
    if code.find('K') != -1:
        out_file.write(code + '\n')
out_file.close()
