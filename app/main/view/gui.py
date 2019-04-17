from PyQt5 import QtCore, QtGui, QtWidgets
from app.main.config import config
from app.main.service.routerservice import RouterService
# from app.main.view.routergbox import RouterGBox
from app.main.view.routertab import RouterTab


class MainWidget(object):
    def setupUi(self, Form):
        self._translate = QtCore.QCoreApplication.translate
        Form.setMinimumSize(QtCore.QSize(578, 401))
        Form.setMaximumSize(QtCore.QSize(578, 401))
        Form.setWindowTitle(self._translate("Form", "RouterBoard Monitor"))

        self.setDefaultSettings()

        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setCurrentIndex(0)

        self.tabmonitor = RouterTab("monitor")
        self.tabConfig = RouterTab("config")
        self.tabmonitor.monitor()
        self.tabConfig.config()

        self.tabWidget.addTab(self.tabmonitor.tab, "")
        self.tabWidget.addTab(self.tabConfig.tab, "")

        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabmonitor.tab), self._translate("Form", "Monitor")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabConfig.tab), self._translate("Form", "Config")
        )

        self.tabConfig.tabobjects[4].clicked.connect(self.saveConfig)

        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.addWidget(self.tabWidget)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def setDefaultSettings(self):
        default_settings = {"enabled": False, "ip": "", "port": "", "usr": "", "pwd": ""}

        self.configs = {
            "gbox_1": config.value("gbox_1", default_settings),
            "gbox_2": config.value("gbox_2", default_settings),
            "gbox_3": config.value("gbox_3", default_settings),
            "gbox_4": config.value("gbox_4", default_settings)
        }

    def setWidgetConfigs(self):
        self.settingsList = [{}, {}, {}, {}]
        self.settingsList[0]["api"] = RouterService(
            ip=self.configs["gbox_1"]["ip"],
            port=self.configs["gbox_1"]["port"],
            user=self.configs["gbox_1"]["usr"],
            pwd=self.configs["gbox_1"]["pwd"],
        )
        self.settingsList[1]["api"] = RouterService(
            ip=self.configs["gbox_2"]["ip"],
            port=self.configs["gbox_2"]["port"],
            user=self.configs["gbox_2"]["usr"],
            pwd=self.configs["gbox_2"]["pwd"],
        )
        self.settingsList[2]["api"] = RouterService(
            ip=self.configs["gbox_3"]["ip"],
            port=self.configs["gbox_3"]["port"],
            user=self.configs["gbox_3"]["usr"],
            pwd=self.configs["gbox_3"]["pwd"],
        )
        self.settingsList[3]["api"] = RouterService(
            ip=self.configs["gbox_4"]["ip"],
            port=self.configs["gbox_4"]["port"],
            user=self.configs["gbox_4"]["usr"],
            pwd=self.configs["gbox_4"]["pwd"],
        )

    def signal(self):
        from random import randint

        try:
            _translate = QtCore.QCoreApplication.translate
            for idx in range(0, 4):
                camvalue = "--"
                gcamvalue = "--"
                if self.widgetConfigList[idx].camGBox.isChecked():
                    self.settingsList[idx]["api"].getStock()
                    self.widgetList[idx].connectionRouterLbl.setPixmap(
                        QtGui.QPixmap(":/icons/wifi_big.png")
                    )
                    if (
                        len(self.settingsList[idx]["api"].stock) > 0
                        and self.settingsList[idx]["api"].stock != "Connection Failed"
                    ):
                        code, quality = self.settingsList[idx]["api"].getSignalQuality()
                        if code == 200:
                            camvalue = quality[0]
                            gcamvalue = quality[1]
                            self.widgetList[idx].connectionRouterLbl.setPixmap(
                                QtGui.QPixmap(":/icons/wifi_big.png")
                            )
                            self.widgetList[idx].signalCamLbl.setPixmap(
                                QtGui.QPixmap(self.getSignalIcon(camvalue))
                            )
                            self.widgetList[idx].signalValueCamLbl.setText(
                                _translate("tabWidget", "{} %".format(camvalue))
                            )
                            self.widgetList[idx].signalGcamLbl.setPixmap(
                                QtGui.QPixmap(self.getSignalIcon(gcamvalue))
                            )
                            self.widgetList[idx].signalValueGcamLbl.setText(
                                _translate("tabWidget", "{} %".format(gcamvalue))
                            )
                            continue
                self.widgetList[idx].connectionRouterLbl.setPixmap(
                    QtGui.QPixmap(":/icons/wifi_big_disabled.png")
                )
                self.widgetList[idx].signalCamLbl.setPixmap(
                    QtGui.QPixmap(self.getSignalIcon(camvalue))
                )
                self.widgetList[idx].signalValueCamLbl.setText(
                    _translate("tabWidget", "{} %".format(camvalue))
                )
                self.widgetList[idx].signalGcamLbl.setPixmap(
                    QtGui.QPixmap(self.getSignalIcon(gcamvalue))
                )
                self.widgetList[idx].signalValueGcamLbl.setText(
                    _translate("tabWidget", "{} %".format(gcamvalue))
                )
        finally:
            QtCore.QTimer.singleShot(5000, self.signal)

    def getSignalIcon(self, value):
        if isinstance(value, str):
            return ":/icons/signal-none.png"
        if value >= 75:
            return ":/icons/signal-75-100.png"
        if value >= 50 and value < 75:
            return ":/icons/signal-50-75.png"
        if value >= 25 and value < 50:
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
                self.settingsList[idx]["api"] = RouterService(
                    ip=settings["ip"],
                    port=settings["port"],
                    user=settings["usr"],
                    pwd=settings["pwd"],
                )
                self.settingsList[idx]["api"].getStock()
                continue
            self.widgetList[idx].camGBox.setEnabled(False)
            config.setValue(self.widgetConfigList[idx].camGBox.objectName(), settings)

    def saveConfig(self):
        self.setGBoxData()
        self.tabWidget.setCurrentIndex(0)
        config.sync()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = MainWidget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
