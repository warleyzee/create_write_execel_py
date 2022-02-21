import xlsxwriter

workbook = xlsxwriter.Workbook('Exemplo2.xlsx')
worksheet = workbook.add_worksheet()

row = 0
column = 0

content = ["Pato","Cachorro","Onça","Sapo","Rato","Gato","Macaco","Tuna"]

for item in content:
    worksheet.write(row, column, item)
    row +=1

workbook.close()