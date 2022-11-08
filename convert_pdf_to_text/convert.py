from PyPDF2 import PdfReader
import os
from time import sleep

if os.path.isdir('temp') == False:
  os.mkdir('temp')                     # cria um diretório chamado temp, caso ele já não exista

pdf_path = ''

pdf_path = input('Insira o nome de seu arquivo PDF - Use a barra invertida para colocar o caminho de seu diretório: ') # insira o caminho onde está o PDF
print('Convertendo...')
sleep(1)
print('convertido para txt!')

reader = PdfReader(pdf_path) 
page = reader.pages[0].extract_text() # depois de ler o PDF, vai ser extraído o texto desse arquivo.

txt_pdf = open('temp/convertido.txt', 'a') # cria um arquivo TXT caso não tenha, em modo escrita
txt_pdf.write(page) 
txt_pdf.close()



