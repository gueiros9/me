import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from db_conn import conectar, fechar_conexao
from subprocess import call
import subprocess
import os

def open_window(script_name, *args):
    # Obtenha o caminho completo para o script no diretório "Despesas"
    script_path = os.path.join("Despesas", f"{script_name}.py")
    # Chame o script com argumentos separados
    subprocess.Popen(["python", script_path] + list(args))

class JanelaInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Gastos Pessoais")

        # Conectar ao banco de dados
        conexao = conectar()
        if conexao:
            self.conexao = conexao
        else:
            messagebox.showerror("Erro", "Erro ao conectar ao banco de dados.")

        # Criar botões para direcionar para outras funcionalidades
        btn_adicionar = ttk.Button(root, text="Adicionar Gasto", command=self.abrir_adicionar_gasto)
        btn_visualizar = ttk.Button(root, text="Visualizar Gastos", command=self.abrir_visualizar_gastos)
        btn_alterar_remover = ttk.Button(root, text="Alterar/Remover Gasto", command=self.abrir_alterar_remover_gasto)
        btn_visualizar_stats = ttk.Button(root, text="Visualizar Estatísticas", command=self.abrir_visualizar_estatisticas)

        # Posicionar os botões na janela
        btn_adicionar.pack(pady=10)
        btn_visualizar.pack(pady=10)
        btn_alterar_remover.pack(pady=10)
        btn_visualizar_stats.pack(pady=10)

    def abrir_adicionar_gasto(self):
        open_window("addDespesas")

    def abrir_visualizar_gastos(self):
        open_window("allDespesas")

    def abrir_alterar_remover_gasto(self):
        # Abre a janela para alterar ou remover gastos
        janela_ar = tk.Toplevel(self.root)
        janela_ar.title("Alterar/Remover Gasto")

        # Criar um rótulo e uma caixa de combinação para selecionar a operação desejada
        lbl_operacao = ttk.Label(janela_ar, text="Selecione a Operação:")
        combo_operacao = ttk.Combobox(janela_ar, values=["Alterar", "Remover"])
        combo_operacao.set("Alterar")  # Padrão para "Alterar"
        btn_confirmar = ttk.Button(janela_ar, text="Confirmar", command=lambda: self.executar_operacao(combo_operacao.get(), janela_ar))

        # Posicionar os widgets na janela
        lbl_operacao.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        combo_operacao.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        btn_confirmar.grid(row=1, column=0, columnspan=2, pady=10)

    def abrir_visualizar_estatisticas(self):
        # Abre a janela para visualizar estatísticas
        janela_estatisticas = tk.Toplevel(self.root)
        janela_estatisticas.title("Visualizar Estatísticas")

        # Criar uma caixa de combinação para selecionar o ano
        lbl_ano = ttk.Label(janela_estatisticas, text="Selecione o Ano:")
        combo_ano = ttk.Combobox(janela_estatisticas, values=self.obter_anos_unicos(), state="readonly")
        combo_ano.set("")  # Padrão para ano vazio
        lbl_mes = ttk.Label(janela_estatisticas, text="Selecione o Mês:")
        combo_mes = ttk.Combobox(janela_estatisticas, state="readonly")
        btn_confirmar = ttk.Button(janela_estatisticas, text="Confirmar", command=lambda: self.abrir_stats_despesas(combo_ano.get(), combo_mes.get()))

        # Definir um evento para quando o ano for selecionado
        combo_ano.bind("<<ComboboxSelected>>", lambda event: self.preencher_combo_mes(combo_mes, combo_ano.get()))

        # Posicionar os widgets na janela de estatísticas
        lbl_ano.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        combo_ano.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        lbl_mes.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        combo_mes.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
        btn_confirmar.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Obtenha o ano e mês selecionados
        ano = combo_ano.get()
        mes = combo_mes.get()

        if ano and mes:
            # Chame a função para gerar o gráfico no próprio JanelaInicial
            subprocess.call(["python", "statsDespesas.py", str(ano), str(mes)])
            
    def executar_operacao(self, operacao, janela):
        if operacao == "Alterar":
            open_window("altDespesas")
        elif operacao == "Remover":
            open_window("delDespesas")
        else:
            messagebox.showerror("Erro", "Operação inválida.")

        # Fechar a janela de alterar/remover gasto
        janela.destroy()

    def obter_meses_unicos(self, ano):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT DISTINCT MONTH(date) FROM expenses WHERE YEAR(date) = %s", (ano,))
        meses = [str(mes[0]) for mes in cursor.fetchall()]
        return meses

    def obter_anos_unicos(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT DISTINCT YEAR(date) FROM expenses")
        anos = [str(ano[0]) for ano in cursor.fetchall()]
        return anos

    def preencher_combo_mes(self, combo_mes, ano_selecionado):
        if ano_selecionado:
            meses = self.obter_meses_unicos(ano_selecionado)
            combo_mes["values"] = meses
            combo_mes.set("")  # Limpar a seleção do mês

    def abrir_stats_despesas(self, ano, mes):
        open_window("statsDespesas", ano, mes)

if __name__ == "__main__":
    # Conectar ao banco de dados
    conexao = conectar()

    if conexao:
        root = tk.Tk()
        app = JanelaInicial(root)
        root.mainloop()

        # Fechar a conexão ao sair da aplicação
        fechar_conexao(conexao)
