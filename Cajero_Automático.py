from datetime import datetime #Importo datetime para usar funciones de fecha y hora

cuenta = {                                                        #Hago un diccionario con la cuenta enlazando el pin y cual es, así como el saldo y cual es
    "pin": 1234,
    "saldo": 1000
}

historial_transacciones = []                                      #Lista para guardar el historial de transacciones

intentos_fallidos = 0                                      #Variable para contar los intentos fallidos al verificar el PIN
contador_nuevo_pin = 0                                     #Variable para contarl las veces que se intenta cambiar al mismo PIN

def verificar_pin():
    global intentos_fallidos                                       #global es para que use la variable que está definida fuera de la función, sino se haría una variable nueva dentro de la función
    while intentos_fallidos < 3:
        try:
            pin_ingresado = int(input("Ingrese su PIN: "))              #Se pide el PIN al usuario, se usa int() para que sea un número y no un string, ya que el PIN es numérico
            if pin_ingresado == cuenta["pin"]:
                return True                                          #Si el PIN es correcto la función da True
            else:
                intentos_fallidos += 1
                print("PIN incorrecto. Intentos restantes: ", 3 - intentos_fallidos)
        except ValueError:
            print("El PIN es un número.")    
    print("Demasiados intentos fallidos. Acceso bloqueado.")
    return False                                                    #Si se pasan los intentos fallidos da False
    
def consultar_saldo():
    print(f"El saldo actual es de: ${cuenta["saldo"]}")             #Se usa diccionario[valor] para llamar a un valor específico de un diccionario

def añadir_dinero(cantidad):                       #Hice una función para añadir dinero a la cuenta, para mayor limpieza del código
    if cantidad < 0:
        print("Debes depositar una cantidad positiva.")
        print("Vuelve a intentarlo.")
    else:
        cuenta["saldo"] += cantidad                                                  #+= se usa para sumar y a la vez modificar la variable con la suma
        print(f"${cantidad} depositados. Ahora el saldo es de: ${cuenta['saldo']}")
        historial_transacciones.append({"fecha": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),"hora": datetime.now().strftime("%H:%M"), "tipo": "Depósito", "cantidad": cantidad})  #Guardo la transacción en el historial
        return

def quitar_dinero(cantidad):
    if cantidad > cuenta["saldo"]:
        print("No tienes suficiente saldo para retirar esa cantidad.")
        return
    if cantidad < 0: 
        print("Debes retirar una cantidad positiva.")
        print("Vuelve a intentarlo.")
        return
    else:
        cuenta["saldo"] -= cantidad
        print(f"Se han retirado ${cantidad} del saldo. Le quedan: ${cuenta['saldo']}")
        historial_transacciones.append({"fecha": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),"hora": datetime.now().strftime("%H:%M"), "tipo": "Retiro", "cantidad": cantidad})
        return

def ver_historial():
    print("\n--- Historial de Transacciones ---")
    for historial in historial_transacciones:
        print(f"Fecha: {historial['fecha']}, Hora: {historial['hora']}, Tipo: {historial['tipo']}, Cantidad: ${historial['cantidad']}")

def depositar_dinero():
    try:
        while True:
                print("""
            --- Depositar Dinero ---
            1- 100
            2-250
            3-500
            4-1000
            5-1500
            6- Ingresar cantidad
            7- Volver al menú principal""")
                
                eleccion = int(input("Elija una opcion: "))
                match eleccion: #Usé match para hacer un menú de opciones, es una forma más limpia de hacerlo con un if-elif-else
                        case 1:
                            añadir_dinero(100)
                            break
                        case 2:
                            añadir_dinero(250)
                            break
                        case 3:
                            añadir_dinero(500)
                            break
                        case 4:
                            añadir_dinero(1000)
                            break
                        case 5:
                            añadir_dinero(1500)
                            break
                        case 6:
                            try:
                                cantidad = float(input("Ingrese la cantidad a depositar: "))
                                añadir_dinero(cantidad)
                                break
                            except ValueError:
                                print("Debe ingresar un número. Vielve a intentar")
                                continue
                        case 7:
                            print("Volviendo al menú principal...")
                            return
                        case _:
                            print("Opción no válida, vuelve a intentarlo.")
                            continue
    except ValueError:
        print("Debe ingresar un número. Intentelo nuevamente")

