import pyaudio
import wave


#parameters of the audio
#name of the file generated
filename="output.wav"
#length of the recording period
seconds = 5
# frameperbuffer is in bytes
frameperbuffer = 3200
#sizedepthwidth as in format is bit depth of a audio and is related to accuracy of a audio and has only two values 16 bit(2x) and 24 bits(3x)
sizedepthwidth = pyaudio.paInt16
#channels are the number of audio channels(like mono(1) or stereo(2))
channel = 1
#framerate as in rate is frequency(or sample frequency or cycle) of a audio and is related to its quality and also affects its file size usually, 48k or 16k or 44.1k
framerate = 16000


#pyaudio object creation
p = pyaudio.PyAudio()


#set audio parameter 
stream = p.open(
   format=sizedepthwidth,
   channels=channel,
   rate=framerate,
   input=True,
   frames_per_buffer=frameperbuffer
)


print("start recording...",framerate / frameperbuffer * seconds)


# starts recording voice in stream and stores in frames 
frames = []
for i in range(0, int(framerate / frameperbuffer * seconds)):
    data = stream.read(frameperbuffer)
    frames.append(data)


#terminates/close recording
#stop recording
stream.stop_stream()
#close recording object
stream.close()
#terminates pyaudio object
p.terminate()


print("recording stopped")


#store the stream(recorded audio) to a file
filename=input("Enter the filename for this record:")
filename=filename+".wav"
wf = wave.open(filename, 'wb')
wf.setnchannels(channel)
wf.setsampwidth(p.get_sample_size(sizedepthwidth))
wf.setframerate(framerate)
wf.writeframes(b''.join(frames))
wf.close()