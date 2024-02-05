import tkinter as tk

def calcular_vantagem():
    try:
        nome_produto1 = nome_produto1_entry.get()
        nome_produto2 = nome_produto2_entry.get()
        
        preco1_str = preco1_entry.get().replace(',', '.')  # Substitui vírgula por ponto
        preco2_str = preco2_entry.get().replace(',', '.')
        
        preco1 = float(preco1_str)
        gramas1 = float(gramas1_entry.get())
        preco2 = float(preco2_str)
        gramas2 = float(gramas2_entry.get())

        vantajoso = ""
        preco_por_grama1 = preco1 / gramas1
        preco_por_grama2 = preco2 / gramas2

        if preco_por_grama1 < preco_por_grama2:
            vantajoso = f"{nome_produto1} | É mais vantajoso comprar este produto."
        elif preco_por_grama1 > preco_por_grama2:
            vantajoso = f"{nome_produto2} | É mais vantajoso comprar este produto."
        else:
            vantajoso = "Ambos os produtos têm o mesmo preço por grama."

        resultado_label.config(text=vantajoso)
        custo_por_grama_label.config(text=f"Custo por grama | {nome_produto1}: R${preco_por_grama1:.2f} - {nome_produto2}: R${preco_por_grama2:.2f}")
    except ValueError:
        resultado_label.config(text="Por favor, insira valores válidos.")

# Configuração da janela
janela = tk.Tk()
janela.title("Mercadômetro v1.0 | by @alanmugiwaras")
janela.geometry("400x400")  # Definindo o tamanho da janela

# Produto 1
nome_produto1_label = tk.Label(janela, text="Digite o nome do produto 1:")
nome_produto1_label.pack(anchor="w")
nome_produto1_entry = tk.Entry(janela)
nome_produto1_entry.pack(anchor="w")

preco1_label = tk.Label(janela, text="Digite o preço do produto 1 (R$):")
preco1_label.pack(anchor="w")
preco1_entry = tk.Entry(janela)
preco1_entry.pack(anchor="w")

gramas1_label = tk.Label(janela, text="Digite a quantidade de Gramas do produto 1:")
gramas1_label.pack(anchor="w")
gramas1_entry = tk.Entry(janela)
gramas1_entry.pack(anchor="w")

# Espaço entre produtos
tk.Label(janela, text="").pack()

# Produto 2
nome_produto2_label = tk.Label(janela, text="Digite o nome do produto 2:")
nome_produto2_label.pack(anchor="w")
nome_produto2_entry = tk.Entry(janela)
nome_produto2_entry.pack(anchor="w")

preco2_label = tk.Label(janela, text="Digite o preço do produto 2 (R$):")
preco2_label.pack(anchor="w")
preco2_entry = tk.Entry(janela)
preco2_entry.pack(anchor="w")

gramas2_label = tk.Label(janela, text="Digite a quantidade de Gramas do produto 2:")
gramas2_label.pack(anchor="w")
gramas2_entry = tk.Entry(janela)
gramas2_entry.pack(anchor="w")

# Botão de cálculo
calcular_button = tk.Button(janela, text="Calcular", command=calcular_vantagem)
calcular_button.pack()

# Rótulo para o resultado
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

# Rótulo para o custo por grama
custo_por_grama_label = tk.Label(janela, text="")
custo_por_grama_label.pack()

# Iniciar a interface gráfica
janela.mainloop()
