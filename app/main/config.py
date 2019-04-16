from PyQt5.QtCore import QSettings

config = QSettings("application", "mainapp")
config.sync()
