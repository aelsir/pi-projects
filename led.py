from gpiozero import LED
from time import sleep
import wave

sample = wave.open("./sample.wav", 'rb')

sample_soundwave = sample.readframes(-1)
print("hello world")
print(sample.getframes())