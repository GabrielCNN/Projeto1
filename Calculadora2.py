import tkinter as tk
from tkinter import ttk

def calcular():
    try:
        expressao = entry_expressao.get()
        resultado = eval(expressao)
        label_resultado.config(text=f"Resultado: {resultado}")
    except Exception as e:
        label_resultado.config(text="Erro na expressão")

def limpar():
    entry_expressao.delete(0, tk.END)
    label_resultado.config(text="")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Título
titulo = tk.Label(janela, text="Calculadora", font=("Helvetica", 16))
titulo.pack(pady=10)

# Entrada para a expressão
label_expressao = tk.Label(janela, text="Digite a expressão:")
label_expressao.pack()
entry_expressao = tk.Entry(janela, width=30)
entry_expressao.pack(pady=5)

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