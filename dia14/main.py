import os
from pathlib import Path
import shutil

def crear_carpeta(ruta):
    # Crear una carpeta
    Path(ruta).mkdir(parents=True, exist_ok=True)
    print(f"Carpeta '{ruta}' creada.")

def borrar_carpeta(ruta):
    # Borrar una carpeta
    directorio = Path(ruta)
    if directorio.exists() and directorio.is_dir():
        shutil.rmtree(directorio)
        print(f"Carpeta '{ruta}' borrada.") 
    else:
        print(f"Carpeta '{ruta}' no existe para borrar.")

def crear_fichero_texto():
    # Crear un fichero de texto
    fichero = "mi_fichero.txt"
    with open(fichero, "w") as f:
        f.write("Este es un fichero de texto de ejemplo.")
    print(f"Fichero de texto '{fichero}' creado.")

def crear_fichero_binario():

    # Crear un fichero binario
    fichero = "mi_fichero.bin"
    with open(fichero, "wb") as f:
        f.write(b'\x00\x01\x02\x03\x04')
    print(f"Fichero binario '{fichero}' creado.")

def borrar_fichero(fichero):

    fichero = Path(fichero)
    if fichero.exists() and fichero.is_file():
        fichero.unlink()
        print(f"Fichero '{fichero}' borrado.")
    else:
        print(f"Fichero '{fichero}' no existe para borrar.")

def mover_fichero(origen, destino):
    
    path_origen = Path(origen)
    path_destino = Path(destino)
    if path_origen.exists() and path_origen.is_file():
        shutil.move(str(path_origen), str(path_destino))
        print(f"Fichero movido de '{origen}' a '{destino}'.")
    else:
        print(f"Fichero '{path_origen}' no existe para mover.")


def menu_app ():
    while True:
        print("\n\033[0;97m=== Menú de opciones ===\033[0m")
        print("1. Crear carpeta")
        print("2. Borrar carpeta")
        print("3. Crear fichero de texto")
        print("4. Crear fichero binario")
        print("5. Borrar fichero")
        print("6. Mover fichero")
        print("0. Salir")

        opcion = input("\n\033[0;97mIngrese el número de la opción deseada: \033[0m")

        if opcion == "0":
            print("Saliendo del programa...")
            break
        
        elif opcion == "1":
            ruta = input("\033[0;97mIngrese la ruta de la carpeta a crear: \033[0m")
            crear_carpeta(ruta)
        
        elif opcion == "2":
            ruta = input("\033[0;97mIngrese la ruta de la carpeta a borrar: \033[0m")
            borrar_carpeta(ruta)
        
        elif opcion == "3":
            crear_fichero_texto()
        
        elif opcion == "4":
            crear_fichero_binario()
        
        elif opcion == "5":
            fichero = input("\033[0;97mIngrese el nombre del fichero a borrar: \033[0m")
            borrar_fichero(fichero)
        
        elif opcion == "6":
            origen = input("\033[0;97mIngrese la ruta del fichero a mover: \033[0m")
            destino = input("\033[0;97mIngrese la ruta de destino: \033[0m")
            mover_fichero(origen, destino)
        
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu_app()  