import json
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from tafor import conf, logger
from tafor.utils import CheckTAF, Pattern
from tafor.components.ui import Ui_taf_primary, Ui_taf_becmg, Ui_taf_tempo, Ui_trend


class BaseSegment(QtWidgets.QWidget):
    signal_required = QtCore.pyqtSignal(bool)

    def __init__(self):
        super(BaseSegment, self).__init__()
        self.rules = Pattern()
        self.required = False
        # self.one_second_timer = QtCore.QTimer()
        # self.one_second_timer.timeout.connect(self.message)
        # self.one_second_timer.start(1 * 1000)

    def bind_signal(self):

        if hasattr(self, 'cavok'):
            self.cavok.toggled.connect(self.set_cavok)
            self.skc.toggled.connect(self.set_skc)
            self.nsc.toggled.connect(self.set_nsc)
            self.cavok.clicked.connect(self.check_required)
            self.nsc.clicked.connect(self.check_required)
            self.skc.clicked.connect(self.check_required)
        else:
            self.prob30.toggled.connect(self.set_prob30)
            self.prob40.toggled.connect(self.set_prob40)

        self.cloud1.textEdited.connect(lambda:self._upper_text(self.cloud1))
        self.cloud2.textEdited.connect(lambda:self._upper_text(self.cloud2))
        self.cloud3.textEdited.connect(lambda:self._upper_text(self.cloud3))
        self.cb.textEdited.connect(lambda:self._upper_text(self.cb))

        self.wind.textChanged.connect(self.check_required)
        self.vis.textChanged.connect(self.check_required)
        self.cloud1.textChanged.connect(self.check_required)
        self.cloud2.textChanged.connect(self.check_required)
        self.cloud3.textChanged.connect(self.check_required)
        self.cb.textChanged.connect(self.check_required)


    def clouds(self, enbale):
        if enbale:
            self.cloud1.setEnabled(True)
            self.cloud2.setEnabled(True)
            self.cloud3.setEnabled(True)
            self.cb.setEnabled(True)
        else:
            self.cloud1.clear()
            self.cloud1.setEnabled(False)
            self.cloud2.clear()
            self.cloud2.setEnabled(False)
            self.cloud3.clear()
            self.cloud3.setEnabled(False)
            self.cb.clear()
            self.cb.setEnabled(False)


    def set_cavok(self, checked):
        if checked:
            self.skc.setChecked(False)
            self.nsc.setChecked(False)

            self.vis.clear()
            self.vis.setEnabled(False)
            self.weather.setEnabled(False)
            self.weather_with_intensity.setEnabled(False)
            self.clouds(False)
        else:
            self.vis.setEnabled(True)
            self.weather.setEnabled(True)
            self.weather_with_intensity.setEnabled(True)
            self.clouds(True)

    def set_skc(self, checked):
        if checked:
            self.cavok.setChecked(False)
            self.nsc.setChecked(False)
            self.clouds(False)
        else:
            self.clouds(True)

    def set_nsc(self, checked):
        if checked:
            self.cavok.setChecked(False)
            self.skc.setChecked(False)
            self.clouds(False)
        else:
            self.clouds(True)

    def set_prob30(self, checked):
        if checked:
            self.prob40.setChecked(False)
        
    def set_prob40(self, checked):
        if checked:
            self.prob30.setChecked(False)

    def set_validator(self):
        self.valid_wind = QtGui.QRegExpValidator(QtCore.QRegExp(self.rules.wind))
        self.wind.setValidator(self.valid_wind)

        valid_gust = QtGui.QRegExpValidator(QtCore.QRegExp(self.rules.gust))
        self.gust.setValidator(valid_gust)

        valid_vis = QtGui.QRegExpValidator(QtCore.QRegExp(self.rules.vis))
        self.vis.setValidator(valid_vis)

        valid_cloud = QtGui.QRegExpValidator(QtCore.QRegExp(self.rules.cloud, QtCore.Qt.CaseInsensitive))
        self.cloud1.setValidator(valid_cloud)
        self.cloud2.setValidator(valid_cloud)
        self.cloud3.setValidator(valid_cloud)
        self.cb.setValidator(valid_cloud)

        weather = conf.value('message/weather')
        weathers = [''] + json.loads(weather) if weather else ['']
        self.weather.addItems(weathers)

        weather_with_intensity = conf.value('message/weather_with_intensity')
        weathers_with_intensity = ['']
        if weather_with_intensity:
            for w in json.loads(weather_with_intensity):
                weathers_with_intensity.extend(['-' + w, w, '+' + w])
        self.weather_with_intensity.addItems(weathers_with_intensity)

    def message(self):
        wind = self.wind.text() if self.wind.hasAcceptableInput() else None
        gust = self.gust.text() if self.gust.hasAcceptableInput() else None

        if wind:
            winds = ''.join([wind, 'G', gust, 'MPS']) if gust else ''.join([wind, 'MPS'])
        else:
            winds = None

        vis = self.vis.text() if self.vis.hasAcceptableInput() else None
        weather = self.weather.currentText()
        weather_with_intensity = self.weather_with_intensity.currentText()
        cloud1 = self.cloud1.text() if self.cloud1.hasAcceptableInput() else None
        cloud2 = self.cloud2.text() if self.cloud2.hasAcceptableInput() else None
        cloud3 = self.cloud3.text() if self.cloud3.hasAcceptableInput() else None
        cb = self.cb.text() + 'CB' if self.cb.hasAcceptableInput() else None

        clouds = sorted(filter(None, [cloud1, cloud2, cloud3, cb]), key=lambda cloud: int(cloud[3:6]))

        if hasattr(self, 'cavok'):
            if self.cavok.isChecked():
                msg_list = [winds, 'CAVOK']
            elif self.skc.isChecked():
                msg_list = [winds, vis, weather, weather_with_intensity, 'SKC']
            elif self.nsc.isChecked():
                msg_list = [winds, vis, weather, weather_with_intensity, 'NSC']
            else:
                msg_list = [winds, vis, weather, weather_with_intensity] + clouds
        else:
            msg_list = [winds, vis, weather, weather_with_intensity] + clouds
        self.msg = ' '.join(filter(None, msg_list))
        # logger.debug(self.msg)

    def _upper_text(self, line):
        line.setText(line.text().upper())

    def check_required(self):
        raise NotImplemented

    def clear(self):
        self.wind.clear()
        self.gust.clear()
        self.vis.clear()
        self.weather.setCurrentIndex(-1)
        self.weather_with_intensity.setCurrentIndex(-1)
        self.cloud1.clear()
        self.cloud2.clear()
        self.cloud3.clear()
        self.cb.clear()


