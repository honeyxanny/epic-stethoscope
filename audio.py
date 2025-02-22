import pyaudio
import numpy as np
import wave

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

    def get_info_about_system(self) -> tuple[list[tuple[str, int]], list[tuple[str, int]]]:
        input_device_names = []
        output_device_names = []

        for i in range(self.p.get_device_count()):
            device_info = self.p.get_device_info_by_index(i)

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
        volume: int
    ) -> None:
        self.is_playing = True

        thread = Thread(target=self._play, args=(device_id, shape, frequency, volume,))
        thread.start()

    def stop_sound(self) -> None:
        self.is_playing = False
    
    def _play(
        self, 
        device_id: int, 
        shape: str,
        frequency: int, 
        volume: float
    ) -> None:
        sample_rate = int(self.p.get_device_info_by_index(device_id).get('defaultSampleRate'))

        t = np.arange(0, sample_rate / frequency) / sample_rate
        waveform = volume * self.shapes[shape](frequency * t)
        waveform = (waveform * 32767).astype(np.int16)

        stream = self.p.open(format=pyaudio.paInt16, output_device_index=device_id, channels=1, rate=sample_rate, output=True)
        
        while self.is_playing:
            stream.write(waveform.tobytes())
        else:
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
            input=True
        )

        print(f'{device_id} start: {datetime.now().timestamp()}')
        
        frames = []

        while self.is_recording:
            data = stream.read(self.chunk)
            frames.append(data)
        else:
            stream.stop_stream()
            stream.close()

            wf = wave.open(f'({device_id}) {datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.wav', 'wb')
            wf.setnchannels(self.p.get_device_info_by_index(device_id).get('maxInputChannels'))
            wf.setsampwidth(self.p.get_sample_size(self.sample_format))
            wf.setframerate(sample_rate)
            wf.writeframes(b''.join(frames))
            wf.close()
            
    def start_record(
        self, 
        device1_id: int, 
        device2_id: int,
        sample_rate: int
    ) -> None:
        self.is_recording = True

        thread1 = Thread(target=self._record, args=(device1_id, sample_rate,))
        thread2 = Thread(target=self._record, args=(device2_id, sample_rate,))
        
        thread1.start()
        thread2.start()

    def stop_record(self) -> None:
        self.is_recording = False