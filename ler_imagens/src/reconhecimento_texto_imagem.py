'''
    links uteis:
        corrigir instalação windows: https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
        instalar outra língua: https://github.com/tesseract-ocr/tessdata
    pegar linguas: print(pytesseract.get_languages())
'''

### Importações:
import pytesseract
import cv2

#imagem = cv2.imread(r'..\other\print_magalu.JPG')
imagem = cv2.imread(r'..\other\email.JPG')

caminho = r'C:\Users\beck_\AppData\Local\Tesseract-OCR'
pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
texto = pytesseract.image_to_string(imagem, lang='por')

print(texto)
