precio=float(input("ingresa el precio del producto que vas a comprar "))
descuento=float(input("ingresa el descuento que se aplicara "))

descuento2=precio * (descuento/100)
preciofinal= precio - descuento2
print(f"el precio final aplciando el descuento de un {descuento}% es de: {preciofinal}")