class TAFPrimarySegment(BaseSegment, Ui_taf_primary.Ui_Form):

    def __init__(self):
        super(TAFPrimarySegment, self).__init__()
        self.setupUi(self)

        self.set_validator()
        self.period.setEnabled(False)
        self.ccc.setEnabled(False)
        self.aaa.setEnabled(False)
        self.aaa_cnl.setEnabled(False)

        self.bind_signal()

    def set_validator(self):
        super(TAFPrimarySegment, self).set_validator()

        valid_date = QtGui.QRegExpValidator(QtCore.QRegExp(self.rules.date))
        self.date.setValidator(valid_date)

        valid_temp = QtGui.QRegExpValidator(QtCore.QRegExp(self.rules.temp))
        self.tmax.setValidator(valid_temp)
        self.tmin.setValidator(valid_temp)

        valid_temp_hours = QtGui.QRegExpValidator(QtCore.QRegExp(self.rules.hours))
        self.tmax_time.setValidator(valid_temp_hours)
        self.tmin_time.setValidator(valid_temp_hours)

    def bind_signal(self):
        super(TAFPrimarySegment, self).bind_signal()

        # 设置下一步按钮
        self.date.textEdited.connect(self.check_required)
        self.period.textChanged.connect(self.check_required)
        self.tmax.textChanged.connect(self.check_required)
        self.tmax_time.textChanged.connect(self.check_required)
        self.tmin.textChanged.connect(self.check_required)
        self.tmin_time.textChanged.connect(self.check_required)

    def check_required(self):
        self.required = False
        must_required = (
                        self.date.hasAcceptableInput(), 
                        self.period.text(), 
                        self.wind.hasAcceptableInput(), 
                        self.tmax.hasAcceptableInput(), 
                        self.tmax_time.hasAcceptableInput(), 
                        self.tmin.hasAcceptableInput(), 
                        self.tmin_time.hasAcceptableInput()
                        )
        one_required = (
                        self.nsc.isChecked(), 
                        self.skc.isChecked(), 
                        self.cloud1.hasAcceptableInput(), 
                        self.cloud2.hasAcceptableInput(), 
                        self.cloud3.hasAcceptableInput(), 
                        self.cb.hasAcceptableInput()
                        )
        
        if all(must_required):
            if self.cavok.isChecked():
                self.required = True
            elif self.vis.hasAcceptableInput() and any(one_required):
                self.required = True

        self.signal_required.emit(self.required)


    def message(self):
        super(TAFPrimarySegment, self).message()
        amd = 'AMD' if self.amd.isChecked() else ''
        cor = 'COR' if self.cor.isChecked() else ''
        icao = conf.value('message/icao')
        timez = self.date.text() + 'Z'
        period = self.period.text()
        tmax = ''.join(['TX', self.tmax.text(), '/', self.tmax_time.text(), 'Z'])
        tmin = ''.join(['TN', self.tmin.text(), '/', self.tmin_time.text(), 'Z'])
        msg_list = ['TAF', amd, cor, icao, timez, period, self.msg, tmax, tmin]
        self.msg = ' '.join(filter(None, msg_list))
        return self.msg

    def head(self):
        intelligence = conf.value('message/intelligence')
        icao = conf.value('message/icao')
        time = self.date.text()
        tt = ''
        if self.fc.isChecked():
            tt = 'FC'
        elif self.ft.isChecked():
            tt = 'FT'

        ccc = self.ccc.text() if self.cor.isChecked() else None
        aaa = self.aaa.text() if self.amd.isChecked() else None
        aaa_cnl = self.aaa_cnl.text() if self.cnl.isChecked() else None
        msg_list = [tt + intelligence, icao, time, ccc, aaa, aaa_cnl]
        return ' '.join(filter(None, msg_list))

    def clear(self):
        super(TAFPrimarySegment, self).clear()

        self.becmg1_checkbox.setChecked(False)
        self.becmg2_checkbox.setChecked(False)
        self.becmg3_checkbox.setChecked(False)
        self.tempo1_checkbox.setChecked(False)
        self.tempo2_checkbox.setChecked(False)

        self.cavok.setChecked(False)
        self.skc.setChecked(False)
        self.nsc.setChecked(False)

        self.tmax.clear()
        self.tmax_time.clear()
        self.tmin.clear()
        self.tmin_time.clear()


