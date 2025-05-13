import random
import datetime
import os
import json

# Ruta de archivo para los remitentes y envios
RUTA_REMITENTES = os.path.join('data', 'remitentes.json')
RUTA_ENVIOS = os.path.join('data', 'envios.json')

# Estado inicial posible
ESTADO_INICIAL = "En camino."

# Cargar remitentes
def cargar_remitentes():
    if os.path.exists(RUTA_REMITENTES):
        with open(RUTA_REMITENTES, 'r') as archivo:
            return json.load(archivo)
    return []

# Cargar envios existentes
def cargar_envios():
    if os.path.exists(RUTA_ENVIOS):
        with open(RUTA_ENVIOS, 'r') as archivo:
            return json.load(archivo)
    return []

# Guardar envios en archivo
def guardar_envios(envios):
    os.makedirs(os.path.dirname(RUTA_ENVIOS), exist_ok=True)
    with open(RUTA_ENVIOS, 'w') as archivo:
        json.dump(envios, archivo, indent=4, ensure_ascii=False)

# Generar numero de guia unico
def generar_numero_guia():
    return str(random.randint(100000, 999999))

# Registrar un envio
def registrar_envio():
    remitentes = cargar_remitentes()
    print("=== Registro de Envío ===")
    
    id_remitente = input("Número de identificación del remitente: ")
    if not any(remitente['id'] == id_remitente for remitente in remitentes):
        print("El remitente no está registrado. El envío no puede ser procesado.")
        return

    nombre_destinatario = input("Nombre del destinatario: ")
    direccion_destinatario = input("Dirección del destinatario: ")
    telefono_destinatario = input("Teléfono del destinatario: ")
    ciudad_destinatario = input("Ciudad del destinatario: ")
    barrio_destinatario = input("Barrio del destinatario: ")

    fecha_envio = datetime.datetime.now().strftime("%Y-%m-%d")
    hora_envio = datetime.datetime.now().strftime("%H:%M:%S")
    numero_guia = generar_numero_guia()

    envio = {
        "fecha_envio": fecha_envio,
        "hora_envio": hora_envio,
        "numero_guia": numero_guia,
        "estado": ESTADO_INICIAL,
        "remitente": {
            "id": id_remitente
        },
        "destinatario": {
            "nombre": nombre_destinatario,
            "direccion": direccion_destinatario,
            "telefono": telefono_destinatario,
            "ciudad": ciudad_destinatario,
            "barrio": barrio_destinatario
        }
    }

    envios = cargar_envios()
    envios.append(envio)
    guardar_envios(envios)

    print(f"\n¡Envío registrado con éxito!\nNúmero de Guía: {numero_guia}\nEstado inicial: {ESTADO_INICIAL}")
    return envio

#Menu principal de envios.
def main_envios():
    envio = registrar_envio()
    if envio:
        print("\nResumen del Envío:")
        print(f"Fecha: {envio['fecha_envio']} | Hora: {envio['hora_envio']}")
        print(f"Número de Guía: {envio['numero_guia']}")
        print(f"Estado: {envio['estado']}")
        print(f"Destinatario: {envio['destinatario']['nombre']}")
        print(f"Remitente ID: {envio['remitente']['id']}")
        print('\nRegresando al menu principal.')

def mostrar_historial_envios():
    envios = cargar_envios()

    if not envios:
        print("No hay envíos registrados aún.")
        return

    print("\n=== Historial de Envíos Registrados ===")
    for i, envio in enumerate(envios, start=1):
        print(f"\nEnvío #{i}")
        print(f"Número de Guía   : {envio['numero_guia']}")
        print(f"Fecha y Hora     : {envio['fecha_envio']} {envio['hora_envio']}")
        print(f"Estado           : {envio['estado']}")
        print(f"Remitente ID     : {envio['remitente']['id']}")
        print(f"Destinatario     : {envio['destinatario']['nombre']}")
        print(f"  Dirección      : {envio['destinatario']['direccion']}")
        print(f"  Teléfono       : {envio['destinatario']['telefono']}")
        print(f"  Ciudad         : {envio['destinatario']['ciudad']}")
        print(f"  Barrio         : {envio['destinatario']['barrio']}")

#Impide que al exportarse se ejecute directamente.
if __name__ == "__main__":
    main_envios()