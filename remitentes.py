import os
import json
from envios import main_envios,cargar_envios

#Ruta de archivos para los remitentes y envios.
RUTA_REMITENTES = os.path.join('data', 'remitentes.json')
RUTA_ENVIOS = os.path.join('data', 'envios.json')


def cargar_remitentes():
    if os.path.exists(RUTA_REMITENTES):
        try:
            with open(RUTA_REMITENTES, 'r') as archivo:
                return json.load(archivo)
        except json.JSONDecodeError:
            print(" El archivo de remitentes está vacío o corrupto. Se usará una lista vacía.")
            return []
    return []


def guardar_remitentes(remitentes):
    os.makedirs(os.path.dirname(RUTA_REMITENTES), exist_ok=True)
    with open(RUTA_REMITENTES, 'w') as archivo:
        json.dump(remitentes, archivo, indent=4, ensure_ascii=False)

#Registra un remitente con id propio.
def registrar_remitentes():
    remitentes = cargar_remitentes()

    print("\n=== Registro de Remitente ===")
    identificacion = input("Número de identificación: ")
        
    if any(r['id'] == identificacion for r in remitentes):
        print("Este remitente ya está registrado.")
        

    nombre = input("Nombre: ")
    telefono = input("Teléfono de contacto: ")
    direccion = input("Dirección: ")

    remitente = {
                "id": identificacion,
                "nombre": nombre,
                "telefono": telefono,
                "direccion": direccion
            }

    remitentes.append(remitente)
    guardar_remitentes(remitentes)
    print("Remitente registrado con éxito.")

#Menu principal de remitentes.
def main_remitentes():
    while True:
        print('\n=== Remitentes.Mercadolibre ===')
        print('1. Registrarse como remitente')
        print('2. Registrar pedido')
        print('3. Para ver los pedidos asignados del remitente.')
        print('4. para salir.')

        try:
            opcion = int(input('Digite una opción: '))
        except ValueError:
            print("Por favor, digita un número válido.")
            continue

        if opcion == 1:
            registrar_remitentes()

        elif opcion == 2:
            main_envios()
        
        elif opcion == 3:
            envios_por_remitente()

        elif opcion == 4:
            print("Saliendo del menú de remitentes...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

#Muestra los pedidos asignados del remitente.
def envios_por_remitente():
    id_remitente = input("Ingrese su número de identificación: ").strip()
    envios = cargar_envios()

    envios_del_remitente = [envio for envio in envios if envio["remitente"]["id"] == id_remitente]

    if not envios_del_remitente:
        print(f"No se encontraron envíos asignados al remitente con ID: {id_remitente}")
        return

    print(f"\n=== Envíos asignados al remitente con ID: {id_remitente} ===")
    for i, envio in enumerate(envios_del_remitente, start=1):
        print(f"\nEnvío #{i}")
        print(f"Número de Guía   : {envio['numero_guia']}")
        print(f"Fecha y Hora     : {envio['fecha_envio']} {envio['hora_envio']}")
        print(f"Estado           : {envio['estado']}")
        print(f"Destinatario     : {envio['destinatario']['nombre']}")
        print(f"  Dirección      : {envio['destinatario']['direccion']}")
        print(f"  Teléfono       : {envio['destinatario']['telefono']}")
        print(f"  Ciudad         : {envio['destinatario']['ciudad']}")
        print(f"  Barrio         : {envio['destinatario']['barrio']}")
        
#Muestra los remitentes registrados.
def mostrar_remitentes():
    remitentes = cargar_remitentes()
    if not remitentes:
        print("No hay remitentes registrados.")
        return

    print("\n=== Lista de Remitentes ===")
    for r in remitentes:
        print(f"- {r['nombre']} (ID: {r['id']})")

#Impide que al exportarse se ejecute directamente.   
if __name__ == '__main__':
    main_remitentes()