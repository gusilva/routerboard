from PyQt5 import QtCore, QtGui, QtWidgets
from app.main.config import config
from app.main.service.routerservice import RouterService
from app.main.view.routertab import RouterTab

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread

class WorkerThread(QObject):
    workersignal = pyqtSignal(int, int, list)

    def __init__(self):
        super().__init__()

    def setSettingsList(self, settingsListApi, index):
        self.idx = index
        self.settingsListApi = settingsListApi
        

    @pyqtSlot()
    def run(self):
        self.settingsListApi.getStock()
        code = 0
        quality = []
        if (len(self.settingsListApi.stock) > 0 and self.settingsListApi.stock != "Connection Failed"):
            code, quality = self.settingsListApi.getSignalQuality()
        self.workersignal.emit("finished", self.idx, code, quality)



class MainWidget(object):
    def setupUi(self, Form):
        self._translate = QtCore.QCoreApplication.translate
        Form.resize(QtCore.QSize(578, 401))
        Form.setWindowTitle(self._translate("Form", "RouterBoard Monitor"))

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

        self.tabConfig.tabobjects[6].clicked.connect(self.saveConfig)

        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.addWidget(self.tabWidget)

        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.setConfigs()

    def setConfigs(self):
        self.settingsList = []
        for idx in range(1, 7):
            default_settings = {"enabled": False, "ip": "", "port": "", "usr": "", "pwd": ""}
            self.tabConfig.tabobjects[idx-1].setLineEdit(
                ipEdit=config.value(f"gbox_{idx}", default_settings)["ip"],
                portEdit=config.value(f"gbox_{idx}", default_settings)["port"],
                usrEdit=config.value(f"gbox_{idx}", default_settings)["usr"],
                pwdEdit=config.value(f"gbox_{idx}", default_settings)["pwd"]
                )
            self.settingsList.append({
                'api': RouterService(
                    ip=config.value(f"gbox_{idx}", default_settings)["ip"],
                    port=config.value(f"gbox_{idx}", default_settings)["port"],
                    user=config.value(f"gbox_{idx}", default_settings)["usr"],
                    pwd=config.value(f"gbox_{idx}", default_settings)["pwd"])
                })

    def cron(self):
        try:
            _translate = QtCore.QCoreApplication.translate
            for idx in range(0, 6):
                camvalue = "--"
                gcamvalue = "--"
                if self.tabConfig.tabobjects[idx].camGBox.isChecked():
                    self.tabmonitor.tabobjects[idx].connectionRouterLbl.setPixmap(QtGui.QPixmap(":/icons/wifi_big.png"))
                    self.worker = WorkerThread()
                    self.worker.setSettingsList(self.settingsList[idx]["api"], idx)
                    self.thread = QThread()
                    self.thread.started.connect(self.worker.run)
                    self.thread.finished.connect(self.onFinished)
                    self.worker.workersignal.connect(self.onWorkerSignal)
                    self.worker.moveToThread(self.thread)
                    self.thread.start()
                # if self.tabConfig.tabobjects[idx].camGBox.isChecked():
                #     self.settingsList[idx]["api"].getStock()
                #     self.tabmonitor.tabobjects[idx].connectionRouterLbl.setPixmap(
                #         QtGui.QPixmap(":/icons/wifi_big.png")
                #     )
                #     if (
                #         len(self.settingsList[idx]["api"].stock) > 0
                #         and self.settingsList[idx]["api"].stock != "Connection Failed"
                #     ):
                #         code, quality = self.settingsList[idx]["api"].getSignalQuality()
                #         if code == 200:
                #             camvalue = quality[0]
                #             gcamvalue = quality[1]
                #             self.tabmonitor.tabobjects[idx].connectionRouterLbl.setPixmap(
                #                 QtGui.QPixmap(":/icons/wifi_big.png")
                #             )
                #             self.tabmonitor.tabobjects[idx].signalCamLbl.setPixmap(
                #                 QtGui.QPixmap(self.getSignalIcon(camvalue))
                #             )
                #             self.tabmonitor.tabobjects[idx].signalValueCamLbl.setText(
                #                 _translate("tabWidget", "{} %".format(camvalue))
                #             )
                #             self.tabmonitor.tabobjects[idx].signalGcamLbl.setPixmap(
                #                 QtGui.QPixmap(self.getSignalIcon(gcamvalue))
                #             )
                #             self.tabmonitor.tabobjects[idx].signalValueGcamLbl.setText(
                #                 _translate("tabWidget", "{} %".format(gcamvalue))
                #             )
                #             continue
                # self.tabmonitor.tabobjects[idx].connectionRouterLbl.setPixmap(
                #     QtGui.QPixmap(":/icons/wifi_big_disabled.png")
                # )
                # self.tabmonitor.tabobjects[idx].signalCamLbl.setPixmap(
                #     QtGui.QPixmap(self.getSignalIcon(camvalue))
                # )
                # self.tabmonitor.tabobjects[idx].signalValueCamLbl.setText(
                #     _translate("tabWidget", "{} %".format(camvalue))
                # )
                # self.tabmonitor.tabobjects[idx].signalGcamLbl.setPixmap(
                #     QtGui.QPixmap(self.getSignalIcon(gcamvalue))
                # )
                # self.tabmonitor.tabobjects[idx].signalValueGcamLbl.setText(
                #     _translate("tabWidget", "{} %".format(gcamvalue))
                # )
        finally:
            pass
            # QtCore.QTimer.singleShot(5000, self.cron)


    def onFinished(self):
        print("thread finished")
        QtCore.QTimer.singleShot(5000, self.cron)
        self.threadsignal.emit("finished")


    def onWorkerSignal(self, idx, code, quality):
        camvalue = "--"
        gcamvalue = "--"
        if code == 200:
            camvalue = quality[0]
            gcamvalue = quality[1]
            self.tabmonitor.tabobjects[idx].connectionRouterLbl.setPixmap(QtGui.QPixmap(":/icons/wifi_big.png"))
            self.tabmonitor.tabobjects[idx].signalCamLbl.setPixmap(QtGui.QPixmap(self.getSignalIcon(camvalue)))
            self.tabmonitor.tabobjects[idx].signalValueCamLbl.setText(_translate("tabWidget", "{} %".format(camvalue)))
            self.tabmonitor.tabobjects[idx].signalGcamLbl.setPixmap(QtGui.QPixmap(self.getSignalIcon(gcamvalue)))
            self.tabmonitor.tabobjects[idx].signalValueGcamLbl.setText(_translate("tabWidget", "{} %".format(gcamvalue)))
        else:
            self.tabmonitor.tabobjects[idx].connectionRouterLbl.setPixmap(QtGui.QPixmap(":/icons/wifi_big_disabled.png"))
            self.tabmonitor.tabobjects[idx].signalCamLbl.setPixmap(QtGui.QPixmap(self.getSignalIcon(camvalue)))
            self.tabmonitor.tabobjects[idx].signalValueCamLbl.setText(_translate("tabWidget", "{} %".format(camvalue)))
            self.tabmonitor.tabobjects[idx].signalGcamLbl.setPixmap(QtGui.QPixmap(self.getSignalIcon(gcamvalue)))
            self.tabmonitor.tabobjects[idx].signalValueGcamLbl.setText(_translate("tabWidget", "{} %".format(gcamvalue)))       
        self.thread.terminate()


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
        for idx in range(0, 6):
            settings = {
                "enabled": False,
                "ip": self.tabConfig.tabobjects[idx].ipEdit.text(),
                "port": self.tabConfig.tabobjects[idx].portEdit.text(),
                "usr": self.tabConfig.tabobjects[idx].usrEdit.text(),
                "pwd": self.tabConfig.tabobjects[idx].pwdEdit.text(),
            }
            if self.tabConfig.tabobjects[idx].camGBox.isChecked():
                self.tabmonitor.tabobjects[idx].camGBox.setEnabled(True)
                settings["enabled"] = True
                config.setValue(
                    self.tabConfig.tabobjects[idx].camGBox.objectName(), settings
                )
                self.settingsList[idx]["api"] = RouterService(
                    ip=settings["ip"],
                    port=settings["port"],
                    user=settings["usr"],
                    pwd=settings["pwd"],
                )
                self.settingsList[idx]["api"].getStock()
                continue
            self.tabmonitor.tabobjects[idx].camGBox.setEnabled(False)
            config.setValue(self.tabConfig.tabobjects[idx].camGBox.objectName(), settings)

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
