from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
import re

# Leer markdown
with open('DOCUMENTO_MAESTRO_COMPLETO.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Crear PDF
pdf_file = 'GUIA_ACADEMICA_ORGANIZACION_INDUSTRIAL.pdf'
doc = SimpleDocTemplate(pdf_file, pagesize=letter,
                        topMargin=1*inch, bottomMargin=0.75*inch,
                        leftMargin=1*inch, rightMargin=1*inch)

# Estilos profesionales
styles = getSampleStyleSheet()

# Título principal
styles.add(ParagraphStyle(
    name='MainTitle',
    parent=styles['Title'],
    fontSize=20,
    textColor=colors.HexColor('#1a237e'),
    spaceAfter=20,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
))

# Subtítulo
styles.add(ParagraphStyle(
    name='Subtitle',
    parent=styles['Normal'],
    fontSize=14,
    textColor=colors.HexColor('#424242'),
    spaceAfter=30,
    alignment=TA_CENTER,
    fontName='Helvetica'
))

# H1
styles.add(ParagraphStyle(
    name='CustomH1',
    parent=styles['Heading1'],
    fontSize=16,
    textColor=colors.HexColor('#1565c0'),
    spaceAfter=12,
    spaceBefore=24,
    fontName='Helvetica-Bold'
))

# H2
styles.add(ParagraphStyle(
    name='CustomH2',
    parent=styles['Heading2'],
    fontSize=13,
    textColor=colors.HexColor('#283593'),
    spaceAfter=8,
    spaceBefore=12,
    fontName='Helvetica-Bold'
))

# H3
styles.add(ParagraphStyle(
    name='CustomH3',
    parent=styles['Heading3'],
    fontSize=11,
    textColor=colors.HexColor('#424242'),
    spaceAfter=6,
    spaceBefore=8,
    fontName='Helvetica-Bold'
))

# Cuerpo
styles.add(ParagraphStyle(
    name='CustomBody',
    parent=styles['Normal'],
    fontSize=10,
    leading=14,
    spaceAfter=4,
    alignment=TA_JUSTIFY,
    fontName='Helvetica'
))

# Código/Fórmulas
styles.add(ParagraphStyle(
    name='CustomCode',
    parent=styles['Normal'],
    fontSize=9,
    leading=12,
    fontName='Courier',
    leftIndent=20,
    spaceAfter=8,
    spaceBefore=4
))

story = []

# Función limpiar texto
def clean_text(text):
    # Reemplazos de caracteres especiales
    replacements = {
        'π': 'pi',
        '₁': '1',
        '₂': '2',
        '₃': '3',
        '≠': '!=',
        '≥': '>=',
        '≤': '<=',
        '×': 'x',
        '→': '->',
        '⭐': '*',
        '✅': '[OK]',
        '❌': '[X]',
        '📊': '',
        '🔵': '',
        '🔴': '',
        '📋': '',
        '🎯': '',
        '📚': '',
        '🚨': '',
        '📝': '',
        '🎓': '',
        '⚡': '',
        '📘': '',
        '📌': '',
        'η': 'eta',
        'ε': 'epsilon',
        'δ': 'delta',
        'Σ': 'Suma',
        '∫': 'Integral',
        '∞': 'infinito'
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    return text

# Procesar documento
lines = content.split('\n')
in_code_block = False

for i, line in enumerate(lines):
    line_clean = clean_text(line)
    
    # Detectar bloques de código
    if line.strip().startswith('```'):
        in_code_block = not in_code_block
        continue
    
    # Si estamos en bloque de código
    if in_code_block:
        if line_clean.strip():
            try:
                story.append(Paragraph(line_clean, styles['CustomCode']))
            except:
                pass
        continue
    
    # Separadores (---)
    if line.strip() == '---' or line.strip() == '___':
        story.append(Spacer(1, 0.2*inch))
        continue
    
    # Título principal (primer #)
    if line.startswith('# ') and i < 5:
        text = line_clean[2:].strip()
        try:
            story.append(Paragraph(text, styles['MainTitle']))
        except:
            pass
        continue
    
    # H1 (# )
    if line.startswith('# '):
        story.append(PageBreak())
        text = line_clean[2:].strip()
        try:
            story.append(Paragraph(text, styles['CustomH1']))
        except:
            pass
        continue
    
    # Subtítulo (##) en primeras líneas
    if line.startswith('## ') and i < 10:
        text = line_clean[3:].strip()
        try:
            story.append(Paragraph(text, styles['Subtitle']))
        except:
            pass
        continue
    
    # H2 (##)
    if line.startswith('## '):
        text = line_clean[3:].strip()
        try:
            story.append(Paragraph(text, styles['CustomH2']))
        except:
            pass
        continue
    
    # H3 (###)
    if line.startswith('### '):
        text = line_clean[4:].strip()
        try:
            story.append(Paragraph(text, styles['CustomH3']))
        except:
            pass
        continue
    
    # Líneas vacías
    if not line.strip():
        story.append(Spacer(1, 0.1*inch))
        continue
    
    # Fórmulas matemáticas ($$)
    if line.strip().startswith('$$') or '$' in line:
        # Limpiar $$ y tratar como código
        formula = line_clean.replace('$$', '').replace('$', '').strip()
        if formula:
            try:
                story.append(Paragraph(formula, styles['CustomCode']))
            except:
                pass
        continue
    
    # Texto normal
    if line_clean.strip():
        # Procesar markdown básico
        text = line_clean
        
        # Bold (**text**)
        text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
        
        # Italic (*text*)
        text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
        
        # Code (`text`)
        text = re.sub(r'`(.*?)`', r'<font name="Courier">\1</font>', text)
        
        # Listas (- o * al inicio)
        if text.strip().startswith('- ') or text.strip().startswith('* '):
            text = '  • ' + text.strip()[2:]
        
        # Listas numeradas
        if re.match(r'^\d+\.', text.strip()):
            text = '  ' + text.strip()
        
        try:
            story.append(Paragraph(text, styles['CustomBody']))
        except Exception as e:
            # Si falla, intentar sin formato
            try:
                plain = line_clean.replace('**', '').replace('*', '').replace('`', '')
                story.append(Paragraph(plain, styles['CustomBody']))
            except:
                pass

# Pie de página
def add_page_number(canvas, doc):
    page_num = canvas.getPageNumber()
    text = f"Página {page_num}"
    canvas.saveState()
    canvas.setFont('Helvetica', 9)
    canvas.drawRightString(7.5*inch, 0.5*inch, text)
    canvas.restoreState()

# Generar PDF
doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
print(f"PDF ACADEMICO GENERADO: {pdf_file}")
print(f"Total de páginas: {len(story)//10}")
