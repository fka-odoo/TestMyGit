import csv


new_prescription_ingre = open('customer_prescriptions_ingredients_new_1.csv', 'a')

writer = csv.writer(new_prescription_ingre, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

i = 1
item = 1
    
prescription = open('customer_prescriptions_ingredients_new.csv', 'rb')
reader_line = csv.reader(prescription, delimiter=',', quotechar='"')
j = 1 

for row_line in reader_line:
    if j == 1:
        j = j + 1
        writer.writerow(row_line)
        continue
    print "\n???rowline", row_line
    if row_line[2] == 'Y':
    	continue
    prepare_row = row_line
    	
    writer.writerow(prepare_row)

    print item
    item = item + 1
