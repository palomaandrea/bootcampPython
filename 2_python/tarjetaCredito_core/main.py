from Tarjeta import TarjetaCredito

tenpo= TarjetaCredito(500,2000,0.01)
liderBci= TarjetaCredito(500,2000,0.02)
abcDin=TarjetaCredito(100,1500,0.03)

#Para la primera tarjeta, haz 2 compras y un pago. Luego cobra los intereses y muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
tenpo.compra(100).compra(200).pago(150).cobrar_interes().mostrar_info_tarjeta()

#Para la segunda tarjeta, haz 3 compras y 2 pagos. Luego cobra los intereses y muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
liderBci.compra(100).compra(150).compra(85).pago(50).pago(75).cobrar_interes().mostrar_info_tarjeta()

#Para la tercera tarjeta, haz 5 compras y excede su límite de crédito. Luego muestra la información de la tarjeta; todo esto en una sola línea a través de la encadenación.
abcDin.compra(500).compra(1000).compra(200).compra(150).compra(1050).mostrar_info_tarjeta()

#en la tercera tarjeta no me aparece el mensaje de rechazo, corregir!!