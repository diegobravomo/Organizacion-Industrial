import PyPDF2
import os

folder = r'c:\Users\Dell\Documents\github\Organizacion-Industrial\Material apoyo'

for filename in os.listdir(folder):
    if filename.endswith('.pdf'):
        print(f'\n{"="*80}')
        print(f'ARCHIVO: {filename}')
        print(f'{"="*80}\n')
        
        pdf_path = os.path.join(folder, filename)
        reader = PyPDF2.PdfReader(pdf_path)
        
        full_text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            full_text += page.extract_text()
        
        print(full_text)
        print('\n')
