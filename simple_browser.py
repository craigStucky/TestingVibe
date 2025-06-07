import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QToolBar, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Browser')
        self.resize(1024, 768)

        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)

        nav_bar = QToolBar()
        self.addToolBar(nav_bar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.web_view.back)
        nav_bar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.web_view.forward)
        nav_bar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.web_view.reload)
        nav_bar.addAction(reload_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_bar.addWidget(self.url_bar)

        self.web_view.urlChanged.connect(self.update_url_bar)
        self.web_view.load(QUrl('https://www.example.com'))

    def navigate_to_url(self):
        url = QUrl(self.url_bar.text())
        if url.scheme() == '':
            url.setScheme('http')
        self.web_view.load(url)

    def update_url_bar(self, url):
        self.url_bar.setText(url.toString())


def main():
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
