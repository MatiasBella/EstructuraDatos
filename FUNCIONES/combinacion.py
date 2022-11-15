def funcion(a,b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print(args)
    print(kwargs)

funcion(3,4,5,6,7,8,'f','a', color='rojo',size=12)