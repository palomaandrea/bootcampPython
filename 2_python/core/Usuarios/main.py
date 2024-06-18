from Usuario import Usuario

Paloma=Usuario("Paloma","Contreras","pal.contrerasm@gmail.com")

Paloma.mostrar_saldo_usuario()
Paloma.hacer_compra(100).hacer_compra(200).hacer_compra(300)
Paloma.mostrar_saldo_usuario()
Paloma.hacer_compra(2500)
Paloma.pagar_tarjeta(500).mostrar_saldo_usuario()