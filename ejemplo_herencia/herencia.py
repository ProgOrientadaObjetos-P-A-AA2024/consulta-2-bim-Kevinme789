class Persona:
    def __init__(self, nombre, apellido, identificacion):
        self.nombre = nombre
        self.apellido = apellido
        self.identificacion = identificacion

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.identificacion})"


class InstitucionEducativa:
    def __init__(self, nombre, siglas):
        self.nombre = nombre
        self.siglas = siglas

    def __str__(self):
        return f"{self.nombre} ({self.siglas})"


class PrestamoAutomovil:
    def __init__(self, tipo, marca, garante, valor, beneficiario, meses, ciudad):
        self.tipo = tipo
        self.marca = marca
        self.garante = garante
        self.valor = valor
        self.beneficiario = beneficiario
        self.meses = meses
        self.ciudad = ciudad
        self.valor_pago_prestamo = 0

    def establecer_ciudad(self, ciudad):
        self.ciudad = ciudad

    def establecer_valor_pago_prestamo(self):
        self.valor_pago_prestamo = self.valor / self.meses

    def __str__(self):
        return (f"Tipo: {self.tipo}, Marca: {self.marca}, Garante: {self.garante}, "
                f"Valor: {self.valor}, Beneficiario: {self.beneficiario}, Meses: {self.meses}, "
                f"Ciudad: {self.ciudad}, Valor Pago Prestamo: {self.valor_pago_prestamo}")


class PrestamoEducativo:
    def __init__(self, beneficiario, meses, ciudad, nivel_estudio, institucion, valor):
        self.beneficiario = beneficiario
        self.meses = meses
        self.ciudad = ciudad
        self.nivel_estudio = nivel_estudio
        self.institucion = institucion
        self.valor = valor
        self.pago_mensual_prestamo = 0

    def establecer_ciudad(self, ciudad):
        self.ciudad = ciudad

    def establecer_pago_mensual_prestamo(self):
        self.pago_mensual_prestamo = self.valor / self.meses

    def __str__(self):
        return (f"Beneficiario: {self.beneficiario}, Meses: {self.meses}, Ciudad: {self.ciudad}, "
                f"Nivel de Estudio: {self.nivel_estudio}, Institucion: {self.institucion}, "
                f"Valor: {self.valor}, Pago Mensual Prestamo: {self.pago_mensual_prestamo}")


if __name__ == "__main__":
    prestamoA = []
    prestamoE = []

    while True:
        opc = int(input("[1] para Ingresar Prestamos de Automovil\n[2] para Ingresar Prestamos Educativos\n"))
        
        if opc == 1:
            tipo = input("Ingrese tipo de Automovil: ")
            marca = input("Ingrese marca del Automovil: ")
            nombreB = input("Ingrese nombres del Beneficiario: ")
            apellidoB = input("Ingrese apellidos del Beneficiario: ")
            idB = input("Ingrese identificacion del Beneficiario: ")
            nombreG = input("Ingrese nombres del Garante: ")
            apellidoG = input("Ingrese apellidos del Garante: ")
            idG = input("Ingrese identificacion del Garante: ")
            ciudad = input("Ingrese Ciudad donde se emitira el Prestamo: ")
            valor = float(input("Ingrese el valor del Automovil: "))
            meses = int(input("Ingrese el numero de meses del Prestamo: "))

            beneficiario = Persona(nombreB, apellidoB, idB)
            garante = Persona(nombreG, apellidoG, idG)
            prestamo = PrestamoAutomovil(tipo, marca, garante, valor, beneficiario, meses, ciudad)
            prestamo.establecer_ciudad(ciudad)
            prestamo.establecer_valor_pago_prestamo()
            prestamoA.append(prestamo)

        elif opc == 2:
            nombreB = input("Ingrese nombres del Beneficiario: ")
            apellidoB = input("Ingrese apellidos del Beneficiario: ")
            idB = input("Ingrese identificacion del Beneficiario: ")
            ciudad = input("Ingrese Ciudad donde se emitira el Prestamo: ")
            nivelE = input("Ingrese el nivel de Estudio del Beneficiario: ")
            nombreC = input("Ingrese nombre del Centro Educativo: ")
            siglasC = input("Ingrese siglas del Centro Educativo: ")
            valor = float(input("Ingrese el valor de la Carrera: "))
            meses = int(input("Ingrese el numero de meses del Prestamo: "))

            beneficiario = Persona(nombreB, apellidoB, idB)
            institucion = InstitucionEducativa(nombreC, siglasC)
            prestamo = PrestamoEducativo(beneficiario, meses, ciudad, nivelE, institucion, valor)
            prestamo.establecer_ciudad(ciudad)
            prestamo.establecer_pago_mensual_prestamo()
            prestamoE.append(prestamo)
        
        else:
            print("Opcion incorrecta")

        cont = int(input("Ingrese [0] para ya no ingresar mas prestamos, cualquier otro numero para continuar: "))
        if cont == 0:
            break

    print("---Prestamos de Automovil---")
    for prestamo in prestamoA:
        print(prestamo)
        print()

    print("---Prestamos Educativos---")
    for prestamo in prestamoE:
        print(prestamo)
        print()
