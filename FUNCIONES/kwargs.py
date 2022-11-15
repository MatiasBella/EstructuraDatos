def config(**kwargs):
    print(kwargs)

config(font='arial',color='red',size=12)

def config(**kwargs):
    for x in kwargs:
        print(x,':',kwargs[x])

config(font='arial',color='red',size=12)