import sys
from PyQt4 import QtGui, QtCore
import re

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle('RegexPy')
        self.setWindowIcon(QtGui.QIcon('favicon.png'))

        # add an exit feature
        exitAction = QtGui.QAction('&Quit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Leave the App')
        exitAction.triggered.connect(self.close_application)

        # menu part of exit feature
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(exitAction)
        
        self.home()

    def home(self):

        # result display box
        self.resultDisp = QtGui.QTextEdit()
        self.resultDisp.setReadOnly(True)
        self.resultDispWidget = QtGui.QDockWidget('', self)
        self.resultDispWidget.setFeatures(QtGui.QDockWidget.DockWidgetMovable)
        self.resultDispWidget.setWidget(self.resultDisp)
        self.resultDispWidget.setFloating(False)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.resultDispWidget)

        # text input box
        self.textInput = QtGui.QTextEdit()
        self.textInputWidget = QtGui.QDockWidget('', self)
        self.textInputWidget.setWidget(self.textInput)
        self.textInputWidget.setFloating(False)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.textInputWidget)

        # regex input box
        self.regexInput = QtGui.QLineEdit()
        self.regexInput.returnPressed.connect(self.executeRegex)
        self.regexInput.setPlaceholderText('input your regex here')
        self.regexInputWidget = QtGui.QDockWidget('', self)
        self.regexInputWidget.setWidget(self.regexInput)
        self.regexInputWidget.setFloating(False)
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, self.regexInputWidget)

        # this should always be last
        self.show()

    def executeRegex(self):
      regex = str(self.regexInput.text())
      result = re.findall(regex,self.textInput.toPlainText())
      for j in result:
        self.resultDisp.append(QtCore.QString(j))

    def addInput(self):
        # skip empty text
        if self.textInputWidget.text():
            self.myText = self.textInputWidget.text()
            self.textInput.append(self.myText)
        
    def close_application(self):
        # add functionality to see if we want to exit
        choice = QtGui.QMessageBox.question(self,'Exit','Are you sure you want to exit?',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

def run(): 
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()