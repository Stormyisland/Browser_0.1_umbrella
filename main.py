import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon, QKeySequence

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Create the web engine view
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.####.com"))
         super().__init__()
        layout = QVBoxLayout(self)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))

        layout.addWidget(self.browser)


class MainWindow(QMainWindow): 
    def __init__(self):
        super().__init__()

        self.setWindowTitle("my web browser JOOGLE")
        self.setWindowIcon(QIcon("icons/purple.png")) 
        self.resize(1200, 800)

        # Enable useful settings
        profile = QWebEngineProfile.defaultProfile()
        profile.settings().setAttribute(profile.settings().JavascriptEnabled, True)
        profile.settings().setAttribute(profile.settings().PluginsEnabled, True)

        # Tab widget
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.on_tab_changed)

        self.setCentralWidget(self.tabs)
        
