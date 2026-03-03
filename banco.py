# función para depositar dinero
def depositar(saldo):
    cantidad = float(input("Ingrese la cantidad a depositar: "))
    if cantidad > 0:
        saldo += cantidad
        print(f"Depósito exitoso. Su nuevo saldo es: {saldo:.2f}")
    else:
        print("Cantidad inválida. El depósito debe ser mayor a cero.")
    return saldo

# función para retirar dinero
def retirar(saldo):
    cantidad = float(input("Ingrese la cantidad a retirar: "))
    if cantidad > 0:
        if cantidad <= saldo:
            saldo -= cantidad
            print(f"Retiro exitoso. Su nuevo saldo es: {saldo:.2f}")
        else:
            print("Fondos insuficientes. No puede retirar más de su saldo actual.")
    else:
        print("Cantidad inválida. El retiro debe ser mayor a cero.")
    return saldo

#función para mostrar el saldo
def mostrar_saldo(saldo):
    print(f"Su saldo actual es: {saldo:.2f}")
    
# función principal
def main():
    saldo = 0.0
    
    while True:
        print("\nBienvenido al Banco")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Mostrar saldo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            saldo = depositar(saldo)
        elif opcion == '2':
            saldo = retirar(saldo)
        elif opcion == '3':
            mostrar_saldo(saldo)
        elif opcion == '4':
            print("Gracias por usar el Banco. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

main()