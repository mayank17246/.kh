import PyPDF2
import csv
import sys
import pymysql
from tabula import read_pdf
csv_path = 'C:\Users\DELL\Desktop\Key Ideas'
#df = read_pdf('dc.pdf')
#print(df)
a = PyPDF2.PdfFileReader('310031647.pdf')
print(a.documentInfo)
print(a.getPage(0).extractText())
b = PyPDF2.PdfFileReader('445045644.pdf')
print(b.documentInfo)
print(b.getPage(0).extractText())
#Using this I was able to extract data from all pdf file but I faced difficulty in other part

