from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
def xdd():
    QDesktopServices.openUrl(QUrl("https://support.qq.com/products/173442"))
if __name__ == '__main__':
    xdd()