from subprocess import call
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from db_conn import conectar, fechar_conexao

def open_window(script_name, ano, mes):
    call(["python", f"{script_name}.py", ano, mes])

def exibir_grafico_despesas(ano, mes):
    # Conecte-se ao banco de dados
    conexao = conectar()
    if not conexao:
        print("Erro ao conectar ao banco de dados.")
        return

    cursor = conexao.cursor()

    # Filtrar as despesas com base no ano e mês
    cursor.execute("SELECT category, SUM(amount) FROM expenses WHERE YEAR(date) = %s AND MONTH(date) = %s GROUP BY category", (ano, mes))
    resultado = cursor.fetchall()

    if not resultado:
        print("Nenhum dado encontrado para o mês e ano selecionados.")
        fechar_conexao(conexao)
        return

    categorias = [item[0] for item in resultado]
    valores = [item[1] for item in resultado]

    # Criar o gráfico de pizza
    plt.figure(figsize=(6, 6))
    plt.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=140)
    plt.title(f"Gastos por Categoria em {mes}/{ano}")
    plt.axis('equal')

    # Exibir o gráfico
    plt.show()

    # Fechar a conexão ao banco de dados
    fechar_conexao(conexao)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Uso: statsDespesas.py ano mes")
    else:
        ano, mes = sys.argv[1], sys.argv[2]
        exibir_grafico_despesas(ano, mes)
