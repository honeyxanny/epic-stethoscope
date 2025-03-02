import pyaudio
import numpy as np
import wave
import matplotlib.pyplot as plt
import os

from scipy.signal import sawtooth, square
from datetime import datetime
from threading import Thread
from config import config

class AudioProcessor:
    p = pyaudio.PyAudio()

    chunk = 1024
    sample_format = pyaudio.paInt16

    is_playing = False
    is_recording = False

    stream1_start = None
    stream2_start = None
    
    shapes = {
        'Синусоида': lambda scale: np.sin(2 * np.pi * scale),
        'Квадрат': lambda scale: square(2 * np.pi * scale),
        'Пила': lambda scale: sawtooth(2 * np.pi * scale, width=0.5)
    }

    def get_system_apis(self):
        return [(self.p.get_host_api_info_by_index(i)['name'], i) for i in range(self.p.get_host_api_count())]
    
    def get_device_names_by_api(self, api_index: int) -> tuple[list[tuple[str, int]]]:
        input_device_names = []
        output_device_names = []
        
        for i in range(self.p.get_host_api_info_by_index(api_index)['deviceCount']):
            device_info = self.p.get_device_info_by_host_api_device_index(api_index, i)

            if device_info['maxInputChannels'] > 0:
                input_device_names.append((device_info["name"].encode("cp1251").decode("utf-8"), i))
            elif device_info['maxOutputChannels'] > 0:
                output_device_names.append((device_info["name"].encode("cp1251").decode("utf-8"), i))

        return input_device_names, output_device_names

    def start_sound(
        self, 
        device_id: int,
        shape: str,
        frequency: int,
        volume: int,
        duration: int = - 1
    ) -> None:
        self.is_playing = True

        thread = Thread(target=self._play, args=(device_id, shape, frequency, volume, duration))
        thread.start()

    def stop_sound(self) -> None:
        self.is_playing = False
    
    def _play(
        self, 
        device_id: int, 
        shape: str,
        frequency: int, 
        volume: float,
        duration: int
    ) -> None:
        sample_rate = int(self.p.get_device_info_by_index(device_id).get('defaultSampleRate'))

        t = np.arange(0, sample_rate / frequency) / sample_rate
        waveform = volume * self.shapes[shape](frequency * t)
        waveform = (waveform * 32767).astype(np.int16)

        num_iterations = int(sample_rate * duration / len(waveform))

        stream = self.p.open(format=pyaudio.paInt16, output_device_index=device_id, channels=1, rate=sample_rate, output=True)

        if duration < 0:
            while self.is_playing:
                stream.write(waveform.tobytes())
        else:
            for _ in range(num_iterations):
                if not self.is_playing:
                    break
                stream.write(waveform.tobytes())

        stream.stop_stream()
        stream.close()

    def _record(
        self, 
        device_id: int,
        sample_rate: int
    ):
        stream = self.p.open(
            format=self.sample_format,
            channels=self.p.get_device_info_by_index(device_id).get('maxInputChannels'),
            rate=sample_rate,
            frames_per_buffer=self.chunk,
            input_device_index=device_id,
            input=True,
        )

        print(f'{device_id} start: {datetime.now().timestamp()}')

        frames = []

        while self.is_recording:
            data = stream.read(self.chunk)
            frames.append(data)
        else:
            stream.stop_stream()
            stream.close()

            wf = wave.open(f'./output/({device_id}) {datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.wav', 'wb')
            wf.setnchannels(self.p.get_device_info_by_index(device_id).get('maxInputChannels'))
            wf.setsampwidth(self.p.get_sample_size(self.sample_format))
            wf.setframerate(sample_rate)
            wf.writeframes(b''.join(frames))
            wf.close()
            
    def start_record(
        self, 
        device1_id: int, 
        device2_id: int,
        sample_rate: int,
    ) -> None:
        self.is_recording = True
        self.is_playing = True

        thread1 = Thread(target=self._record, args=(device1_id, sample_rate,))
        thread2 = Thread(target=self._record, args=(device2_id, sample_rate,))

        thread1.start()
        thread2.start()

    def stop_record(self) -> None:
        self.is_recording = False
        self.is_playing = False

    def _get_data_from_sound(self, file_path: str) -> list:
        with wave.open(file_path, 'rb') as wav_file:
            n_channels = wav_file.getnchannels()
            n_frames = wav_file.getnframes()

            audio_data = wav_file.readframes(n_frames)

        result = np.frombuffer(audio_data, dtype=np.int16)

        if n_channels == 2:
            result = result.reshape(-1, 2).mean(axis=1)

        # можем получить время в секундах на оси x
        # times = np.linspace(0, n_frames / frame_rate, num=n_frames)
        
        return result

    def plot_sound(self, file_path1: str, file_path2: str):
        data1 = self._get_data_from_sound(file_path1)
        data2 = self._get_data_from_sound(file_path2)

        length1 = len(data1)
        length2 = len(data2)

        if length1 < length2:
            data2 = data2[:length1]
        else:
            data1 = data1[:length2]

        _, (ax1, ax2, ax3) = plt.subplots(3, 1)

        data1 = data1 / np.max(np.abs(data1))
        data2 = data2 / np.max(np.abs(data2))

        ax1.plot(data1, color='b')
        ax1.set_title(os.path.basename(file_path1))

        ax2.plot(data2, color='r')
        ax2.set_title(os.path.basename(file_path2))

        ax3.plot(data1 - data2, color='k')
        ax3.set_title('Разница')

        plt.tight_layout()
        plt.show()