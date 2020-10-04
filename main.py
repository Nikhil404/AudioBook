import pyttsx3
import PyPDF2

book = open('phoenix.pdf','rb')
pagenum = input("Please Select a page number: ")
pagenum = int(pagenum)
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()
for num in range(pagenum,pages):
    page = pdfReader.getPage(pagenum)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()