class TAFBecmgSegment(BaseSegment, Ui_taf_becmg.Ui_Form):

    def __init__(self, name='becmg'):
        super(TAFBecmgSegment, self).__init__()
        self.setupUi(self)
        self.name.setText(name)

        self.set_validator()

        # self.cavok.clicked.connect(self.set_cavok)
        # self.skc.clicked.connect(self.set_skc_nsc)
        # self.nsc.clicked.connect(self.set_skc_nsc)

        self.bind_signal()

    def set_validator(self):
        super(TAFBecmgSegment, self).set_validator()

        valid_interval = QtGui.QRegExpValidator(QtCore.QRegExp(self.rules.interval))
        self.interval.setValidator(valid_interval)

    def bind_signal(self):
        super(TAFBecmgSegment, self).bind_signal()

        self.interval.textChanged.connect(self.check_required)
        self.weather.currentIndexChanged.connect(self.check_required)
        self.weather_with_intensity.currentIndexChanged.connect(self.check_required)

    def message(self):
        super(TAFBecmgSegment, self).message()
        interval = self.interval.text()
        msg_list = ['BECMG', interval, self.msg]
        self.msg = ' '.join(msg_list)
        # logger.debug(self.msg)
        return self.msg

    def check_required(self):
        self.required = False
        one_required = (
            self.nsc.isChecked(), 
            self.skc.isChecked(),
            self.cavok.isChecked(), 
            self.wind.hasAcceptableInput(), 
            self.vis.hasAcceptableInput(), 
            self.weather.currentText(),
            self.weather_with_intensity.currentText(),
            self.cloud1.hasAcceptableInput(), 
            self.cloud2.hasAcceptableInput(), 
            self.cloud3.hasAcceptableInput(), 
            self.cb.hasAcceptableInput()
        )

        if self.interval.hasAcceptableInput() and any(one_required):
            self.required = True

        self.signal_required.emit(self.required)

    def clear(self):
        super(TAFBecmgSegment, self).clear()

        self.interval.clear()

        self.cavok.setChecked(False)
        self.skc.setChecked(False)
        self.nsc.setChecked(False)


