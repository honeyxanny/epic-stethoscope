from main_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from audio import AudioProcessor

from config import config

class MainWindow(QMainWindow):
    previous_device1_index = 0
    previous_device2_index = 0

    def __init__(self, audio_processor: AudioProcessor):
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ap = audio_processor

        input_device_names, output_device_names = self.ap.get_info_about_system()

        self.ui.firstDeviceComboBox.addItems(input_device_names)
        self.ui.secondDeviceComboBox.addItems(input_device_names)
        self.ui.secondDeviceComboBox.setCurrentIndex(1)
        self.previous_device2_index = 1
        self.ui.outputDeviceComboBox.addItems(output_device_names)

        self.ui.sampleRateComboBox.addItems([str(sample_rate) for sample_rate in config.sample_rates])
        self.ui.bitDepthComboBox.addItems([str(bit_depth) for bit_depth in config.bit_depths])
        self.ui.shapeComboBox.addItems(["Синусоида", "Квадрат", "Пила"])

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
        if self.ap.is_playing:
            self.ap.stop_sound()

            self.__change_options_state(True)
            self.ui.playButton.setText('Звук')
        else:
            self.ap.start_sound(
                self.ui.outputDeviceComboBox.currentIndex(),
                self.ui.shapeComboBox.currentText(),
                int(self.ui.sampleRateComboBox.currentText()),
                int(self.ui.sampleRateComboBox.currentText()),
                self.ui.volumeSlider.value()
            )

            self.__change_options_state(False)
            self.ui.playButton.setText('Стоп')

    def __register_first_index(self):
        self.previous_device1_index = self.ui.firstDeviceComboBox.currentIndex()

    def __register_second_index(self):
        self.previous_device2_index = self.ui.secondDeviceComboBox.currentIndex()

    def __validate_input_device_selection(self):
        index1 = self.ui.firstDeviceComboBox.currentIndex()
        index2 = self.ui.secondDeviceComboBox.currentIndex()
        
        if index1 == index2:
            if index1 != self.previous_device1_index:
                self.ui.secondDeviceComboBox.setCurrentIndex(self.previous_device1_index)
            elif index2 != self.previous_device2_index:
                self.ui.firstDeviceComboBox.setCurrentIndex(self.previous_device2_index)