# -*- coding:utf-8 -*-
import pyaudio
import wave
import os

def main():
    pa = pyaudio.PyAudio()
    print(pa.get_device_count())# 0 no device found
    try:
        os.mkdir('audio')
    except FileExistsError :
        pass

    f = wave.open('audio/input.wav','wb')
    f.close()

if __name__=="__main__":
    main()