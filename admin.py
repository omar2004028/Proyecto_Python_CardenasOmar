from clientes import cargar_clientes, guardar_clientes,registrar_nuevo_cliente
from remitentes import cargar_remitentes,guardar_remitentes,registrar_remitentes
from envios import mostrar_historial_envios
import os
import json
#Rutas de los archivos json...
RUTA_CLIENTES = os.path.join('data', 'clientes.json')
RUTA_REMITENTES = os.path.join('data', 'remitentes.json')
RUTA_ENVIOS = os.path.join('data', 'envios.json')

#Funcion para mostrar cuanto clientes estan registrados.
def clientes_registrados():
        clientes = cargar_clientes()
        print("\nClientes registrados:")
        for c in clientes:
            print(f"- {c['nombres']} {c['apellidos']}")

#Funcion para mostrar cuantos remitentes estan registrados.
def remitentes_registrados():
    remitentes = cargar_remitentes()
    if not remitentes:
        print("No hay remitentes registrados.")
        return

    print("\n=== Lista de Remitentes ===")
    for r in remitentes:
        print(f"- {r['nombre']} (ID: {r['id']})")


#Funcion para eliminar clientes.
def eliminar_cliente(nombre):
    clientes = cargar_clientes()
    original = len(clientes)

    # Filtrar todos los clientes que no tienen ese nombre
    clientes_filtrados = [c for c in clientes if c["nombres"].lower() != nombre.lower()]

    if len(clientes_filtrados) < original:
        guardar_clientes(clientes_filtrados)
        print(f"Cliente(s) con nombre '{nombre}' eliminado(s) exitosamente.")
    else:
        print(f"No se encontró ningún cliente con el nombre '{nombre}'.")

#Funcion para eliminar remitentes por nombre.
def eliminar_remitente(nombre):
    remitentes = cargar_remitentes()
    original = len(remitentes)

    # Filtrar todos los remitentes que no tienen ese nombre
    remitentes_filtrados = [r for r in remitentes if r["nombre"].lower() != nombre.lower()]

    if len(remitentes_filtrados) < original:
        guardar_remitentes(remitentes_filtrados)
        print(f"Remitente(s) con nombre '{nombre}' eliminado(s) exitosamente.")
    else:
        print(f"No se encontró ningún remitente con el nombre '{nombre}'.")

#Funcion para eliminar el historial de envios.
def eliminar_historial_envios():
    confirmacion = input("¿Estás seguro de que deseas eliminar todo el historial de envíos? (s/n): ").lower()
    if confirmacion == 's':
        with open(RUTA_ENVIOS, 'w') as archivo:
            json.dump([], archivo, indent=4)
        print(" Historial de envíos eliminado correctamente.")
    else:
        print(" Operación cancelada. El historial no fue eliminado.")

def ver_clientes_remitentes_registrados():
    while True:
        print('''\nBase de registros.
          1. Ver clientes registrados.
          2. Ver remitentes registrados.
          3. Regresar.''')
        try:
            opcion = int(input('Digita aqui => '))
        except ValueError:
            print('Digita solo numeros.')
            continue
        if opcion == 1:
            clientes_registrados()

        elif opcion == 2:
            remitentes_registrados()

        elif opcion == 3:
            print('Regresando.')
            break

        else:
            print('opcion no valida.')
       

#Principal ejecutador de las funciones admin.
def main_administrador():
    print('Por favor digite su nombre y clave.                         (admin-12345)')#LaDejoEscritaParaQueNoSeMolestenEnBuscarla.

    PASSWORD = {'omar': '098765', 'admin': '12345'}

    nombre = input("Nombre de usuario: ")
    clave = input("Contraseña: ")

    if nombre in PASSWORD and PASSWORD[nombre] == clave:
        print("\n===> Bienvenido Sr Administrador <===")

        while True:
            print(''' \n     1. Registrar cliente.
     2. Eliminar cliente.
     3. Registrar remitente.
     4. Eliminar remitente.
     5. Mostrar historial de envios.
     6. Eliminar todo el historial de envios.
     7. ver clientes y remitentes registrados.
     8. Salir al menu principal.''')
            try:
                opcion = int(input('Digite una opcion. > '))
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número.")
                continue

            if opcion == 1:
                registrar_nuevo_cliente()

            elif opcion == 2:
                clientes_registrados()
                nombre = input("Ingresa el nombre del cliente a eliminar: ")
                eliminar_cliente(nombre)

            elif opcion == 3:
                registrar_remitentes()

            elif opcion == 4:
                remitentes_registrados()
                nombre = input("Ingresa el nombre del remitente a eliminar: ")
                eliminar_remitente(nombre)
            
            elif opcion == 5:
                mostrar_historial_envios()

            elif opcion == 6:
                eliminar_historial_envios()

            elif opcion == 7:
                ver_clientes_remitentes_registrados()

            elif opcion == 8:
                print('Regresando a menu principal.')
                break
            
            else:
                print('Opción no válida. Digite de nuevo.')

    else:
        print("Nombre o clave incorrectos")

#Impide que al exportarse se ejecute directamente.
if __name__=='__main__':
    main_administrador()

