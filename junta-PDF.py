import PyPDF2
from tkinter import filedialog, Tk, Button, Label, Entry


"""arq1 = open("C:/Users/Matheus/Documents/Teste Python/arq1.pdf","rb")
arq2 = open("C:/Users/Matheus/Documents/Teste Python/arq2.pdf","rb")
mesclador = PyPDF2.PdfMerger()

mesclador.append(arq1)
mesclador.append(arq2)

mesclador.write("Arquivos mesclados.pdf")"""

def escolheArquivo():
	pass

def mesclaArquivo():
	pass


def salvaArquivo():
	pass


app = Tk()
app.geometry("400x400")

# ---- Linha 01

textoBotaoEscolheArquivo1 = Label(app)
textoBotaoEscolheArquivo1.grid(column=0,row=0)

botaoEscolheArquivo1 = Button(app,text="Escolha os arquivos")
botaoEscolheArquivo1.grid(column=1,row=0)


# ---- Linha 02

textoBotaoEscolheArquivo2 = Label(app)
textoBotaoEscolheArquivo2.grid(column=0,row=1)

botaoEscolheArquivo2 = Button(app,text="Escolha os arquivos")
botaoEscolheArquivo2.grid(column=1,row=1)


# ---- Linha 03

textoBotaoEscolheArquivo3 = Label(app)
textoBotaoEscolheArquivo3.grid(column=0,row=2)

botaoEscolheArquivo3 = Button(app,text="Escolha os arquivos")
botaoEscolheArquivo3.grid(column=1,row=2)




# ---- Linha 04
textoNomeArquivo = Label(app,text="Digite o nome do arquivo")
textoNomeArquivo.grid(column=0,row=3)

caixaTextoNomeArquivo = Entry(app,width=10)
caixaTextoNomeArquivo.grid(column=1,row=3)


# ---- Linha 05
textoBotaoMesclar = Label(app,text="")
textoBotaoMesclar.grid(column=0,row=4)

botaoMesclar = Button(app,text="Juntar PDFs",command=mesclaArquivo())
botaoMesclar.grid(column=1,row=4)



app.mainloop()

