#pip install gtts


from gtts import gTTS

texto = "voo"
lingua = "pt"
tts = gTTS(texto, lang=lingua)
tts.save("u_voo.mp3")

