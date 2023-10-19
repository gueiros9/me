import tkinter as tk
from tkinter import ttk, messagebox
from db_conn import conectar, fechar_conexao

class JanelaEditarGastos:
    def __init__(self, root):
        self.root = root
        self.root.title("Editar Gastos")
        self.janela_edicao = None  # Adicionado atributo para a janela de edição

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
                self.tree = ttk.Treeview(root)
                self.tree["columns"] = ("ID", "Descrição", "Valor", "Data", "Categoria")

                # Definir as colunas
                self.tree.column("#0", width=0, stretch=tk.NO)  # Espaço em branco
                self.tree.column("ID", anchor=tk.W, width=50)
                self.tree.column("Descrição", anchor=tk.W, width=150)
                self.tree.column("Valor", anchor=tk.W, width=100)
                self.tree.column("Data", anchor=tk.W, width=100)
                self.tree.column("Categoria", anchor=tk.W, width=150)

                # Configurar os cabeçalhos das colunas
                self.tree.heading("#0", text="", anchor=tk.W)
                self.tree.heading("ID", text="ID", anchor=tk.W)
                self.tree.heading("Descrição", text="Descrição", anchor=tk.W)
                self.tree.heading("Valor", text="Valor", anchor=tk.W)
                self.tree.heading("Data", text="Data", anchor=tk.W)
                self.tree.heading("Categoria", text="Categoria", anchor=tk.W)

                # Adicionar os dados à treeview
                for resultado in resultados:
                    self.tree.insert("", tk.END, values=resultado)

                # Adicionar um botão para editar
                btn_editar = ttk.Button(root, text="Editar Selecionado", command=self.editar_selecionado)
                btn_editar.pack(pady=10)

                # Posicionar a treeview na janela
                self.tree.pack(expand=True, fill=tk.BOTH)

            except Exception as e:
                print(f"Erro ao editar gastos: {e}")

            finally:
                # Fechar o cursor e a conexão
                cursor.close()
                fechar_conexao(conexao)

    def editar_selecionado(self):
        # Obter o item selecionado na treeview
        item_selecionado = self.tree.selection()

        if item_selecionado:
            # Obter os valores das colunas
            id_selecionado = self.tree.item(item_selecionado, "values")[0]
            descricao = self.tree.item(item_selecionado, "values")[1]
            valor = self.tree.item(item_selecionado, "values")[2]
            data = self.tree.item(item_selecionado, "values")[3]
            categoria = self.tree.item(item_selecionado, "values")[4]

            # Exemplo: Abra uma nova janela para editar os dados
            self.janela_edicao = tk.Toplevel(self.root)
            self.janela_edicao.title(f"Editar Gasto ID: {id_selecionado}")

            # Criar widgets para edição
            lbl_descricao = ttk.Label(self.janela_edicao, text="Descrição:")
            entry_descricao = ttk.Entry(self.janela_edicao)
            entry_descricao.insert(0, descricao)

            lbl_valor = ttk.Label(self.janela_edicao, text="Valor:")
            entry_valor = ttk.Entry(self.janela_edicao)
            entry_valor.insert(0, valor)

            lbl_data = ttk.Label(self.janela_edicao, text="Data (AAAA-MM-DD):")
            entry_data = ttk.Entry(self.janela_edicao)
            entry_data.insert(0, data)

            lbl_categoria = ttk.Label(self.janela_edicao, text="Categoria:")
            entry_categoria = ttk.Entry(self.janela_edicao)
            entry_categoria.insert(0, categoria)

            btn_confirmar = ttk.Button(self.janela_edicao, text="Confirmar Edição", command=lambda: self.confirmar_edicao(id_selecionado, entry_descricao.get(), entry_valor.get(), entry_data.get(), entry_categoria.get()))

            # Posicionar os widgets na janela de edição
            lbl_descricao.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
            entry_descricao.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

            lbl_valor.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
            entry_valor.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

            lbl_data.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
            entry_data.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

            lbl_categoria.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
            entry_categoria.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

            btn_confirmar.grid(row=4, column=0, columnspan=2, pady=10)
        else:
            messagebox.showwarning("Aviso", "Selecione um item para editar.")

    def confirmar_edicao(self, id_selecionado, nova_descricao, novo_valor, nova_data, nova_categoria):
        # Implemente a lógica para confirmar a edição
        # Exemplo: Atualizar os dados no banco de dados
        print(f"Editar ID {id_selecionado}:")
        print(f"Nova Descrição: {nova_descricao}")
        print(f"Novo Valor: {novo_valor}")
        print(f"Nova Data: {nova_data}")
        print(f"Nova Categoria: {nova_categoria}")

        # Atualizar os dados na treeview
        item_selecionado = self.tree.selection()
        self.tree.item(item_selecionado, values=(id_selecionado, nova_descricao, novo_valor, nova_data, nova_categoria))

        # Fechar a janela de edição
        messagebox.showinfo("Sucesso", "Edição confirmada.")
        self.janela_edicao.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = JanelaEditarGastos(root)
    root.mainloop()
