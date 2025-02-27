import tkinter as tk

def calcular_multiplicacao():
    try:
        numero1 = int(entry_numero1.get())
        numero2 = int(entry_numero2.get())
        resultado = f"{numero1} x {numero2} = {numero1 * numero2}"
        label_resultado.config(text=resultado)
    except ValueError:
        label_resultado.config(text="Por favor, insira números válidos.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora de Multiplicação")

# Título
titulo = tk.Label(janela, text="Bem-vindo à Calculadora de Multiplicação", font=("Helvetica", 16))
titulo.pack(pady=10)

# Instruções
instrucoes = tk.Label(janela, text="Digite dois números e clique em 'Calcular Multiplicação' para ver o resultado.")
instrucoes.pack(pady=5)

# Entrada para o primeiro número
label_numero1 = tk.Label(janela, text="Digite o primeiro número:")
label_numero1.pack()
entry_numero1 = tk.Entry(janela)
entry_numero1.pack(pady=5)

# Entrada para o segundo número
label_numero2 = tk.Label(janela, text="Digite o segundo número:")
label_numero2.pack()
entry_numero2 = tk.Entry(janela)
entry_numero2.pack(pady=5)

# Botão para calcular a multiplicação
botao_calcular = tk.Button(janela, text="Calcular Multiplicação", command=calcular_multiplicacao)
botao_calcular.pack(pady=5)

# Label para mostrar o resultado
label_resultado = tk.Label(janela, text="", justify="left")
label_resultado.pack(pady=10)

# Iniciar o loop da interface gráfica
janela.mainloop()