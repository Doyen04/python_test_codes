from PyQt5.QtWidgets import (QTextEdit, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
QCalendarWidget, QCheckBox, QColorDialog, QColumnView, QComboBox, QCommandLinkButton, QDateEdit, QDateTimeEdit, QDesktopWidget, QDial, QDialog, QDialogButtonBox, QDockWidget, QDoubleSpinBox, QErrorMessage, QFileDialog, QFocusFrame, QFontComboBox, QFontDialog, QFrame, QGraphicsView, QGroupBox, QInputDialog, QKeySequenceEdit, QLCDNumber, QLabel, QLineEdit, QListView, QListWidget, QMainWindow, QMdiArea, QMdiSubWindow, QMenu, QMenuBar, QMessageBox, QOpenGLWidget, QPlainTextEdit, QProgressBar, QProgressDialog, QPushButton, QRadioButton, QScrollArea, QScrollBar, QSlider, QSpinBox, QSplashScreen, QSplitter,  QStackedWidget, QStatusBar, QTabBar, QTabWidget, QTableView, QTableWidget, QTextBrowser, QTextEdit, QTimeEdit, QToolBar, QToolBox, QToolButton, QTreeView, QTreeWidget, QUndoView, QWizard, QWizardPage,
                             QHBoxLayout, QVBoxLayout, QWidget,QScroller, QMainWindow)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        widgets = [      QCalendarWidget, QCheckBox, QColorDialog,QColumnView, QComboBox, QCommandLinkButton, QDateEdit, QDateTimeEdit, QDesktopWidget, QDial, QDialog, QDialogButtonBox,QDockWidget, QDoubleSpinBox, QErrorMessage,  QFileDialog, QFocusFrame,  QFontComboBox, QFontDialog,  QFrame, QGraphicsView, QGroupBox, QInputDialog, QKeySequenceEdit, QLCDNumber, QLabel, QLineEdit,QListView, QListWidget, QMainWindow, QMdiArea, QMdiSubWindow, QMenu, QMenuBar,QMessageBox,
   #QOpenGLWidget, 
   QPlainTextEdit, QProgressBar,   QProgressDialog, QPushButton, QRadioButton,  QScrollArea, QScrollBar,QSlider, QSpinBox,  QSplashScreen, QSplitter,  QStackedWidget, QStatusBar,QTabBar, QTabWidget, QTableView, QTableWidget,QTextBrowser, QTextEdit, QTimeEdit,  QToolBar, QToolBox, QToolButton,  QTreeView, QTreeWidget,
  QUndoView, QWizard, QWizardPage,
        ]
        for i in widgets:
            #object = QLabel(f"TextLabel{i}")
            self.vbox.addWidget(i())

        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        QScroller.grabGesture(
            self.scroll.viewport(), QScroller.LeftMouseButtonGesture
        )
        self.setCentralWidget(self.scroll)

       # self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Scroll Area Demonstration')
        self.show()

        return

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()