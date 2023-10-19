import tkinter as tk
from tkinter import ttk, messagebox
from db_conn import conectar, fechar_conexao

class JanelaExcluirGastos:
    def __init__(self, root):
        self.root = root
        self.root.title("Excluir Gastos")
        self.janela_exclusao = None  # Adicionado atributo para a janela de exclusão

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

                # Adicionar um botão para excluir
                btn_excluir = ttk.Button(root, text="Excluir Selecionado", command=self.excluir_selecionado)
                btn_excluir.pack(pady=10)

                # Posicionar a treeview na janela
                self.tree.pack(expand=True, fill=tk.BOTH)

            except Exception as e:
                print(f"Erro ao excluir gastos: {e}")

            finally:
                # Fechar o cursor e a conexão
                cursor.close()
                fechar_conexao(conexao)

    def excluir_selecionado(self):
        # Obter o item selecionado na treeview
        item_selecionado = self.tree.selection()

        if item_selecionado:
            # Obter o ID selecionado
            id_selecionado = self.tree.item(item_selecionado, "values")[0]

            # Exemplo: Confirmar a exclusão
            resposta = messagebox.askyesno("Confirmação", f"Tem certeza que deseja excluir o gasto com ID {id_selecionado}?")

            if resposta:
                # Implemente a lógica para excluir o gasto do banco de dados
                # Exemplo: Remover o item da treeview
                self.tree.delete(item_selecionado)
                messagebox.showinfo("Sucesso", "Exclusão realizada com sucesso.")
        else:
            messagebox.showwarning("Aviso", "Selecione um item para excluir.")

if __name__ == "__main__":
    root = tk.Tk()
    app = JanelaExcluirGastos(root)
    root.mainloop()
