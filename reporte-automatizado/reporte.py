import csv
import os
from grafica import crear_grafica

# ==========================================
# TICKET 2: Generar reporte en Markdown con manejo de errores
# Responsable: Sara Valeria Guevara Buitrago / Equipo
# ==========================================

def procesar_datos_y_generar_reporte():
    ruta_csv = "datos/registros.csv"
    ruta_reporte = "salida/reporte.md"

    if not os.path.exists(ruta_csv):
        print(f"Error: No se encuentra el archivo {ruta_csv}")
        return

    registros_validos = []
    registros_omitidos = 0
    total_recaudado = 0

    # Leer el archivo CSV aplicando manejo de errores try/except fila por fila
    with open(ruta_csv, mode='r', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            try:
                # Intentamos validar y convertir los datos numéricos y campos obligatorios
                id_reg = int(fila["id"])
                fecha = fila["fecha"].strip()
                tipo_animal = fila["tipo_animal"].strip()
                costo = int(fila["costo_adopcion"])

                # Si la fecha está vacía o el tipo de animal está vacío, forzamos un error
                if not fecha or fecha == "fecha-invalida" or not tipo_animal:
                    raise ValueError("Campo clave con formato inválido o vacío")

                # Si todo está bien, acumulamos la información válida
                total_recaudado += costo
                registros_validos.append(fila)

            except (ValueError, KeyError, TypeError) as e:
                # El bloque try/except captura la falla en la fila dañada y continúa sin detener el script
                registros_omitidos += 1
                continue

    # Generar la gráfica interactiva requerida invocando a grafica.py
    crear_grafica()

    # Asegurar que exista la carpeta de salida
    os.makedirs("salida", exist_ok=True)

    # Escribir el informe en formato Markdown (.md)
    total_procesados = len(registros_validos)
    
    contenido_md = f"""# Reporte Ejecutivo: Refugio de Animales

## Resumen General de Operaciones

* **Total de registros válidos procesados:** {total_procesados}
* **Registros descartados por errores/datos corruptos:** {registros_omitidos}
* **Total recaudado en cuotas de adopción:** ${total_recaudado:,.2f} COP

---

## Control de Calidad y Manejo de Excepciones

Durante el procesamiento automatizado, la aplicación utilizó bloques `try/except` para prevenir caídas imprevistas del sistema. Se omitieron un total de **{registros_omitidos} filas** que contenían inconsistencias (como costos no numéricos o fechas inválidas).

---

## Visualización Interactiva

La visualización de distribución por tipo de animal ha sido generada exitosamente. Puedes consultar el archivo interactivo adjunto en:
`salida/grafica.html`

---
*Reporte generado automáticamente por Valeriana Software.*
"""

    with open(ruta_reporte, mode='w', encoding='utf-8') as f_md:
        f_md.write(contenido_md)

    print(f"¡Éxito! Reporte generado correctamente en: {ruta_reporte}")
    print(f"Se procesaron {total_procesados} filas válidas y se omitieron {registros_omitidos} filas dañadas.")

if __name__ == "__main__":
    procesar_datos_y_generar_reporte()