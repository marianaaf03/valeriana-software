import csv
import random

# ==========================================
# TICKET 1: Generar datos simulados del Refugio de Animales
# Responsable: Mariana Alvarez Franco
# ==========================================

especies = ["Perro", "Gato", "Conejo", "Hamster"]
razas = ["Criollo", "Golden", "Siames", "Angora", "Labrador"]
estados = ["Disponible", "Adoptado", "En tratamiento", "Reservado"]
medios_pago = ["Efectivo", "Transferencia", "Nequi"]

def generar_registros():
    """Genera 100 registros válidos y 5 registros con errores intencionales."""
    registros = []
    
    # 1. Generación de 100 filas de datos válidos
    for i in range(1, 101):
        reg = {
            "id": i,
            "fecha": f"2026-10-{random.randint(1, 28):02d}",
            "tipo_animal": random.choice(especies),
            "especie": random.choice(razas),
            "edad_meses": random.randint(2, 120),
            "costo_adopcion": random.randint(30000, 150000),
            "medio_pago": random.choice(medios_pago),
            "estado": random.choice(estados)
        }
        registros.append(reg)
    
    # 2. Inserción de al menos 5 filas dañadas a propósito para probar el try/except del Ticket 2
    registros.append({"id": 101, "fecha": "2026-10-10", "tipo_animal": "Perro", "especie": "Criollo", "edad_meses": 12, "costo_adopcion": "", "medio_pago": "Efectivo", "estado": "Disponible"})
    registros.append({"id": 102, "fecha": "fecha-invalida", "tipo_animal": "Gato", "especie": "Siames", "edad_meses": 6, "costo_adopcion": 50000, "medio_pago": "Nequi", "estado": "Adoptado"})
    registros.append({"id": 103, "fecha": "2026-10-12", "tipo_animal": "Conejo", "especie": "Angora", "edad_meses": 4, "costo_adopcion": "treinta-mil", "medio_pago": "Transferencia", "estado": "Reservado"})
    registros.append({"id": 104, "fecha": "", "tipo_animal": "Perro", "especie": "Golden", "edad_meses": 24, "costo_adopcion": 80000, "medio_pago": "Efectivo", "estado": "Disponible"})
    registros.append({"id": 105, "fecha": "2026-10-15", "tipo_animal": "", "especie": "Criollo", "edad_meses": 8, "costo_adopcion": 40000, "medio_pago": "Nequi", "estado": "Adoptado"})

    return registros

def guardar_csv():
    """Crea la ruta 'datos/registros.csv' y escribe todos los diccionarios en formato CSV."""
    ruta = "datos/registros.csv"
    datos = generar_registros()
    keys = datos[0].keys()
    
    with open(ruta, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(datos)
        
    print(f"¡Éxito! Archivo de registros generado correctamente en: {ruta}")

if __name__ == "__main__":
    guardar_csv()