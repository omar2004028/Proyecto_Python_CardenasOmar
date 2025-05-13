import json
import os
from envios import cargar_envios

#Ruta de archivo json.
RUTA_CLIENTES = os.path.join('data', 'clientes.json')
RUTA_ENVIOS = os.path.join('data', 'envios.json')

#Lee y verifica si el archivo json existe si no lo crea.
def cargar_clientes():
    if os.path.exists(RUTA_CLIENTES):
        with open(RUTA_CLIENTES, 'r') as archivo:
         return json.load(archivo)
    return []

#Guarda los datos en el archivo json.
def guardar_clientes(clientes):
    os.makedirs(os.path.dirname(RUTA_CLIENTES), exist_ok=True)
    with open(RUTA_CLIENTES, 'w') as archivo:
        json.dump(clientes, archivo, indent=4, ensure_ascii=False)

#Retorna diccionario con todos los datos.
def registrar_cliente():
    print('\n==== Registro de clientes ====')
    cliente = {
        "nombres": input("Nombres: "),
        "apellidos": input("Apellidos: "),
        "identificacion": input("Número de identificación: "),
        "tipo_identificacion": input("Tipo de identificación (CC, TI, CE): ").upper(),
        "direccion": input("Dirección: "),
        "telefono_fijo": input("Teléfono fijo: "),
        "celular": input("Número celular: "),
        "barrio": input("Barrio de residencia: ")
    }
    return cliente
  
#Registra un nuevo cliente y lo guarda permanentemente en el archivo json. Luego muestra todos los clientes registrados.
def registrar_nuevo_cliente():
    clientes = cargar_clientes()
    nuevo_cliente = registrar_cliente()
    clientes.append(nuevo_cliente)
    guardar_clientes(clientes)
    print('Cliente registrado exitosamente!!!.')
    clientes_registrados()

#Muestra los clientes registrados.
def clientes_registrados():
        clientes = cargar_clientes()
        print("\nClientes registrados:")
        for c in clientes:
            print(f"- {c['nombres']} {c['apellidos']}")

#Aqui el cliente puede ver la info de su pedido.
def envios_clientes():
    nombre_destinatario = input("Ingresa el nombre del destinatario: ").strip().lower()
    envios = cargar_envios()

    # Filtramos envios donde el nombre coincida (ignorando mayusculas/minusculas)
    envios_destinatario = [
        envio for envio in envios
        if envio['destinatario']['nombre'].strip().lower() == nombre_destinatario
    ]

    if not envios_destinatario:
        print(f"No se encontraron envíos para el destinatario: {nombre_destinatario}")
        return

    print(f"\n=== Envíos para el destinatario: {nombre_destinatario} ===")
    for i, envio in enumerate(envios_destinatario, start=1):
        print(f"\nEnvío #{i}")
        print(f"Número de Guía   : {envio['numero_guia']}")
        print(f"Fecha y Hora     : {envio['fecha_envio']} {envio['hora_envio']}")
        print(f"Estado           : {envio['estado']}")
        print(f"Remitente ID     : {envio['remitente']['id']}")
        print(f"Dirección        : {envio['destinatario']['direccion']}")
        print(f"Teléfono         : {envio['destinatario']['telefono']}")
        print(f"Ciudad           : {envio['destinatario']['ciudad']}")
        print(f"Barrio           : {envio['destinatario']['barrio']}")

#Actualiza los datos de los clientes.
def actualizar_cliente():
    clientes_registrados()
    clientes = cargar_clientes()
    if not clientes:
        print("No hay clientes registrados.")
        return

    identificacion = input("Ingresa tu número de identificación: ").strip()
    cliente = next((c for c in clientes if c["identificacion"] == identificacion), None)

    if not cliente:
        print("Cliente no encontrado.")
        return

    print(f"\n=== Actualizar datos de {cliente['nombres']} {cliente['apellidos']} ===")
    print("Presiona Enter si no deseas cambiar algún dato.")

    nuevo_nombre = input(f"Nombres ({cliente['nombres']}): ").strip()
    nuevo_apellido = input(f"Apellidos ({cliente['apellidos']}): ").strip()
    nuevo_direccion = input(f"Dirección ({cliente['direccion']}): ").strip()
    nuevo_barrio = input(f"Barrio ({cliente['barrio']}): ").strip()
    nuevo_telefono_fijo = input(f"Teléfono fijo ({cliente['telefono_fijo']}): ").strip()
    nuevo_celular = input(f"Celular ({cliente['celular']}): ").strip()

    if nuevo_nombre:
        cliente["nombres"] = nuevo_nombre
    if nuevo_apellido:
        cliente["apellidos"] = nuevo_apellido
    if nuevo_direccion:
        cliente["direccion"] = nuevo_direccion
    if nuevo_barrio:
        cliente["barrio"] = nuevo_barrio
    if nuevo_telefono_fijo:
        cliente["telefono_fijo"] = nuevo_telefono_fijo
    if nuevo_celular:
        cliente["celular"] = nuevo_celular

    guardar_clientes(clientes)
    print("Información actualizada con éxito.")

#Menu principal de clientes.
def main_clientes():
    clientes = cargar_clientes()

    while True:
        print('''\nMenu de clientes.
        1. Quieres registrarte?.
        2. Ver tus envios.
        3. Actualiza tu informacion aqui.
        4. Si deseas salir.''')
        try:
            opcion = int(input('Digite la opcion deseada.=> '))
        except ValueError:
            print('\nPor favor digite solo numeros!.')
            continue

        if opcion == 1:
            registrar_nuevo_cliente()

            continuar = input("¿Deseas registrar otro cliente? (s/n): ").lower()
            if continuar != 's':
                break            
            print("\nClientes registrados:")
            for c in clientes:
                print(f"- {c['nombres']} {c['apellidos']}")

        elif opcion == 2:
            envios_clientes()

        elif opcion == 3:
            actualizar_cliente()

        elif opcion == 4:
            print('Saliendo al menu principal...')
            break


#Impide que al exportarse se ejecute directamente.
if __name__ == "__main__":
    main_clientes()