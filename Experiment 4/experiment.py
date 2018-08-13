#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: IEEE 802.15.4 Transceiver using OQPSK PHY
# Generated: Mon Jul 16 14:43:14 2018
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
import subprocess
import threading


pid=os.getpid()
f=open("/tmp/raw_data_file","w")
# subprocess.Popen(["pidstat","-hruv","-p",str(pid),"1","100"], stdout=f)

def popenAndCall(quitting, popenArgs):
    """
    Runs the given args in a subprocess.Popen, and then calls the function
    onExit when the subprocess completes.
    onExit is a callable object, and popenArgs is a list/tuple of args that 
    would give to subprocess.Popen.
    """
    def runInThread(quitting, popenArgs):
        proc = subprocess.Popen(*popenArgs, stdout=f)
        proc.wait()
        quitting()
        return
    thread = threading.Thread(target=runInThread, args=(quitting, [popenArgs]))
    thread.start()
    # returns immediately after the thread starts
    return thread

# def onExit(quitting):
#     print "done"
#     quitting()
#     os.system("echo 'Time:UID:PID:%usr:%system:%guest:%CPU:CPU:minflt/s:majflt/s:VSZ:RSS:%MEM:threads:fd-nr:Command' > /tmp/nice_data_file.csv")
#     os.system("sed '1d;/^[#]/d;/^$/d;s/^[ ]*//;s/[ ]\+/:/g;s/,/./g' /tmp/raw_data_file >> /tmp/nice_data_file.csv")
    


sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from ieee802_15_4_oqpsk_phy import ieee802_15_4_oqpsk_phy  # grc-generated hier_block
from optparse import OptionParser
import foo
import ieee802_15_4
import limesdr
import sip
from gnuradio import qtgui





class transceiver_OQPSK(gr.top_block, Qt.QWidget):

    def __init__(self):
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
        self.qtgui_sink_x_1 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	4e6, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        #self.qtgui_sink_x_1.set_update_time(1.0/10)
        #self._qtgui_sink_x_1_win = sip.wrapinstance(self.qtgui_sink_x_1.pyqwidget(), Qt.QWidget)
        #self.top_grid_layout.addWidget(self._qtgui_sink_x_1_win)

        #self.qtgui_sink_x_1.enable_rf_freq(False)



        self.limesdr_source_0_0 = limesdr.source(0,
        			 2,
        			 1,
        			 0,
        			 0,
        			 '/home/saptarshi/Documents/MasterThesis@RISE/lime-gnuradio/src/limesuite/build/example',
        			 2.48e9,
        			 4e6,
        			 0,
        			 1,
        			 4e6,
        			 0,
        			 10e6,
        			 1,
        			 2,
        			 1,
        			 1,
        			 4e6,
        			 0,
        			 10e6,
        			 1,
        			 4e6,
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
        		       4e6,
        		       0,
        		       1,
        		       4e6,
        		       0,
        		       10e6,
        		       1,
        		       2,
        		       1,
        		       0,
        		       5e6,
        		       0,
        		       10e6,
        		       0,
        		       4e6,
        		       0,
        		       0,
        		       60,
        		       60)
        self.ieee802_15_4_rime_stack_0 = ieee802_15_4.rime_stack(([129]), ([131]), ([132]), ([23,42]))
        self.ieee802_15_4_oqpsk_phy_0 = ieee802_15_4_oqpsk_phy()
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
        self.foo_rtt_0 = foo.rtt(500,10)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/tmp/timings', False)
        self.blocks_file_sink_0_0.set_unbuffered(True)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.foo_rtt_0, 'out'), (self.ieee802_15_4_rime_stack_0, 'bcin'))
        self.msg_connect((self.ieee802_15_4_mac_0, 'pdu out'), (self.ieee802_15_4_oqpsk_phy_0, 'txin'))
        self.msg_connect((self.ieee802_15_4_mac_0, 'app out'), (self.ieee802_15_4_rime_stack_0, 'fromMAC'))
        self.msg_connect((self.ieee802_15_4_oqpsk_phy_0, 'rxout'), (self.ieee802_15_4_mac_0, 'pdu in'))
        self.msg_connect((self.ieee802_15_4_rime_stack_0, 'bcout'), (self.foo_rtt_0, 'in'))
        self.msg_connect((self.ieee802_15_4_rime_stack_0, 'toMAC'), (self.ieee802_15_4_mac_0, 'app in'))
        self.connect((self.foo_rtt_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.ieee802_15_4_oqpsk_phy_0, 0), (self.limesdr_sink_1, 0))
        self.connect((self.limesdr_source_0_0, 0), (self.ieee802_15_4_oqpsk_phy_0, 0))
        #self.connect((self.limesdr_source_0_0, 0), (self.qtgui_sink_x_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "transceiver_OQPSK")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain

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

    tb = top_block_cls()
    def quitting():
        print "done"
        os.system("echo 'Time:UID:PID:%usr:%system:%guest:%CPU:CPU:minflt/s:majflt/s:VSZ:RSS:%MEM:cswitch/s:nvcswitch/s:threads:fd-nr:Command' > /tmp/nice_data_file.csv")
        os.system("sed '1d;/^[#]/d;/^$/d;s/^[ ]*//;s/[ ]\+/:/g;s/,/./g' /tmp/raw_data_file >> /tmp/nice_data_file.csv")
        tb.stop()
        tb.wait()

    popenAndCall(quitting,["pidstat","-hruvw","-p",str(pid),"1","100"])
    tb.start(2000)
    tb.show()

    
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
