class CasaDelArbol:
    def __init__(self):
        self.luces_encendidas = False
        self.puerta_secreta_abierta = False

    def encender_luces(self):
        if not self.luces_encendidas:
            self.luces_encendidas = True
            print("\nLas luces están ahora encendidas.")
        else:
            print("\nLas luces ya están encendidas.")

    def apagar_luces(self):
        if self.luces_encendidas:
            self.luces_encendidas = False
            print("\nLas luces están ahora apagadas.")
        else:
            print("\nLas luces ya están apagadas.")

    def abrir_puerta_secreta(self):
        if not self.puerta_secreta_abierta:
            self.puerta_secreta_abierta = True
            print("\nLa puerta secreta está ahora abierta. ¡Descubre los secretos que guarda!")
        else:
            print("\nLa puerta secreta ya está abierta.")

    def cerrar_puerta_secreta(self):
        if self.puerta_secreta_abierta:
            self.puerta_secreta_abierta = False
            print("\nLa puerta secreta está ahora cerrada.")
        else:
            print("\nLa puerta secreta ya está cerrada.")

def menu():
    casa = CasaDelArbol()
    while True:
        print("\nControl de la Casa del Árbol")
        print("\n")
        print("1. Encender luces")
        print("2. Apagar luces")
        print("3. Abrir puerta secreta")
        print("4. Cerrar puerta secreta")
        print("5. Salir\n")
        opcion = input("Selecciona una opción: \n")

        if opcion == '1':
            casa.encender_luces()
        elif opcion == '2':
            casa.apagar_luces()
        elif opcion == '3':
            casa.abrir_puerta_secreta()
        elif opcion == '4':
            casa.cerrar_puerta_secreta()
        elif opcion == '5':
            print("Saliendo del control de la casa del árbol.")
            break
        else:
            print("Opción inválida. Por favor, elige una opción del 1 al 5.")

if __name__ == "__main__":
    menu()
