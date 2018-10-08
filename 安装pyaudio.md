# 安装pyaudio

1. 安装过程中可能会报错：

   `failed error: portaudio.h:`没有这个文件

2. pyaudio的运行需要依赖于portaudio这个库，要先安装一个portaudio库

3. 安装portaudio方法：

   1. 下载portaudio库http://portaudio.com/download.html

   2. 解压：

      `tar -xzvf pa_stable_v190600_20161030.tgz`

   3. 进入目录：

      `cd portaudio/`

   4. 执行代码：

      ```shell
      ./configure
      
      make
      
      make install
      ```

   5. 进入~/.bashrc文件：vim ~/.bashrc

      　　　　在文件最后一行加入  export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib

      　　　　然后执行命令ldconfig

4. 安装pyaudio库，pip3 install pyaudio

5. 在上面的安装完成后会出这样的问题：`OSError: [Errno -9996] Invalid input device (no default output device)`

   解决方法：先卸载

   ```shell
   sudo apt remove python-pyaudio python3-pyaudio
   sudo apt autoremove
   ```

   再安装：

   ```shell
   sudo apt install libasound-dev#一定要有这一句，这是解决问题的关键
   ./configure
   make
   sudo make install
   ```

   最后：

   ```shell
   pip3 install pyaudio
   ```

