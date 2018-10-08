# -*- coding：utf-8 -*-
# -*- 2018/07/12; 15:19
# -*- python3.5
import pyaudio
import wave
import os


input_filename = "input.wav" # 麦克风采集的语音输入
file_path = 'audio'
try:
    os.mkdir(file_path)
except FileExistsError:
    pass
input_filepath = file_path              # 输入文件的path
in_path = os.path.join(input_filepath,input_filename)

class Audio(object):
    def __init__(self,filepath):
        self.CHUNK = 256
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1                # 声道数
        self.RATE = 11025                # 采样率
        self.RECORD_SECONDS = 5  #时间
        self.WAVE_OUTPUT_FILENAME = filepath

    def get_audio(self):
        pa = pyaudio.PyAudio()
        self.stream = pa.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
        print("*" * 10, "开始录音：请在5秒内输入语音")
        frames = []
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = self.stream.read(self.CHUNK)
            frames.append(data)
        print("*" * 10, "录音结束\n")




def get_audio(filepath):
    aa = str(input("是否开始录音？   （Y/N）"))
    if aa == str("Y") :
        CHUNK = 256
        FORMAT = pyaudio.paInt16
        CHANNELS = 1                # 声道数
        RATE = 11025                # 采样率
        RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = filepath
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("*"*10, "开始录音：请在5秒内输入语音")
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("*"*10, "录音结束\n")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')

        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
    elif aa == str("N"):
        exit()
    else:
        print("无效输入，请重新选择")
        get_audio(in_path)

if __name__ =='__main__':
    get_audio(in_path)