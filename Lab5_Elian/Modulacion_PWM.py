#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Modulacion_PWM
# Author: Elian-ciee
# Copyright: ciee-e3t
# GNU Radio version: 3.9.5.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import ModulosEfren



from gnuradio import qtgui

class Modulacion_PWM(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Modulacion_PWM", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Modulacion_PWM")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Modulacion_PWM")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.fm = fm = 1000
        self.samp_rate = samp_rate = 1e6
        self.offset = offset = 0
        self.f_saw = f_saw = 10*fm
        self.Amplitud_Saw_tooth = Amplitud_Saw_tooth = 1

        ##################################################
        # Blocks
        ##################################################
        self._offset_range = Range(-5, 5, 0.01, 0, 200)
        self._offset_win = RangeWidget(self._offset_range, self.set_offset, "nivel offset diente de sierra", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._offset_win)
        self._Amplitud_Saw_tooth_range = Range(0, 10, 0.01, 1, 200)
        self._Amplitud_Saw_tooth_win = RangeWidget(self._Amplitud_Saw_tooth_range, self.set_Amplitud_Saw_tooth, "Amplitud_Saw_tooth", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Amplitud_Saw_tooth_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024*2, #size
            samp_rate, #samp_rate
            "", #name
            3, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, f_saw, 2*Amplitud_Saw_tooth, -Amplitud_Saw_tooth +offset, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, fm, 1, 0, 0)
        self.ModulosEfren_Compara_0 = ModulosEfren.Compara()


        ##################################################
        # Connections
        ##################################################
        self.connect((self.ModulosEfren_Compara_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.analog_sig_source_x_0, 0), (self.ModulosEfren_Compara_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.ModulosEfren_Compara_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Modulacion_PWM")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_fm(self):
        return self.fm

    def set_fm(self, fm):
        self.fm = fm
        self.set_f_saw(10*self.fm)
        self.analog_sig_source_x_0.set_frequency(self.fm)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self.analog_sig_source_x_0_0.set_offset(-self.Amplitud_Saw_tooth +self.offset)

    def get_f_saw(self):
        return self.f_saw

    def set_f_saw(self, f_saw):
        self.f_saw = f_saw
        self.analog_sig_source_x_0_0.set_frequency(self.f_saw)

    def get_Amplitud_Saw_tooth(self):
        return self.Amplitud_Saw_tooth

    def set_Amplitud_Saw_tooth(self, Amplitud_Saw_tooth):
        self.Amplitud_Saw_tooth = Amplitud_Saw_tooth
        self.analog_sig_source_x_0_0.set_amplitude(2*self.Amplitud_Saw_tooth)
        self.analog_sig_source_x_0_0.set_offset(-self.Amplitud_Saw_tooth +self.offset)




def main(top_block_cls=Modulacion_PWM, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
