from PyQt5 import QtWidgets, QtCore, QtGui


class RouterGBox(object):

    parent = None
    objectname = None

    def __init__(self, obj_name="Group Box", parent=None):
        self._translate = QtCore.QCoreApplication.translate
        self.parent = parent
        self.objectname = obj_name

    def setMonitorLayout(self):
        gLayout = QtWidgets.QGridLayout(self.camGBox)
        gLayout.addWidget(self.camLbl, 0, 0, 1, 1)
        gLayout.addWidget(self.signalCamLbl, 0, 1, 1, 1)
        gLayout.addWidget(self.signalValueCamLbl, 0, 2, 1, 1)
        gLayout.addWidget(self.connectionRouterLbl, 0, 3, 2, 1)
        gLayout.addWidget(self.gcamLbl, 1, 0, 1, 1)
        gLayout.addWidget(self.signalGcamLbl, 1, 1, 1, 1)
        gLayout.addWidget(self.signalValueGcamLbl, 1, 2, 1, 1)

    def setConfigLayout(self):
        gLayout = QtWidgets.QGridLayout(self.camGBox)
        gLayout.addWidget(self.ipLbl, 0, 0, 1, 1)
        gLayout.addWidget(self.ipEdit, 0, 1, 1, 1)
        gLayout.addWidget(self.portEdit, 0, 2, 1, 1)
        gLayout.addWidget(self.usrLbl, 1, 0, 1, 1)
        gLayout.addWidget(self.usrEdit, 1, 1, 1, 2)
        gLayout.addWidget(self.pwdLbl, 2, 0, 1, 1)
        gLayout.addWidget(self.pwdEdit, 2, 1, 1, 2)

    def setMonitorFonts(self):
        self.fontSglValue = QtGui.QFont()
        self.fontGcam = QtGui.QFont()
        self.fontSglValue.setPointSize(13)
        self.fontSglValue.setBold(False)
        self.fontGcam.setFamily("Globoface")
        self.fontGcam.setPointSize(16)
        self.fontGcam.setBold(True)

    def setConfigFonts(self):
        self.lblFont = QtGui.QFont()
        self.editFont = QtGui.QFont()
        self.lblFont.setFamily("Globoface CGJ")
        self.lblFont.setBold(True)
        self.lblFont.setPointSize(13)
        self.lblFont.setWeight(50)
        self.editFont.setFamily("Globoface CGJ  light")
        self.editFont.setPointSize(8)
        self.editFont.setWeight(50)

    def setCamGBox(self):
        self.fontGBox = QtGui.QFont()
        self.fontGBox.setFamily("Globoface CGJ")
        self.fontGBox.setPointSize(25)
        self.fontGBox.setBold(True)
        self.fontGBox.setWeight(75)

        self.camGBox = QtWidgets.QGroupBox(self.parent)
        self.camGBox.setFont(self.fontGBox)
        self.camGBox.setAlignment(QtCore.Qt.AlignCenter)
        self.camGBox.setObjectName(self.objectname)

    def setMonitorLables(self):
        self.camLbl = QtWidgets.QLabel(self.camGBox)
        self.camLbl.setPixmap(QtGui.QPixmap(":/icons/camera.png"))
        self.camLbl.setAlignment(QtCore.Qt.AlignCenter)

        self.signalCamLbl = QtWidgets.QLabel(self.camGBox)
        self.signalCamLbl.setPixmap(QtGui.QPixmap(":/icons/signal-none.png"))
        self.signalCamLbl.setAlignment(QtCore.Qt.AlignCenter)

        self.signalValueCamLbl = QtWidgets.QLabel(self.camGBox)
        self.signalValueCamLbl.setFont(self.fontSglValue)
        self.signalValueCamLbl.setAlignment(QtCore.Qt.AlignCenter)

        self.connectionRouterLbl = QtWidgets.QLabel(self.camGBox)
        self.connectionRouterLbl.setPixmap(
            QtGui.QPixmap(":/icons/wifi_big_disabled.png")
        )
        self.connectionRouterLbl.setAlignment(QtCore.Qt.AlignCenter)

        self.gcamLbl = QtWidgets.QLabel(self.camGBox)
        self.gcamLbl.setFont(self.fontGcam)
        self.gcamLbl.setAlignment(QtCore.Qt.AlignCenter)

        self.signalGcamLbl = QtWidgets.QLabel(self.camGBox)
        self.signalGcamLbl.setPixmap(QtGui.QPixmap(":/icons/signal-none.png"))
        self.signalGcamLbl.setAlignment(QtCore.Qt.AlignCenter)

        self.signalValueGcamLbl = QtWidgets.QLabel(self.camGBox)
        self.signalValueGcamLbl.setFont(self.fontSglValue)
        self.signalValueGcamLbl.setAlignment(QtCore.Qt.AlignCenter)

    def setConfigLables(self):
        self.ipLbl = QtWidgets.QLabel(self.camGBox)
        self.ipLbl.setFont(self.lblFont)
        self.ipLbl.setAlignment(QtCore.Qt.AlignCenter)

        self.usrLbl = QtWidgets.QLabel(self.camGBox)
        self.usrLbl.setFont(self.lblFont)
        self.usrLbl.setAlignment(QtCore.Qt.AlignCenter)

        self.pwdLbl = QtWidgets.QLabel(self.camGBox)
        self.pwdLbl.setFont(self.lblFont)
        self.pwdLbl.setAlignment(QtCore.Qt.AlignCenter)

    def setConfigLEdit(self):
        self.ipEdit = QtWidgets.QLineEdit(self.camGBox)
        self.ipEdit.setFont(self.editFont)

        self.portEdit = QtWidgets.QLineEdit(self.camGBox)
        self.portEdit.setMinimumSize(QtCore.QSize(41, 0))
        self.portEdit.setMaximumSize(QtCore.QSize(41, 16777215))
        self.portEdit.setFont(self.editFont)
        self.portEdit.setInputMethodHints(QtCore.Qt.ImhNone)

        self.usrEdit = QtWidgets.QLineEdit(self.camGBox)
        self.usrEdit.setFont(self.editFont)

        self.pwdEdit = QtWidgets.QLineEdit(self.camGBox)
        self.pwdEdit.setFont(self.editFont)
        self.pwdEdit.setEchoMode(QtWidgets.QLineEdit.Password)

    def setLineEdit(self, ipEdit, portEdit, usrEdit, pwdEdit):
        self.ipEdit.setText(ipEdit)
        self.portEdit.setText(portEdit)
        self.usrEdit.setText(usrEdit)
        self.pwdEdit.setText(pwdEdit)

    def monitor(self):
        self.setMonitorFonts()
        self.setCamGBox()
        self.setMonitorLables()
        self.setMonitorLayout()

    def config(self):
        self.setConfigFonts()
        self.setCamGBox()
        self.setConfigLables()
        self.setConfigLEdit()
        self.setConfigLayout()
        self.camGBox.setCheckable(True)
        self.camGBox.setChecked(False)
