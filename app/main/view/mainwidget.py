from PyQt5 import QtCore, QtGui, QtWidgets

class MainWidget(object):

    def monitorTab(self):
        self.monitor = QtWidgets.QWidget()
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.monitor)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.verticalLayout = QtWidgets.QVBoxLayout()

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.groupBox = QtWidgets.QGroupBox(self.monitor)

        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)

        self.gridLayout = QtWidgets.QGridLayout()

        self.label_2 = QtWidgets.QLabel(self.groupBox)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setPixmap(QtGui.QPixmap(":/icons/signal-none.png"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setPixmap(QtGui.QPixmap(":/icons/wifi_big_disabled.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 3, 2, 1)

        self.label_3 = QtWidgets.QLabel(self.groupBox)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setPixmap(QtGui.QPixmap(":/icons/signal-none.png"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)

        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QtWidgets.QGroupBox(self.monitor)

        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)

        self.gridLayout_6 = QtWidgets.QGridLayout()

        self.label_20 = QtWidgets.QLabel(self.groupBox_2)

        self.gridLayout_6.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setPixmap(QtGui.QPixmap(":/icons/signal-none.png"))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_21, 0, 1, 1, 1)

        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_22, 0, 2, 1, 1)

        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setPixmap(QtGui.QPixmap(":/icons/wifi_big_disabled.png"))
        self.label_23.setScaledContents(False)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_23, 0, 3, 2, 1)

        self.label_24 = QtWidgets.QLabel(self.groupBox_2)

        self.gridLayout_6.addWidget(self.label_24, 1, 0, 1, 1)

        self.label_25 = QtWidgets.QLabel(self.groupBox_2)
        self.label_25.setPixmap(QtGui.QPixmap(":/icons/signal-none.png"))
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_25, 1, 1, 1, 1)

        self.label_26 = QtWidgets.QLabel(self.groupBox_2)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_26, 1, 2, 1, 1)

        self.gridLayout_5.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.horizontalLayout.addWidget(self.groupBox_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()

        self.groupBox_3 = QtWidgets.QGroupBox(self.monitor)

        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_3)

        self.gridLayout_8 = QtWidgets.QGridLayout()

        self.label_27 = QtWidgets.QLabel(self.groupBox_3)

        self.gridLayout_8.addWidget(self.label_27, 0, 0, 1, 1)

        self.label_28 = QtWidgets.QLabel(self.groupBox_3)
        self.label_28.setPixmap(QtGui.QPixmap(":/icons/signal-none.png"))
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_28, 0, 1, 1, 1)

        self.label_29 = QtWidgets.QLabel(self.groupBox_3)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_29, 0, 2, 1, 1)

        self.label_30 = QtWidgets.QLabel(self.groupBox_3)
        self.label_30.setPixmap(QtGui.QPixmap(":/icons/wifi_big_disabled.png"))
        self.label_30.setScaledContents(False)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_30, 0, 3, 2, 1)

        self.label_31 = QtWidgets.QLabel(self.groupBox_3)

        self.gridLayout_8.addWidget(self.label_31, 1, 0, 1, 1)

        self.label_32 = QtWidgets.QLabel(self.groupBox_3)
        self.label_32.setPixmap(QtGui.QPixmap(":/icons/signal-none.png"))
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_32, 1, 1, 1, 1)

        self.label_33 = QtWidgets.QLabel(self.groupBox_3)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_33, 1, 2, 1, 1)

        self.gridLayout_7.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.horizontalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QtWidgets.QGroupBox(self.monitor)

        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_4)

        self.gridLayout_10 = QtWidgets.QGridLayout()

        self.label_34 = QtWidgets.QLabel(self.groupBox_4)

        self.gridLayout_10.addWidget(self.label_34, 0, 0, 1, 1)

        self.label_35 = QtWidgets.QLabel(self.groupBox_4)
        self.label_35.setPixmap(QtGui.QPixmap(":/icons/signal-none.png"))
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_35, 0, 1, 1, 1)

        self.label_36 = QtWidgets.QLabel(self.groupBox_4)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_36, 0, 2, 1, 1)

        self.label_37 = QtWidgets.QLabel(self.groupBox_4)
        self.label_37.setPixmap(QtGui.QPixmap(":/icons/wifi_big_disabled.png"))
        self.label_37.setScaledContents(False)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_37, 0, 3, 2, 1)

        self.label_38 = QtWidgets.QLabel(self.groupBox_4)

        self.gridLayout_10.addWidget(self.label_38, 1, 0, 1, 1)

        self.label_39 = QtWidgets.QLabel(self.groupBox_4)
        self.label_39.setPixmap(QtGui.QPixmap(":/icons/signal-none.png"))
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_39, 1, 1, 1, 1)

        self.label_40 = QtWidgets.QLabel(self.groupBox_4)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_40, 1, 2, 1, 1)

        self.gridLayout_9.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.horizontalLayout_2.addWidget(self.groupBox_4)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3.addLayout(self.verticalLayout)
        return self.monitor
        
    def configTab(self):
        self.config = QtWidgets.QWidget()
        self.config.setObjectName("config")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.config)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.groupBox_5 = QtWidgets.QGroupBox(self.config)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(41, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(41, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 1, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 2, 1, 1, 2)
        self.horizontalLayout_4.addLayout(self.gridLayout_2)
        self.horizontalLayout_11.addWidget(self.groupBox_5)
        self.groupBox_10 = QtWidgets.QGroupBox(self.config)
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.gridLayout_23 = QtWidgets.QGridLayout()
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.label_75 = QtWidgets.QLabel(self.groupBox_10)
        self.label_75.setAlignment(QtCore.Qt.AlignCenter)
        self.label_75.setObjectName("label_75")
        self.gridLayout_23.addWidget(self.label_75, 0, 0, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.gridLayout_23.addWidget(self.lineEdit_25, 0, 1, 1, 1)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_26.setMinimumSize(QtCore.QSize(41, 0))
        self.lineEdit_26.setMaximumSize(QtCore.QSize(41, 16777215))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout_23.addWidget(self.lineEdit_26, 0, 2, 1, 1)
        self.label_76 = QtWidgets.QLabel(self.groupBox_10)
        self.label_76.setAlignment(QtCore.Qt.AlignCenter)
        self.label_76.setObjectName("label_76")
        self.gridLayout_23.addWidget(self.label_76, 1, 0, 1, 1)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.gridLayout_23.addWidget(self.lineEdit_27, 1, 1, 1, 2)
        self.label_77 = QtWidgets.QLabel(self.groupBox_10)
        self.label_77.setAlignment(QtCore.Qt.AlignCenter)
        self.label_77.setObjectName("label_77")
        self.gridLayout_23.addWidget(self.label_77, 2, 0, 1, 1)
        self.lineEdit_28 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.gridLayout_23.addWidget(self.lineEdit_28, 2, 1, 1, 2)
        self.horizontalLayout_10.addLayout(self.gridLayout_23)
        self.horizontalLayout_11.addWidget(self.groupBox_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.groupBox_13 = QtWidgets.QGroupBox(self.config)
        self.groupBox_13.setObjectName("groupBox_13")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.gridLayout_24 = QtWidgets.QGridLayout()
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.label_78 = QtWidgets.QLabel(self.groupBox_13)
        self.label_78.setAlignment(QtCore.Qt.AlignCenter)
        self.label_78.setObjectName("label_78")
        self.gridLayout_24.addWidget(self.label_78, 0, 0, 1, 1)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.groupBox_13)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.gridLayout_24.addWidget(self.lineEdit_29, 0, 1, 1, 1)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.groupBox_13)
        self.lineEdit_30.setMinimumSize(QtCore.QSize(41, 0))
        self.lineEdit_30.setMaximumSize(QtCore.QSize(41, 16777215))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.gridLayout_24.addWidget(self.lineEdit_30, 0, 2, 1, 1)
        self.label_79 = QtWidgets.QLabel(self.groupBox_13)
        self.label_79.setAlignment(QtCore.Qt.AlignCenter)
        self.label_79.setObjectName("label_79")
        self.gridLayout_24.addWidget(self.label_79, 1, 0, 1, 1)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.groupBox_13)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.gridLayout_24.addWidget(self.lineEdit_31, 1, 1, 1, 2)
        self.label_80 = QtWidgets.QLabel(self.groupBox_13)
        self.label_80.setAlignment(QtCore.Qt.AlignCenter)
        self.label_80.setObjectName("label_80")
        self.gridLayout_24.addWidget(self.label_80, 2, 0, 1, 1)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.groupBox_13)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.gridLayout_24.addWidget(self.lineEdit_32, 2, 1, 1, 2)
        self.horizontalLayout_13.addLayout(self.gridLayout_24)
        self.horizontalLayout_12.addWidget(self.groupBox_13)
        self.groupBox_14 = QtWidgets.QGroupBox(self.config)
        self.groupBox_14.setObjectName("groupBox_14")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.groupBox_14)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.gridLayout_25 = QtWidgets.QGridLayout()
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.label_81 = QtWidgets.QLabel(self.groupBox_14)
        self.label_81.setAlignment(QtCore.Qt.AlignCenter)
        self.label_81.setObjectName("label_81")
        self.gridLayout_25.addWidget(self.label_81, 0, 0, 1, 1)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.groupBox_14)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.gridLayout_25.addWidget(self.lineEdit_33, 0, 1, 1, 1)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.groupBox_14)
        self.lineEdit_34.setMinimumSize(QtCore.QSize(41, 0))
        self.lineEdit_34.setMaximumSize(QtCore.QSize(41, 16777215))
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.gridLayout_25.addWidget(self.lineEdit_34, 0, 2, 1, 1)
        self.label_82 = QtWidgets.QLabel(self.groupBox_14)
        self.label_82.setAlignment(QtCore.Qt.AlignCenter)
        self.label_82.setObjectName("label_82")
        self.gridLayout_25.addWidget(self.label_82, 1, 0, 1, 1)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.groupBox_14)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.gridLayout_25.addWidget(self.lineEdit_35, 1, 1, 1, 2)
        self.label_83 = QtWidgets.QLabel(self.groupBox_14)
        self.label_83.setAlignment(QtCore.Qt.AlignCenter)
        self.label_83.setObjectName("label_83")
        self.gridLayout_25.addWidget(self.label_83, 2, 0, 1, 1)
        self.lineEdit_36 = QtWidgets.QLineEdit(self.groupBox_14)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.gridLayout_25.addWidget(self.lineEdit_36, 2, 1, 1, 2)
        self.horizontalLayout_14.addLayout(self.gridLayout_25)
        self.horizontalLayout_12.addWidget(self.groupBox_14)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        return self.config


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(575, 355)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 556, 343))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.addTab(self.monitorTab(), "")
        self.tabWidget.addTab(self.configTab(), "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "RouterBoard Monitor"))
        self.groupBox.setTitle(_translate("Form", "CAM 01"))
        self.label_2.setText(_translate("Form", "WLAN 0"))
        self.label_6.setText(_translate("Form", "100 %"))
        self.label_3.setText(_translate("Form", "WLAN 1"))
        self.label_7.setText(_translate("Form", "100 %"))
        self.groupBox_2.setTitle(_translate("Form", "CAM 02"))
        self.label_20.setText(_translate("Form", "WLAN 0"))
        self.label_22.setText(_translate("Form", "100 %"))
        self.label_24.setText(_translate("Form", "WLAN 1"))
        self.label_26.setText(_translate("Form", "100 %"))
        self.groupBox_3.setTitle(_translate("Form", "CAM 03"))
        self.label_27.setText(_translate("Form", "WLAN 0"))
        self.label_29.setText(_translate("Form", "100 %"))
        self.label_31.setText(_translate("Form", "WLAN 1"))
        self.label_33.setText(_translate("Form", "100 %"))
        self.groupBox_4.setTitle(_translate("Form", "CAM 04"))
        self.label_34.setText(_translate("Form", "WLAN 0"))
        self.label_36.setText(_translate("Form", "100 %"))
        self.label_38.setText(_translate("Form", "WLAN 1"))
        self.label_40.setText(_translate("Form", "100 %"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.monitor), _translate("Form", "Monitor"))
        self.groupBox_5.setTitle(_translate("Form", "CAM 01"))
        self.label_8.setText(_translate("Form", "IP"))
        self.label_10.setText(_translate("Form", "User"))
        self.label_11.setText(_translate("Form", "Pass"))
        self.groupBox_10.setTitle(_translate("Form", "CAM 02"))
        self.label_75.setText(_translate("Form", "IP"))
        self.label_76.setText(_translate("Form", "User"))
        self.label_77.setText(_translate("Form", "Pass"))
        self.groupBox_13.setTitle(_translate("Form", "CAM 03"))
        self.label_78.setText(_translate("Form", "IP"))
        self.label_79.setText(_translate("Form", "User"))
        self.label_80.setText(_translate("Form", "Pass"))
        self.groupBox_14.setTitle(_translate("Form", "CAM 04"))
        self.label_81.setText(_translate("Form", "IP"))
        self.label_82.setText(_translate("Form", "User"))
        self.label_83.setText(_translate("Form", "Pass"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.config), _translate("Form", "Config"))


