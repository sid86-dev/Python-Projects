import re
import PyPDF2
loc = "pdfs/book1.pdf"
read = PyPDF2.PdfFileReader(loc)

# print(read.documentInfo)

text = read.getPage(5).extractText()
pages = read.numPages

analyzed_text = ""
punctions = '''!"#$%&'()*+-/:;<=>?@[\]^_`{|}~™'''
for char in text:
    if char not in punctions:
        analyzed_text = analyzed_text + char

realanyzed_text = ""
for char in analyzed_text:
    if char != "\n" and char != "\r":
        realanyzed_text = realanyzed_text + char

print(realanyzed_text)

