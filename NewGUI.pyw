from __future__ import division
import sys
from math import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * # QApplication, QDialog, QTextBrowser, QLineEdit
from PyQt5.QtGui import *


class Form(QDialog):
    def __init__(self, parent = None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.lineedit.returnPressed.connect(self.updateUI)
    #    self.connect(self.lineedit, SIGNAL("returnPressed()"), self.updateUi)
        self.setWindowTitle("Calculate")


    def updateUI(self):
        #words = str(self.lineedit.words())

        try:
            text = str(self.lineedit.text())
#            text = str(self)
            self.browser.append("%s = <b>%</b>" % (self, eval(self)))
#            self.browser.append("answer is" % eval(self))
        except:
           self.browser.append("<font color = red>%s is invalid!</font>" % text)

#UnboundLocalError: local variable 'words' referenced before assignment
#if __name__ == '__main__':
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec()
