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

# Botões para selecionar a operação
def selecionar_operacao(op, botao):
    operacao_selecionada.set(op)
    for b in botoes_operacoes:
        b.config(relief=tk.RAISED)
    botao.config(relief=tk.SUNKEN)

operacao_selecionada = tk.StringVar(janela)
operacao_selecionada.set("Adição")  # valor padrão

frame_operacoes = tk.Frame(janela)
frame_operacoes.pack(pady=5)

botoes_operacoes = []

botao_adicao = tk.Button(frame_operacoes, text="+", command=lambda: selecionar_operacao("Adição", botao_adicao))
botao_adicao.pack(side=tk.LEFT, padx=5)
botoes_operacoes.append(botao_adicao)

botao_subtracao = tk.Button(frame_operacoes, text="-", command=lambda: selecionar_operacao("Subtração", botao_subtracao))
botao_subtracao.pack(side=tk.LEFT, padx=5)
botoes_operacoes.append(botao_subtracao)

botao_multiplicacao = tk.Button(frame_operacoes, text="x", command=lambda: selecionar_operacao("Multiplicação", botao_multiplicacao))
botao_multiplicacao.pack(side=tk.LEFT, padx=5)
botoes_operacoes.append(botao_multiplicacao)

botao_divisao = tk.Button(frame_operacoes, text="÷", command=lambda: selecionar_operacao("Divisão", botao_divisao))
botao_divisao.pack(side=tk.LEFT, padx=5)
botoes_operacoes.append(botao_divisao)

# Set initial shadow for the default operation
botao_adicao.config(relief=tk.SUNKEN)

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