def retirar_dinero():
    try:
        while True:
                print("""
            --- Retirar Dinero ---
            1- 100
            2-250
            3-500
            4-1000
            5-1500
            6- Ingresar cantidad
            7- Volver al menú principal""")
                
                eleccion = int(input("Elija una opción: "))
                match eleccion:
                        case 1:
                            quitar_dinero(100)
                            break
                        case 2:
                            quitar_dinero(250)
                            break
                        case 3:
                            quitar_dinero(500)
                            break
                        case 4:
                            quitar_dinero(1000)
                            break
                        case 5:
                            quitar_dinero(1500)
                            break
                        case 6:
                            try:
                                cantidad = float(input("Ingrese la cantidad a retirar: "))
                                retirar_dinero(cantidad)
                                break
                            except ValueError:  
                                print("Debes ingresar un número. Vuelve a intentar")
                                continue
                        case 7:
                            print("Volviendo al menú principal...")
                            return
                        case _:
                            print("Opción no válida, vuelve a intentarlo.")
                            continue
    except ValueError:
        print("Debe ingresar un número. Intentelo nuevamente")
def cambiar_pin():
    try:    
        if verificar_pin():
            while True:
                nuevo_pin = (input("Inserte el nuevo PIN: "))
                global contador_nuevo_pin
                if len(nuevo_pin) != 4:                                  #Verifico que el nuevo PIN tenga 4 dígitos
                    print("El PIN debe de tener 4 dígitos. Vuelve a intentarlo.")
                    continue
                if not nuevo_pin.isdigit():                                 
                    print("El PIN solo debe tener numeros. Vuelve a intentarlo.")
                    continue
                if not nuevo_pin:
                    print("Escribe un PIN, vuelva a intentarlo.")
                    continue
                if nuevo_pin == cuenta["pin"]:                           #Verifico que el nuevo PIN no sea igual al actual
                    print("Es el mismo PIN que el actual, ingresa uno diferente.")
                    print("Si quieres mantener el PIN actual, ingresa el mismo PIN por " + str(3 - contador_nuevo_pin) + " vez/veces más.")
                    contador_nuevo_pin += 1
                    if contador_nuevo_pin == 3:
                        print("Has puesto el pin actual 3 veces, se mantiene el PIN actual")
                        break
                    continue
                else:
                    cuenta["pin" ] = nuevo_pin
                    print("PIN cambiado con éxito")
                    break
    except ValueError:
        print("Error inesperado, intenta nuevamente.") #Por si acaso jaja 

def menu():
    try:
        while True:
            print("\n--- CAJERO AUTOMÁTICO ---")
            print("\n1. Consultar saldo ")
            print("2. Depositar ")
            print("3. Retirar ")
            print("4. Cambiar PIN")
            print("5. Ver historial de transacciones")
            print("6. Salir")
            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 1:
                    consultar_saldo()
                case 2:
                    depositar_dinero()
                case 3:
                    retirar_dinero()
                case 4:
                    cambiar_pin()
                case 5:
                    ver_historial()
                case 6:
                    print("Gracias por usar el cajero, nos vemos!")
                    break
                case _:
                    print("Debes de elegir una de las opciones dadas, intenta de nuevo.")
    except ValueError:
        print("Debe ingresar un número. Intentelo nuevamente.")

def main():                                                                #Esto da inicio a todo el proceso, si bien en Python se puede llamar de cualquier forma en otros lenguajes como C# o C++ sin main() nada funciona
    if verificar_pin():
        menu()
    else:
        print("Fallaste con el PIN, el programa se cerrará")
if __name__ == "__main__":                                                #Esta condicional hace que el código dentro de main() se ejecute solo si el archivo se ejecuta directamente, no si se importa en otro archivo
    main()                                                        