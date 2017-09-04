import xlsxwriter
import random

workbook = xlsxwriter.Workbook('donut-info-colors.xlsx')
worksheet1 = workbook.add_worksheet('One-hundred Donuts')

bold = workbook.add_format({'bold':1})

fDType = workbook.add_format({'bg_color': '#ffd493', 'underline': 34})
fIcing = workbook.add_format({'bg_color': '#ffe0fb'})
fFilling = workbook.add_format({'bg_color': '#d1ffd2', 'italic': 1})
# fTopping = workbook.add_format({'bg_color': '#d1deff', 'rotation': 45})
fTopping = workbook.add_format({'bg_color': '#d1deff'})

numCols = 4
worksheet1.write('A1', 'Donut Type', bold)
worksheet1.write('B1', 'Icing', bold)
worksheet1.write('C1', 'Filling', bold)
worksheet1.write('D1', 'Topping', bold)


donuttypes = [
    'yeast ring',
    'chocolate cake ring',
    'plain cake ring',
    'blueberry cake ring',
    'old fashioned ring',
    'pumpkin spice ring',
    'yeast filled',
    ]

icings = [
    'original glaze', 
    'chocolate', 
    'strawberry',
    'berry',
    'maple',
    'vanilla',
    'green tea',
    ]

fillings = [
    'none',
    'chocolate',
    'custard',
    'cookies and cream',
    ]

toppings = [
    'none',
    'multicolor sprinkles',
    'chocolate sprinkles',
    ]
    
    
#start at row 1 to accommodate titles
row = 1
col = 0

records = []

#==============helper functions================================

def newrecord():
    record = []
    record.append(donuttypes[random.randint(0,len(donuttypes)-1)])
    record.append(icings[random.randint(0,len(icings)-1)])
    record.append(fillings[random.randint(0,len(fillings)-1)])
    record.append(toppings[random.randint(0,len(toppings)-1)])
    return record

def randcomment():
    
    subjects = [
        'Donuts',
        'Sugars',
        'Dry ingredients',
        'Wet ingredients',
        'Organic ingredients',
        'Fried delicacies',
        'Snacks'
        ]

    verbs = [
        'are',
        'look',
        'taste',
        'smell',
        'appear',
        ]
        
    descriptors = [
        'sweet',
        'colorful',
        'delicious',
        'bright',
        'aromatic',
        'unique',
        'solid',
        'disgusting'
        ]
    
    comment = ''
    comment += subjects[random.randint(0,len(subjects)-1)]
    comment += verbs[random.randint(0,len(verbs)-1)]
    comment += descriptors[random.randint(0,len(descriptors)-1)]
        
    return comment


#==============Assemble the workbook here================================

numRecords = 100

for i in range(numRecords):
    
    record = newrecord()
    
    #enforce unique records
    # while record in records:
    #     record = newrecord()
    records.append(record)

#convert records to tuple for excel library
data = tuple(records)

for dtype, ice, fill, top in (data):
    worksheet1.write_string(row,col, dtype, fDType)
    worksheet1.write_string(row,col+1, ice, fIcing)
    worksheet1.write_string(row,col+2, fill, fFilling)
    worksheet1.write_string(row,col+3, top, fTopping)
    row+=1
    
for i in range(random.randint(10,30)):
    alpha = [chr(x) for x in range(65,65+numCols)]
    col = alpha[random.randint(0,len(alpha)-1)]
    row = str(random.randint(0, numRecords))
    cell = col+row
    worksheet1.write_comment(cell,randcomment())

workbook.close()