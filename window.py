from main_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from audio import AudioProcessor

from config import config

class MainWindow(QMainWindow):
    _previous_device1_index = 0
    _previous_device2_index = 0

    def __init__(self, audio_processor: AudioProcessor):
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ap = audio_processor

        system_apis = self.ap.get_system_apis()

        if len(system_apis) == 0:
            self._show_message_box('В системе отсутствует API для работы со звуком!')
            return 
        
        for api in system_apis:
            self.ui.apiComboBox.addItem(*api)
        
        self._show_devices_by_api(system_apis[0][1])

    def run(self) -> None:
        self.ui.firstDeviceComboBox.currentIndexChanged.connect(self._validate_input_device_selection)
        self.ui.secondDeviceComboBox.currentIndexChanged.connect(self._validate_input_device_selection)
        
        self.ui.firstDeviceComboBox.currentIndexChanged.connect(self._register_first_index)
        self.ui.secondDeviceComboBox.currentIndexChanged.connect(self._register_second_index)

        self.ui.recordButton.clicked.connect(self._register_record_button_click)
        self.ui.playButton.clicked.connect(self._register_play_button_click)
        self.ui.plotButton.clicked.connect(self._plot_button_handler)

        self.ui.apiComboBox.currentIndexChanged.connect(self._api_change_handler)
        self.show()
    
    def _change_options_state(self, flag: bool) -> None:
        self.ui.firstDeviceComboBox.setEnabled(flag)
        self.ui.secondDeviceComboBox.setEnabled(flag)
        self.ui.sampleRateComboBox.setEnabled(flag)
        self.ui.outputDeviceComboBox.setEnabled(flag)
        self.ui.volumeSlider.setEnabled(flag)
        self.ui.sampleRateComboBox.setEnabled(flag)
        self.ui.shapeComboBox.setEnabled(flag)
        self.ui.frequencySpinBox.setEnabled(flag)
    
    def _register_record_button_click(self):
        try:
            if self.ap.is_recording:
                self._change_options_state(True)
                self.ap.stop_record()
                self.ui.recordButton.setText('Запись')
            else:
                self._change_options_state(False)

                self.ap.start_record(
                    self.ui.firstDeviceComboBox.currentData(),
                    self.ui.secondDeviceComboBox.currentData(),
                    int(self.ui.sampleRateComboBox.currentText()),
                )

                self.ap.start_sound(
                    self.ui.outputDeviceComboBox.currentData(),
                    self.ui.shapeComboBox.currentText(),
                    int(self.ui.frequencySpinBox.value()),
                    self.ui.volumeSlider.value() / self.ui.volumeSlider.maximum(),
                    self.ui.durationSpinBox.value()
                )

                self.ui.recordButton.setText('Стоп')
        except Exception as error:
            self._show_message_box(error)

    def _show_message_box(self, message: str):
        box = QMessageBox()
        box.setWindowTitle("Внимание")
        box.setText(message)
        box.exec()

    def _register_play_button_click(self):
        if self.ap.is_playing:
            self.ap.stop_sound()
            self._change_options_state(True)
            self.ui.playButton.setText('Звук')
        else:
            self.ap.start_sound(
                self.ui.outputDeviceComboBox.currentData(),
                self.ui.shapeComboBox.currentText(),
                int(self.ui.frequencySpinBox.value()),
                self.ui.volumeSlider.value() / self.ui.volumeSlider.maximum()
            )

            self._change_options_state(False)
            self.ui.playButton.setText('Стоп')

    def _register_first_index(self):
        self._previous_device1_index = self.ui.firstDeviceComboBox.currentIndex()

    def _register_second_index(self):
        self._previous_device2_index = self.ui.secondDeviceComboBox.currentIndex()

    def _validate_input_device_selection(self):
        index1 = self.ui.firstDeviceComboBox.currentIndex()
        index2 = self.ui.secondDeviceComboBox.currentIndex()
        
        if index1 == index2:
            if index1 != self._previous_device1_index:
                self.ui.secondDeviceComboBox.setCurrentIndex(self._previous_device1_index)
            elif index2 != self._previous_device2_index:
                self.ui.firstDeviceComboBox.setCurrentIndex(self._previous_device2_index)

    def _plot_button_handler(self):
        file_dialog = QFileDialog(self)
        file_paths, _ = file_dialog.getOpenFileNames(
            self, 
            "Выберите файлы", 
            "", 
            "WAV файлы (*.wav)"
        )
        
        file_count = len(file_paths)

        if file_count == 2:
            self.ap.plot_sound(*file_paths)
        elif file_count > 2:
            self._show_message_box('Нельзя открыть более двух файлов!')
    
    def _api_change_handler(self):
        self._show_devices_by_api(self.ui.apiComboBox.currentData())

    def _show_devices_by_api(self, api_index: int) -> None:
        self.ui.firstDeviceComboBox.clear()
        self.ui.secondDeviceComboBox.clear()
        self.ui.outputDeviceComboBox.clear()

        input_device_info, output_device_info = self.ap.get_device_names_by_api(api_index)

        for input_device in input_device_info:
            self.ui.firstDeviceComboBox.addItem(*input_device)
            self.ui.secondDeviceComboBox.addItem(*input_device)

        self._previous_device1_index = 0
        self.ui.firstDeviceComboBox.setCurrentIndex(0)

        self._previous_device2_index = 1

        if len(input_device_info) > 1:
            self.ui.secondDeviceComboBox.setCurrentIndex(1)
            self.ui.secondDeviceComboBox.setEnabled(True)
        else:
            self.ui.secondDeviceComboBox.setEnabled(False)

        for ouput_device in output_device_info:
            self.ui.outputDeviceComboBox.addItem(*ouput_device)

        self.ui.sampleRateComboBox.addItems([str(sample_rate) for sample_rate in config.sample_rates])
        self.ui.shapeComboBox.addItems(self.ap.shapes.keys())