from PyQt5 import QtWidgets, QtCore, QtGui
from app.main.view.routergbox import RouterGBox

class RouterTab(object):    

    def __init__(self, obj_name="Tab", parent=None):
        self._translate = QtCore.QCoreApplication.translate
        self.parent = parent
        self.objectname = obj_name
        self.tabobjects = []
        self.tab = QtWidgets.QWidget()

    def monitorLayout(self):
        gLayout = QtWidgets.QGridLayout(self.tab)
        gLayout.addWidget(self.tabobjects[0].camGBox, 0, 0, 1, 1)
        gLayout.addWidget(self.tabobjects[1].camGBox, 0, 1, 1, 1)
        gLayout.addWidget(self.tabobjects[2].camGBox, 1, 0, 1, 1)
        gLayout.addWidget(self.tabobjects[3].camGBox, 1, 1, 1, 1)

    def configLayout(self):
        gLayout = QtWidgets.QGridLayout(self.tab)
        gLayout.addWidget(self.tabobjects[0].camGBox, 0, 0, 1, 1)
        gLayout.addWidget(self.tabobjects[1].camGBox, 0, 1, 1, 1)
        gLayout.addWidget(self.tabobjects[2].camGBox, 1, 0, 1, 1)
        gLayout.addWidget(self.tabobjects[3].camGBox, 1, 1, 1, 1)
        gLayout.addWidget(self.tabobjects[4], 2, 0, 2, 0, QtCore.Qt.AlignCenter)

    def monitor(self):
        for i in range(1, 5):
            gbox = RouterGBox("gbox_{}".format(i), self.tab)
            gbox.monitor()
            gbox.camGBox.setEnabled(False)
            self.tabobjects.append(gbox)

        self.monitorLayout()
        self.retranslateMonitorTab()

    def config(self):
        for i in range(1, 5):
            cam = "gbox_{}".format(i)
            gbox = RouterGBox(cam, self.tab)
            gbox.config()
            self.tabobjects.append(gbox)

        self.tabobjects.append(QtWidgets.QPushButton())
        self.configLayout()
        self.retranslateConfigTab()

    def retranslateMonitorTab(self):
        self.tabobjects[0].camGBox.setTitle(self._translate("Form", "CAM 01"))
        self.tabobjects[0].signalValueCamLbl.setText(self._translate("Form", "100 %"))
        self.tabobjects[0].gcamLbl.setText(self._translate("Form", "GCAM"))
        self.tabobjects[0].signalValueGcamLbl.setText(self._translate("Form", "100 %"))
        self.tabobjects[1].camGBox.setTitle(self._translate("Form", "CAM 02"))
        self.tabobjects[1].signalValueCamLbl.setText(self._translate("Form", "100 %"))
        self.tabobjects[1].gcamLbl.setText(self._translate("Form", "GCAM"))
        self.tabobjects[1].signalValueGcamLbl.setText(self._translate("Form", "100 %"))
        self.tabobjects[2].camGBox.setTitle(self._translate("Form", "CAM 03"))
        self.tabobjects[2].signalValueCamLbl.setText(self._translate("Form", "100 %"))
        self.tabobjects[2].gcamLbl.setText(self._translate("Form", "GCAM"))
        self.tabobjects[2].signalValueGcamLbl.setText(self._translate("Form", "100 %"))
        self.tabobjects[3].camGBox.setTitle(self._translate("Form", "CAM 04"))
        self.tabobjects[3].signalValueCamLbl.setText(self._translate("Form", "100 %"))
        self.tabobjects[3].gcamLbl.setText(self._translate("Form", "GCAM"))
        self.tabobjects[3].signalValueGcamLbl.setText(self._translate("Form", "100 %"))

    def retranslateConfigTab(self):
        self.tabobjects[0].camGBox.setTitle(self._translate("Form", "CAM 01"))
        self.tabobjects[0].ipLbl.setText(self._translate("Form", "IP"))
        self.tabobjects[0].usrLbl.setText(self._translate("Form", "User"))
        self.tabobjects[0].pwdLbl.setText(self._translate("Form", "Pass"))
        self.tabobjects[1].camGBox.setTitle(self._translate("Form", "CAM 02"))
        self.tabobjects[1].ipLbl.setText(self._translate("Form", "IP"))
        self.tabobjects[1].usrLbl.setText(self._translate("Form", "User"))
        self.tabobjects[1].pwdLbl.setText(self._translate("Form", "Pass"))
        self.tabobjects[2].camGBox.setTitle(self._translate("Form", "CAM 03"))
        self.tabobjects[2].ipLbl.setText(self._translate("Form", "IP"))
        self.tabobjects[2].usrLbl.setText(self._translate("Form", "User"))
        self.tabobjects[2].pwdLbl.setText(self._translate("Form", "Pass"))
        self.tabobjects[3].camGBox.setTitle(self._translate("Form", "CAM 04"))
        self.tabobjects[3].ipLbl.setText(self._translate("Form", "IP"))
        self.tabobjects[3].usrLbl.setText(self._translate("Form", "User"))
        self.tabobjects[3].pwdLbl.setText(self._translate("Form", "Pass"))
        self.tabobjects[4].setText(self._translate("Form", "Save"))