class TAFTempoSegment(BaseSegment, Ui_taf_tempo.Ui_Form):

    def __init__(self, name='tempo'):
        super(TAFTempoSegment, self).__init__()
        self.setupUi(self)
        self.name.setText(name)

        self.set_validator()

        self.bind_signal()

    def set_validator(self):
        super(TAFTempoSegment, self).set_validator()

        valid_interval = QtGui.QRegExpValidator(QtCore.QRegExp(self.rules.interval))
        self.interval.setValidator(valid_interval)

    def bind_signal(self):
        super(TAFTempoSegment, self).bind_signal()

        self.interval.textChanged.connect(self.check_required)
        self.weather.currentIndexChanged.connect(self.check_required)
        self.weather_with_intensity.currentIndexChanged.connect(self.check_required)

    def message(self):
        super(TAFTempoSegment, self).message()
        interval = self.interval.text()
        msg_list = ['TEMPO', interval, self.msg]
        if self.prob30.isChecked():
            msg_list.insert(0, 'PROB30')
        if self.prob40.isChecked():
            msg_list.insert(0, 'PROB40')
        self.msg = ' '.join(msg_list)
        # logger.debug(self.msg)
        return self.msg

    def check_required(self):
        self.required = False
        one_required = (
            self.wind.hasAcceptableInput(), 
            self.vis.hasAcceptableInput(), 
            self.weather.currentText(),
            self.weather_with_intensity.currentText(),
            self.cloud1.hasAcceptableInput(), 
            self.cloud2.hasAcceptableInput(), 
            self.cloud3.hasAcceptableInput(), 
            self.cb.hasAcceptableInput()
        )

        if self.interval.hasAcceptableInput() and any(one_required):
            self.required = True

        self.signal_required.emit(self.required)

    def clear(self):
        super(TAFTempoSegment, self).clear()

        self.interval.clear()

        self.prob30.setChecked(False)
        self.prob40.setChecked(False)


