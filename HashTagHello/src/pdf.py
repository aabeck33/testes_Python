import pypdf
import os

filelist = os.listdir("c:/temp")

for file in filelist:
    if (".pdf" in file):
        pdf_reader = pypdf.PdfReader(f"c:/temp/{file}")
        pdf_writer = pypdf.PdfWriter()

        for page in range (0, len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

        with open(f'c:/temp/_{file}', 'wb') as fh:
                pdf_writer.write(fh)
    else:
         print('Não é PDF.')