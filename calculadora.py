def calculadora():
    while True:
        print("\n=================================")
        print("     CALCULADORA VS CODE        ")
        print("=================================")
        print("1. Suma (+)")
        print("2. Resta (-)")
        print("3. Multiplicación (*)")
        print("4. División (/)")
        print("5. Salir")
        print("=================================")
        
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '5':
            print("¡Hasta luego!")
            break

        if opcion in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print(" Error: Ingresa solo números válidos.")
                continue

            if opcion == '1':
                print(f"\nResultado: {num1} + {num2} = {num1 + num2}")
            elif opcion == '2':
                print(f"\nResultado: {num1} - {num2} = {num1 - num2}")
            elif opcion == '3':
                print(f"\nResultado: {num1} * {num2} = {num1 * num2}")
            elif opcion == '4':
                if num2 != 0:
                    print(f"\nResultado: {num1} / {num2} = {num1 / num2}")
                else:
                    print("\n Error: No se puede dividir entre cero.")
        else:
            print(" Opción no válida.")

calculadora()
