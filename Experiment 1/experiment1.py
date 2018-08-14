#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: IEEE 802.15.4 Transceiver using OQPSK PHY
# Generated: Mon Aug 13 15:21:07 2018
# GNU Radio version: 3.7.12.0
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))
from optparse import OptionParser

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot,QTimer
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from input_chain import input_chain  # grc-generated hier_block
from optparse import OptionParser
from output_chain import output_chain  # grc-generated hier_block
import foo
import ieee802_15_4
import limesdr
import sip
from gnuradio import qtgui


class transceiver_OQPSK(gr.top_block, Qt.QWidget):

    def __init__(self):
        parser = OptionParser()
        parser.add_option("--length", type="int", dest="length", help="MAC payload length(1-112)", default="10")
        parser.add_option("--rate", type="float", dest="rate", help="Tx and Rx sample rate", default=4e6)
        parser.add_option("--period", type="int", dest="period", help="Message Source Period", default=500)
        (options, args) = parser.parse_args()


        gr.top_block.__init__(self, "IEEE 802.15.4 Transceiver using OQPSK PHY")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("IEEE 802.15.4 Transceiver using OQPSK PHY")
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

        self.settings = Qt.QSettings("GNU Radio", "transceiver_OQPSK")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.tx_gain = tx_gain = 0.75
        self.samp_rate = samp_rate = options.rate
        self.rx_gain = rx_gain = 0.75


        self.freq = freq = 2480000000

        ##################################################
        # Blocks
        ##################################################
        self._tx_gain_range = Range(0, 1, 0.01, 0.75, 200)
        self._tx_gain_win = RangeWidget(self._tx_gain_range, self.set_tx_gain, "tx_gain", "counter_slider", float)
        self.top_grid_layout.addWidget(self._tx_gain_win)
        self._rx_gain_range = Range(0, 1, 0.01, 0.75, 200)
        self._rx_gain_win = RangeWidget(self._rx_gain_range, self.set_rx_gain, "rx_gain", "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_gain_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	4e6, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.output_chain_0 = output_chain(
            samp_rate=samp_rate,
        )
        self.limesdr_source_0_0 = limesdr.source(0,
        			 2,
        			 1,
        			 0,
        			 0,
        			 '/home/saptarshi/Documents/MasterThesis@RISE/lime-gnuradio/src/limesuite/build/example',
        			 2.48e9,
        			 samp_rate,
        			 0,
        			 1,
        			 samp_rate,
        			 0,
        			 10e6,
        			 1,
        			 2,
        			 1,
        			 1,
        			 5e6 + samp_rate%5e6 *int( samp_rate/5e6),
        			 0,
        			 10e6,
        			 0,
        			 samp_rate,
        			 0,
        			 0,
        			 60,
        			 60)
        self.limesdr_sink_1 = limesdr.sink(0,
        		       2,
        		       1,
        		       0,
        		       0,
        		       '',
        		       2.48e9,
        		       samp_rate,
        		       0,
        		       1,
        		       samp_rate,
        		       0,
        		       10e6,
        		       1,
        		       2,
        		       1,
        		       1,
        		       5e6 + samp_rate%5e6 *int( samp_rate/5e6),
        		       0,
        		       10e6,
        		       0,
        		       4e6,
        		       0,
        		       0,
        		       60,
        		       60)
        self.input_chain_0 = input_chain(
            omega=samp_rate/2e6,
        )
        self.ieee802_15_4_rime_stack_0 = ieee802_15_4.rime_stack(([129]), ([131]), ([132]), ([23,42]))
        self.ieee802_15_4_mac_0 = ieee802_15_4.mac(False,0x8841,0,0x1aaa,0xffff,0x3344)
        self._freq_options = [1000000 * (2400 + 5 * (i - 10)) for i in range(11, 27)]
        self._freq_labels = [str(i) for i in range(11, 27)]
        self._freq_tool_bar = Qt.QToolBar(self)
        self._freq_tool_bar.addWidget(Qt.QLabel('Channel'+": "))
        self._freq_combo_box = Qt.QComboBox()
        self._freq_tool_bar.addWidget(self._freq_combo_box)
        for label in self._freq_labels: self._freq_combo_box.addItem(label)
        self._freq_callback = lambda i: Qt.QMetaObject.invokeMethod(self._freq_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._freq_options.index(i)))
        self._freq_callback(self.freq)
        self._freq_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_freq(self._freq_options[i]))
        self.top_grid_layout.addWidget(self._freq_tool_bar)
        self.foo_rtt_0 = foo.rtt(options.period,options.length)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/tmp/timings', False)
        self.blocks_file_sink_0_0.set_unbuffered(True)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.foo_rtt_0, 'out'), (self.ieee802_15_4_rime_stack_0, 'bcin'))
        self.msg_connect((self.ieee802_15_4_mac_0, 'app out'), (self.ieee802_15_4_rime_stack_0, 'fromMAC'))
        self.msg_connect((self.ieee802_15_4_mac_0, 'pdu out'), (self.output_chain_0, 'txin'))
        self.msg_connect((self.ieee802_15_4_rime_stack_0, 'bcout'), (self.foo_rtt_0, 'in'))
        self.msg_connect((self.ieee802_15_4_rime_stack_0, 'toMAC'), (self.ieee802_15_4_mac_0, 'app in'))
        self.msg_connect((self.input_chain_0, 'rxout'), (self.ieee802_15_4_mac_0, 'pdu in'))
        self.connect((self.foo_rtt_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.limesdr_source_0_0, 0), (self.input_chain_0, 0))
        #self.connect((self.limesdr_source_0_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.output_chain_0, 0), (self.limesdr_sink_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "transceiver_OQPSK")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.output_chain_0.set_samp_rate(self.samp_rate)
        self.input_chain_0.set_omega(self.samp_rate/2e6)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_callback(self.freq)


def main(top_block_cls=transceiver_OQPSK, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    def quitting():
        tb.stop()
        tb.wait()
        
    timer= QTimer()
    timer.timeout.connect(quitting);
    timer.setSingleShot(True)
    tb = top_block_cls()
    tb.start()
    timer.start(100000)
    tb.show()

    
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
