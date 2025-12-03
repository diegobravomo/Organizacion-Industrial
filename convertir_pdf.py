from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, 'Organizacion Industrial - Documento Maestro', new_x='LMARGIN', new_y='NEXT', align='C')
        self.ln(5)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}', align='C')

# Leer el archivo markdown
with open('DOCUMENTO_MAESTRO_COMPLETO.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Crear PDF
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font('Helvetica', '', 10)

# Función para limpiar emojis y caracteres especiales
def clean_text(text):
    # Remover emojis y caracteres no-latin
    import re
    # Mantener solo caracteres básicos, números, espacios y puntuación común
    return ''.join(char for char in text if ord(char) < 256 or char in ' ')

# Procesar línea por línea
lines = md_content.split('\n')

for line in lines:
    clean_line = clean_text(line)
    
    # Títulos H1
    if clean_line.startswith('# '):
        pdf.set_font('Helvetica', 'B', 16)
        pdf.ln(5)
        pdf.multi_cell(0, 10, clean_line[2:])
        pdf.set_font('Helvetica', '', 10)
        pdf.ln(2)
    # Títulos H2
    elif clean_line.startswith('## '):
        pdf.set_font('Helvetica', 'B', 14)
        pdf.ln(3)
        pdf.multi_cell(0, 8, clean_line[3:])
        pdf.set_font('Helvetica', '', 10)
        pdf.ln(2)
    # Títulos H3
    elif clean_line.startswith('### '):
        pdf.set_font('Helvetica', 'B', 12)
        pdf.ln(2)
        pdf.multi_cell(0, 7, clean_line[4:])
        pdf.set_font('Helvetica', '', 10)
        pdf.ln(1)
    # Líneas en blanco
    elif clean_line.strip() == '':
        pdf.ln(3)
    # Bloques de código
    elif clean_line.startswith('```'):
        continue
    # Texto normal
    else:
        # Limpiar markdown básico
        text = clean_line.replace('**', '').replace('*', '').replace('`', '')
        if text.strip():
            try:
                pdf.multi_cell(0, 5, text)
            except Exception as e:
                print(f"Saltando linea problematica: {e}")
                continue

# Guardar PDF
pdf.output('DOCUMENTO_MAESTRO_COMPLETO.pdf')
print("✅ PDF creado exitosamente: DOCUMENTO_MAESTRO_COMPLETO.pdf")
