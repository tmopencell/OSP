# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'settingsScreen.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class settingsScreen(QtGui.QWidget):
    def __init__(self):
        super(settingsScreen, self).__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName(_fromUtf8("self"))
        self.resize(800, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(800, 480))
        self.setStyleSheet(_fromUtf8("background-color: rgb(97, 161, 243);"))
        self.layoutWidget = QtGui.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 401))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.back_button = QtGui.QPushButton(self.layoutWidget)
        self.back_button.hide()
        self.back_button.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(14)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);\n"
""))
        self.back_button.setObjectName(_fromUtf8("back_button"))
        self.horizontalLayout_17.addWidget(self.back_button)
        spacerItem = QtGui.QSpacerItem(675, 35, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_17)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.line_7 = QtGui.QFrame(self.layoutWidget)
        self.line_7.setFrameShadow(QtGui.QFrame.Plain)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.verticalLayout_10.addWidget(self.line_7)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.title_label = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setMaximumSize(QtCore.QSize(555, 40))
        self.title_label.setStyleSheet(_fromUtf8("font: 75 25pt \"Roboto\";"))
        self.title_label.setTextFormat(QtCore.Qt.AutoText)
        self.title_label.setObjectName(_fromUtf8("title_label"))
        self.horizontalLayout_9.addWidget(self.title_label)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.line_8 = QtGui.QFrame(self.layoutWidget)
        self.line_8.setFrameShadow(QtGui.QFrame.Plain)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.verticalLayout_10.addWidget(self.line_8)
        self.verticalLayout_3.addLayout(self.verticalLayout_10)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_6.addWidget(self.label_5)
        spacerItem4 = QtGui.QSpacerItem(210, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem5 = QtGui.QSpacerItem(35, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem6 = QtGui.QSpacerItem(20, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem7 = QtGui.QSpacerItem(35, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.led_logo_2 = QtGui.QLabel(self.layoutWidget)
        self.led_logo_2.setMaximumSize(QtCore.QSize(200, 200))
        self.led_logo_2.setText(_fromUtf8(""))
        self.led_logo_2.setPixmap(QtGui.QPixmap(_fromUtf8("../Python Files/Images/botttomLed.png")))
        self.led_logo_2.setScaledContents(True)
        self.led_logo_2.setAlignment(QtCore.Qt.AlignCenter)
        self.led_logo_2.setObjectName(_fromUtf8("led_logo_2"))
        self.horizontalLayout_8.addWidget(self.led_logo_2)
        spacerItem8 = QtGui.QSpacerItem(35, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        spacerItem9 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem10 = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem11 = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.led1_label = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.led1_label.sizePolicy().hasHeightForWidth())
        self.led1_label.setSizePolicy(sizePolicy)
        self.led1_label.setMinimumSize(QtCore.QSize(50, 50))
        self.led1_label.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.led1_label.setFont(font)
        self.led1_label.setObjectName(_fromUtf8("led1_label"))
        self.horizontalLayout_3.addWidget(self.led1_label)
        self.led1_spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.led1_spinBox.setMaximumSize(QtCore.QSize(75, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.led1_spinBox.setFont(font)
        self.led1_spinBox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.led1_spinBox.setMinimum(0)
        self.led1_spinBox.setMaximum(1000)
        self.led1_spinBox.setProperty("value", 490)
        self.led1_spinBox.setObjectName(_fromUtf8("led1_spinBox"))
        self.horizontalLayout_3.addWidget(self.led1_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem12 = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.led2_label = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.led2_label.sizePolicy().hasHeightForWidth())
        self.led2_label.setSizePolicy(sizePolicy)
        self.led2_label.setMinimumSize(QtCore.QSize(50, 50))
        self.led2_label.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.led2_label.setFont(font)
        self.led2_label.setObjectName(_fromUtf8("led2_label"))
        self.horizontalLayout_2.addWidget(self.led2_label)
        self.led2_spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.led2_spinBox.setMaximumSize(QtCore.QSize(75, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.led2_spinBox.setFont(font)
        self.led2_spinBox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.led2_spinBox.setMinimum(0)
        self.led2_spinBox.setMaximum(1000)
        self.led2_spinBox.setProperty("value", 490)
        self.led2_spinBox.setObjectName(_fromUtf8("led2_spinBox"))
        self.horizontalLayout_2.addWidget(self.led2_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem13 = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem13)
        self.led3_label = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.led3_label.sizePolicy().hasHeightForWidth())
        self.led3_label.setSizePolicy(sizePolicy)
        self.led3_label.setMinimumSize(QtCore.QSize(50, 50))
        self.led3_label.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.led3_label.setFont(font)
        self.led3_label.setObjectName(_fromUtf8("led3_label"))
        self.horizontalLayout.addWidget(self.led3_label)
        self.led3_spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.led3_spinBox.setMaximumSize(QtCore.QSize(75, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.led3_spinBox.setFont(font)
        self.led3_spinBox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.led3_spinBox.setMinimum(0)
        self.led3_spinBox.setMaximum(1000)
        self.led3_spinBox.setProperty("value", 490)
        self.led3_spinBox.setObjectName(_fromUtf8("led3_spinBox"))
        self.horizontalLayout.addWidget(self.led3_spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        spacerItem14 = QtGui.QSpacerItem(35, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_4.addWidget(self.line)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_4.addWidget(self.label_7)
        self.line_3 = QtGui.QFrame(self.layoutWidget)
        self.line_3.setFrameShadow(QtGui.QFrame.Plain)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_4.addWidget(self.line_3)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_4.addWidget(self.label_6)
        self.scanstoavg_spinbox = QtGui.QSpinBox(self.layoutWidget)
        self.scanstoavg_spinbox.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scanstoavg_spinbox.setFont(font)
        self.scanstoavg_spinbox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.scanstoavg_spinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.scanstoavg_spinbox.setObjectName(_fromUtf8("scanstoavg_spinbox"))
        self.verticalLayout_4.addWidget(self.scanstoavg_spinbox)
        spacerItem15 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem15)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.line_9 = QtGui.QFrame(self.layoutWidget)
        self.line_9.setFrameShadow(QtGui.QFrame.Plain)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.verticalLayout_6.addWidget(self.line_9)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem16)
        self.set_button = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_button.sizePolicy().hasHeightForWidth())
        self.set_button.setSizePolicy(sizePolicy)
        self.set_button.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_button.setFont(font)
        self.set_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);\n"
""))
        self.set_button.setObjectName(_fromUtf8("set_button"))
        self.horizontalLayout_7.addWidget(self.set_button)
        spacerItem17 = QtGui.QSpacerItem(40, 35, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem17)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.show()

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "OSP", None))
        self.setWindowIcon(QtGui.QIcon("../Python Files/Images/logo_icon.png"))
        self.back_button.setText(_translate("self", "Back", None))
        self.title_label.setText(_translate("self", "<html><head/><body><p align=\"center\">SETTINGS</p></body></html>", None))
        self.label_5.setText(_translate("self", "Set the wavelength of individual LEDs for excitement of wells.", None))
        self.led1_label.setText(_translate("self", "LED 1", None))
        self.led1_spinBox.setSuffix(_translate("self", " nm", None))
        self.led2_label.setText(_translate("self", "LED 2", None))
        self.led2_spinBox.setSuffix(_translate("self", " nm", None))
        self.led3_label.setText(_translate("self", "LED 3", None))
        self.led3_spinBox.setSuffix(_translate("self", " nm", None))
        self.label_7.setText(_translate("self", " Measurement Options:", None))
        self.label_6.setText(_translate("self", "# Scans to Average:", None))
        self.set_button.setText(_translate("self", "SET", None))

