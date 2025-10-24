# Helv-CCGG

Este proyecto está diseñado para extraer texto de archivos PDF utilizando OCR (Reconocimiento Óptico de Caracteres) con la ayuda de las bibliotecas Tesseract y pdf2image en Python.

Pensado para documentos que están en formato imagen dentro de los PDFs, este script convierte cada página del PDF en una imagen y luego aplica OCR para extraer el texto.

## Requisitos

- Python 3.x
- Tesseract OCR instalado en tu sistema. [Instrucciones de instalación](https://github.com/tesseract-ocr/tesseract)
- Poppler instalado en tu sistema. [Instrucciones de instalación](https://github.com/oschwartz10612/poppler-windows/releases)
- Biblioteca pdf2image.
- Biblioteca Pillow.
- Biblioteca pytesseract.

### Instalación de dependencias

Puedes instalar las bibliotecas necesarias utilizando pip:

```bash
pip install pytesseract pdf2image Pillow
```

- Instala Tesseract y Poppler siguiendo las instrucciones en sus respectivos enlaces. Asegúrate de copiar y pegar la ruta de poppler/bin para usarla en el script.
- Crea una carpeta llamada `inputs` en el mismo directorio donde se encuentra el script y coloca los archivos PDF que deseas procesar allí.
- Crea una carpeta llamada `outputs` en el mismo directorio donde se encuentra el script. Los archivos de texto extraídos se guardarán aquí.

## Uso

1. Coloca los archivos PDF en la carpeta `inputs`.
2. Ejecuta el script:

```bash
python main.py
```
3. Los archivos de texto extraídos se guardarán en la carpeta `outputs` con el mismo nombre que el archivo PDF original, pero con extensión `.txt`.