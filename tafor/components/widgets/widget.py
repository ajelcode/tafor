import json
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication

from tafor.models import db, Tafor
from tafor.utils import CheckTAF
from tafor.components.ui import Ui_main_recent


def createAlarmMsgBox(parent, text):
    title = QCoreApplication.translate('MainWindow', 'Alarm')
    message = QCoreApplication.translate('MainWindow', 'Time to post {}').format(text)
    messageBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Question, title, message, parent=parent)
    snooze = messageBox.addButton(QCoreApplication.translate('MainWindow', 'Snooze'), QtWidgets.QMessageBox.ApplyRole)
    dismiss = messageBox.addButton(QCoreApplication.translate('MainWindow', 'Dismiss'), QtWidgets.QMessageBox.RejectRole)
    messageBox.exec_()

    if messageBox.clickedButton() == snooze:
        return True

    return False


class RecentTAF(QtWidgets.QWidget, Ui_main_recent.Ui_Recent):
    def __init__(self, parent, container, tt):
        super(RecentTAF, self).__init__(parent)
        self.setupUi(self)
        self.tt = tt

        container.addWidget(self)

    def updateGUI(self):
        item = db.query(Tafor).filter_by(tt=self.tt).order_by(Tafor.sent.desc()).first()

        if not item:
            self.hide()
            return 

        self.groupBox.setTitle(item.tt)
        self.sendTime.setText(item.sent.strftime('%Y-%m-%d %H:%M:%S'))
        self.rpt.setText(item.report)
        if item.confirmed:
            self.check.setText('<img src=":/checkmark.png" width="24" height="24"/>')
        else:
            self.check.setText('<img src=":/cross.png" width="24" height="24"/>')


class CurrentTAF(QtWidgets.QWidget):
    def __init__(self, parent, container):
        super(CurrentTAF, self).__init__(parent)

        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.fc = QtWidgets.QLabel()
        self.ft = QtWidgets.QLabel()

        layout.addWidget(self.fc)
        layout.addSpacing(10)
        layout.addWidget(self.ft)

        container.addWidget(self)

    def updateGUI(self):
        self.fc.setText(self.current('FC'))
        self.ft.setText(self.current('FT'))

    def current(self, tt):
        taf = CheckTAF(tt)
        if taf.local():
            text = ''
        else:
            text = tt + taf.warningPeriod(withDay=False)
        return text


class Clock(QtWidgets.QWidget):
    def __init__(self, parent, container):
        super(Clock, self).__init__(parent)

        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        # layout.addWidget(QtWidgets.QLabel('世界时'))
        layout.addSpacing(5)
        self.label = QtWidgets.QLabel()
        layout.addWidget(self.label)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateGUI)
        self.timer.start(1 * 1000)

        self.updateGUI()

        container.addWidget(self)

    def updateGUI(self):
        utc = datetime.datetime.utcnow()
        self.label.setText(utc.strftime('%Y-%m-%d %H:%M:%S'))
