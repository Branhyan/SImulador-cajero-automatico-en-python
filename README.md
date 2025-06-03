Cajero Automático en Python
Este es un proyecto simple de consola en Python que simula el funcionamiento básico de un cajero automático. El programa permite al usuario:

-Verificar su PIN

-Consultar el saldo

-Depositar dinero

-Retirar dinero

-Cambiar el PIN

-Ver el historial de transacciones

Requisitos
-Python 3.10 o superior (Ya que usa match-case)

-Se usa en la terminal (de momento)

Cómo ejecutar
Clonarlo y ejecutar el archivo Simulador_Automático.py


-Funcionalidades
-Inicio con verificación de PIN (máximo 3 intentos)

-Consulta de saldo

-Depósito de dinero (montos predefinidos o personalizados)

-Retiros con validación de fondos

-Cambio de PIN con restricciones:

-No puede ser igual al anterior

-Debe ser numérico y de 4 dígitos

-Historial de transacciones con fecha, hora, tipo y cantidad



Notas
-El PIN inicial por defecto es 1234

-El saldo inicial es $1000

-Las funciones están documentadas con comentarios para facilitar su comprensión

📚 Aprendizajes
Este proyecto sirvió para practicar:
-Diccionarios
-Funciones
-Manejo de errores con try/except
-Bucles while
-Condicionales match-case
-Módulo datetime
-Validaciones básicas de entrada

Futuras actualizaciones: 
-Implementar SQLite para guardar cambios y agregar diferentes usuarios
-Añadir una interfaz simple con Tkinter

