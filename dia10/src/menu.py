from src.screen import paint_logo, paint_menu, get_data
from src.conf import config

def main():
    config_options = config()
    while True:
        paint_logo()
        paint_menu()

        opcion = input("\n\033[0;97mIngrese el número de la opción deseada: \033[0m")

        if opcion == "0":
            paint_logo()
            print("Saliendo del programa...")
            break
        
        elif opcion.isdigit() and 1 <= int(opcion) <= len(config_options):
            option_index = int(opcion) - 1
            selected_option = config_options[option_index]
            if selected_option:
                values = []
                for i in range(selected_option["values"]):
                    value = get_data(f"Ingrese el valor {i + 1}: ")
                    values.append(value)
                selected_option["function"](*values)

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


        input("\n\033[0;97mPresiona Enter para continuar...\033[0m")