# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Work\tafor\tafor\components\ui\taf_becmg.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 80)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout = QtWidgets.QGridLayout()
        self.layout.setObjectName("layout")
        self.intervalLabel = QtWidgets.QLabel(Form)
        self.intervalLabel.setObjectName("intervalLabel")
        self.layout.addWidget(self.intervalLabel, 2, 4, 1, 1)
        self.cloud2Label = QtWidgets.QLabel(Form)
        self.cloud2Label.setObjectName("cloud2Label")
        self.layout.addWidget(self.cloud2Label, 2, 12, 1, 1)
        self.cb = QtWidgets.QLineEdit(Form)
        self.cb.setObjectName("cb")
        self.layout.addWidget(self.cb, 5, 14, 1, 1)
        self.windLabel = QtWidgets.QLabel(Form)
        self.windLabel.setObjectName("windLabel")
        self.layout.addWidget(self.windLabel, 2, 5, 1, 1)
        self.gustLabel = QtWidgets.QLabel(Form)
        self.gustLabel.setObjectName("gustLabel")
        self.layout.addWidget(self.gustLabel, 2, 6, 1, 1)
        self.interval = QtWidgets.QLineEdit(Form)
        self.interval.setObjectName("interval")
        self.layout.addWidget(self.interval, 5, 4, 1, 1)
        self.visLabel = QtWidgets.QLabel(Form)
        self.visLabel.setObjectName("visLabel")
        self.layout.addWidget(self.visLabel, 2, 7, 1, 1)
        self.cloud3Label = QtWidgets.QLabel(Form)
        self.cloud3Label.setObjectName("cloud3Label")
        self.layout.addWidget(self.cloud3Label, 2, 13, 1, 1)
        self.vis = QtWidgets.QLineEdit(Form)
        self.vis.setObjectName("vis")
        self.layout.addWidget(self.vis, 5, 7, 1, 1)
        self.cavok = QtWidgets.QCheckBox(Form)
        self.cavok.setObjectName("cavok")
        self.layout.addWidget(self.cavok, 6, 7, 1, 1)
        self.cloud1 = QtWidgets.QLineEdit(Form)
        self.cloud1.setObjectName("cloud1")
        self.layout.addWidget(self.cloud1, 5, 11, 1, 1)
        self.nsc = QtWidgets.QCheckBox(Form)
        self.nsc.setObjectName("nsc")
        self.layout.addWidget(self.nsc, 6, 12, 1, 1)
        self.cloud3 = QtWidgets.QLineEdit(Form)
        self.cloud3.setObjectName("cloud3")
        self.layout.addWidget(self.cloud3, 5, 13, 1, 1)
        self.skc = QtWidgets.QCheckBox(Form)
        self.skc.setObjectName("skc")
        self.layout.addWidget(self.skc, 6, 11, 1, 1)
        self.gust = QtWidgets.QLineEdit(Form)
        self.gust.setObjectName("gust")
        self.layout.addWidget(self.gust, 5, 6, 1, 1)
        self.wind = QtWidgets.QLineEdit(Form)
        self.wind.setObjectName("wind")
        self.layout.addWidget(self.wind, 5, 5, 1, 1)
        self.cloud2 = QtWidgets.QLineEdit(Form)
        self.cloud2.setObjectName("cloud2")
        self.layout.addWidget(self.cloud2, 5, 12, 1, 1)
        self.name = QtWidgets.QLabel(Form)
        self.name.setMinimumSize(QtCore.QSize(76, 0))
        self.name.setStyleSheet("color: rgb(120, 120, 120);")
        self.name.setObjectName("name")
        self.layout.addWidget(self.name, 5, 0, 1, 1)
        self.cloud1Label = QtWidgets.QLabel(Form)
        self.cloud1Label.setObjectName("cloud1Label")
        self.layout.addWidget(self.cloud1Label, 2, 11, 1, 1)
        self.cbLabel = QtWidgets.QLabel(Form)
        self.cbLabel.setObjectName("cbLabel")
        self.layout.addWidget(self.cbLabel, 2, 14, 1, 1)
        self.weather = QtWidgets.QComboBox(Form)
        self.weather.setObjectName("weather")
        self.layout.addWidget(self.weather, 5, 10, 1, 1)
        self.weatherWithIntensity = QtWidgets.QComboBox(Form)
        self.weatherWithIntensity.setObjectName("weatherWithIntensity")
        self.layout.addWidget(self.weatherWithIntensity, 5, 8, 1, 1)
        self.weatherLabel = QtWidgets.QLabel(Form)
        self.weatherLabel.setObjectName("weatherLabel")
        self.layout.addWidget(self.weatherLabel, 2, 10, 1, 1)
        self.weatherWithIntensityLabel = QtWidgets.QLabel(Form)
        self.weatherWithIntensityLabel.setObjectName("weatherWithIntensityLabel")
        self.layout.addWidget(self.weatherWithIntensityLabel, 2, 8, 1, 1)
        self.verticalLayout.addLayout(self.layout)
        self.intervalLabel.setBuddy(self.interval)
        self.cloud2Label.setBuddy(self.cloud2)
        self.windLabel.setBuddy(self.wind)
        self.gustLabel.setBuddy(self.gust)
        self.visLabel.setBuddy(self.vis)
        self.cloud3Label.setBuddy(self.cloud3)
        self.cloud1Label.setBuddy(self.cloud1)
        self.cbLabel.setBuddy(self.cb)
        self.weatherLabel.setBuddy(self.weather)
        self.weatherWithIntensityLabel.setBuddy(self.weatherWithIntensity)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.interval, self.wind)
        Form.setTabOrder(self.wind, self.gust)
        Form.setTabOrder(self.gust, self.vis)
        Form.setTabOrder(self.vis, self.cloud1)
        Form.setTabOrder(self.cloud1, self.cloud2)
        Form.setTabOrder(self.cloud2, self.cloud3)
        Form.setTabOrder(self.cloud3, self.cb)
        Form.setTabOrder(self.cb, self.cavok)
        Form.setTabOrder(self.cavok, self.skc)
        Form.setTabOrder(self.skc, self.nsc)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.intervalLabel.setText(_translate("Form", "Interval"))
        self.cloud2Label.setText(_translate("Form", "Cloud2"))
        self.windLabel.setText(_translate("Form", "Wind"))
        self.gustLabel.setText(_translate("Form", "Gust"))
        self.visLabel.setText(_translate("Form", "Visibility"))
        self.cloud3Label.setText(_translate("Form", "Cloud3"))
        self.cavok.setText(_translate("Form", "CAVOK"))
        self.nsc.setText(_translate("Form", "NSC"))
        self.skc.setText(_translate("Form", "SKC"))
        self.name.setText(_translate("Form", "BECMG"))
        self.cloud1Label.setText(_translate("Form", "Cloud1"))
        self.cbLabel.setText(_translate("Form", "Cumulonimbus"))
        self.weatherLabel.setText(_translate("Form", "Weather2"))
        self.weatherWithIntensityLabel.setText(_translate("Form", "Weather1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

