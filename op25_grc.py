#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Op25 Grc
# Generated: Thu Mar  6 19:26:55 2014
##################################################

from baz import message_callback
from baz import op25
from gnuradio import audio
from gnuradio import blks2
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import ConfigParser
import baz
import math
import wx

class op25_grc(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Op25 Grc")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self._config_freq_config = ConfigParser.ConfigParser()
		self._config_freq_config.read(".grc_op25")
		try: config_freq = self._config_freq_config.getfloat("main", "freq")
		except: config_freq = 425504000
		self.config_freq = config_freq
		self.freq = freq = config_freq
		self._config_xlate_offset_config = ConfigParser.ConfigParser()
		self._config_xlate_offset_config.read(".grc_op25")
		try: config_xlate_offset = self._config_xlate_offset_config.getfloat("main", "xlate_offset")
		except: config_xlate_offset = 0
		self.config_xlate_offset = config_xlate_offset
		self.click_freq = click_freq = freq-config_xlate_offset
		self.xlate_offset_fine = xlate_offset_fine = 0
		self.xlate_offset = xlate_offset = freq-click_freq
		self.samp_rate = samp_rate = 1000000*1+250000*0
		self.samp_per_sym = samp_per_sym = 5+1
		self.decim = decim = 20
		self._config_xlate_bandwidth_config = ConfigParser.ConfigParser()
		self._config_xlate_bandwidth_config.read(".grc_op25")
		try: config_xlate_bandwidth = self._config_xlate_bandwidth_config.getfloat("main", "xlate_bandwidth")
		except: config_xlate_bandwidth = 24000
		self.config_xlate_bandwidth = config_xlate_bandwidth
		self.auto_tune_offset = auto_tune_offset = 0
		self.xlate_bandwidth = xlate_bandwidth = config_xlate_bandwidth
		self.variable_static_text_0 = variable_static_text_0 = freq+xlate_offset+xlate_offset_fine+auto_tune_offset
		self.pre_channel_rate = pre_channel_rate = samp_rate/decim
		self.gain = gain = 20
		self.fine_click_freq = fine_click_freq = 0
		self.channel_rate = channel_rate = op25.SYMBOL_RATE*samp_per_sym
		self.auto_tune_offset_freq = auto_tune_offset_freq = auto_tune_offset*op25.SYMBOL_DEVIATION
		self.audio_mul = audio_mul = 2

		##################################################
		# Message Queues
		##################################################
		op25_decoder_0_msgq_out = baz_message_callback_0_msgq_in = gr.msg_queue(2)

		##################################################
		# Blocks
		##################################################
		_xlate_offset_fine_sizer = wx.BoxSizer(wx.VERTICAL)
		self._xlate_offset_fine_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_xlate_offset_fine_sizer,
			value=self.xlate_offset_fine,
			callback=self.set_xlate_offset_fine,
			label="Fine Offset",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._xlate_offset_fine_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_xlate_offset_fine_sizer,
			value=self.xlate_offset_fine,
			callback=self.set_xlate_offset_fine,
			minimum=-10000,
			maximum=10000,
			num_steps=1000,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_xlate_offset_fine_sizer)
		self._xlate_offset_text_box = forms.text_box(
			parent=self.GetWin(),
			value=self.xlate_offset,
			callback=self.set_xlate_offset,
			label="Xlate Offset",
			converter=forms.float_converter(),
		)
		self.Add(self._xlate_offset_text_box)
		_xlate_bandwidth_sizer = wx.BoxSizer(wx.VERTICAL)
		self._xlate_bandwidth_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_xlate_bandwidth_sizer,
			value=self.xlate_bandwidth,
			callback=self.set_xlate_bandwidth,
			label="Xlate BW",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._xlate_bandwidth_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_xlate_bandwidth_sizer,
			value=self.xlate_bandwidth,
			callback=self.set_xlate_bandwidth,
			minimum=5000,
			maximum=50000,
			num_steps=1000,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_xlate_bandwidth_sizer)
		self.nb = self.nb = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
		self.nb.AddPage(grc_wxgui.Panel(self.nb), "BB-1")
		self.nb.AddPage(grc_wxgui.Panel(self.nb), "BB-2")
		self.nb.AddPage(grc_wxgui.Panel(self.nb), "Xlate-1")
		self.nb.AddPage(grc_wxgui.Panel(self.nb), "Xlate-2")
		self.nb.AddPage(grc_wxgui.Panel(self.nb), "4FSK")
		self.nb.AddPage(grc_wxgui.Panel(self.nb), "Dibits")
		self.Add(self.nb)
		_gain_sizer = wx.BoxSizer(wx.VERTICAL)
		self._gain_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_gain_sizer,
			value=self.gain,
			callback=self.set_gain,
			label="Gain",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._gain_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_gain_sizer,
			value=self.gain,
			callback=self.set_gain,
			minimum=0,
			maximum=50,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_gain_sizer)
		self._freq_text_box = forms.text_box(
			parent=self.GetWin(),
			value=self.freq,
			callback=self.set_freq,
			label="Frequency",
			converter=forms.float_converter(),
		)
		self.Add(self._freq_text_box)
		self._auto_tune_offset_freq_static_text = forms.static_text(
			parent=self.GetWin(),
			value=self.auto_tune_offset_freq,
			callback=self.set_auto_tune_offset_freq,
			label="Auto tune",
			converter=forms.float_converter(),
		)
		self.Add(self._auto_tune_offset_freq_static_text)
		_audio_mul_sizer = wx.BoxSizer(wx.VERTICAL)
		self._audio_mul_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_audio_mul_sizer,
			value=self.audio_mul,
			callback=self.set_audio_mul,
			label="Audio mul",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._audio_mul_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_audio_mul_sizer,
			value=self.audio_mul,
			callback=self.set_audio_mul,
			minimum=0,
			maximum=10,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_audio_mul_sizer)
		self.wxgui_waterfallsink2_0_0 = waterfallsink2.waterfall_sink_c(
			self.nb.GetPage(3).GetWin(),
			baseband_freq=0,
			dynamic_range=100,
			ref_level=50,
			ref_scale=2.0,
			sample_rate=channel_rate,
			fft_size=512,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="Waterfall Plot",
		)
		self.nb.GetPage(3).Add(self.wxgui_waterfallsink2_0_0.win)
		self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
			self.nb.GetPage(1).GetWin(),
			baseband_freq=freq,
			dynamic_range=100,
			ref_level=50,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=512,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="Waterfall Plot",
		)
		self.nb.GetPage(1).Add(self.wxgui_waterfallsink2_0.win)
		self.wxgui_scopesink2_1 = scopesink2.scope_sink_f(
			self.nb.GetPage(4).GetWin(),
			title="Scope Plot",
			sample_rate=channel_rate,
			v_scale=1.5,
			v_offset=0,
			t_scale=0.05,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.nb.GetPage(4).Add(self.wxgui_scopesink2_1.win)
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
			self.nb.GetPage(5).GetWin(),
			title="Scope Plot",
			sample_rate=op25.SYMBOL_RATE,
			v_scale=1,
			v_offset=0,
			t_scale=0.05,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.nb.GetPage(5).Add(self.wxgui_scopesink2_0.win)
		self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_c(
			self.nb.GetPage(2).GetWin(),
			baseband_freq=fine_click_freq,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=channel_rate,
			fft_size=1024,
			fft_rate=30,
			average=True,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
		)
		self.nb.GetPage(2).Add(self.wxgui_fftsink2_0_0.win)
		def wxgui_fftsink2_0_0_callback(x, y):
			self.set_fine_click_freq(x)
		
		self.wxgui_fftsink2_0_0.set_callback(wxgui_fftsink2_0_0_callback)
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
			self.nb.GetPage(0).GetWin(),
			baseband_freq=freq,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=1024,
			fft_rate=30,
			average=True,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
		)
		self.nb.GetPage(0).Add(self.wxgui_fftsink2_0.win)
		def wxgui_fftsink2_0_callback(x, y):
			self.set_click_freq(x)
		
		self.wxgui_fftsink2_0.set_callback(wxgui_fftsink2_0_callback)
		self._variable_static_text_0_static_text = forms.static_text(
			parent=self.GetWin(),
			value=self.variable_static_text_0,
			callback=self.set_variable_static_text_0,
			label="Final freq",
			converter=forms.float_converter(),
		)
		self.Add(self._variable_static_text_0_static_text)
		self.rtl2832_source_0 = baz.rtl_source_c(defer_creation=True, output_size=gr.sizeof_gr_complex)
		self.rtl2832_source_0.set_verbose(True)
		self.rtl2832_source_0.set_vid(0x0)
		self.rtl2832_source_0.set_pid(0x0)
		self.rtl2832_source_0.set_tuner_name("")
		self.rtl2832_source_0.set_default_timeout(0)
		self.rtl2832_source_0.set_use_buffer(True)
		self.rtl2832_source_0.set_fir_coefficients(([]))
		
		self.rtl2832_source_0.set_read_length(1024*128*2)
		
		
		
		
		if self.rtl2832_source_0.create() == False: raise Exception("Failed to create RTL2832 Source: rtl2832_source_0")
		
		
		self.rtl2832_source_0.set_sample_rate(samp_rate)
		
		self.rtl2832_source_0.set_frequency(freq)
		
		
		
		self.rtl2832_source_0.set_auto_gain_mode(False)
		self.rtl2832_source_0.set_relative_gain(True)
		self.rtl2832_source_0.set_gain(gain)
		  
		self.op25_decoder_0 = op25.op25_decoder(channel_rate=channel_rate, defer_creation=True, output_dibits=True, key="")
		self.op25_decoder_0.auto_tune_msgq = op25_decoder_0_msgq_out
		self.op25_decoder_0.create()
		self.gr_quadrature_demod_cf_0 = gr.quadrature_demod_cf((channel_rate/(2.0 * math.pi * op25.SYMBOL_DEVIATION)))
		self.gr_multiply_const_vxx_0 = gr.multiply_const_vff((audio_mul, ))
		self.gr_freq_xlating_fir_filter_xxx_0 = gr.freq_xlating_fir_filter_ccc(decim, (firdes.low_pass(1, samp_rate, xlate_bandwidth/2, 1000)), xlate_offset+xlate_offset_fine-fine_click_freq-auto_tune_offset_freq, samp_rate)
		self.gr_fir_filter_xxx_0 = gr.fir_filter_fff(1, ((1.0/samp_per_sym,)*samp_per_sym))
		self.blks2_rational_resampler_xxx_1 = blks2.rational_resampler_ccc(
			interpolation=channel_rate,
			decimation=pre_channel_rate,
			taps=None,
			fractional_bw=None,
		)
		self.blks2_rational_resampler_xxx_0 = blks2.rational_resampler_fff(
			interpolation=44100,
			decimation=8000,
			taps=None,
			fractional_bw=None,
		)
		self.baz_message_callback_0 = message_callback.message_callback(msgq=baz_message_callback_0_msgq_in,	callback=self.set_auto_tune_offset, msg_part="arg1", custom_parts="", dummy=False)
			
		self.audio_sink_0 = audio.sink(44100, "", True)

		##################################################
		# Connections
		##################################################
		self.connect((self.rtl2832_source_0, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.rtl2832_source_0, 0), (self.wxgui_waterfallsink2_0, 0))
		self.connect((self.gr_freq_xlating_fir_filter_xxx_0, 0), (self.blks2_rational_resampler_xxx_1, 0))
		self.connect((self.blks2_rational_resampler_xxx_1, 0), (self.wxgui_fftsink2_0_0, 0))
		self.connect((self.blks2_rational_resampler_xxx_1, 0), (self.wxgui_waterfallsink2_0_0, 0))
		self.connect((self.blks2_rational_resampler_xxx_1, 0), (self.gr_quadrature_demod_cf_0, 0))
		self.connect((self.gr_quadrature_demod_cf_0, 0), (self.gr_fir_filter_xxx_0, 0))
		self.connect((self.gr_fir_filter_xxx_0, 0), (self.op25_decoder_0, 0))
		self.connect((self.blks2_rational_resampler_xxx_0, 0), (self.gr_multiply_const_vxx_0, 0))
		self.connect((self.gr_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
		self.connect((self.op25_decoder_0, 1), (self.wxgui_scopesink2_0, 0))
		self.connect((self.gr_fir_filter_xxx_0, 0), (self.wxgui_scopesink2_1, 0))
		self.connect((self.op25_decoder_0, 0), (self.blks2_rational_resampler_xxx_0, 0))
		self.connect((self.rtl2832_source_0, 0), (self.gr_freq_xlating_fir_filter_xxx_0, 0))

	def get_config_freq(self):
		return self.config_freq

	def set_config_freq(self, config_freq):
		self.config_freq = config_freq
		self.set_freq(self.config_freq)

	def get_freq(self):
		return self.freq

	def set_freq(self, freq):
		self.freq = freq
		self.set_variable_static_text_0(self.freq+self.xlate_offset+self.xlate_offset_fine+self.auto_tune_offset)
		self._freq_text_box.set_value(self.freq)
		self.set_xlate_offset(self.freq-self.click_freq)
		self.set_click_freq(self.freq-self.config_xlate_offset)
		self.wxgui_waterfallsink2_0.set_baseband_freq(self.freq)
		self.wxgui_fftsink2_0.set_baseband_freq(self.freq)
		self.rtl2832_source_0.set_frequency(self.freq)
		self._config_freq_config = ConfigParser.ConfigParser()
		self._config_freq_config.read(".grc_op25")
		if not self._config_freq_config.has_section("main"):
			self._config_freq_config.add_section("main")
		self._config_freq_config.set("main", "freq", str(self.freq))
		self._config_freq_config.write(open(".grc_op25", 'w'))

	def get_config_xlate_offset(self):
		return self.config_xlate_offset

	def set_config_xlate_offset(self, config_xlate_offset):
		self.config_xlate_offset = config_xlate_offset
		self.set_click_freq(self.freq-self.config_xlate_offset)

	def get_click_freq(self):
		return self.click_freq

	def set_click_freq(self, click_freq):
		self.click_freq = click_freq
		self.set_xlate_offset(self.freq-self.click_freq)

	def get_xlate_offset_fine(self):
		return self.xlate_offset_fine

	def set_xlate_offset_fine(self, xlate_offset_fine):
		self.xlate_offset_fine = xlate_offset_fine
		self._config_xlate_offset_config = ConfigParser.ConfigParser()
		self._config_xlate_offset_config.read(".grc_op25")
		if not self._config_xlate_offset_config.has_section("main"):
			self._config_xlate_offset_config.add_section("main")
		self._config_xlate_offset_config.set("main", "xlate_offset", str(self.xlate_offset+self.xlate_offset_fine))
		self._config_xlate_offset_config.write(open(".grc_op25", 'w'))
		self.set_variable_static_text_0(self.freq+self.xlate_offset+self.xlate_offset_fine+self.auto_tune_offset)
		self._xlate_offset_fine_slider.set_value(self.xlate_offset_fine)
		self._xlate_offset_fine_text_box.set_value(self.xlate_offset_fine)
		self.gr_freq_xlating_fir_filter_xxx_0.set_center_freq(self.xlate_offset+self.xlate_offset_fine-self.fine_click_freq-self.auto_tune_offset_freq)

	def get_xlate_offset(self):
		return self.xlate_offset

	def set_xlate_offset(self, xlate_offset):
		self.xlate_offset = xlate_offset
		self._config_xlate_offset_config = ConfigParser.ConfigParser()
		self._config_xlate_offset_config.read(".grc_op25")
		if not self._config_xlate_offset_config.has_section("main"):
			self._config_xlate_offset_config.add_section("main")
		self._config_xlate_offset_config.set("main", "xlate_offset", str(self.xlate_offset+self.xlate_offset_fine))
		self._config_xlate_offset_config.write(open(".grc_op25", 'w'))
		self.set_variable_static_text_0(self.freq+self.xlate_offset+self.xlate_offset_fine+self.auto_tune_offset)
		self._xlate_offset_text_box.set_value(self.xlate_offset)
		self.gr_freq_xlating_fir_filter_xxx_0.set_center_freq(self.xlate_offset+self.xlate_offset_fine-self.fine_click_freq-self.auto_tune_offset_freq)

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.set_pre_channel_rate(self.samp_rate/self.decim)
		self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate)
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
		self.gr_freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1, self.samp_rate, self.xlate_bandwidth/2, 1000)))
		self.rtl2832_source_0.set_sample_rate(self.samp_rate)

	def get_samp_per_sym(self):
		return self.samp_per_sym

	def set_samp_per_sym(self, samp_per_sym):
		self.samp_per_sym = samp_per_sym
		self.set_channel_rate(op25.SYMBOL_RATE*self.samp_per_sym)
		self.gr_fir_filter_xxx_0.set_taps(((1.0/self.samp_per_sym,)*self.samp_per_sym))

	def get_decim(self):
		return self.decim

	def set_decim(self, decim):
		self.decim = decim
		self.set_pre_channel_rate(self.samp_rate/self.decim)

	def get_config_xlate_bandwidth(self):
		return self.config_xlate_bandwidth

	def set_config_xlate_bandwidth(self, config_xlate_bandwidth):
		self.config_xlate_bandwidth = config_xlate_bandwidth
		self.set_xlate_bandwidth(self.config_xlate_bandwidth)

	def get_auto_tune_offset(self):
		return self.auto_tune_offset

	def set_auto_tune_offset(self, auto_tune_offset):
		self.auto_tune_offset = auto_tune_offset
		self.set_variable_static_text_0(self.freq+self.xlate_offset+self.xlate_offset_fine+self.auto_tune_offset)
		self.set_auto_tune_offset_freq(self.auto_tune_offset*op25.SYMBOL_DEVIATION)

	def get_xlate_bandwidth(self):
		return self.xlate_bandwidth

	def set_xlate_bandwidth(self, xlate_bandwidth):
		self.xlate_bandwidth = xlate_bandwidth
		self._xlate_bandwidth_slider.set_value(self.xlate_bandwidth)
		self._xlate_bandwidth_text_box.set_value(self.xlate_bandwidth)
		self.gr_freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1, self.samp_rate, self.xlate_bandwidth/2, 1000)))
		self._config_xlate_bandwidth_config = ConfigParser.ConfigParser()
		self._config_xlate_bandwidth_config.read(".grc_op25")
		if not self._config_xlate_bandwidth_config.has_section("main"):
			self._config_xlate_bandwidth_config.add_section("main")
		self._config_xlate_bandwidth_config.set("main", "xlate_bandwidth", str(self.xlate_bandwidth))
		self._config_xlate_bandwidth_config.write(open(".grc_op25", 'w'))

	def get_variable_static_text_0(self):
		return self.variable_static_text_0

	def set_variable_static_text_0(self, variable_static_text_0):
		self.variable_static_text_0 = variable_static_text_0
		self._variable_static_text_0_static_text.set_value(self.variable_static_text_0)

	def get_pre_channel_rate(self):
		return self.pre_channel_rate

	def set_pre_channel_rate(self, pre_channel_rate):
		self.pre_channel_rate = pre_channel_rate

	def get_gain(self):
		return self.gain

	def set_gain(self, gain):
		self.gain = gain
		self._gain_slider.set_value(self.gain)
		self._gain_text_box.set_value(self.gain)
		self.rtl2832_source_0.set_gain(self.gain)

	def get_fine_click_freq(self):
		return self.fine_click_freq

	def set_fine_click_freq(self, fine_click_freq):
		self.fine_click_freq = fine_click_freq
		self.wxgui_fftsink2_0_0.set_baseband_freq(self.fine_click_freq)
		self.gr_freq_xlating_fir_filter_xxx_0.set_center_freq(self.xlate_offset+self.xlate_offset_fine-self.fine_click_freq-self.auto_tune_offset_freq)

	def get_channel_rate(self):
		return self.channel_rate

	def set_channel_rate(self, channel_rate):
		self.channel_rate = channel_rate
		self.gr_quadrature_demod_cf_0.set_gain((self.channel_rate/(2.0 * math.pi * op25.SYMBOL_DEVIATION)))
		self.wxgui_scopesink2_1.set_sample_rate(self.channel_rate)
		self.wxgui_waterfallsink2_0_0.set_sample_rate(self.channel_rate)
		self.wxgui_fftsink2_0_0.set_sample_rate(self.channel_rate)

	def get_auto_tune_offset_freq(self):
		return self.auto_tune_offset_freq

	def set_auto_tune_offset_freq(self, auto_tune_offset_freq):
		self.auto_tune_offset_freq = auto_tune_offset_freq
		self._auto_tune_offset_freq_static_text.set_value(self.auto_tune_offset_freq)
		self.gr_freq_xlating_fir_filter_xxx_0.set_center_freq(self.xlate_offset+self.xlate_offset_fine-self.fine_click_freq-self.auto_tune_offset_freq)

	def get_audio_mul(self):
		return self.audio_mul

	def set_audio_mul(self, audio_mul):
		self.audio_mul = audio_mul
		self._audio_mul_slider.set_value(self.audio_mul)
		self._audio_mul_text_box.set_value(self.audio_mul)
		self.gr_multiply_const_vxx_0.set_k((self.audio_mul, ))

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = op25_grc()
	tb.Run(True)

