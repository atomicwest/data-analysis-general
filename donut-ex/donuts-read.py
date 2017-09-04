from openpyxl import load_workbook

filename = "donut-info.xlsx"

wb = load_workbook(filename=filename, read_only=True)
ws = wb['One-hundred Donuts']

for row in ws.rows:
    
    # print type(row)
    # for cell in row:
    #     print(cell.value)
    row = ""
    for cell in row:
        print type(cell.value)
        row+=str(cell.value)
    print row
    