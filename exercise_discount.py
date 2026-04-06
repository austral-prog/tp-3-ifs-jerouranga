from exercise_password import password


def discount():

    precio = float(input())
    cant = int(input())
    subtotal = precio * cant
    if cant >= 10:
        descuento = "20%"
        aplicado = subtotal * 0.2

    elif cant >= 5 and cant <= 9:
        descuento = "10%"
        aplicado = subtotal * 0.10
    else:
        descuento = "0%"
        aplicado = 0

    print(f"Subtotal: {subtotal}")
    print(f"Descuento aplicado: {descuento}")
    print(f"Monto de descuento: {float(aplicado)}")
    print(f"Total final: {subtotal - aplicado}")



