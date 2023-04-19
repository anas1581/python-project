import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()

# Load the audio file
with sr.AudioFile('harvard.wav') as source:
    audio = r.record(source)

# Convert the audio to text
text = r.recognize_google(audio)

# Print the extracted text
print(text)
