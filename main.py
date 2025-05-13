from admin import main_administrador
from clientes import main_clientes
from remitentes import main_remitentes

#Menu principal del programa.
print('\nBienvenido a Mercado libre entregas.')
while True:
    print('''\n    1. Administradores.
    2. Clientes y nuevas personas.
    3. Solo empleados o personas que deseen trabajar con nosotros.
    4. Exit.''')
    try:
        opcion = int(input('Escribe una opcion (solo numeros!)=> '))
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número.")
        continue
    
    if opcion == 1:
            main_administrador()

    elif opcion == 2:
        main_clientes()

    elif opcion == 3:
        main_remitentes()

    elif opcion == 4:
        print('Gracias por usas los servicios de mercado libre :3')
        break