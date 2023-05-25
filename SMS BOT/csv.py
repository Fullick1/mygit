import csv

with open('input.csv', 'r') as input_file, open('output.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    
    for row in reader:
        if len(row[0]) == 12:
            if row[0][:2] == '89':
                row[0] = '79' + row[0][2:]
            writer.writerow(row)
        elif len(row[0]) == 11 and row[0][0] == '9':
            row[0] = '7' + row[0]
            writer.writerow(row)