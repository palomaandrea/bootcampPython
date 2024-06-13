class TarjetaCredito:
    tarjetas = []

    #Incluye en este método valores por default
    def __init__(self, saldo_pagar, limite_credito, intereses):
        #TU CODIGO (Aquí va los atributos de instancia y sus asignaciones de valor)
        self.saldo_pagar=saldo_pagar
        self.limite_credito=limite_credito
        self.intereses=intereses

        TarjetaCredito.tarjetas.append(self)

    def compra(self, monto):
        #TU CODIGO
        if(self.saldo_pagar + monto > self.limite_credito):
            print("Tarjeta rechazada, has alcanzado el límite de crédito")
        return self

    def pago(self, monto):
        #TU CODIGO
        self.saldo_pagar-= monto
        return self

    def mostrar_info_tarjeta(self):
        #TU CODIGO
        print(f"Saldo a pagar: ${self.saldo_pagar}")
        return self

    def cobrar_interes(self):
        #TU CODIGO
        self.saldo_pagar += self.saldo_pagar *self.intereses
        return self
    
    @classmethod
    def mostrar_todas_tarjetas(cls):
        for cls.tarjeta in cls.tarjeta:
            tarjeta.mostrar_info_tarjeta()
