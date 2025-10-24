import pytesseract
import os
from pdf2image import convert_from_path
from PIL import Image


def ensure_poppler_installed():
    try:
        convert_from_path
    except Exception as e:
        raise ImportError("pdf2image no está instalado o poppler no está configurado correctamente.") from e


def ensure_tesseract_installed():
    try:
        pytesseract.get_tesseract_version()
    except Exception as e:
        raise ImportError("Tesseract OCR no está instalado o no está configurado correctamente.") from e


def check_dependencies():
    ensure_poppler_installed()
    ensure_tesseract_installed()


def main():
    check_dependencies()

    # Cambia la ruta de tesseract según tu instalación
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Ruta del poppler (bin que hayas descargado)
    poppler_path = r'C:\poppler-25.07.0\Library\bin'

    BASE_DIR = os.path.dirname(__file__)
    inputs_dir = os.path.join(BASE_DIR, 'inputs')
    outputs_dir = os.path.join(BASE_DIR, 'outputs')

    os.makedirs(inputs_dir, exist_ok=True)
    os.makedirs(outputs_dir, exist_ok=True)

    supported_images = {'.jpg', '.jpeg', '.png', '.tif', '.tiff', '.bmp', '.gif'}

    files = sorted(os.listdir(inputs_dir))
    if not files:
        print(f'No hay ficheros en {inputs_dir}')
    for fname in files:
        fpath = os.path.join(inputs_dir, fname)
        if os.path.isdir(fpath):
            continue
        name, ext = os.path.splitext(fname)
        ext = ext.lower()
        text_completo = ''
        try:
            if ext == '.pdf':
                pages = convert_from_path(fpath, dpi=300, poppler_path=poppler_path)
                for i, page in enumerate(pages):
                    texto = pytesseract.image_to_string(page, lang='spa')
                    text_completo += f'\n--- Página {i+1} ---\n{texto}'
            elif ext in supported_images:
                img = Image.open(fpath)
                texto = pytesseract.image_to_string(img, lang='spa')
                text_completo = texto
            else:
                print(f'Omitiendo {fname}: formato no soportado')
                continue

            output_path = os.path.join(outputs_dir, name + '.txt')
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text_completo)

            print(f'Procesado: {fname} -> {output_path}')
        except Exception as e:
            print(f'Error procesando {fname}: {e}')

    print('Extracción completada. Textos guardados en:', outputs_dir)


if __name__ == '__main__':
    main()
