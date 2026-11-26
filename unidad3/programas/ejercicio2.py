#tienda
monto=float(input("Ingrese el monto de la compra: "))
if monto>=1000:
    descuento=monto*0.10
    total=monto-descuento
    print("El monto de la compra es:",monto)
    print("El descuento es:",descuento)
    print("El total a pagar es:",total)
else:
    print("El monto de la compra es:",monto)
