import tkinter as tk
from tkinter import ttk, messagebox
from db_conn import conectar, fechar_conexao
from subprocess import call  # Módulo para chamar scripts externos

def open_window(script_name, root):
    root.update_idletasks()  # Garante que as informações da janela principal foram atualizadas
    posicao_x = root.winfo_x() + (root.winfo_width() - 371) // 2
    posicao_y = root.winfo_y() + (root.winfo_height() - 247) // 2
    call(["python", f"{script_name}.py", f"--x={posicao_x}", f"--y={posicao_y}"])

class JanelaInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Gastos Pessoais")

        # Criar um frame para conter os botões
        frame_botoes = ttk.Frame(root)
        frame_botoes.pack(expand=True, padx=20, pady=20)

        # Criar botões para direcionar para outras funcionalidades
        btn_adicionar = ttk.Button(frame_botoes, text="Adicionar Gasto", command=lambda: self.abrir_adicionar_gasto(root))
        btn_visualizar = ttk.Button(frame_botoes, text="Visualizar Gastos", command=lambda: self.abrir_visualizar_gastos(root))
        btn_alterar_remover = ttk.Button(frame_botoes, text="Alterar/Remover Gasto", command=lambda: self.abrir_alterar_remover_gasto(root))

        # Ajustar o tamanho da janela
        tamanho_janela = (371, 247)

        posicao_x = int((root.winfo_screenwidth() - tamanho_janela[0]) // 2)
        posicao_y = int((root.winfo_screenheight() - tamanho_janela[1]) // 2)

        self.root.geometry(f"{tamanho_janela[0]}x{tamanho_janela[1]}+{posicao_x}+{posicao_y}")

        # Posicionar os botões centralizados no frame
        btn_adicionar.grid(row=0, column=0, pady=10)
        btn_visualizar.grid(row=1, column=0, pady=10)
        btn_alterar_remover.grid(row=2, column=0, pady=10)

    def abrir_adicionar_gasto(self, root):
        open_window("Despesas/addDespesas", root)

    def abrir_visualizar_gastos(self, root):
        open_window("Despesas/allDespesas", root)

    def abrir_alterar_remover_gasto(self, root):
        # Abre a janela para alterar ou remover gastos
        janela_ar = tk.Toplevel(root)
        janela_ar.title("Alterar/Remover Gasto")

        # Criar um rótulo e uma caixa de combinação para selecionar a operação desejada
        lbl_operacao = ttk.Label(janela_ar, text="Selecione a Operação:")
        combo_operacao = ttk.Combobox(janela_ar, values=["Alterar", "Remover"])
        combo_operacao.set("Alterar")  # Padrão para "Alterar"
        btn_confirmar = ttk.Button(janela_ar, text="Confirmar", command=lambda: self.executar_operacao(combo_operacao.get(), janela_ar, root))

        # Posicionar os widgets na janela
        lbl_operacao.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        combo_operacao.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        btn_confirmar.grid(row=1, column=0, columnspan=2, pady=10)

    def executar_operacao(self, operacao, janela, root):
        if operacao == "Alterar":
            open_window("Despesas/altDespesas", root)
        elif operacao == "Remover":
            open_window("Despesas/delDespesas", root)
        else:
            messagebox.showerror("Erro", "Operação inválida.")

        # Fechar a janela de alterar/remover gasto
        janela.destroy()

if __name__ == "__main__":
    # Conectar ao banco de dados
    conexao = conectar()

    if conexao:
        root = tk.Tk()
        app = JanelaInicial(root)
        root.mainloop()

        # Fechar a conexão ao sair da aplicação
        fechar_conexao(conexao)
