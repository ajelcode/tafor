# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Work\tafor\tafor\ui\widgets_becmg.ui'
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
        self.becmg_layout = QtWidgets.QGridLayout()
        self.becmg_layout.setObjectName("becmg_layout")
        self.becmg_cloud3_label = QtWidgets.QLabel(Form)
        self.becmg_cloud3_label.setObjectName("becmg_cloud3_label")
        self.becmg_layout.addWidget(self.becmg_cloud3_label, 0, 12, 1, 1)
        self.becmg_wind_label = QtWidgets.QLabel(Form)
        self.becmg_wind_label.setObjectName("becmg_wind_label")
        self.becmg_layout.addWidget(self.becmg_wind_label, 0, 5, 1, 1)
        self.becmg_cloud2_label = QtWidgets.QLabel(Form)
        self.becmg_cloud2_label.setObjectName("becmg_cloud2_label")
        self.becmg_layout.addWidget(self.becmg_cloud2_label, 0, 11, 1, 1)
        self.becmg_period = QtWidgets.QLineEdit(Form)
        self.becmg_period.setObjectName("becmg_period")
        self.becmg_layout.addWidget(self.becmg_period, 2, 4, 1, 1)
        self.becmg_gust_label = QtWidgets.QLabel(Form)
        self.becmg_gust_label.setObjectName("becmg_gust_label")
        self.becmg_layout.addWidget(self.becmg_gust_label, 0, 6, 1, 1)
        self.becmg_period_label = QtWidgets.QLabel(Form)
        self.becmg_period_label.setObjectName("becmg_period_label")
        self.becmg_layout.addWidget(self.becmg_period_label, 0, 4, 1, 1)
        self.becmg_cb = QtWidgets.QLineEdit(Form)
        self.becmg_cb.setObjectName("becmg_cb")
        self.becmg_layout.addWidget(self.becmg_cb, 2, 13, 1, 1)
        self.becmg_vis_label = QtWidgets.QLabel(Form)
        self.becmg_vis_label.setObjectName("becmg_vis_label")
        self.becmg_layout.addWidget(self.becmg_vis_label, 0, 7, 1, 1)
        self.becmg_cloud1 = QtWidgets.QLineEdit(Form)
        self.becmg_cloud1.setObjectName("becmg_cloud1")
        self.becmg_layout.addWidget(self.becmg_cloud1, 2, 10, 1, 1)
        self.becmg_weather2_label = QtWidgets.QLabel(Form)
        self.becmg_weather2_label.setObjectName("becmg_weather2_label")
        self.becmg_layout.addWidget(self.becmg_weather2_label, 0, 9, 1, 1)
        self.becmg_cloud1_label = QtWidgets.QLabel(Form)
        self.becmg_cloud1_label.setObjectName("becmg_cloud1_label")
        self.becmg_layout.addWidget(self.becmg_cloud1_label, 0, 10, 1, 1)
        self.becmg_cavok = QtWidgets.QCheckBox(Form)
        self.becmg_cavok.setObjectName("becmg_cavok")
        self.becmg_layout.addWidget(self.becmg_cavok, 3, 7, 1, 1)
        self.becmg_nsc = QtWidgets.QCheckBox(Form)
        self.becmg_nsc.setObjectName("becmg_nsc")
        self.becmg_layout.addWidget(self.becmg_nsc, 3, 11, 1, 1)
        self.becmg_gust = QtWidgets.QLineEdit(Form)
        self.becmg_gust.setObjectName("becmg_gust")
        self.becmg_layout.addWidget(self.becmg_gust, 2, 6, 1, 1)
        self.becmg_cloud3 = QtWidgets.QLineEdit(Form)
        self.becmg_cloud3.setObjectName("becmg_cloud3")
        self.becmg_layout.addWidget(self.becmg_cloud3, 2, 12, 1, 1)
        self.becmg_skc = QtWidgets.QCheckBox(Form)
        self.becmg_skc.setObjectName("becmg_skc")
        self.becmg_layout.addWidget(self.becmg_skc, 3, 10, 1, 1)
        self.becmg_cloud2 = QtWidgets.QLineEdit(Form)
        self.becmg_cloud2.setObjectName("becmg_cloud2")
        self.becmg_layout.addWidget(self.becmg_cloud2, 2, 11, 1, 1)
        self.becmg_weather1 = QtWidgets.QComboBox(Form)
        self.becmg_weather1.setObjectName("becmg_weather1")
        self.becmg_layout.addWidget(self.becmg_weather1, 2, 8, 1, 1)
        self.becmg_vis = QtWidgets.QLineEdit(Form)
        self.becmg_vis.setObjectName("becmg_vis")
        self.becmg_layout.addWidget(self.becmg_vis, 2, 7, 1, 1)
        self.becmg_weather2 = QtWidgets.QComboBox(Form)
        self.becmg_weather2.setObjectName("becmg_weather2")
        self.becmg_layout.addWidget(self.becmg_weather2, 2, 9, 1, 1)
        self.becmg_weather1_label = QtWidgets.QLabel(Form)
        self.becmg_weather1_label.setObjectName("becmg_weather1_label")
        self.becmg_layout.addWidget(self.becmg_weather1_label, 0, 8, 1, 1)
        self.becmg_cb_label = QtWidgets.QLabel(Form)
        self.becmg_cb_label.setObjectName("becmg_cb_label")
        self.becmg_layout.addWidget(self.becmg_cb_label, 0, 13, 1, 1)
        self.becmg_wind = QtWidgets.QLineEdit(Form)
        self.becmg_wind.setObjectName("becmg_wind")
        self.becmg_layout.addWidget(self.becmg_wind, 2, 5, 1, 1)
        self.tempo_title = QtWidgets.QLabel(Form)
        self.tempo_title.setMinimumSize(QtCore.QSize(90, 0))
        self.tempo_title.setStyleSheet("color: rgb(120, 120, 120);")
        self.tempo_title.setObjectName("tempo_title")
        self.becmg_layout.addWidget(self.tempo_title, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.becmg_layout)
        self.becmg_cloud3_label.setBuddy(self.becmg_cloud3)
        self.becmg_wind_label.setBuddy(self.becmg_wind)
        self.becmg_cloud2_label.setBuddy(self.becmg_cloud2)
        self.becmg_gust_label.setBuddy(self.becmg_gust)
        self.becmg_period_label.setBuddy(self.becmg_period)
        self.becmg_vis_label.setBuddy(self.becmg_vis)
        self.becmg_weather2_label.setBuddy(self.becmg_weather2)
        self.becmg_cloud1_label.setBuddy(self.becmg_cloud1)
        self.becmg_weather1_label.setBuddy(self.becmg_weather1)
        self.becmg_cb_label.setBuddy(self.becmg_cb)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.becmg_period, self.becmg_wind)
        Form.setTabOrder(self.becmg_wind, self.becmg_gust)
        Form.setTabOrder(self.becmg_gust, self.becmg_vis)
        Form.setTabOrder(self.becmg_vis, self.becmg_weather1)
        Form.setTabOrder(self.becmg_weather1, self.becmg_weather2)
        Form.setTabOrder(self.becmg_weather2, self.becmg_cloud1)
        Form.setTabOrder(self.becmg_cloud1, self.becmg_cloud2)
        Form.setTabOrder(self.becmg_cloud2, self.becmg_cloud3)
        Form.setTabOrder(self.becmg_cloud3, self.becmg_cb)
        Form.setTabOrder(self.becmg_cb, self.becmg_cavok)
        Form.setTabOrder(self.becmg_cavok, self.becmg_skc)
        Form.setTabOrder(self.becmg_skc, self.becmg_nsc)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.becmg_cloud3_label.setText(_translate("Form", "云组3"))
        self.becmg_wind_label.setText(_translate("Form", "风向风速"))
        self.becmg_cloud2_label.setText(_translate("Form", "云组2"))
        self.becmg_gust_label.setText(_translate("Form", "阵风"))
        self.becmg_period_label.setText(_translate("Form", "时段"))
        self.becmg_vis_label.setText(_translate("Form", "能见度"))
        self.becmg_weather2_label.setText(_translate("Form", "天气现象2"))
        self.becmg_cloud1_label.setText(_translate("Form", "云组1"))
        self.becmg_cavok.setText(_translate("Form", "CAVOK"))
        self.becmg_nsc.setText(_translate("Form", "NSC"))
        self.becmg_skc.setText(_translate("Form", "SKC"))
        self.becmg_weather1_label.setText(_translate("Form", "天气现象1"))
        self.becmg_cb_label.setText(_translate("Form", "积雨云"))
        self.tempo_title.setText(_translate("Form", "BECMG"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
