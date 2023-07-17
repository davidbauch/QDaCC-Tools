from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QTextBrowser

class TextBrowserExternal(QTextBrowser):
    def __init__ (self, parent = None):
        super().__init__(parent)
        self.setOpenExternalLinks(True)
    def setSource(self, url, type = None):
        print(f"setSource: {url}")
        if url.isLocalFile():
            QDesktopServices.openUrl(url)
    def doSetSource(self, url, type = None):
        print(f"doSetSource: {url}")
        if url.isLocalFile():
            QDesktopServices.openUrl(url)
