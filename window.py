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

        input_device_info, output_device_info = self.ap.get_info_about_system()

        for input_device in input_device_info:
            self.ui.firstDeviceComboBox.addItem(*input_device)
            self.ui.secondDeviceComboBox.addItem(*input_device)

        self.ui.secondDeviceComboBox.setCurrentIndex(1)
        self.previous_device2_index = 1
        
        for ouput_device in output_device_info:
            self.ui.outputDeviceComboBox.addItem(*ouput_device)

        self.ui.sampleRateComboBox.addItems([str(sample_rate) for sample_rate in config.sample_rates])
        self.ui.shapeComboBox.addItems(self.ap.shapes.keys())

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
        self.ui.outputDeviceComboBox.setEnabled(flag)
        self.ui.volumeSlider.setEnabled(flag)
        self.ui.sampleRateComboBox.setEnabled(flag)
        self.ui.shapeComboBox.setEnabled(flag)
        self.ui.frequencySpinBox.setEnabled(flag)
    
    def __register_record_button_click(self):
        if self.ap.is_recording:
            self.__change_options_state(True)
            self.ap.stop_record()
            self.ui.recordButton.setText('Запись')
        else:
            self.__change_options_state(False)

            self.ap.start_record(
                self.ui.firstDeviceComboBox.currentData(),
                self.ui.secondDeviceComboBox.currentData(),
                int(self.ui.sampleRateComboBox.currentText())
            )

            self.ui.recordButton.setText('Стоп')

    def __register_play_button_click(self):
        if self.ap.is_playing:
            self.ap.stop_sound()
            self.__change_options_state(True)
            self.ui.playButton.setText('Звук')
        else:
            self.ap.start_sound(
                self.ui.outputDeviceComboBox.currentData(),
                self.ui.shapeComboBox.currentText(),
                int(self.ui.frequencySpinBox.value()),
                self.ui.volumeSlider.value() / self.ui.volumeSlider.maximum()
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