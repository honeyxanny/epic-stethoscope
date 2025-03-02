# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(458, 457)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        MainWindow.setAcceptDrops(True)
        MainWindow.setWindowTitle(u"\u0421\u0442\u0435\u0442\u043e\u0441\u043a\u043e\u043f")
        MainWindow.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.recordTitle = QLabel(self.centralwidget)
        self.recordTitle.setObjectName(u"recordTitle")
        font = QFont()
        font.setBold(True)
        self.recordTitle.setFont(font)
        self.recordTitle.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.recordTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.recordTitle)

        self.apiSelection = QHBoxLayout()
        self.apiSelection.setObjectName(u"apiSelection")
        self.apiLabel = QLabel(self.centralwidget)
        self.apiLabel.setObjectName(u"apiLabel")

        self.apiSelection.addWidget(self.apiLabel)

        self.apiComboBox = QComboBox(self.centralwidget)
        self.apiComboBox.setObjectName(u"apiComboBox")

        self.apiSelection.addWidget(self.apiComboBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.apiSelection.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.apiSelection)

        self.firstDeviceSelection = QHBoxLayout()
        self.firstDeviceSelection.setObjectName(u"firstDeviceSelection")
        self.firstDeviceLabel = QLabel(self.centralwidget)
        self.firstDeviceLabel.setObjectName(u"firstDeviceLabel")
        self.firstDeviceLabel.setMaximumSize(QSize(16777215, 16777215))
        self.firstDeviceLabel.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.firstDeviceLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.firstDeviceSelection.addWidget(self.firstDeviceLabel)

        self.firstDeviceComboBox = QComboBox(self.centralwidget)
        self.firstDeviceComboBox.setObjectName(u"firstDeviceComboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.firstDeviceComboBox.sizePolicy().hasHeightForWidth())
        self.firstDeviceComboBox.setSizePolicy(sizePolicy2)

        self.firstDeviceSelection.addWidget(self.firstDeviceComboBox)


        self.verticalLayout.addLayout(self.firstDeviceSelection)

        self.secondDeviceSelection = QHBoxLayout()
        self.secondDeviceSelection.setObjectName(u"secondDeviceSelection")
        self.secondDeviceLabel = QLabel(self.centralwidget)
        self.secondDeviceLabel.setObjectName(u"secondDeviceLabel")
        self.secondDeviceLabel.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.secondDeviceLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.secondDeviceSelection.addWidget(self.secondDeviceLabel)

        self.secondDeviceComboBox = QComboBox(self.centralwidget)
        self.secondDeviceComboBox.setObjectName(u"secondDeviceComboBox")
        sizePolicy2.setHeightForWidth(self.secondDeviceComboBox.sizePolicy().hasHeightForWidth())
        self.secondDeviceComboBox.setSizePolicy(sizePolicy2)

        self.secondDeviceSelection.addWidget(self.secondDeviceComboBox)


        self.verticalLayout.addLayout(self.secondDeviceSelection)

        self.fillerLabel1 = QLabel(self.centralwidget)
        self.fillerLabel1.setObjectName(u"fillerLabel1")

        self.verticalLayout.addWidget(self.fillerLabel1)

        self.inputDevicesOptions = QHBoxLayout()
        self.inputDevicesOptions.setObjectName(u"inputDevicesOptions")
        self.sampleRateLabel = QLabel(self.centralwidget)
        self.sampleRateLabel.setObjectName(u"sampleRateLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sampleRateLabel.sizePolicy().hasHeightForWidth())
        self.sampleRateLabel.setSizePolicy(sizePolicy3)
        self.sampleRateLabel.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.sampleRateLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.inputDevicesOptions.addWidget(self.sampleRateLabel)

        self.sampleRateComboBox = QComboBox(self.centralwidget)
        self.sampleRateComboBox.setObjectName(u"sampleRateComboBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.sampleRateComboBox.sizePolicy().hasHeightForWidth())
        self.sampleRateComboBox.setSizePolicy(sizePolicy4)

        self.inputDevicesOptions.addWidget(self.sampleRateComboBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.inputDevicesOptions.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.inputDevicesOptions)

        self.fillerLabel3 = QLabel(self.centralwidget)
        self.fillerLabel3.setObjectName(u"fillerLabel3")

        self.verticalLayout.addWidget(self.fillerLabel3)

        self.playTitle = QLabel(self.centralwidget)
        self.playTitle.setObjectName(u"playTitle")
        self.playTitle.setFont(font)
        self.playTitle.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.playTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.playTitle)

        self.outputDeviceSelection = QHBoxLayout()
        self.outputDeviceSelection.setObjectName(u"outputDeviceSelection")
        self.poutputDeviceLabel = QLabel(self.centralwidget)
        self.poutputDeviceLabel.setObjectName(u"poutputDeviceLabel")
        self.poutputDeviceLabel.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.poutputDeviceLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.outputDeviceSelection.addWidget(self.poutputDeviceLabel)

        self.outputDeviceComboBox = QComboBox(self.centralwidget)
        self.outputDeviceComboBox.setObjectName(u"outputDeviceComboBox")
        sizePolicy2.setHeightForWidth(self.outputDeviceComboBox.sizePolicy().hasHeightForWidth())
        self.outputDeviceComboBox.setSizePolicy(sizePolicy2)

        self.outputDeviceSelection.addWidget(self.outputDeviceComboBox)


        self.verticalLayout.addLayout(self.outputDeviceSelection)

        self.fillerLabel2 = QLabel(self.centralwidget)
        self.fillerLabel2.setObjectName(u"fillerLabel2")

        self.verticalLayout.addWidget(self.fillerLabel2)

        self.volumeSelection = QHBoxLayout()
        self.volumeSelection.setObjectName(u"volumeSelection")
        self.volumeLabel = QLabel(self.centralwidget)
        self.volumeLabel.setObjectName(u"volumeLabel")
        self.volumeLabel.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.volumeLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.volumeSelection.addWidget(self.volumeLabel)

        self.volumeSlider = QSlider(self.centralwidget)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(50)
        self.volumeSlider.setOrientation(Qt.Orientation.Horizontal)
        self.volumeSlider.setTickInterval(0)

        self.volumeSelection.addWidget(self.volumeSlider)


        self.verticalLayout.addLayout(self.volumeSelection)

        self.ouputDeviceGroup = QHBoxLayout()
        self.ouputDeviceGroup.setObjectName(u"ouputDeviceGroup")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ouputDeviceGroup.addItem(self.horizontalSpacer)

        self.durationLabel = QLabel(self.centralwidget)
        self.durationLabel.setObjectName(u"durationLabel")

        self.ouputDeviceGroup.addWidget(self.durationLabel)

        self.durationSpinBox = QSpinBox(self.centralwidget)
        self.durationSpinBox.setObjectName(u"durationSpinBox")
        self.durationSpinBox.setMinimum(0)
        self.durationSpinBox.setMaximum(600)
        self.durationSpinBox.setSingleStep(1)
        self.durationSpinBox.setValue(3)

        self.ouputDeviceGroup.addWidget(self.durationSpinBox)


        self.verticalLayout.addLayout(self.ouputDeviceGroup)

        self.outputAudioOptions = QHBoxLayout()
        self.outputAudioOptions.setObjectName(u"outputAudioOptions")
        self.shapeLabel = QLabel(self.centralwidget)
        self.shapeLabel.setObjectName(u"shapeLabel")
        self.shapeLabel.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.shapeLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.outputAudioOptions.addWidget(self.shapeLabel)

        self.shapeComboBox = QComboBox(self.centralwidget)
        self.shapeComboBox.setObjectName(u"shapeComboBox")
        sizePolicy4.setHeightForWidth(self.shapeComboBox.sizePolicy().hasHeightForWidth())
        self.shapeComboBox.setSizePolicy(sizePolicy4)

        self.outputAudioOptions.addWidget(self.shapeComboBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.outputAudioOptions.addItem(self.horizontalSpacer_3)

        self.frequencyLabel = QLabel(self.centralwidget)
        self.frequencyLabel.setObjectName(u"frequencyLabel")
        sizePolicy3.setHeightForWidth(self.frequencyLabel.sizePolicy().hasHeightForWidth())
        self.frequencyLabel.setSizePolicy(sizePolicy3)
        self.frequencyLabel.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.frequencyLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.outputAudioOptions.addWidget(self.frequencyLabel)

        self.frequencySpinBox = QSpinBox(self.centralwidget)
        self.frequencySpinBox.setObjectName(u"frequencySpinBox")
        self.frequencySpinBox.setMaximumSize(QSize(16777215, 16777215))
        self.frequencySpinBox.setMaximum(44100)
        self.frequencySpinBox.setValue(8000)

        self.outputAudioOptions.addWidget(self.frequencySpinBox)


        self.verticalLayout.addLayout(self.outputAudioOptions)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.controlsGroup = QHBoxLayout()
        self.controlsGroup.setObjectName(u"controlsGroup")
        self.plotButton = QPushButton(self.centralwidget)
        self.plotButton.setObjectName(u"plotButton")

        self.controlsGroup.addWidget(self.plotButton)

        self.playButton = QPushButton(self.centralwidget)
        self.playButton.setObjectName(u"playButton")

        self.controlsGroup.addWidget(self.playButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.controlsGroup.addItem(self.horizontalSpacer_5)

        self.recordButton = QPushButton(self.centralwidget)
        self.recordButton.setObjectName(u"recordButton")

        self.controlsGroup.addWidget(self.recordButton)


        self.verticalLayout.addLayout(self.controlsGroup)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 458, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.secondDeviceComboBox, self.firstDeviceComboBox)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.recordTitle.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u044c", None))
        self.apiLabel.setText(QCoreApplication.translate("MainWindow", u"API:", None))
        self.firstDeviceLabel.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e 1", None))
        self.secondDeviceLabel.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e 2", None))
        self.fillerLabel1.setText("")
        self.sampleRateLabel.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430 \u0434\u0438\u0441\u043a\u0440\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.fillerLabel3.setText("")
        self.playTitle.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0435", None))
        self.poutputDeviceLabel.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e", None))
        self.fillerLabel2.setText("")
        self.volumeLabel.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u043e\u043c\u043a\u043e\u0441\u0442\u044c", None))
        self.durationLabel.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.shapeLabel.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430 \u0441\u0438\u0433\u043d\u0430\u043b\u0430", None))
        self.frequencyLabel.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430", None))
        self.plotButton.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a", None))
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0432\u0443\u043a", None))
        self.recordButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u044c", None))
        pass
    # retranslateUi

