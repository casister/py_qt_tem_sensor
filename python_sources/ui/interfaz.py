# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
import pyqtgraph

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)




class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1207, 519)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.ledTab = QtGui.QTabWidget(Dialog)
        self.ledTab.setObjectName(_fromUtf8("ledTab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab)
        #  self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.led1_2 = QtGui.QRadioButton(self.tab)
        self.led1_2.setText(_fromUtf8(""))
        self.led1_2.setAutoExclusive(False)
        self.led1_2.setObjectName(_fromUtf8("led1_2"))
        self.horizontalLayout_2.addWidget(self.led1_2)
        self.led2_2 = QtGui.QRadioButton(self.tab)
        self.led2_2.setText(_fromUtf8(""))
        self.led2_2.setAutoExclusive(False)
        self.led2_2.setObjectName(_fromUtf8("led2_2"))
        self.horizontalLayout_2.addWidget(self.led2_2)
        self.led3_2 = QtGui.QRadioButton(self.tab)
        self.led3_2.setText(_fromUtf8(""))
        self.led3_2.setAutoExclusive(False)
        self.led3_2.setObjectName(_fromUtf8("led3_2"))
        self.horizontalLayout_2.addWidget(self.led3_2)
        self.led4_2 = QtGui.QRadioButton(self.tab)
        self.led4_2.setText(_fromUtf8(""))
        self.led4_2.setAutoExclusive(False)
        self.led4_2.setObjectName(_fromUtf8("led4_2"))
        self.horizontalLayout_2.addWidget(self.led4_2)
        self.led5_2 = QtGui.QRadioButton(self.tab)
        self.led5_2.setText(_fromUtf8(""))
        self.led5_2.setAutoExclusive(False)
        self.led5_2.setObjectName(_fromUtf8("led5_2"))
        self.horizontalLayout_2.addWidget(self.led5_2)
        self.led6_2 = QtGui.QRadioButton(self.tab)
        self.led6_2.setText(_fromUtf8(""))
        self.led6_2.setAutoExclusive(False)
        self.led6_2.setObjectName(_fromUtf8("led6_2"))
        self.horizontalLayout_2.addWidget(self.led6_2)
        self.led7_2 = QtGui.QRadioButton(self.tab)
        self.led7_2.setText(_fromUtf8(""))
        self.led7_2.setAutoExclusive(False)
        self.led7_2.setObjectName(_fromUtf8("led7_2"))
        self.horizontalLayout_2.addWidget(self.led7_2)
        self.led8_2 = QtGui.QRadioButton(self.tab)
        self.led8_2.setText(_fromUtf8(""))
        self.led8_2.setAutoExclusive(False)
        self.led8_2.setObjectName(_fromUtf8("led8_2"))
        self.horizontalLayout_2.addWidget(self.led8_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.sendButton = QtGui.QPushButton(self.tab)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.verticalLayout.addWidget(self.sendButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.ledInformation = QtGui.QTextEdit(self.tab)
        self.ledInformation.setReadOnly(True)
        self.ledInformation.setObjectName(_fromUtf8("ledInformation"))
        self.horizontalLayout_4.addWidget(self.ledInformation)
        self.ledTab.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.tab_2)
        #  self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.widget = QtGui.QWidget(self.tab_2)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        #  self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.status = QtGui.QPushButton(self.widget)
        self.status.setText(_fromUtf8(""))
        self.status.setObjectName(_fromUtf8("status"))
        self.verticalLayout_2.addWidget(self.status)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.start = QtGui.QPushButton(self.widget)
        self.start.setObjectName(_fromUtf8("start"))
        self.horizontalLayout_5.addWidget(self.start)
        self.stop = QtGui.QPushButton(self.widget)
        self.stop.setObjectName(_fromUtf8("stop"))
        self.horizontalLayout_5.addWidget(self.stop)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.lcd = QtGui.QLCDNumber(self.widget)
        self.lcd.setObjectName(_fromUtf8("lcd"))
        self.verticalLayout_2.addWidget(self.lcd)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_6.addWidget(self.widget)
        self.graphComponent = PlotWidget(self.tab_2)
        self.graphComponent.setObjectName(_fromUtf8("graphComponent"))
        self.horizontalLayout_6.addWidget(self.graphComponent)
        self.ledTab.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.ledTab)

        self.retranslateUi(Dialog)
        self.ledTab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "MLAB - ICTP", None))
        self.sendButton.setText(_translate("Dialog", "SEND LED VALUES", None))
        self.ledTab.setTabText(self.ledTab.indexOf(self.tab), _translate("Dialog", "Leds", None))
        self.start.setText(_translate("Dialog", "START", None))
        self.stop.setText(_translate("Dialog", "STOP", None))
        self.ledTab.setTabText(self.ledTab.indexOf(self.tab_2), _translate("Dialog", "Temperature", None))


from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
