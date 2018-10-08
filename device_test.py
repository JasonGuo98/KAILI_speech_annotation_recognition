# -*- coding:utf-8 -*-
import pyaudio
import os

def main():
    pa = pyaudio.PyAudio()
    print(pa.get_device_count())# 0 no device found


if __name__=="__main__":
    main()