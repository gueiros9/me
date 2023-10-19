import tkinter as tk
from tkinter import ttk, messagebox
from db_conn import conectar, fechar_conexao
from subprocess import call
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def open_window(script_name):
    call(["python", f"{script_name}.py"])

class JanelaGraficos:
    def __init__(self, root):
        self.root = root
        self.root.title("Gráficos de Gastos por Categoria")

        # Configurar o estilo para os widgets
        estilo = ttk.Style()
        estilo.configure("TButton", font=('Helvetica', 10, 'bold'))
        estilo.configure("TLabel", font=('Helvetica', 10, 'bold'))
        estilo.configure("TCombobox", font=('Helvetica', 10, 'bold'))
        estilo.configure("TFrame")

        # Lógica para obter dados do banco de dados e criar gráficos aqui
        dados = self.obter_dados_do_banco()

        # Exemplo de gráfico de pizza
        categorias = []
        valores = []

        for categoria, valor in dados:
            categorias.append(categoria)
            valores.append(valor)

        fig, ax = plt.subplots()
        ax.pie(valores, labels=categorias, autopct='%1.2f%%', startangle=90)
        ax.axis('equal')  # Assegura que o gráfico de pizza é desenhado como um círculo

        # Criar um widget de tela de desenho do Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()

        # Exibir o widget de tela de desenho
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def obter_dados_do_banco(self):
        # Conectar ao banco de dados
        conexao = conectar()
        if not conexao:
            messagebox.showerror("Erro", "Erro ao conectar ao banco de dados.")
            return []

        try:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute("SELECT category, SUM(amount) as total FROM expenses GROUP BY category")
            dados = cursor.fetchall()
            return [(dado['category'], dado['total']) for dado in dados]
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao obter dados do banco de dados: {str(e)}")
            return []
        finally:
            fechar_conexao(conexao)

if __name__ == "__main__":
    # Conectar ao banco de dados
    conexao = conectar()

    if conexao:
        root = tk.Tk()
        app = JanelaGraficos(root)
        root.mainloop()

        # Fechar a conexão ao sair da aplicação
        fechar_conexao(conexao)
