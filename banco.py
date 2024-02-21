import pandas
import mysql.connector
from tkinter import filedialog

def carregaPlanilha():
    planilha = pandas.read_excel(filedialog.askopenfilename(filetypes=[("Excel","*.xlsx")]))
    return planilha

def conecta():
    local = "localhost" #str(input("Local: "))
    usuario = "sistema" #str(input("Usuário: "))
    senha = "12345" #str(input("Senha: "))
    db = "banco" #str(input("Banco de dados: "))
    conexao = mysql.connector.connect(host=local,user=usuario,password=senha,database=db)
    return conexao


def insereDados(conexao,dados):
    comandos = conexao.cursor()
    for index,i in dados.itertuples():
        sql = f"insert into meninas (nome) values ('{i}')"
        comandos.execute(sql)
        print(f"Inserimos o nome '{i}'...")
    conexao.commit()
    comandos.close()


dados_a = carregaPlanilha()
conexao_a = conecta()
insereDados(conexao_a,dados_a)