import PyPDF2
import pdfplumber
import re
import openpyxl
from openpyxl import load_workbook
import os

#PDF Reader
pdf_obj = open('caminho\\sample.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_obj)
pdf_numpages = len(pdf_reader.pages)
pdf_pages = pdf_reader.pages[0]

#Excel File
wb_path = 'caminho\\planilha.xlsx'
wb_open = load_workbook(wb_path)
ws_pdf = wb_open['PDF']

with pdfplumber.open('caminho\sample.pdf') as pdf:
    for page in pdf.pages:
        pdf_current_page = page.extract_text()

        pdfFinder1 = pdf_current_page.find('Dado1')
        pdfDado1 = (pdf_current_page[pdfFinder1:pdfFinder1+62])

        pdfFinder2 = pdf_current_page.find('Dado2')
        pdfDado2 = (pdf_current_page[pdfFinder2:pdfFinder2+15])


        rPDF = len(ws_pdf['A']) + 1
        columnA = "A" + str(rPDF)
        columnB = "B" +str(rPDF)

        ws_pdf[columnA] = pdfDado1
        ws_pdf[columnB] = pdfDado2

wb_open.save(filename=wb_path)
os.startfile(wb_path)
