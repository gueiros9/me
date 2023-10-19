import tkinter as tk
from tkinter import ttk, messagebox
from db_conn import conectar, fechar_conexao

class JanelaAdicionarGasto:
    def __init__(self, root):
        self.root = root
        self.root.title("Adicionar Gasto")

        # Criar variáveis para armazenar os dados do gasto
        self.descricao_var = tk.StringVar()
        self.valor_var = tk.DoubleVar()
        self.data_var = tk.StringVar()
        self.categoria_var = tk.StringVar()

        # Criar rótulos e entradas para descrição, valor, data e categoria
        lbl_descricao = ttk.Label(root, text="Descrição:")
        entry_descricao = ttk.Entry(root, textvariable=self.descricao_var)

        lbl_valor = ttk.Label(root, text="Valor:")
        entry_valor = ttk.Entry(root, textvariable=self.valor_var)

        lbl_data = ttk.Label(root, text="Data (AAAA-MM-DD):")
        entry_data = ttk.Entry(root, textvariable=self.data_var)

        lbl_categoria = ttk.Label(root, text="Categoria:")
        entry_categoria = ttk.Entry(root, textvariable=self.categoria_var)

        btn_adicionar = ttk.Button(root, text="Adicionar", command=self.adicionar_gasto)

        # Posicionar os widgets na janela
        lbl_descricao.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        entry_descricao.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        lbl_valor.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        entry_valor.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        lbl_data.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        entry_data.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        lbl_categoria.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        entry_categoria.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        btn_adicionar.grid(row=4, column=0, columnspan=2, pady=10)

    def adicionar_gasto(self):
        # Obter os valores dos widgets
        descricao = self.descricao_var.get()
        valor = self.valor_var.get()
        data = self.data_var.get()
        categoria = self.categoria_var.get()

        # Conectar ao banco de dados
        conexao = conectar()

        if conexao:
            try:
                # Criar um cursor
                cursor = conexao.cursor()

                # Inserir os dados na tabela de gastos
                query = "INSERT INTO expenses (description, amount, date, category) VALUES (%s, %s, %s, %s)"
                valores = (descricao, valor, data, categoria)
                cursor.execute(query, valores)

                # Commit para salvar as alterações
                conexao.commit()

                messagebox.showinfo("Sucesso", "Gasto adicionado com sucesso.")

            except Exception as e:
                print(f"Erro ao adicionar gasto: {e}")
                messagebox.showerror("Erro", f"Erro ao adicionar gasto:\n{e}")

            finally:
                # Fechar o cursor e a conexão
                cursor.close()
                fechar_conexao(conexao)

if __name__ == "__main__":
    root = tk.Tk()
    app = JanelaAdicionarGasto(root)
    root.mainloop()
