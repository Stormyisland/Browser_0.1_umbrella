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

        # NAVIGATION toolbar
        navtb = QToolbar(Navigation")
        navtb.setIconSize(QSize(16, 16)) 
        self.addToolBar(navtb)

        # Back
        back_btn = QAction(QIcon(os.path.join("icons", "back.png")), "Back", self)
        back_btn.triggered.connect(lambda: self.current_browser().back())
        navtb.addAction(back_btn)

 # Forward
        next_btn = QAction(QIcon(os.path.join("icons", "forward.png")), "Forward", self)
        next_btn.triggered.connect(lambda: self.current_browser().forward())
        navtb.addAction(next_btn)

 # Reload
        reload_btn = QAction(QIcon(os.path.join("icons", "purple.png")), "Reload", self)
        reload_btn.triggered.connect(lambda: self.current_browser().reload())
        navtb.addAction(reload_btn)


 # Home
        home_btn = QAction(QIcon(os.path.join("icons", "OOOGLE.png")), "Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

 # URL bar
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)
# Try QtPy6


        # Start with one tab
        self.add_new_tab("https://google.com")

        # Hook downloads
        profile.downloadRequested.connect(self.handle_download)

     def add_new_tab(self, url="https://###.com"):
        tab = BrowserTab(url)
        idx = self.tabs.addTab(tab, "New Tab")
        self.tabs.setCurrentIndex(idx)

        tab.browser.urlChanged.connect(self.update_urlbar)
        tab.browser.loadFinished.connect(self.update_tab_title) 

        tab.browser.urlChanged.connect(self.update_urlbar)
        tab.browser.loadFinished.connect(self.update_tab_title)
         #need to make my own home page

           def close_tab(self, index):
                if self.tabs.count() > 1:
                self.tabs.removeTab(index)

         def on_tab_changed(self, index):
        if index != -1:
            url = self.tabs.widget(index).browser.url().toString()
            self.urlbar.setText(url)

        ef current_browser(self) -> QWebEngineView:
        return self.tabs.currentWidget().browser

         def navigate_home(self):
        self.current_browser().setUrl(QUrl("https://google.com"))

        def on_tab_changed(self, index):
        if index != -1:
            url = self.tabs.widget(index).browser.url().toString()
            self.urlbar.setText(url)

        def current_browser(self) -> QWebEngineView:
           return self.tabs.currentWidget().browser

        def navigate_home(self):
        self.current_browser().setUrl(QUrl("https://google.com"))


        def navigate_to_url(self):
           url = self.urlbar.text()


         if not url.startswith("http"):
            url = "http://" + url
         self.current_browser().setUrl(QUrl(url))

            def update_urlbar(self, qurl):
         self.urlbar.setText(qurl.toString())
         self.urlbar.setCursorPosition(0)

        def update_tab_title(self):
        browser = self.current_browser()
        index = self.tabs.currentIndex()
        self.tabs.setTabText(index, browser.page().title())
