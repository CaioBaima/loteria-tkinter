import random
import tkinter as tk

# Geometria
root = tk.Tk()
root.title('Biscoito da Sorte')

# Label superior
label = tk.Label(root, text='Clique e gere seu número da sorte!', font=20)

# Randomizando números
def sorteio():
    megaNumeros = []
    for n in range(1,61):
        megaNumeros.append(n)
    numeros = sorted(random.sample(megaNumeros, k=6))           
    label1 = tk.Label(root, text=numeros, font=20)
    return label1.grid(column=0, row=1)

# Botões
sortear = tk.Button(root, text='Sortear!', command=sorteio)
encerrar = tk.Button(root, text='Fechar', command=root.destroy)

# montagem
label.grid(column=0, row=0)
sortear.grid(column=0,row=2)
encerrar.grid(column=0, row=3)

root.mainloop()