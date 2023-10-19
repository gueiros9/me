import tkinter as tk
from tkinter import ttk
from db_conn import conectar, fechar_conexao

class JanelaVisualizarGastos:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizar Gastos")

        # Conectar ao banco de dados
        conexao = conectar()

        if conexao:
            try:
                # Criar um cursor
                cursor = conexao.cursor()

                # Executar a consulta para obter os gastos
                cursor.execute("SELECT * FROM expenses")

                # Obter os resultados da consulta
                resultados = cursor.fetchall()

                # Criar uma treeview para exibir os dados
                tree = ttk.Treeview(root)
                tree["columns"] = ("ID", "Descrição", "Valor", "Data", "Categoria")

                # Definir as colunas
                tree.column("#0", width=0, stretch=tk.NO)  # Espaço em branco
                tree.column("ID", anchor=tk.W, width=50)
                tree.column("Descrição", anchor=tk.W, width=150)
                tree.column("Valor", anchor=tk.W, width=100)
                tree.column("Data", anchor=tk.W, width=100)
                tree.column("Categoria", anchor=tk.W, width=150)

                # Configurar os cabeçalhos das colunas
                tree.heading("#0", text="", anchor=tk.W)
                tree.heading("ID", text="ID", anchor=tk.W)
                tree.heading("Descrição", text="Descrição", anchor=tk.W)
                tree.heading("Valor", text="Valor", anchor=tk.W)
                tree.heading("Data", text="Data", anchor=tk.W)
                tree.heading("Categoria", text="Categoria", anchor=tk.W)

                # Adicionar os dados à treeview
                for resultado in resultados:
                    tree.insert("", tk.END, values=resultado)

                # Posicionar a treeview na janela
                tree.pack(expand=True, fill=tk.BOTH)

            except Exception as e:
                print(f"Erro ao visualizar gastos: {e}")

            finally:
                # Fechar o cursor e a conexão
                cursor.close()
                fechar_conexao(conexao)

if __name__ == "__main__":
    root = tk.Tk()
    app = JanelaVisualizarGastos(root)
    root.mainloop()
