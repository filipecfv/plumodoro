import sounddevice as sd
import soundfile as sf
import os

path = os.path.dirname( __file__ )

def alarm():
    data, samplerate = sf.read(path + '/sounds/alarm.ogg')
    sd.play(data, samplerate, blocksize=8192)
    sd.wait()

alarm()
