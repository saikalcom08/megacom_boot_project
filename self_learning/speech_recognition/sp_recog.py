import speech_recognition as sr

# Creating a recognition object
r = sr.Recognizer()

# Extracting the audio & removing ambient noice
audio_file = sr.AudioFile('video.wav')
with audio_file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)

# Recognize the audio
print(r.recognize_google(audio))