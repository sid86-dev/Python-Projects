from PyPDF2.pdf import PdfFileReader
import pyttsx3
import PyPDF2

# user input
# pg = int(input("Enter the page number: "))

# text extraction
loc = "pdfs/book2.pdf"


read = PyPDF2.PdfFileReader(loc)

pages = read.numPages
print(pages)
text=""
for n in range(0, pages):
    text = text + read.getPage(n).extractText()

analyzed_text = ""
punctions = '''"#$%&'()*+-/:;<=>?@[\]^_`{|}~™˜˛ˆˇ˝˙˚'''
for char in text:
    if char not in punctions:
        analyzed_text = analyzed_text + char

realanyzed_text = ""
for char in analyzed_text:
    if char != "\n" and char != "\r":
        realanyzed_text = realanyzed_text + char

print(realanyzed_text)

# text to speech
speaker = pyttsx3.init()
newVoiceRate = 130
speaker.setProperty('rate',newVoiceRate)
speaker.save_to_file(realanyzed_text, 'test.mp3')
speaker.say(realanyzed_text)
speaker.runAndWait()

