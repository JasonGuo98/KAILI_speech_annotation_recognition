# -*- coding：utf-8 -*-
# -*- 2018/07/12; 15:19
# -*- python3.5
import pyaudio
import wave
import os
import numpy as np
import matplotlib.pyplot as plt


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
        self.frames = []
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = self.stream.read(self.CHUNK)
            self.frames.append(data)
        print("*" * 10, "录音结束\n")


        self.stream.stop_stream()
        self.stream.close()
        pa.terminate()

        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')

        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(pa.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def wavread(self,path=''):
        if path == '':
            path = self.WAVE_OUTPUT_FILENAME
        wavfile = wave.open(path, "rb")
        params = wavfile.getparams()

        framesra, frameswav = params[2], params[3]

        datawav = wavfile.readframes(frameswav)
        wavfile.close()
        datause = np.fromstring(datawav, dtype=np.short)
        print(datause.shape)
        datause.shape = -1, 1# 单声道
        datause = datause.T
        print(datause.shape)
        time = np.arange(0, frameswav) * (1.0 / framesra)
        return datause, time

    def print_wave(self):# 输出波形图
        #path = input("The Path is:")
        wavdata, wavtime = self.wavread()
        plt.title("wav's Frames")
        plt.subplot(211)
        plt.plot(wavtime, wavdata[0], color='green')
        # plt.subplot(212)
        # plt.plot(wavtime, wavdata[1])
        plt.show()






# def get_audio(filepath):
#     aa = str(input("是否开始录音？   （Y/N）"))
#     if aa == str("Y") :
#         CHUNK = 256
#         FORMAT = pyaudio.paInt16
#         CHANNELS = 1                # 声道数
#         RATE = 11025                # 采样率
#         RECORD_SECONDS = 5
#         WAVE_OUTPUT_FILENAME = filepath
#         p = pyaudio.PyAudio()
#
#         stream = p.open(format=FORMAT,
#                         channels=CHANNELS,
#                         rate=RATE,
#                         input=True,
#                         frames_per_buffer=CHUNK)
#
#         print("*"*10, "开始录音：请在5秒内输入语音")
#         frames = []
#         for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#             data = stream.read(CHUNK)
#             frames.append(data)
#         print("*"*10, "录音结束\n")
#
#         stream.stop_stream()
#         stream.close()
#         p.terminate()
#
#         wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#
#         wf.setnchannels(CHANNELS)
#         wf.setsampwidth(p.get_sample_size(FORMAT))
#         wf.setframerate(RATE)
#         wf.writeframes(b''.join(frames))
#         wf.close()
#     elif aa == str("N"):
#         exit()
#     else:
#         print("无效输入，请重新选择")
#         get_audio(in_path)

if __name__ =='__main__':
    au = Audio(in_path)
    au.get_audio()
    au.print_wave()

