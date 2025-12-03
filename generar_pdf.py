from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER

# Leer markdown
with open('DOCUMENTO_MAESTRO_COMPLETO.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Crear PDF
pdf_file = 'DOCUMENTO_MAESTRO_COMPLETO.pdf'
doc = SimpleDocTemplate(pdf_file, pagesize=letter,
                        topMargin=0.5*inch, bottomMargin=0.5*inch,
                        leftMargin=0.75*inch, rightMargin=0.75*inch)

# Estilos
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='CustomTitle', parent=styles['Heading1'],
                         fontSize=18, spaceAfter=12, textColor='#2c3e50'))
styles.add(ParagraphStyle(name='CustomHeading', parent=styles['Heading2'],
                         fontSize=14, spaceAfter=10))
styles.add(ParagraphStyle(name='CustomBody', parent=styles['Normal'],
                         fontSize=10, spaceAfter=6, leading=14))

story = []

# Procesar líneas
lines = content.split('\n')

for line in lines:
    # Eliminar caracteres problemáticos
    line = line.replace('π', 'pi').replace('₁', '1').replace('₂', '2')
    line = line.replace('≠', '!=').replace('≥', '>=').replace('≤', '<=')
    line = line.replace('×', 'x').replace('→', '->').replace('⭐', '*')
    line = line.replace('✅', '[OK]').replace('❌', '[X]').replace('📊', '')
    line = line.replace('🔵', '').replace('🔴', '').replace('📋', '')
    line = line.replace('🎯', '').replace('📚', '').replace('🚨', '')
    line = line.replace('📝', '').replace('🎓', '').replace('⚡', '')
    
    # Títulos H1
    if line.startswith('# '):
        story.append(PageBreak())
        story.append(Paragraph(line[2:], styles['CustomTitle']))
        story.append(Spacer(1, 0.2*inch))
    # Títulos H2
    elif line.startswith('## '):
        story.append(Spacer(1, 0.1*inch))
        story.append(Paragraph(line[3:], styles['CustomHeading']))
    # Títulos H3
    elif line.startswith('### '):
        story.append(Paragraph('<b>' + line[4:] + '</b>', styles['CustomBody']))
    # Líneas de código o separadores
    elif line.startswith('```') or line.startswith('---'):
        continue
    # Texto normal
    elif line.strip():
        # Limpiar markdown
        text = line.replace('**', '<b>').replace('*', '')
        # Cerrar tags bold si hay
        if '<b>' in text and '</b>' not in text:
            text = text.replace('<b>', '<b>') + '</b>'
        
        try:
            story.append(Paragraph(text, styles['CustomBody']))
        except:
            # Si falla, intentar sin formato
            try:
                clean = line.replace('**', '').replace('*', '').replace('`', '')
                story.append(Paragraph(clean, styles['CustomBody']))
            except:
                pass

# Generar PDF
doc.build(story)
print(f"✅ PDF creado: {pdf_file}")
