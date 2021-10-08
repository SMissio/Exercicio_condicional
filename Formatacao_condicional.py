Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import xlsxwriter as opcoesDOXL

import os

nomeArquivo = 'C:\\Users\\User1\\Desktop\\RPA1\\xlsx\\FormatacaoCondicional.xlsx'
planilhaExcel = opcoesDOXL.Workbook(nomeArquivo)

sheetDados = planilhaExcel.add_worksheet("Dados")

formatoMaior = planilhaExcel.add_format({'bg_color': 'green',
                                        'font_color': 'white'})

formatoMenor = planilhaExcel.add_format({'bg_color': 'red',
                                        'font_color': 'white'})
inserirDados = [
["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4", ],
    [34,50,12,34],
    [23,32,76,51],
    [43,47,44,34],
    [29,33,38,31],
]

sheetDados.write('A1', "Cálulas com valor >= 50 estão em verde e <= 50 estão em vermelho")

for i, range in enumerate (inserirDados):
    sheetDados.write_row(i+2,1,range)
    
sheetDados.conditional_format('B4:E8', {'type': 'cell',
                                       'criteria': '>=',
                                       'value': 50,
                                       'format': formatoMaior})

sheetDados.conditional_format('B4:E8', {'type': 'cell',
                                       'criteria': '<',
                                       'value': 50,
                                       'format': formatoMenor})
    


planilhaExcel.close()

os.startfile(nomeArquivo)
