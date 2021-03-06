from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
from app.main.config import config
from app.main.service.routerservice import RouterService
from app.main.view.routertab import RouterTab

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
        self.workersignal.emit(self.idx, code, quality)



class MainWidget(object):
    def setupUi(self, Form):
        print("Monitoring has started.")
        self.worker = [None]*6
        self.thread = [None]*6
        self._translate = QtCore.QCoreApplication.translate
        Form.resize(QtCore.QSize(578, 401))
        Form.setWindowTitle(self._translate("Form", "RouterBoard Monitor"))

        app_ico = QtGui.QIcon()
        app_ico.addFile(':/icons/wifi16x16.ico', QtCore.QSize(16,16))
        app_ico.addFile(':/icons/wifi24x24.ico', QtCore.QSize(24,24))
        app_ico.addFile(':/icons/wifi32x32.ico', QtCore.QSize(32,32))
        app_ico.addFile(':/icons/wifi64x64.ico', QtCore.QSize(64,64))
        app_ico.addFile(':/icons/wifi128x128.ico', QtCore.QSize(128,128))
        app_ico.addFile(':/icons/wifi256x256.ico', QtCore.QSize(256,256))
        Form.setWindowIcon(app_ico)

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
                if self.thread[idx] is not None:
                    self.thread[idx].terminate()
                if self.tabConfig.tabobjects[idx].camGBox.isChecked():
                    self.worker[idx] = WorkerThread()
                    self.thread[idx] = QThread()
                    self.worker[idx].setSettingsList(self.settingsList[idx]["api"], idx)
                    self.thread[idx].started.connect(self.worker[idx].run)
                    self.thread[idx].finished.connect(self.onFinished)
                    self.worker[idx].workersignal.connect(self.onWorkerSignal)
                    self.worker[idx].moveToThread(self.thread[idx])
                    self.thread[idx].start()
        finally:
            QtCore.QTimer.singleShot(5000, self.cron)


    def onFinished(self):
        print("thread finished")
        print(self.thread)

    def onWorkerSignal(self, idx, code, quality):
        camvalue = "--"
        gcamvalue = "--"
        if code == 200:
            camvalue = quality[0]
            gcamvalue = quality[1]
            self.tabmonitor.tabobjects[idx].connectionRouterLbl.setPixmap(QtGui.QPixmap(":/icons/wifi_big.png"))
            self.tabmonitor.tabobjects[idx].signalCamLbl.setPixmap(QtGui.QPixmap(self.getSignalIcon(camvalue)))
            self.tabmonitor.tabobjects[idx].signalValueCamLbl.setText(self._translate("tabWidget", "{} %".format(camvalue)))
            self.tabmonitor.tabobjects[idx].signalGcamLbl.setPixmap(QtGui.QPixmap(self.getSignalIcon(gcamvalue)))
            self.tabmonitor.tabobjects[idx].signalValueGcamLbl.setText(self._translate("tabWidget", "{} %".format(gcamvalue)))
        else:
            self.tabmonitor.tabobjects[idx].connectionRouterLbl.setPixmap(QtGui.QPixmap(":/icons/wifi_big_disabled.png"))
            self.tabmonitor.tabobjects[idx].signalCamLbl.setPixmap(QtGui.QPixmap(self.getSignalIcon(camvalue)))
            self.tabmonitor.tabobjects[idx].signalValueCamLbl.setText(self._translate("tabWidget", "{} %".format(camvalue)))
            self.tabmonitor.tabobjects[idx].signalGcamLbl.setPixmap(QtGui.QPixmap(self.getSignalIcon(gcamvalue)))
            self.tabmonitor.tabobjects[idx].signalValueGcamLbl.setText(self._translate("tabWidget", "{} %".format(gcamvalue)))
        if self.thread[idx].isRunning():
            print("Thread "+str(idx)+" has been finished: "+self.tabmonitor.tabobjects[idx].objectname)  
            self.thread[idx].terminate()


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
