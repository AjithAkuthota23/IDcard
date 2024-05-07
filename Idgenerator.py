import fpdf
import csv
import os

pdf = fpdf.FPDF(unit='in', format='Letter')
pdf.set_auto_page_break(auto=True, margin=0.5)

id_template = './id.png'

with open('employee_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    header = reader.fieldnames

    for row in reader:
        name = row['Name']
        position = row['Position']
        photo_path = row['Photo']

        pdf.add_page()

        pdf.image(id_template, 0, 0, 6.5, 4)

        pdf.set_font('times', 'B', 24)
        pdf.text(1.2, 3.5, name)

        pdf.set_font('times', '', 16)
        pdf.text(2.5, 3.8, position)

        pdf.image(photo_path, 4, 0.6, 1.5, 2, type='JPG')

pdf.output('ID.pdf')