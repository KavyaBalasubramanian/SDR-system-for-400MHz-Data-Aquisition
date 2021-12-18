#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Jul  5 12:13:14 2017
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

from datetime import datetime
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import threading
import time
import writeFile as wf
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.func_probe = func_probe = 0
        self.writeProbe = writeProbe = 0
        self.writeFile = writeFile = wf

        ##Change the sampling rate here
        self.samp_rate = samp_rate = 250e3


        self.ComplexValue = ComplexValue = func_probe

        ##################################################
        # Blocks
        ##################################################
        self.probe = blocks.probe_signal_c()
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_0.win)
        
        def _writeProbe_probe():
            while True:
                val = self.writeFile.write(self.probe.level())
                try:
                    self.set_writeProbe(val)
                except AttributeError:
                    pass
                ##Change the Polling Rate Here i.e No.Of data Points to be acquired every second
                time.sleep(1.0 / (20))
        _writeProbe_thread = threading.Thread(target=_writeProbe_probe)
        _writeProbe_thread.daemon = True
        _writeProbe_thread.start()
            
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)

        ##Change the Center Frequency Here
        self.osmosdr_source_0.set_center_freq(400e6, 0)

        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)

        ##Set the Gain Source Here
        self.osmosdr_source_0.set_gain(10, 0)

        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        
        def _func_probe_probe():
            while True:
                val = self.probe.level()
                try:
                    self.set_func_probe(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (20))
        _func_probe_thread = threading.Thread(target=_func_probe_probe)
        _func_probe_thread.daemon = True
        _func_probe_thread.start()
            
        self._ComplexValue_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.ComplexValue,
        	callback=self.set_ComplexValue,
        	label='ComplexValue',
        	converter=forms.str_converter(),
        )
        self.Add(self._ComplexValue_text_box)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.osmosdr_source_0, 0), (self.probe, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.wxgui_scopesink2_0, 0))    

    def get_func_probe(self):
        return self.func_probe

    def set_func_probe(self, func_probe):
        self.func_probe = func_probe
        self.set_ComplexValue(self.func_probe)

    def get_writeProbe(self):
        return self.writeProbe

    def set_writeProbe(self, writeProbe):
        self.writeProbe = writeProbe

    def get_writeFile(self):
        return self.writeFile

    def set_writeFile(self, writeFile):
        self.writeFile = writeFile

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_ComplexValue(self):
        return self.ComplexValue

    def set_ComplexValue(self, ComplexValue):
        self.ComplexValue = ComplexValue
        self._ComplexValue_text_box.set_value(self.ComplexValue)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
