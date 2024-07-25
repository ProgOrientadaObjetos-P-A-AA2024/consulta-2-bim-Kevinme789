class Arriendo:
    def __init__(self, nombre, cuota_base):
        self.nombre_arrendatario = nombre
        self.cuota_base = cuota_base
        self.arriendo_mensual = 0.0

    def establecer_nombre_arrendatario(self, nombre):
        self.nombre_arrendatario = nombre

    def establecer_cuota_base(self, cuota_base):
        self.cuota_base = cuota_base

    def establecer_arriendo_mensual(self):
        raise NotImplementedError("Subclase debe implementar este método")

    def obtener_nombre_arrendatario(self):
        return self.nombre_arrendatario

    def obtener_cuota_base(self):
        return self.cuota_base

    def obtener_arriendo_mensual(self):
        return self.arriendo_mensual

    def __str__(self):
        return f"Nombre Arrendatario: {self.nombre_arrendatario}, Cuota Base: {self.cuota_base}, Arriendo Mensual: {self.arriendo_mensual}"


class ArriendoLocalComida(Arriendo):
    def __init__(self, nombre, cuota_base, iva=0, valor_agua=0, valor_luz=0):
        super().__init__(nombre, cuota_base)
        self.iva = iva
        self.valor_agua = valor_agua
        self.valor_luz = valor_luz

    def establecer_iva(self, iva):
        self.iva = iva

    def establecer_valor_agua(self, valor_agua):
        self.valor_agua = valor_agua

    def establecer_valor_luz(self, valor_luz):
        self.valor_luz = valor_luz

    def establecer_arriendo_mensual(self):
        self.arriendo_mensual = self.cuota_base + (self.cuota_base * self.iva / 100) + self.valor_agua + self.valor_luz

    def __str__(self):
        return super().__str__() + f", IVA: {self.iva}, Valor Agua: {self.valor_agua}, Valor Luz: {self.valor_luz}"


class ArriendoLocalComercial(Arriendo):
    def __init__(self, nombre, cuota_base, valor_adicional_fijo=0):
        super().__init__(nombre, cuota_base)
        self.valor_adicional_fijo = valor_adicional_fijo

    def establecer_valor_adicional_fijo(self, valor_adicional_fijo):
        self.valor_adicional_fijo = valor_adicional_fijo

    def establecer_arriendo_mensual(self):
        self.arriendo_mensual = self.cuota_base + self.valor_adicional_fijo

    def __str__(self):
        return super().__str__() + f", Valor Adicional Fijo: {self.valor_adicional_fijo}"


class ArriendoLocalSesiones(Arriendo):
    def __init__(self, nombre, cuota_base, valor_sillas=0, valor_amplificacion=0):
        super().__init__(nombre, cuota_base)
        self.valor_sillas = valor_sillas
        self.valor_amplificacion = valor_amplificacion

    def establecer_valor_sillas(self, valor_sillas):
        self.valor_sillas = valor_sillas

    def establecer_valor_amplificacion(self, valor_amplificacion):
        self.valor_amplificacion = valor_amplificacion

    def establecer_arriendo_mensual(self):
        self.arriendo_mensual = self.cuota_base + self.valor_sillas + self.valor_amplificacion

    def __str__(self):
        return super().__str__() + f", Valor Sillas: {self.valor_sillas}, Valor Amplificación: {self.valor_amplificacion}"


if __name__ == "__main__":
    lista_arriendos = []

    arriendo_comida = ArriendoLocalComida("Christian Shepherd", 300)
    arriendo_comida.establecer_iva(10)
    arriendo_comida.establecer_valor_agua(20.2)
    arriendo_comida.establecer_valor_luz(40.2)

    arriendo_comida2 = ArriendoLocalComida("Christian Cruz", 300, 10, 20.2, 40.2)

    arriendo_comercial = ArriendoLocalComercial("Andrew Schroeder", 400)
    arriendo_comercial.establecer_valor_adicional_fijo(100)

    arriendo_sesiones = ArriendoLocalSesiones("Angela Watson", 350)
    arriendo_sesiones.establecer_valor_sillas(10)
    arriendo_sesiones.establecer_valor_amplificacion(20)

    lista_arriendos.append(arriendo_comida)
    lista_arriendos.append(arriendo_comercial)
    lista_arriendos.append(arriendo_sesiones)
    lista_arriendos.append(arriendo_comida2)

    for arriendo in lista_arriendos:
        arriendo.establecer_arriendo_mensual()
        print(arriendo)
        print()
