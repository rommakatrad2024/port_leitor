#pip install gtts

# LINK IDIOMAS https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang

# git add --all
# git commit -a -m "mensage"
# git push


from gtts import gTTS

texto = "outlook"
lingua = "en-uk"
tts = gTTS(texto, lang=lingua)
tts.save("u_outlook.mp3")

