#pip install gtts

# LINK IDIOMAS https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang

# git add --all
# git commit -a -m "mensage"
# git push


from gtts import gTTS

tts = gTTS('outlook', lang='en', tld='us')
tts.save("outlook_u_pt_en.mp3")

