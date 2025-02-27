import tkinter as tk

def calcular():
    try:
        numero1 = int(entry_numero1.get())
        numero2 = int(entry_numero2.get())
        operacao = operacao_selecionada.get()
        
        if operacao == "Adição":
            resultado = f"{numero1:,} + {numero2:,} = {numero1 + numero2:,}"
        elif operacao == "Subtração":
            resultado = f"{numero1:,} - {numero2:,} = {numero1 - numero2:,}"
        elif operacao == "Multiplicação":
            resultado = f"{numero1:,} x {numero2:,} = {numero1 * numero2:,}"
        elif operacao == "Divisão":
            if numero2 != 0:
                resultado = f"{numero1:,} ÷ {numero2:,} = {numero1 / numero2:,}"
            else:
                resultado = "Divisão por zero não é permitida."
        else:
            resultado = "Operação inválida."
        
        label_resultado.config(text=resultado)
    except ValueError:
        label_resultado.config(text="Por favor, insira números válidos.")

def limpar():
    entry_numero1.delete(0, tk.END)
    entry_numero2.delete(0, tk.END)
    label_resultado.config(text="")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Título
titulo = tk.Label(janela, text="Bem-vindo à Calculadora", font=("Helvetica", 16))
titulo.pack(pady=10)

# Instruções
instrucoes = tk.Label(janela, text="Digite dois números, selecione a operação e clique em 'Calcular' para ver o resultado.")
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

# Menu suspenso para selecionar a operação
operacao_selecionada = tk.StringVar(janela)
operacao_selecionada.set("Adição")  # valor padrão
menu_operacoes = tk.OptionMenu(janela, operacao_selecionada, "Adição", "Subtração", "Multiplicação", "Divisão")
menu_operacoes.pack(pady=5)

# Botão para calcular
botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.pack(pady=5)

# Botão para limpar
botao_limpar = tk.Button(janela, text="Limpar", command=limpar)
botao_limpar.pack(pady=5)

# Label para mostrar o resultado
label_resultado = tk.Label(janela, text="", justify="left")
label_resultado.pack(pady=10)

# Iniciar o loop da interface gráfica
janela.mainloop()