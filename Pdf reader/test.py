from gtts import gTTS

import os

language = 'en'

mytext = 'Are '

myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("date.mp3")

# Playing the converted file
# os.system("mpg321 audio.mp3")