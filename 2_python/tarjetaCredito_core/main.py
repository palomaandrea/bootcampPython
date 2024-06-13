from Tarjeta import TarjetaCredito

tenpo= TarjetaCredito()
liderBci= TarjetaCredito(500,100,0.02)
abcDin=TarjetaCredito(100,2000,0.03)

tenpo.compra(100).compra(200).pago(150).cobrar_interes().mostrar_info_tarjeta