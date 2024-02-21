import PyPDF2

arq1 = open("C:/Users/Matheus/Documents/Teste Python/arq1.pdf","rb")
arq2 = open("C:/Users/Matheus/Documents/Teste Python/arq2.pdf","rb")

mesclador = PyPDF2.PdfMerger()

mesclador.append(arq1)
mesclador.append(arq2)

mesclador.write("Arquivos mesclados.pdf")