class TrendSegment(BaseSegment, Ui_trend.Ui_Form):

    def __init__(self):
        super(TrendSegment, self).__init__()
        self.setupUi(self)
        self.set_validator()
        self.bind_signal()

    def bind_signal(self):
        super(TrendSegment, self).bind_signal()

        self.nosig.toggled.connect(self.set_nosig)
        self.at.toggled.connect(self.set_at)
        self.fm.toggled.connect(self.set_fm)
        self.tl.toggled.connect(self.set_tl)

        self.nosig.clicked.connect(self.check_required)
        self.at.clicked.connect(self.check_required)
        self.fm.clicked.connect(self.check_required)
        self.tl.clicked.connect(self.check_required)

    def set_validator(self):
        super(TrendSegment, self).set_validator()

        # 还未验证输入个数
        valid_period = QtGui.QRegExpValidator(QtCore.QRegExp(self.rules.interval))
        self.period.setValidator(valid_period)

    def set_nosig(self, checked):
        status = not checked

        self.group_prefix.setEnabled(status)
        self.group_type.setEnabled(status)

        self.period.setEnabled(status)
        self.wind.setEnabled(status)
        self.gust.setEnabled(status)
        self.vis.setEnabled(status)
        self.weather.setEnabled(status)
        self.weather_with_intensity.setEnabled(status)
        self.cloud1.setEnabled(status)
        self.cloud2.setEnabled(status)
        self.cloud3.setEnabled(status)
        self.cb.setEnabled(status)

        self.cavok.setEnabled(status)
        self.skc.setEnabled(status)
        self.nsc.setEnabled(status)


    def set_at(self, checked):
        if checked:
            self.fm.setChecked(False)
            self.tl.setChecked(False)
            self.period.setEnabled(True)
        else:
            self.period.setEnabled(False)

    def set_fm(self, checked):
        if checked:
            self.at.setChecked(False)
            self.tl.setChecked(False)
            self.period.setEnabled(True)
        else:
            self.period.setEnabled(False)

    def set_tl(self, checked):
        if checked:
            self.fm.setChecked(False)
            self.at.setChecked(False)
            self.period.setEnabled(True)
        else:
            self.period.setEnabled(False)

    def check_required(self):
        self.required = False
        one_required = (
            self.nsc.isChecked(), 
            self.skc.isChecked(),
            self.cavok.isChecked(), 
            self.wind.hasAcceptableInput(), 
            self.vis.hasAcceptableInput(), 
            self.weather.currentText(),
            self.weather_with_intensity.currentText(),
            self.cloud1.hasAcceptableInput(), 
            self.cloud2.hasAcceptableInput(), 
            self.cloud3.hasAcceptableInput(), 
            self.cb.hasAcceptableInput()
        )

        prefix_checked = (
            self.at.isChecked(),
            self.fm.isChecked(),
            self.tl.isChecked()
        )

        if self.nosig.isChecked():
            self.required = True

        if any(one_required):
            if any(prefix_checked):
                if self.period.hasAcceptableInput():
                    self.required = True
            else:
                self.required = True

        self.signal_required.emit(self.required)

    def message(self):
        super(TrendSegment, self).message()

        if self.nosig.isChecked():
            self.msg = 'NOSIG'
        else:
            msg_list = []

            if self.becmg.isChecked():
                trend_type = 'BECMG'
            if self.tempo.isChecked():
                trend_type = 'TEMPO'

            msg_list.append(trend_type)

            if any((self.at.isChecked(), self.fm.isChecked(), self.tl.isChecked())):
                if self.at.isChecked():
                    trend_prefix = 'AT'
                if self.fm.isChecked():
                    trend_prefix = 'FM'
                if self.tl.isChecked():
                    trend_prefix = 'TL'

                period = trend_prefix + self.period.text()
                msg_list.append(period)

            msg_list.append(self.msg)
            self.msg = ' '.join(msg_list)

        return self.msg

    def clear(self):
        super(TrendSegment, self).clear()

        self.at.setChecked(False)
        self.fm.setChecked(False)
        self.tl.setChecked(False)
        self.nosig.setChecked(False)

        self.cavok.setChecked(False)
        self.skc.setChecked(False)
        self.nsc.setChecked(False)

        self.period.setEnabled(False)
        self.period.clear()