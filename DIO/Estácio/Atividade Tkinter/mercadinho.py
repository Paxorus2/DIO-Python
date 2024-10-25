import sqlite3
import tkinter as tk
from tkinter import messagebox

# Função para cadastrar produto
def cadastrar_produto():
    nome = entry_nome.get()
    preco = entry_preco.get()

    if nome and preco:
        try:
            conn = sqlite3.connect('mercadinho.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO produtos (nome, preco) VALUES (?, ?)', (nome, float(preco)))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            entry_nome.delete(0, tk.END)
            entry_preco.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar produto: {e}")
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")

# Função para consultar produtos
def consultar_produtos():
    conn = sqlite3.connect('mercadinho.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    conn.close()

    result_window = tk.Toplevel(root)
    result_window.title("Consulta de Produtos")
    result_window.geometry("400x300")

    for produto in produtos:
        label = tk.Label(result_window, text=f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R${produto[2]:.2f}")
        label.pack(pady=2)

# Criação da janela principal
root = tk.Tk()
root.title("Cadastro de Produtos do Mercadinho")
root.geometry("400x300")

# Criação dos campos de entrada
label_nome = tk.Label(root, text="Nome do Produto:", font=('Arial', 12))
label_nome.pack(pady=10)
entry_nome = tk.Entry(root, font=('Arial', 12))
entry_nome.pack(pady=5)

label_preco = tk.Label(root, text="Preço do Produto:", font=('Arial', 12))
label_preco.pack(pady=10)
entry_preco = tk.Entry(root, font=('Arial', 12))
entry_preco.pack(pady=5)

# Botões
btn_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar_produto, font=('Arial', 12))
btn_cadastrar.pack(pady=15)
btn_consultar = tk.Button(root, text="Consultar Produtos", command=consultar_produtos, font=('Arial', 12))
btn_consultar.pack(pady=10)

# Loop principal da interface gráfica
root.mainloop()
