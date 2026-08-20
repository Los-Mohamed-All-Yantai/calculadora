import math

def mostrar_menu():
    print("\n=================================")
    print("     CALCULADORA AVANZADA        ")
    print("=================================")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Potencia (x^y)")
    print("6. Raíz cuadrada (√x)")
    print("7. Módulo / Residuo (%)")
    print("8. Ver Historial")
    print("9. Salir")
    print("=================================")

def calculadora():
    historial = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-9): ").strip()

        if opcion == '9':
            print("\n¡Gracias por usar la calculadora!")
            break

        if opcion == '8':
            print("\n--- HISTORIAL DE OPERACIONES ---")
            if not historial:
                print("No hay operaciones registradas aún.")
            else:
                for idx, op in enumerate(historial, 1):
                    print(f"{idx}. {op}")
            continue

        if opcion in ('1', '2', '3', '4', '5', '7'):
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("\n Error: Ingresa un número válido.")
                continue

            if opcion == '1':
                res = num1 + num2
                registro = f"{num1} + {num2} = {res}"
            elif opcion == '2':
                res = num1 - num2
                registro = f"{num1} - {num2} = {res}"
            elif opcion == '3':
                res = num1 * num2
                registro = f"{num1} * {num2} = {res}"
            elif opcion == '4':
                if num2 == 0:
                    print("\n Error: No se puede dividir entre cero.")
                    continue
                res = num1 / num2
                registro = f"{num1} / {num2} = {res}"
            elif opcion == '5':
                res = num1 ** num2
                registro = f"{num1} ^ {num2} = {res}"
            elif opcion == '7':
                if num2 == 0:
                    print("\n Error: No se puede calcular el módulo con cero.")
                    continue
                res = num1 % num2
                registro = f"{num1} % {num2} = {res}"

            historial.append(registro)
            print(f"\nResultado: {registro}")

        elif opcion == '6':
            try:
                num = float(input("Ingresa el número: "))
                if num < 0:
                    print("\n Error: No se puede calcular la raíz cuadrada de un número negativo.")
                    continue
                res = math.sqrt(num)
                registro = f"√{num} = {res}"
                historial.append(registro)
                print(f"\nResultado: {registro}")
            except ValueError:
                print("\n Error: Ingresa un número válido.")
        else:
            print("\n Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    calculadora()
# soy una gampiiii