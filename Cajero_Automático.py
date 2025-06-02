cuenta = {                                                        #Hago un diccionario con la cuenta enlazando el pin y cual es, así como el saldo y cual es
    "pin": "1234",
    "saldo": 1000
}

intentos_fallidos = 0                                      #Variable para contar los intentos fallidos al verificar el PIN
contador_nuevo_pin = 0                                     #Variable para contarl las veces que se intenta cambiar al mismo PIN
def verificar_pin():
    global intentos_fallidos                                       #global es para que use la variable que está definida fuera de la función, sino se haría una variable nueva dentro de la función
    while intentos_fallidos < 3:
        try:
            pin_ingresado = input("Ingrese su PIN: ")               #Se pide el PIN al usuario, se usa int() para que sea un número y no un string, ya que el PIN es numérico
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

def depositar_dinero():
    monto = float(input("¿Cuanto dinero pensás depositar?:  "))
    if monto < 0:
        print("Debes depositar una cantidad positiva.")
        print("Vuelve a intentarlo.")
    else:
        cuenta["saldo"] += monto                                                   #+= se usa para sumar y a la vez modificar la variable con la suma
        print(f"${monto} depositados. Ahora el saldo es de: ${cuenta['saldo']}")

def retirar_dinero():
    try:
        cantidad = float(input("¿Cuanto dinero vas a retirar?:  "))
        if cantidad > cuenta["saldo"]:
            print("Saldo insuficiente ponga una cantidad adecuada")
        else:
            cuenta["saldo"] -= cantidad
            print(f"Has retirado ${cantidad} ahora te quedan ${cuenta['saldo']}")
    except ValueError:
        print("Debe ingresar un número. Intentelo nuevamente") #Si no se ingresa un número en lugar de dar error, se le pide al usuario que ingrese un número
def cambiar_pin():
    try:    
        if verificar_pin():
            while True:
                nuevo_pin = (input("Inserte el nuevo PIN: "))
                global contador_nuevo_pin
                if len(nuevo_pin) != 4:                                  #Verifico que el nuevo PIN tenga 4 dígitos
                    print("El PIN debe de tener 4 dígitos. Vuelve a intentarlo.")
                    continue
                if not nuevo_pin.isdigit():                                 #Verifico que el nuevo PIN sea sea un número
                    print("El PIN solo debe tener numeros. Vuelve a intentarlo.")
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
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                consultar_saldo()
            elif opcion == "2":
                depositar_dinero()
            elif opcion == "3":
                retirar_dinero()
            elif opcion == "4":
                cambiar_pin()
            elif opcion == "5":
                print("Gracias por usar el cajero, nos vemos!")
                break
            else:
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