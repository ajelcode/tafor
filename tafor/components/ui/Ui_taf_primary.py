# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Work\tafor\tafor\components\ui\taf_primary.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Editor(object):
    def setupUi(self, Editor):
        Editor.setObjectName("Editor")
        Editor.resize(1011, 198)
        Editor.setWindowTitle("PRIMARY")
        self.verticalLayout = QtWidgets.QVBoxLayout(Editor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainLayout = QtWidgets.QGridLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.cloud2Label = QtWidgets.QLabel(Editor)
        self.cloud2Label.setObjectName("cloud2Label")
        self.mainLayout.addWidget(self.cloud2Label, 2, 9, 1, 1)
        self.cloud3 = QtWidgets.QLineEdit(Editor)
        self.cloud3.setObjectName("cloud3")
        self.mainLayout.addWidget(self.cloud3, 3, 10, 1, 1)
        self.period = QtWidgets.QLineEdit(Editor)
        self.period.setObjectName("period")
        self.mainLayout.addWidget(self.period, 3, 1, 1, 1)
        self.weather = QtWidgets.QComboBox(Editor)
        self.weather.setObjectName("weather")
        self.mainLayout.addWidget(self.weather, 3, 7, 1, 1)
        self.wind = QtWidgets.QLineEdit(Editor)
        self.wind.setObjectName("wind")
        self.mainLayout.addWidget(self.wind, 3, 2, 1, 1)
        self.windLabel = QtWidgets.QLabel(Editor)
        self.windLabel.setObjectName("windLabel")
        self.mainLayout.addWidget(self.windLabel, 2, 2, 1, 1)
        self.tempo2Checkbox = QtWidgets.QCheckBox(Editor)
        self.tempo2Checkbox.setText("TEMPO2")
        self.tempo2Checkbox.setObjectName("tempo2Checkbox")
        self.mainLayout.addWidget(self.tempo2Checkbox, 6, 1, 1, 1)
        self.cavok = QtWidgets.QCheckBox(Editor)
        self.cavok.setText("CAVOK")
        self.cavok.setCheckable(True)
        self.cavok.setObjectName("cavok")
        self.mainLayout.addWidget(self.cavok, 4, 4, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tmin = QtWidgets.QLineEdit(Editor)
        self.tmin.setMaximumSize(QtCore.QSize(35, 16777215))
        self.tmin.setObjectName("tmin")
        self.horizontalLayout_2.addWidget(self.tmin)
        self.tminTime = QtWidgets.QLineEdit(Editor)
        self.tminTime.setMaximumSize(QtCore.QSize(35, 16777215))
        self.tminTime.setObjectName("tminTime")
        self.horizontalLayout_2.addWidget(self.tminTime)
        self.mainLayout.addLayout(self.horizontalLayout_2, 6, 11, 1, 1)
        self.dateLabel = QtWidgets.QLabel(Editor)
        self.dateLabel.setObjectName("dateLabel")
        self.mainLayout.addWidget(self.dateLabel, 2, 0, 1, 1)
        self.weatherWithIntensityLabel = QtWidgets.QLabel(Editor)
        self.weatherWithIntensityLabel.setObjectName("weatherWithIntensityLabel")
        self.mainLayout.addWidget(self.weatherWithIntensityLabel, 2, 6, 1, 1)
        self.cloud1Label = QtWidgets.QLabel(Editor)
        self.cloud1Label.setObjectName("cloud1Label")
        self.mainLayout.addWidget(self.cloud1Label, 2, 8, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tmax = QtWidgets.QLineEdit(Editor)
        self.tmax.setMaximumSize(QtCore.QSize(35, 16777215))
        self.tmax.setObjectName("tmax")
        self.horizontalLayout.addWidget(self.tmax)
        self.tmaxTime = QtWidgets.QLineEdit(Editor)
        self.tmaxTime.setMaximumSize(QtCore.QSize(35, 16777215))
        self.tmaxTime.setObjectName("tmaxTime")
        self.horizontalLayout.addWidget(self.tmaxTime)
        self.mainLayout.addLayout(self.horizontalLayout, 6, 10, 1, 1)
        self.becmg1Checkbox = QtWidgets.QCheckBox(Editor)
        self.becmg1Checkbox.setText("BECMG1")
        self.becmg1Checkbox.setObjectName("becmg1Checkbox")
        self.mainLayout.addWidget(self.becmg1Checkbox, 5, 0, 1, 1)
        self.gustLabel = QtWidgets.QLabel(Editor)
        self.gustLabel.setObjectName("gustLabel")
        self.mainLayout.addWidget(self.gustLabel, 2, 3, 1, 1)
        self.visLabel = QtWidgets.QLabel(Editor)
        self.visLabel.setObjectName("visLabel")
        self.mainLayout.addWidget(self.visLabel, 2, 4, 1, 1)
        self.cloud2 = QtWidgets.QLineEdit(Editor)
        self.cloud2.setObjectName("cloud2")
        self.mainLayout.addWidget(self.cloud2, 3, 9, 1, 1)
        self.cloud3Label = QtWidgets.QLabel(Editor)
        self.cloud3Label.setObjectName("cloud3Label")
        self.mainLayout.addWidget(self.cloud3Label, 2, 10, 1, 1)
        self.weatherLabel = QtWidgets.QLabel(Editor)
        self.weatherLabel.setObjectName("weatherLabel")
        self.mainLayout.addWidget(self.weatherLabel, 2, 7, 1, 1)
        self.date = QtWidgets.QLineEdit(Editor)
        self.date.setObjectName("date")
        self.mainLayout.addWidget(self.date, 3, 0, 1, 1)
        self.gust = QtWidgets.QLineEdit(Editor)
        self.gust.setObjectName("gust")
        self.mainLayout.addWidget(self.gust, 3, 3, 1, 1)
        self.tempMaxLabel = QtWidgets.QLabel(Editor)
        self.tempMaxLabel.setObjectName("tempMaxLabel")
        self.mainLayout.addWidget(self.tempMaxLabel, 5, 10, 1, 1)
        self.becmg2Checkbox = QtWidgets.QCheckBox(Editor)
        self.becmg2Checkbox.setText("BECMG2")
        self.becmg2Checkbox.setObjectName("becmg2Checkbox")
        self.mainLayout.addWidget(self.becmg2Checkbox, 6, 0, 1, 1)
        self.becmg3Checkbox = QtWidgets.QCheckBox(Editor)
        self.becmg3Checkbox.setText("BECMG3")
        self.becmg3Checkbox.setObjectName("becmg3Checkbox")
        self.mainLayout.addWidget(self.becmg3Checkbox, 7, 0, 1, 1)
        self.cb = QtWidgets.QLineEdit(Editor)
        self.cb.setObjectName("cb")
        self.mainLayout.addWidget(self.cb, 3, 11, 1, 1)
        self.cbLabel = QtWidgets.QLabel(Editor)
        self.cbLabel.setObjectName("cbLabel")
        self.mainLayout.addWidget(self.cbLabel, 2, 11, 1, 1)
        self.tempMinLabel = QtWidgets.QLabel(Editor)
        self.tempMinLabel.setObjectName("tempMinLabel")
        self.mainLayout.addWidget(self.tempMinLabel, 5, 11, 1, 1)
        self.periodLabel = QtWidgets.QLabel(Editor)
        self.periodLabel.setObjectName("periodLabel")
        self.mainLayout.addWidget(self.periodLabel, 2, 1, 1, 1)
        self.weatherWithIntensity = QtWidgets.QComboBox(Editor)
        self.weatherWithIntensity.setObjectName("weatherWithIntensity")
        self.mainLayout.addWidget(self.weatherWithIntensity, 3, 6, 1, 1)
        self.cloud1 = QtWidgets.QLineEdit(Editor)
        self.cloud1.setObjectName("cloud1")
        self.mainLayout.addWidget(self.cloud1, 3, 8, 1, 1)
        self.typeGroup = QtWidgets.QGroupBox(Editor)
        self.typeGroup.setTitle("")
        self.typeGroup.setObjectName("typeGroup")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.typeGroup)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.fc = QtWidgets.QRadioButton(self.typeGroup)
        self.fc.setText("FC")
        self.fc.setChecked(True)
        self.fc.setObjectName("fc")
        self.gridLayout_6.addWidget(self.fc, 0, 0, 1, 1)
        self.ft = QtWidgets.QRadioButton(self.typeGroup)
        self.ft.setText("FT")
        self.ft.setObjectName("ft")
        self.gridLayout_6.addWidget(self.ft, 0, 1, 1, 1)
        self.mainLayout.addWidget(self.typeGroup, 0, 0, 1, 2)
        self.vis = QtWidgets.QLineEdit(Editor)
        self.vis.setObjectName("vis")
        self.mainLayout.addWidget(self.vis, 3, 4, 1, 1)
        self.tempo1Checkbox = QtWidgets.QCheckBox(Editor)
        self.tempo1Checkbox.setText("TEMPO1")
        self.tempo1Checkbox.setObjectName("tempo1Checkbox")
        self.mainLayout.addWidget(self.tempo1Checkbox, 5, 1, 1, 1)
        self.sortGroup = QtWidgets.QGroupBox(Editor)
        self.sortGroup.setTitle("")
        self.sortGroup.setObjectName("sortGroup")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.sortGroup)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.aaa = QtWidgets.QLineEdit(self.sortGroup)
        self.aaa.setObjectName("aaa")
        self.gridLayout_5.addWidget(self.aaa, 0, 4, 1, 1)
        self.cnl = QtWidgets.QRadioButton(self.sortGroup)
        self.cnl.setObjectName("cnl")
        self.gridLayout_5.addWidget(self.cnl, 0, 5, 1, 1)
        self.ccc = QtWidgets.QLineEdit(self.sortGroup)
        self.ccc.setObjectName("ccc")
        self.gridLayout_5.addWidget(self.ccc, 0, 2, 1, 1)
        self.cor = QtWidgets.QRadioButton(self.sortGroup)
        self.cor.setObjectName("cor")
        self.gridLayout_5.addWidget(self.cor, 0, 1, 1, 1)
        self.amd = QtWidgets.QRadioButton(self.sortGroup)
        self.amd.setObjectName("amd")
        self.gridLayout_5.addWidget(self.amd, 0, 3, 1, 1)
        self.aaaCnl = QtWidgets.QLineEdit(self.sortGroup)
        self.aaaCnl.setObjectName("aaaCnl")
        self.gridLayout_5.addWidget(self.aaaCnl, 0, 6, 1, 1)
        self.normal = QtWidgets.QRadioButton(self.sortGroup)
        self.normal.setChecked(True)
        self.normal.setObjectName("normal")
        self.gridLayout_5.addWidget(self.normal, 0, 0, 1, 1)
        self.prev = QtWidgets.QCheckBox(self.sortGroup)
        self.prev.setObjectName("prev")
        self.gridLayout_5.addWidget(self.prev, 0, 7, 1, 1)
        self.mainLayout.addWidget(self.sortGroup, 0, 4, 1, 8)
        self.nsc = QtWidgets.QCheckBox(Editor)
        self.nsc.setText("NSC")
        self.nsc.setObjectName("nsc")
        self.mainLayout.addWidget(self.nsc, 4, 8, 1, 1)
        self.tempo3Checkbox = QtWidgets.QCheckBox(Editor)
        self.tempo3Checkbox.setText("TEMPO3")
        self.tempo3Checkbox.setObjectName("tempo3Checkbox")
        self.mainLayout.addWidget(self.tempo3Checkbox, 7, 1, 1, 1)
        self.verticalLayout.addLayout(self.mainLayout)
        self.cloud2Label.setBuddy(self.cloud2)
        self.windLabel.setBuddy(self.wind)
        self.dateLabel.setBuddy(self.date)
        self.weatherWithIntensityLabel.setBuddy(self.weatherWithIntensity)
        self.cloud1Label.setBuddy(self.cloud1)
        self.gustLabel.setBuddy(self.gust)
        self.visLabel.setBuddy(self.vis)
        self.cloud3Label.setBuddy(self.cloud3)
        self.weatherLabel.setBuddy(self.weather)
        self.tempMaxLabel.setBuddy(self.tmax)
        self.cbLabel.setBuddy(self.cb)
        self.tempMinLabel.setBuddy(self.tmin)
        self.periodLabel.setBuddy(self.period)

        self.retranslateUi(Editor)
        QtCore.QMetaObject.connectSlotsByName(Editor)
        Editor.setTabOrder(self.fc, self.ft)
        Editor.setTabOrder(self.ft, self.normal)
        Editor.setTabOrder(self.normal, self.cor)
        Editor.setTabOrder(self.cor, self.ccc)
        Editor.setTabOrder(self.ccc, self.amd)
        Editor.setTabOrder(self.amd, self.aaa)
        Editor.setTabOrder(self.aaa, self.cnl)
        Editor.setTabOrder(self.cnl, self.aaaCnl)
        Editor.setTabOrder(self.aaaCnl, self.prev)
        Editor.setTabOrder(self.prev, self.date)
        Editor.setTabOrder(self.date, self.period)
        Editor.setTabOrder(self.period, self.wind)
        Editor.setTabOrder(self.wind, self.gust)
        Editor.setTabOrder(self.gust, self.vis)
        Editor.setTabOrder(self.vis, self.weatherWithIntensity)
        Editor.setTabOrder(self.weatherWithIntensity, self.weather)
        Editor.setTabOrder(self.weather, self.cloud1)
        Editor.setTabOrder(self.cloud1, self.cloud2)
        Editor.setTabOrder(self.cloud2, self.cloud3)
        Editor.setTabOrder(self.cloud3, self.cb)
        Editor.setTabOrder(self.cb, self.cavok)
        Editor.setTabOrder(self.cavok, self.tmax)
        Editor.setTabOrder(self.tmax, self.tmaxTime)
        Editor.setTabOrder(self.tmaxTime, self.tmin)
        Editor.setTabOrder(self.tmin, self.tminTime)
        Editor.setTabOrder(self.tminTime, self.becmg1Checkbox)
        Editor.setTabOrder(self.becmg1Checkbox, self.becmg2Checkbox)
        Editor.setTabOrder(self.becmg2Checkbox, self.becmg3Checkbox)
        Editor.setTabOrder(self.becmg3Checkbox, self.tempo1Checkbox)
        Editor.setTabOrder(self.tempo1Checkbox, self.tempo2Checkbox)

    def retranslateUi(self, Editor):
        _translate = QtCore.QCoreApplication.translate
        self.cloud2Label.setText(_translate("Editor", "Cloud2"))
        self.windLabel.setText(_translate("Editor", "Wind"))
        self.dateLabel.setText(_translate("Editor", "Datetime"))
        self.weatherWithIntensityLabel.setText(_translate("Editor", "Weather1"))
        self.cloud1Label.setText(_translate("Editor", "Cloud1"))
        self.gustLabel.setText(_translate("Editor", "Gust"))
        self.visLabel.setText(_translate("Editor", "Visibility"))
        self.cloud3Label.setText(_translate("Editor", "Cloud3"))
        self.weatherLabel.setText(_translate("Editor", "Weather2"))
        self.tempMaxLabel.setText(_translate("Editor", "Max Temperature"))
        self.cbLabel.setText(_translate("Editor", "Cumulonimbus"))
        self.tempMinLabel.setText(_translate("Editor", "Min Temperature"))
        self.periodLabel.setText(_translate("Editor", "Valid Period"))
        self.cnl.setText(_translate("Editor", "Cancel"))
        self.cor.setText(_translate("Editor", "Correct"))
        self.amd.setText(_translate("Editor", "Amend"))
        self.normal.setText(_translate("Editor", "Normal"))
        self.prev.setText(_translate("Editor", "Previous"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Editor = QtWidgets.QWidget()
    ui = Ui_Editor()
    ui.setupUi(Editor)
    Editor.show()
    sys.exit(app.exec_())

