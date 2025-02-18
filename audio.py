import pyaudio
import signal
import numpy as np
from config import config

class AudioProcessor:
    p = pyaudio.PyAudio()

    is_playing = False
    is_recording = False

    def get_info_about_system(self) -> tuple[list, list]:
        input_device_names = []
        output_device_names = []

        for i in range(self.p.get_device_count()):
            device_info = self.p.get_device_info_by_index(i)

            if device_info['maxInputChannels'] > 0:
                input_device_names.append(device_info["name"].encode("cp1251").decode("utf-8"))
            elif device_info['maxOutputChannels'] > 0:
                output_device_names.append(device_info["name"].encode("cp1251").decode("utf-8"))

        return input_device_names, output_device_names

    def start_sound(
        self, 
        device_id: int,
        shape: str,
        sample_rate: int,
        frequency: int,
        volume: int
    ) -> None:
        self.is_playing = True

        if shape == "Синусоида":
            wave = (np.sin(2 * np.pi * np.arange(sample_rate * 2 * np.pi) * frequency / sample_rate)).astype(np.float32)
        elif shape == "Квадрат":
            wave = (signal.sawtooth(2 * np.pi * np.arange(sample_rate * 2 * np.pi) * frequency / sample_rate)).astype(np.float32)
        elif shape == "Пила":
            wave = (signal.square(2 * np.pi * np.arange(sample_rate * 2 * np.pi) * frequency / sample_rate)).astype(np.float32)

    def stop_sound(self) -> None:
        self.is_playing = False
        
        pass

    def start_record(self, device1_id: int, device2_id: int) -> None:
        self.is_recording = True
        
        pass

    def stop_record(self) -> None:
        self.is_recording = False
        
        pass