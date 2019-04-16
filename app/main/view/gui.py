from PyQt5 import QtCore, QtGui, QtWidgets
from app.main.config import config
from app.main.service.routerservice import RouterService
from app.main.view.routergbox import RouterGBox


class MainWidget(object):
    def setupUi(self, Form):
        self._translate = QtCore.QCoreApplication.translate
        Form.setMinimumSize(QtCore.QSize(578, 401))
        Form.setMaximumSize(QtCore.QSize(578, 401))
        Form.setWindowTitle(self._translate("Form", "RouterBoard Monitor"))

        self.configs = {
            "cam_1": config.value(
                "cam_1", {"enabled": False, "ip": "", "port": "", "usr": "", "pwd": ""}
            ),
            "cam_2": config.value(
                "cam_2", {"enabled": False, "ip": "", "port": "", "usr": "", "pwd": ""}
            ),
            "cam_3": config.value(
                "cam_3", {"enabled": False, "ip": "", "port": "", "usr": "", "pwd": ""}
            ),
            "cam_4": config.value(
                "cam_4", {"enabled": False, "ip": "", "port": "", "usr": "", "pwd": ""}
            ),
        }
 

        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setCurrentIndex(0)

        self.tabMonitor()
        self.retranslateMonitorTab()

        self.tabConfig()
        self.retranslateConfigTab()

        self.setWidgetConfigs()

        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.addWidget(self.tabWidget)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def setWidgetConfigs(self):
        self.settingsList = [{},{},{},{}]
        self.settingsList[0]["api"] = RouterService(ip=self.configs["cam_1"]["ip"], port=self.configs["cam_1"]["port"], user=self.configs["cam_1"]["usr"], pwd=self.configs["cam_1"]["pwd"])
        self.settingsList[1]["api"] = RouterService(ip=self.configs["cam_2"]["ip"], port=self.configs["cam_2"]["port"], user=self.configs["cam_2"]["usr"], pwd=self.configs["cam_2"]["pwd"])
        self.settingsList[2]["api"] = RouterService(ip=self.configs["cam_3"]["ip"], port=self.configs["cam_3"]["port"], user=self.configs["cam_3"]["usr"], pwd=self.configs["cam_3"]["pwd"])
        self.settingsList[3]["api"] = RouterService(ip=self.configs["cam_4"]["ip"], port=self.configs["cam_4"]["port"], user=self.configs["cam_4"]["usr"], pwd=self.configs["cam_4"]["pwd"])

    def signal(self):
        from random import randint
        try:
            _translate = QtCore.QCoreApplication.translate
            for idx in range(0, 4):
                camvalue = "--"
                gcamvalue = "--"
                if self.widgetConfigList[idx].camGBox.isChecked():
                    self.widgetList[idx].connectionRouterLbl.setPixmap(QtGui.QPixmap(":/icons/wifi_big.png"))
                    if len(self.settingsList[idx]["api"].stock) > 0 and self.settingsList[idx]["api"].stock != "Connection Failed":
                        code, quality = self.settingsList[idx]["api"].getSignalQuality()
                        if code == 200:
                            camvalue = quality[0]
                            gcamvalue = quality[1]
                            self.widgetList[idx].connectionRouterLbl.setPixmap(QtGui.QPixmap(":/icons/wifi_big.png"))
                            self.widgetList[idx].signalCamLbl.setPixmap(QtGui.QPixmap(self.getSignalIcon(camvalue)))
                            self.widgetList[idx].signalValueCamLbl.setText(_translate("tabWidget", "{} %".format(camvalue)))
                            self.widgetList[idx].signalGcamLbl.setPixmap(QtGui.QPixmap(self.getSignalIcon(gcamvalue)))
                            self.widgetList[idx].signalValueGcamLbl.setText(_translate("tabWidget", "{} %".format(gcamvalue)))
                            continue
                self.widgetList[idx].connectionRouterLbl.setPixmap(QtGui.QPixmap(":/icons/wifi_big_disabled.png"))
                self.widgetList[idx].signalCamLbl.setPixmap(QtGui.QPixmap(self.getSignalIcon(camvalue)))
                self.widgetList[idx].signalValueCamLbl.setText(_translate("tabWidget", "{} %".format(camvalue)))
                self.widgetList[idx].signalGcamLbl.setPixmap(QtGui.QPixmap(self.getSignalIcon(gcamvalue)))
                self.widgetList[idx].signalValueGcamLbl.setText(_translate("tabWidget", "{} %".format(gcamvalue)))
        finally:
            QtCore.QTimer.singleShot(5000, self.signal)

    def getSignalIcon(self, value):
        if isinstance(value, str):
            return ":/icons/signal-none.png"
        if value >= 75:
            return ":/icons/signal-75-100.png"
        if value >= 50 and value < 75:
            return ":/icons/signal-50-75.png"
        if value >=25 and value < 50:
            return ":/icons/signal-25-50.png"
        if value > 0 and value < 25:
            return ":/icons/signal-0-25.png"
        if value == 0:
            return ":/icons/signal-0.png"
        else:
            return ":/icons/signal-none.png" 

    def setGBoxData(self):
        for idx in range(0, 4):
            settings = {
                "enabled": False,
                "ip": self.widgetConfigList[idx].ipEdit.text(),
                "port": self.widgetConfigList[idx].portEdit.text(),
                "usr": self.widgetConfigList[idx].usrEdit.text(),
                "pwd": self.widgetConfigList[idx].pwdEdit.text(),
            }
            if self.widgetConfigList[idx].camGBox.isChecked():
                self.widgetList[idx].camGBox.setEnabled(True)
                settings["enabled"] = True
                config.setValue(
                    self.widgetConfigList[idx].camGBox.objectName(), settings
                )
                self.settingsList[idx]["api"] = RouterService(ip=settings["ip"], port=settings["port"], user=settings["usr"], pwd=settings["pwd"])
                self.settingsList[idx]["api"].getStock()
                continue
            self.widgetList[idx].camGBox.setEnabled(False)
            config.setValue(
                self.widgetConfigList[idx].camGBox.objectName(), settings
            )

    def saveConfig(self):
        self.setGBoxData()
        self.tabWidget.setCurrentIndex(0)
        config.sync()



    def tabMonitor(self):
        self.monitorTab = QtWidgets.QWidget()
        self.widgetList = []

        for i in range(1, 5):
            gbox = RouterGBox('cam_{}'.format(i), self.monitorTab)
            gbox.monitor()
            gbox.camGBox.setEnabled(False)
            self.widgetList.append(gbox)

        gLayout = QtWidgets.QGridLayout(self.monitorTab)
        gLayout.addWidget(self.widgetList[0].camGBox, 0, 0, 1, 1)
        gLayout.addWidget(self.widgetList[1].camGBox, 0, 1, 1, 1)
        gLayout.addWidget(self.widgetList[2].camGBox, 1, 0, 1, 1)
        gLayout.addWidget(self.widgetList[3].camGBox, 1, 1, 1, 1)

        self.tabWidget.addTab(self.monitorTab, "")

    def tabConfig(self):
        self.configTab = QtWidgets.QWidget()
        self.widgetConfigList = []

        for i in range(1, 5):
            cam = 'cam_{}'.format(i)
            configs = {
                'ipEdit': self.configs[cam]["ip"],
                'portEdit': self.configs[cam]["port"],
                'usrEdit': self.configs[cam]["usr"],
                'pwdEdit': self.configs[cam]["pwd"]
            }
            gbox = RouterGBox(cam, self.configTab)
            gbox.config()
            gbox.setLineEdit(configs['ipEdit'], configs['portEdit'], configs['usrEdit'], configs['pwdEdit'])
            self.widgetConfigList.append(gbox)

        self.saveBtn = QtWidgets.QPushButton()

        gLayout = QtWidgets.QGridLayout(self.configTab)
        gLayout.addWidget(self.widgetConfigList[0].camGBox, 0, 0, 1, 1)
        gLayout.addWidget(self.widgetConfigList[1].camGBox, 0, 1, 1, 1)
        gLayout.addWidget(self.widgetConfigList[2].camGBox, 1, 0, 1, 1)
        gLayout.addWidget(self.widgetConfigList[3].camGBox, 1, 1, 1, 1)
        gLayout.addWidget(self.saveBtn, 2, 0, 2, 0, QtCore.Qt.AlignCenter)

        self.saveBtn.clicked.connect(self.saveConfig)
        self.tabWidget.addTab(self.configTab, "")

    def retranslateMonitorTab(self):
        self.widgetList[0].camGBox.setTitle(self._translate("Form", "CAM 01"))
        self.widgetList[0].signalValueCamLbl.setText(
            self._translate("Form", "100 %")
        )
        self.widgetList[0].gcamLbl.setText(self._translate("Form", "GCAM"))
        self.widgetList[0].signalValueGcamLbl.setText(
            self._translate("Form", "100 %")
        )
        self.widgetList[1].camGBox.setTitle(self._translate("Form", "CAM 02"))
        self.widgetList[1].signalValueCamLbl.setText(
            self._translate("Form", "100 %")
        )
        self.widgetList[1].gcamLbl.setText(self._translate("Form", "GCAM"))
        self.widgetList[1].signalValueGcamLbl.setText(
            self._translate("Form", "100 %")
        )
        self.widgetList[2].camGBox.setTitle(self._translate("Form", "CAM 03"))
        self.widgetList[2].signalValueCamLbl.setText(
            self._translate("Form", "100 %")
        )
        self.widgetList[2].gcamLbl.setText(self._translate("Form", "GCAM"))
        self.widgetList[2].signalValueGcamLbl.setText(
            self._translate("Form", "100 %")
        )
        self.widgetList[3].camGBox.setTitle(self._translate("Form", "CAM 04"))
        self.widgetList[3].signalValueCamLbl.setText(
            self._translate("Form", "100 %")
        )
        self.widgetList[3].gcamLbl.setText(self._translate("Form", "GCAM"))
        self.widgetList[3].signalValueGcamLbl.setText(
            self._translate("Form", "100 %")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.monitorTab), self._translate("Form", "Monitor")
        )

    def retranslateConfigTab(self):
        self.widgetConfigList[0].camGBox.setTitle(self._translate("Form", "CAM 01"))
        self.widgetConfigList[0].ipLbl.setText(self._translate("Form", "IP"))
        self.widgetConfigList[0].usrLbl.setText(self._translate("Form", "User"))
        self.widgetConfigList[0].pwdLbl.setText(self._translate("Form", "Pass"))
        self.widgetConfigList[1].camGBox.setTitle(self._translate("Form", "CAM 02"))
        self.widgetConfigList[1].ipLbl.setText(self._translate("Form", "IP"))
        self.widgetConfigList[1].usrLbl.setText(self._translate("Form", "User"))
        self.widgetConfigList[1].pwdLbl.setText(self._translate("Form", "Pass"))
        self.widgetConfigList[2].camGBox.setTitle(self._translate("Form", "CAM 03"))
        self.widgetConfigList[2].ipLbl.setText(self._translate("Form", "IP"))
        self.widgetConfigList[2].usrLbl.setText(self._translate("Form", "User"))
        self.widgetConfigList[2].pwdLbl.setText(self._translate("Form", "Pass"))
        self.widgetConfigList[3].camGBox.setTitle(self._translate("Form", "CAM 04"))
        self.widgetConfigList[3].ipLbl.setText(self._translate("Form", "IP"))
        self.widgetConfigList[3].usrLbl.setText(self._translate("Form", "User"))
        self.widgetConfigList[3].pwdLbl.setText(self._translate("Form", "Pass"))

        self.saveBtn.setText(self._translate("Form", "Save"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.configTab), self._translate("Form", "Config")
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = MainWidget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
