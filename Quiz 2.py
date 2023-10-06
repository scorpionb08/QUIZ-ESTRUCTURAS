#2222621 Diego alejandro rodriguez
#2222622 Daniel Calderon Bonilla
class Cliente:
    def __init__(self, cedula, nombre, habitacion):
        self.cedula = cedula
        self.nombre = nombre
        self.habitacion = habitacion
        self.siguiente = None

class Habitacion:
    def __init__(self, numero):
        self.numero = numero
        self.ocupada = False
        self.siguiente = None

class Hotel: 
    def __init__(self):
        self.lalista = []
        self.habitaciones = None
        self.clientes = None
        self.habitaciones_disponibles = []

    def listar(self):
        habitaciones_disponibles = []
        habitacion = self.habitaciones
        while habitacion:
            if not habitacion.ocupada:
                habitaciones_disponibles.append(habitacion.numero)
            habitacion = habitacion.siguiente
        return habitaciones_disponibles

    def listarunable(self):
        habitaciones_no_disponibles = []
        habitacion = self.habitaciones
        while habitacion:
            if habitacion.ocupada:
                habitaciones_no_disponibles.append(habitacion.numero)
            habitacion = habitacion.siguiente
        return habitaciones_no_disponibles
    
    def inicializar_habitaciones_disponibles(self):
        habitacion = self.habitaciones
        while habitacion:
            if not habitacion.ocupada:
                self.habitaciones_disponibles.append(habitacion.numero)
            habitacion = habitacion.siguiente

    def actualizar_habitacion(self, numero_habitacion, ocupada):
        habitacion = self.habitaciones
        while habitacion:
            if habitacion.numero == numero_habitacion:
                habitacion.ocupada = ocupada
                return

    def agregar_cliente(self):
        nombre = input("\nIngrese el nombre del huésped: ")
        cedula = int(input("\nIngrese la cédula del huésped: "))

        if not self.habitaciones_disponibles:
            print("\nTodas las habitaciones están ocupadas.")
            return
        print("\nHabitaciones disponibles:", self.habitaciones_disponibles)
        habitacion = int(input("Ingrese el número de habitación: "))
        
        if habitacion not in self.habitaciones_disponibles:
            print("\nLa habitación no existe o ya está ocupada.")
            return

        self.actualizar_habitacion(habitacion, ocupada=True)

        self.habitaciones_disponibles.remove(habitacion)

        clientenuevo = Cliente(cedula, nombre, habitacion)
        clientenuevo.siguiente = self.clientes
        self.clientes = clientenuevo
        self.lalista.append(clientenuevo)

    def registrar_habitacion(self, numero):
        nueva_habitacion = Habitacion(numero)
        nueva_habitacion.siguiente = self.habitaciones
        self.habitaciones = nueva_habitacion

    def consultar(self):
        elec = int(input("Ingrese el método de búsqueda: (1) = Individual, (2) = Total"))
        if elec == 1: 
            cedula = int(input("Ingrese la cédula del huésped a buscar"))

            cliente_encontrado = None  

            for cliente in self.lalista:
                if cliente.cedula == cedula:
                    cliente_encontrado = cliente
                    break  
            if cliente_encontrado:
                print(f"Cédula: {cliente_encontrado.cedula}, Nombre: {cliente_encontrado.nombre}, Habitación: {cliente_encontrado.habitacion}")
            else: 
                print("Huésped no hallado")
            
        if elec == 2: 
            elec2 = int(input("Seleccione por qué dato desea buscarlos: (1) Cédula, (2) Orden de llegada"))

            if elec2 == 1:
                for cliente in self.lalista:
                    print(f"\nCédula: {cliente.cedula}, Nombre: {cliente.nombre}")

            elif elec2 == 2: 
                print("\n\tEl orden va desde el que ingresó más antiguamente hasta el que ingresó más recientemente")
                for cliente in self.lalista:
                    print(f"\nCédula: {cliente.cedula}, Nombre: {cliente.nombre}, Habitación: {cliente.habitacion}")

    def consultar_cuarto(self):
        print("\n INGRESE QUÉ DESEA VER: (1) CUARTOS DISPONIBLES. (2) CUARTOS OCUPADOS")
        ech = int(input(''))

        if ech == 1: 
            habitaciones_disponibles = self.listar()
            print("\nHabitaciones disponibles:", habitaciones_disponibles)
        elif ech == 2:
            habitaciones_no_disponibles = self.listarunable()
            print("\nHabitaciones no disponibles:", habitaciones_no_disponibles)
    
    def eliminar_cliente(self, cedula):
        cliente_anterior = None
        cliente_actual = self.clientes

        while cliente_actual:
            if cliente_actual.cedula == cedula:
                if cliente_anterior:
                    cliente_anterior.siguiente = cliente_actual.siguiente
                else:
                    self.clientes = cliente_actual.siguiente

                
                self.actualizar_habitacion(cliente_actual.habitacion, ocupada=False)
                self.habitaciones_disponibles.append(cliente_actual.habitacion)

                
                self.lalista.remove(cliente_actual)
                print(f"Cliente con cédula {cedula} eliminado.")
                return

            cliente_anterior = cliente_actual
            cliente_actual = cliente_actual.siguiente

        print(f"Cliente con cédula {cedula} no encontrado.")

hotel = Hotel()
hotel.registrar_habitacion(1001)
hotel.registrar_habitacion(5896)
hotel.registrar_habitacion(4265)
hotel.registrar_habitacion(709)
hotel.registrar_habitacion(1896)
hotel.registrar_habitacion(200)

hotel.inicializar_habitaciones_disponibles()

while True:
    print("\nMenú del Hotel")
    print("1. Agregar cliente")
    print("2. Eliminar cliente")
    print("3. Consultar clientes")
    print("4. Consultar habitaciones")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        hotel.agregar_cliente()
    elif opcion == "2":
        cedula = int(input("\nIngrese la cédula del cliente a eliminar: "))
        hotel.eliminar_cliente(cedula)
    elif opcion == "3":
        hotel.consultar()
    elif opcion == "4":
        hotel.consultar_cuarto()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")