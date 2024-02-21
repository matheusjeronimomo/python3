import moviepy
import moviepy.editor
from tkinter import Tk, Button

def extraiAudio(camVideo,camAudio):
	video = moviepy.editor.VideoFileClip(camVideo)
	audio = video.audio
	audio.write_audiofile(camAudio)

def escolheArquivo():
	pass

app = Tk()
app.title("Extrair audio do vídeo")
app.geometry("400x400")

botaoEscolheArquivo = Button(app, text="Escolha o arquivo", command=escolheArquivo)
botaoEscolheArquivo.grid(column=0,row=0)


app.mainloop()