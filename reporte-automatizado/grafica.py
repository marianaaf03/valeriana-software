import csv
import os
import plotly.express as px

# ==========================================
# TICKET 3: Generar gráfica interactiva con Plotly
# Responsable: Mariana Alvarez Franco
# ==========================================

def crear_grafica():
    """Lee los registros del CSV, procesa los datos de adopciones por tipo de animal,
    los ordena de mayor a menor y genera un gráfico interactivo en HTML."""
    
    ruta_csv = "datos/registros.csv"
    ruta_salida = "salida/grafica.html"
    
    # Validar que el archivo de datos exista antes de procesar
    if not os.path.exists(ruta_csv):
        print(f"Error: No se encontró el archivo en {ruta_csv}. Ejecuta primero generar_datos.py")
        return

    conteo_animales = {}

    # Leer el archivo CSV y contar registros por tipo de animal
    with open(ruta_csv, mode='r', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            # Omitimos filas vacías o con errores críticos simulados
            tipo = fila.get("tipo_animal")
            if tipo and tipo.strip() != "":
                conteo_animales[tipo] = conteo_animales.get(tipo, 0) + 1

    # Preparar datos para Plotly ordenados de mayor a menor
    animales_ordenados = sorted(conteo_animales.items(), key=lambda x: x[1], reverse=True)
    
    tipos = [item[0] for item in animales_ordenados]
    cantidades = [item[1] for item in animales_ordenados]

    # Crear la figura interactiva con Plotly Express
    fig = px.bar(
        x=tipos,
        y=cantidades,
        labels={'x': 'Tipo de Animal', 'y': 'Total de Solicitudes / Registros'},
        title='<b>Resumen de Solicitudes por Tipo de Animal - Refugio</b>',
        color=cantidades,
        color_continuous_scale='Teal'
    )

    # Aplicar diseño limpio al gráfico
    fig.update_layout(
        template='plotly_white',
        title_font_size=18,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14
    )

    # Asegurar que la carpeta 'salida' exista
    os.makedirs("salida", exist_ok=True)

    # Guardar el gráfico como un archivo HTML interactivo
    fig.write_html(ruta_salida)
    print(f"¡Éxito! Gráfica interactiva generada correctamente en: {ruta_salida}")

if __name__ == "__main__":
    crear_grafica()