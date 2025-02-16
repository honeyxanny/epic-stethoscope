import pyaudio
from main_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow

from config import config

class MainWindow(QMainWindow):
    previous_first_index = 0
    previous_second_index = 0

    is_recording = False
    is_playing = False

    def __init__(self):
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        p = pyaudio.PyAudio()

        input_device_names = []
        output_device_names = []

        for i in range(p.get_device_count()):
            device_info = p.get_device_info_by_index(i)

            if device_info['maxInputChannels'] > 0:
                input_device_names.append(f'({i}) {device_info["name"].encode("cp1251").decode("utf-8")}')
            if device_info['maxOutputChannels'] > 0:
                output_device_names.append(f'({i}) {device_info["name"].encode("cp1251").decode("utf-8")}')

        self.ui.firstDeviceComboBox.addItems(input_device_names)
        self.ui.secondDeviceComboBox.addItems(input_device_names)
        self.ui.secondDeviceComboBox.setCurrentIndex(1)
        self.previous_second_index = 1
        self.ui.outputDeviceComboBox.addItems(output_device_names)

        self.ui.sampleRateComboBox.addItems([str(sample_rate) for sample_rate in config.sample_rates])
        self.ui.bitDepthComboBox.addItems([str(bit_depth) for bit_depth in config.bit_depths])
        self.ui.shapeComboBox.addItems(config.shape_names)

    def run(self) -> None:
        self.ui.firstDeviceComboBox.currentIndexChanged.connect(self.__validate_input_device_selection)
        self.ui.secondDeviceComboBox.currentIndexChanged.connect(self.__validate_input_device_selection)
        
        self.ui.firstDeviceComboBox.currentIndexChanged.connect(self.__register_first_index)
        self.ui.secondDeviceComboBox.currentIndexChanged.connect(self.__register_second_index)

        self.ui.recordButton.clicked.connect(self.__register_record_button_click)
        self.ui.playButton.clicked.connect(self.__register_play_button_click)

        self.show()
    
    def __change_options_state(self, flag: bool) -> None:
        self.ui.firstDeviceComboBox.setEnabled(flag)
        self.ui.secondDeviceComboBox.setEnabled(flag)
        self.ui.sampleRateComboBox.setEnabled(flag)
        self.ui.bitDepthComboBox.setEnabled(flag)
        self.ui.outputDeviceComboBox.setEnabled(flag)
        self.ui.volumeSlider.setEnabled(flag)
        self.ui.sampleRateComboBox.setEnabled(flag)
        self.ui.shapeComboBox.setEnabled(flag)
        self.ui.frequencySpinBox.setEnabled(flag)
    
    def __register_record_button_click(self):
        if self.is_recording:
            self.__change_options_state(True)

            self.ui.recordButton.setText('Запись')
            self.is_recording = False
        else:
            self.__change_options_state(False)

            self.ui.recordButton.setText('Стоп')
            self.is_recording = True

    def __register_play_button_click(self):
        if self.is_playing:
            self.__change_options_state(True)

            self.ui.playButton.setText('Звук')
            self.is_playing = False
        else:
            self.__change_options_state(False)

            self.ui.playButton.setText('Стоп')
            self.is_playing = True

    def __register_first_index(self):
        self.previous_first_index = self.ui.firstDeviceComboBox.currentIndex()

    def __register_second_index(self):
        self.previous_second_index = self.ui.secondDeviceComboBox.currentIndex()

    def __validate_input_device_selection(self):
        index1 = self.ui.firstDeviceComboBox.currentIndex()
        index2 = self.ui.secondDeviceComboBox.currentIndex()
        
        if index1 == index2:
            if index1 != self.previous_first_index:
                self.ui.secondDeviceComboBox.setCurrentIndex(self.previous_first_index)
            elif index2 != self.previous_second_index:
                self.ui.firstDeviceComboBox.setCurrentIndex(self.previous_second_index)