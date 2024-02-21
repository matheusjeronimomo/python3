import moviepy
import moviepy.editor

video = moviepy.editor.VideoFileClip("Nome do vídeo")
audio = video.audio
audio.write_audiofile("Nome do arquivo")
