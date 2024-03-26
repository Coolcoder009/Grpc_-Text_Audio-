from gtts import gTTS
from io import BytesIO

def text_to_audio(sentence):
    tts = gTTS(text=sentence, lang='en')
    audio_file = BytesIO()
    tts.write_to_fp(audio_file)
    audio_data = audio_file.getvalue()
    return audio_data

