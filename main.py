import pytesseract
import os
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pdf_path = 'A00 CG11-95 LVN Automoviles junio 1996.pdf'
poppler_path = r'C:\poppler-25.07.0\Library\bin'

if not os.path.exists(pdf_path):
    raise FileNotFoundError(f'No se encontró el PDF: {pdf_path}')

# Convertir PDF a imágenes
pages = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)

text_completo = ''
for i, page in enumerate(pages):
    texto = pytesseract.image_to_string(page, lang='spa')  # OCR en español
    text_completo += f'\n--- Página {i+1} ---\n{texto}'

# Guardar el texto en un archivo del mismo nombre que el PDF pero .txt
output_path = os.path.splitext(pdf_path)[0] + '.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(text_completo)

print('Extracción completada. Texto guardado.')
