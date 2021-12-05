from matplotlib.pyplot import stem
import librosa
import pyaudio


filename = './sample.wav'
y, sr = librosa.load(filename)

stream = librosa.stream(filename, block_length=256, frame_length = 4096, hop_length=1024)

for y_block in stream:
    D_block = librosa.stft(y_block, center=False)
    pyaudio.
