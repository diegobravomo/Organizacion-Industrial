import PyPDF2
import os

carpeta_clases = "Clases"

# Lista de PDFs en orden
clases = [
    "Clase_1__introduccion_630259 (1).pdf",
    "Clase_2__of_y_dda_633090 (2).pdf",
    "Clase_3__competencia_perfecta_633658 (2).pdf",
    "Clase_4__Elasticidad_635604 (1).pdf",
    "Clase_5__Historia_de_la_OI_637901 (1).pdf",
    "Clase_6__Mercado_relevante_638485 (1).pdf",
    "Clase_7__Concentracion_de_mercado_639947 (1).pdf",
    "Clase_8__Monopolio_640608 (1).pdf",
    "Clase_9__Discriminacion_de_precios__parte_1_642154 (1).pdf",
    "Clase_10__Monopolio_multiproducto_642578 (1).pdf",
    "Clase_11__Teoria_de_Juegos_parte_1_652140.pdf"
]

print("=" * 80)
print("EXTRACCIÓN DE CONTENIDO DE CLASES")
print("=" * 80)

for i, clase_pdf in enumerate(clases, 1):
    ruta = os.path.join(carpeta_clases, clase_pdf)
    
    print(f"\n{'='*80}")
    print(f"CLASE {i}: {clase_pdf}")
    print(f"{'='*80}\n")
    
    try:
        with open(ruta, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_paginas = len(pdf_reader.pages)
            
            print(f"Número de páginas: {num_paginas}\n")
            
            # Extraer texto de todas las páginas
            texto_completo = ""
            for num_pag in range(num_paginas):
                pagina = pdf_reader.pages[num_pag]
                texto = pagina.extract_text()
                if texto.strip():
                    texto_completo += f"\n--- Página {num_pag + 1} ---\n{texto}\n"
            
            if texto_completo.strip():
                print(texto_completo[:2000])  # Primeros 2000 caracteres
                if len(texto_completo) > 2000:
                    print(f"\n... (texto continúa, total: {len(texto_completo)} caracteres)")
            else:
                print("⚠️ No se pudo extraer texto (posiblemente PDF escaneado)")
                
    except Exception as e:
        print(f"❌ Error al procesar: {e}")

print("\n" + "="*80)
print("EXTRACCIÓN COMPLETADA")
print("="*80)
