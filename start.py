import sys
import app.main.resource.icons
import app.main.resource.fonts
from app.main.view.mainwidget import MainWidget
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication

if sys.platform.startswith("win"):
    import ctypes
    appid = 'tvglobo.sdrmonitor.ver1'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

ORGANIZATION_NAME = "Globo"
ORGANIZATION_DOMAIN = "tvglobo.com.br"
APPLICATION_NAME = "RouterBoard Monitor SAEG"

QCoreApplication.setApplicationName(ORGANIZATION_NAME)
QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
QCoreApplication.setApplicationName(APPLICATION_NAME)


app = QtWidgets.QApplication(sys.argv)
tabWidget = QtWidgets.QTabWidget()
ui = MainWidget()
ui.setupUi(tabWidget)
tabWidget.show()
ui.cron()
sys.exit(app.exec_())
