# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'flrScreen.ui'
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

class flrScreen(QtGui.QWidget):
    def __init__(self):
        super(flrScreen, self).__init__()
        self.initUI()
        self.ischecked = 0
        self.ledOn = 0
        # self.led1_checkBox.stateChanged.connect(lambda: self.change_led_state(1))
        # self.led2_checkBox.stateChanged.connect(lambda: self.change_led_state(2))
        # self.led4_checkBox.stateChanged.connect(lambda: self.change_led_state(3))
        # self.led4_checkBox.stateChanged.connect(lambda: self.change_led_state(4))

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
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.back_button = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        self.back_button.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);"))
        self.back_button.setObjectName(_fromUtf8("back_button"))
        self.horizontalLayout_17.addWidget(self.back_button)
        spacerItem = QtGui.QSpacerItem(675, 35, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem)
        self.verticalLayout_9.addLayout(self.horizontalLayout_17)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.line_7 = QtGui.QFrame(self.layoutWidget)
        self.line_7.setFrameShadow(QtGui.QFrame.Plain)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.verticalLayout_10.addWidget(self.line_7)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
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
        self.horizontalLayout_3.addWidget(self.title_label)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)
        self.line_8 = QtGui.QFrame(self.layoutWidget)
        self.line_8.setFrameShadow(QtGui.QFrame.Plain)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.verticalLayout_10.addWidget(self.line_8)
        spacerItem3 = QtGui.QSpacerItem(20, 90, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem3)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.led_label = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.led_label.sizePolicy().hasHeightForWidth())
        self.led_label.setSizePolicy(sizePolicy)
        self.led_label.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(20)
        self.led_label.setFont(font)
        self.led_label.setObjectName(_fromUtf8("led_label"))
        self.horizontalLayout_2.addWidget(self.led_label)
        self.led1_checkBox = QtGui.QCheckBox(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.led1_checkBox.sizePolicy().hasHeightForWidth())
        self.led1_checkBox.setSizePolicy(sizePolicy)
        self.led1_checkBox.setMinimumSize(QtCore.QSize(50, 0))
        self.led1_checkBox.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(12)
        self.led1_checkBox.setFont(font)
        self.led1_checkBox.setStyleSheet(_fromUtf8("QCheckBox::indicator {\n"
"width: 30px;\n"
" height: 30px;}"))
        self.led1_checkBox.setObjectName(_fromUtf8("led1_checkBox"))
        self.horizontalLayout_2.addWidget(self.led1_checkBox)
        self.led2_checkBox = QtGui.QCheckBox(self.layoutWidget)
        self.led2_checkBox.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(12)
        self.led2_checkBox.setFont(font)
        self.led2_checkBox.setStyleSheet(_fromUtf8("QCheckBox::indicator {\n"
"width: 30px;\n"
" height: 30px;}"))
        self.led2_checkBox.setObjectName(_fromUtf8("led2_checkBox"))
        self.horizontalLayout_2.addWidget(self.led2_checkBox)
        self.led3_checkBox = QtGui.QCheckBox(self.layoutWidget)
        self.led3_checkBox.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(12)
        self.led3_checkBox.setFont(font)
        self.led3_checkBox.setStyleSheet(_fromUtf8("QCheckBox::indicator {\n"
"width: 30px;\n"
" height: 30px;}"))
        self.led3_checkBox.setObjectName(_fromUtf8("led3_checkBox"))
        self.horizontalLayout_2.addWidget(self.led3_checkBox)
        self.led4_checkBox = QtGui.QCheckBox(self.layoutWidget)
        self.led4_checkBox.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(12)
        self.led4_checkBox.setFont(font)
        self.led4_checkBox.setStyleSheet(_fromUtf8("QCheckBox::indicator {\n"
"width: 30px;\n"
" height: 30px;}"))
        self.led4_checkBox.setObjectName(_fromUtf8("led4_checkBox"))
        self.horizontalLayout_2.addWidget(self.led4_checkBox)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem4)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.expTime_label = QtGui.QLabel(self.layoutWidget)
        self.expTime_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.expTime_label.setFont(font)
        self.expTime_label.setObjectName(_fromUtf8("expTime_label"))
        self.horizontalLayout_21.addWidget(self.expTime_label)
        self.expTime_singWave_spinBox = QtGui.QSpinBox(self.layoutWidget)
        self.expTime_singWave_spinBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expTime_singWave_spinBox.sizePolicy().hasHeightForWidth())
        self.expTime_singWave_spinBox.setSizePolicy(sizePolicy)
        self.expTime_singWave_spinBox.setMinimumSize(QtCore.QSize(0, 35))
        self.expTime_singWave_spinBox.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.expTime_singWave_spinBox.setFont(font)
        self.expTime_singWave_spinBox.setStyleSheet(_fromUtf8("background-color: rgb(255,255,255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 1px;"))
        self.expTime_singWave_spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.expTime_singWave_spinBox.setPrefix(_fromUtf8(""))
        self.expTime_singWave_spinBox.setMinimum(1)
        self.expTime_singWave_spinBox.setMaximum(10000)
        self.expTime_singWave_spinBox.setProperty("value", 1)
        self.expTime_singWave_spinBox.setObjectName(_fromUtf8("expTime_singWave_spinBox"))
        self.horizontalLayout_21.addWidget(self.expTime_singWave_spinBox)
        self.verticalLayout_11.addLayout(self.horizontalLayout_21)
        spacerItem5 = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem5)
        self.line_11 = QtGui.QFrame(self.layoutWidget)
        self.line_11.setFrameShadow(QtGui.QFrame.Plain)
        self.line_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.verticalLayout_11.addWidget(self.line_11)
        self.horizontalLayout_19.addLayout(self.verticalLayout_11)
        self.verticalLayout_9.addLayout(self.horizontalLayout_19)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.set_button = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_button.sizePolicy().hasHeightForWidth())
        self.set_button.setSizePolicy(sizePolicy)
        self.set_button.setMaximumSize(QtCore.QSize(150, 75))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.set_button.setFont(font)
        self.set_button.setStyleSheet(_fromUtf8("background-color: rgb(255, 191, 88);"))
        self.set_button.setObjectName(_fromUtf8("set_button"))
        self.horizontalLayout.addWidget(self.set_button)
        spacerItem7 = QtGui.QSpacerItem(40, 75, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.show()

    # def change_led_state(self, led):
    #     if self.ledOn == 0:
    #         if led == 1:
    #             self.led1_checkBox.setEnabled(True)
    #             self.led2_checkBox.setEnabled(False)
    #             self.led3_checkBox.setEnabled(False)
    #             self.led4_checkBox.setEnabled(False)
    #             self.ledOn = 1
    #         if led == 2:
    #             self.led1_checkBox.setEnabled(False)
    #             self.led2_checkBox.setEnabled(True)
    #             self.led4_checkBox.setEnabled(False)
    #             self.led4_checkBox.setEnabled(False)
    #             self.ledOn = 2
    #         if led == 3:
    #             self.led1_checkBox.setEnabled(False)
    #             self.led2_checkBox.setEnabled(False)
    #             self.led3_checkBox.setEnabled(True)
    #             self.led4_checkBox.setEnabled(False)
    #             self.ledOn = 3
    #         if led == 4:
    #             self.led1_checkBox.setEnabled(False)
    #             self.led2_checkBox.setEnabled(False)
    #             self.led3_checkBox.setEnabled(False)
    #             self.led4_checkBox.setEnabled(True)
    #             self.ledOn = 4
    #     elif self.ledOn == led:
    #         self.led1_checkBox.setEnabled(True)
    #         self.led2_checkBox.setEnabled(True)
    #         self.led3_checkBox.setEnabled(True)
    #         self.led4_checkBox.setEnabled(True)
    #         self.ledOn = 0

    def retranslateUi(self):
        self.setWindowTitle(_translate("self", "OSP", None))
        self.setWindowIcon(QtGui.QIcon("../Python Files/Images/logo_icon.png"))
        self.back_button.setText(_translate("self", "Back", None))
        self.title_label.setText(_translate("self", "<html><head/><body><p align=\"center\">FLOURESCENCE</p></body></html>", None))
        self.led_label.setText(_translate("self", "Excitation LED :", None))
        self.led1_checkBox.setText(_translate("self", "LED 1", None))
        self.led2_checkBox.setText(_translate("self", "LED 2", None))
        self.led3_checkBox.setText(_translate("self", "LED 3", None))
        self.led4_checkBox.setText(_translate("self", "FIBER", None))
        self.expTime_label.setText(_translate("self", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Exposure Time : </span></p></body></html>", None))
        self.expTime_singWave_spinBox.setSuffix(_translate("self", " ms", None))
        self.set_button.setText(_translate("self", "SET", None))

