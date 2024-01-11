def total_carrito(request):
    total = 0   
    if request.user.is_authenticated and "carro" in request.session:
        for key, value in request.session["carro"].items():
            total += float(value["precio"])
    return {'total_carrito': total}

def cantidad_productos_carrito(request):
    cantidad = 0
    if request.user.is_authenticated and "carro" in request.session:
        cantidad = sum(value["cantidad"] for value in request.session["carro"].values())
    return {'cantidad_productos_carrito': cantidad}