import pandas
import openpyxl
from tkinter.ttk import *
from tkinter import *
from tkinter import filedialog, Tk, Button, Label, Frame
from tkinter import ttk


def escolheArquivo():
    caminhoArquivo = filedialog.askopenfilename(filetypes=[("Arquivos XLSX", "*.xlsx"), ("Arquivos XLS", "*.xls")])
    texto1["text"] = caminhoArquivo

def carregaPlanilhaOpenpyxl():
    planilhaOpenpyxl = openpyxl.load_workbook(texto1["text"])
    pegaAbas(planilhaOpenpyxl)
    

def carregaPlanilhaPandas():
    planilhaPandas = pandas.read_excel(texto1["text"], sheet_name=combo4.current())
    pegaColunas(planilhaPandas)

def pegaAbas(planilhaOpenpyxl):
    abas = planilhaOpenpyxl.sheetnames
    combo4["values"] = abas

def pegaColunas(planilha):
    colunas = planilha.columns.to_list()
    combo1["values"] = colunas
    combo2["values"] = colunas



# Cria a janela
janela1 = Tk()
janela1.title("Escolher o arquivo")
janela1.geometry("800x600")


#tipo de relief (bordas): solid, reised, sunken, flat
quadro1 = Frame(janela1, borderwidth=1,relief="solid")
quadro1.grid(column=0, row=0)



#------- Linha 0
texto1 = Label(quadro1, text="")
texto1.grid(column=0, row=0)#, padx=10, pady=10)

botao1 = Button(quadro1, text="Selecione o arquivo", command=escolheArquivo)
botao1.grid(column=1, row=0)#, padx=10, pady=10)"""

# ------ Linha 1
texto2 = Label(quadro1, text="")
texto2.grid(column=0, row=1)

botao2 = Button(quadro1, text="Carregar", command=carregaPlanilhaOpenpyxl)
botao2.grid(column=1, row=1)

# ------ Linha 2
texto5 = Label(quadro1, text="Escolha a Planilha")
texto5.grid(column=0, row=2)

combo4 = Combobox(quadro1)
combo4.grid(column=1, row=2)

botao3 = Button(quadro1, text="Avançar", command=carregaPlanilhaPandas)
botao3.grid(column=2, row=2)

# ------ Linha 3
texto3 = Label(quadro1, text="Escolha a coluna com os códigos")
texto3.grid(column=0, row=3)

combo1 = Combobox(quadro1)
combo1["values"] = ""
combo1.grid(column=1, row=3)


# ------ Linha 4
texto4 = Label(quadro1, text="Escolha a coluna com a quantidade")
texto4.grid(column=0, row=4)

listaNomes = [["0", "a","223"],["1", "b","223"]]

combo2 = Combobox(quadro1)
combo2["values"] = ""
combo2.grid(column=1, row=4)

quadro2 = Frame(janela1, borderwidth=1,relief="solid")
quadro2.grid(column=0, row=1)

tv = ttk.Treeview(quadro2, columns=("id","nome","fone"),show="headings")
tv.column("id",minwidth=0,width=50)
tv.column("nome",minwidth=0,width=50)
tv.column("fone",minwidth=0,width=50)

tv.heading("id",text="COD")
tv.heading("nome",text="NOME")
tv.heading("fone",text="TELEFONE")

tv.grid(column=0, row=0)

for (i,nome,fone) in listaNomes:
    tv.insert("","end",values=(i,nome,fone))

janela1.mainloop()