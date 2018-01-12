#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""HTS221: Capacitive digital sensor for relative humidity and temperature."""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["ST Microelectronics"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

from HTS221_constants import *

# name:        HTS221
# description: Capacitive digital sensor for relative humidity and temperature.
# manuf:       ST Microelectronics
# version:     Version 0.1
# url:         http://www.st.com/resource/en/datasheet/hts221.pdf
# date:        2018-01-12


# Derive from this class and implement read and write
class HTS221_Base:
	"""Capacitive digital sensor for relative humidity and temperature."""
	# Register WHO_AM_I
	# 7.1
	#       Device identification. This read-only register contains the device identifier, set to BCh 
	
	
	def setWHO_AM_I(self, val):
		"""Set register WHO_AM_I"""
		self.write(REG.WHO_AM_I, val, 8)
	
	def getWHO_AM_I(self):
		"""Get register WHO_AM_I"""
		return self.read(REG.WHO_AM_I, 8)
	
	# Bits WHO_AM_I
	# Register AV_CONF
	# 7.2
	#       Humidity and temperature resolution mode. To configure humidity/temperature average. 
	# Table 16. Humidity and temperature average configuration
	#       |               Nr. internal  average            |    Noise (RMS)   | IDD 1 Hz |
	#       | AVGx2:0 | Temperature (AVGT) | Humidity (AVGH) | Temp (°C) | rH % |    μA    |
	#       | 000     |                  2 |               4 |      0.08 |  0.4 |     0.80 |
	#       | 001     |                  4 |               8 |      0.05 |  0.3 |     1.05 |
	#       | 010     |                  8 |              16 |      0.04 |  0.2 |     1.40 |
	#       | 011     |                 16 |              32 |      0.03 | 0.15 |     2.10 |
	#       | 100     |                 32 |              64 |      0.02 |  0.1 |     3.43 |
	#       | 101     |                 64 |             128 |     0.015 | 0.07 |     6.15 |
	#       | 110     |                128 |             256 |      0.01 | 0.05 |    11.60 |
	#       | 111     |                256 |             512 |     0.007 | 0.03 |    22.50 | 
	#     
	
	
	def setAV_CONF(self, val):
		"""Set register AV_CONF"""
		self.write(REG.AV_CONF, val, 8)
	
	def getAV_CONF(self):
		"""Get register AV_CONF"""
		return self.read(REG.AV_CONF, 8)
	
	# Bits reserved_0
	# Bits AVGT
	# To select the numbers of averaged temperature samples (2 - 256), see Table 16. 
	# Bits AVGH
	# To select the numbers of averaged humidity samples (4 - 512), see Table 16. 
	# Register CTRL_REG1
	# 7.3 
	#         Control register 1 
	
	
	def setCTRL_REG1(self, val):
		"""Set register CTRL_REG1"""
		self.write(REG.CTRL_REG1, val, 8)
	
	def getCTRL_REG1(self):
		"""Get register CTRL_REG1"""
		return self.read(REG.CTRL_REG1, 8)
	
	# Bits PD
	# power-down control 
	# Bits reserved_0
	# Bits BDU
	# block data update 
	# Bits ODR
	# output data rate selection (see table 17) 
	#             The PD bit is used to turn on the device. The device is in power-down mode when PD = ‘0’
	#             (default value after boot). The device is active when PD is set to ‘1’.
	#             The BDU bit is used to inhibit the output register update between the reading of the upper and lower register parts. In default mode (BDU = ‘0’), the lower and upper register parts are updated continuously. If it is not certain whether the read will be faster than output data rate, it is recommended to set the BDU bit to ‘1’. In this way, after the reading of the lower (upper) register part, the content of that output register is not updated until the upper (lower) part is read also.
	#             This feature prevents the reading of LSB and MSB related to different samples. The ODR1 and ODR0 bits permit changes to the output data rates of humidity and
	#             temperature samples.The default value corresponds to a “one-shot” configuration for both
	#             humidity and temperature output. ODR1 and ODR0 can be configured as described in
	#             Table 17. Output data rate configuration
	#             ODR1 ODR0  Humidity (Hz)  Temperature  (Hz)
	#             0       0       One-shot           One-shot          
	#             0       1           1 Hz               1 Hz
	#             1       0           7 Hz               7 Hz
	#             1       1        12.5 Hz            12.5 Hz 
	#         
	
	# Register CTRL_REG2
	# 7.4 
	#         Control register 2 
	
	
	def setCTRL_REG2(self, val):
		"""Set register CTRL_REG2"""
		self.write(REG.CTRL_REG2, val, 8)
	
	def getCTRL_REG2(self):
		"""Get register CTRL_REG2"""
		return self.read(REG.CTRL_REG2, 8)
	
	# Bits BOOT
	# Reboot memory content 
	#             The BOOT bit is used to refresh the content of the internal registers stored in the Flash
	#             memory block. At device power-up, the content of the Flash memory block is transferred to the internal registers related to trimming functions to permit good behavior of the device itself. If, for any reason, the content of the trimming registers is modified, it is sufficient to use this bit to restore the correct values. When the BOOT bit is set to ‘1’ the content of the internal Flash is copied inside the corresponding internal registers and is used to calibrate the device. These values are factory trimmed and are different for every device. They permit good behavior of the device and normally they should not be changed. At the end of the boot process, the BOOT bit is set again to ‘0’. 
	
	# Bits reserved_0
	# Bits Heater
	# The Heater bit is used to control an internal heating element, that can effectively be used to speed up the sensor recovery time in case of condensation. The heater can be operated only by an external controller, which means that it has to be switched on/off directly by FW. Humidity and temperature output should not be read during the heating cycle; valid data can be read out once the heater has been turned off, after the completion of the heating cycle. Typical power consumption related to VDD is described in Table 18. 
	#             Table 18. Typical power consumption with heater ON:
	#             VDD [V]   I [mA]
	#             3.3           33
	#             2.5	        22
	#             1.8	        12  
	#         
	
	# Bits ONE_SHOT_ENABLE
	# One-shot enable
	#             The ONE_SHOT bit is used to start a new conversion. In this situation a single acquisition of temperature and humidity is started when the ONE_SHOT bit is set to ‘1’. At the end of conversion the new data are available in the output registers, the STATUS_REGBIT 0 =  and STATUS_REGBIT 1 =  bits are set to ‘1’ and the ONE_SHOT bit comes back to ‘0’ by hardware. 
	
	# Register CTRL_REG3
	# 7.5 
	#         Control register 3: Control register for data ready output signal 
	
	
	def setCTRL_REG3(self, val):
		"""Set register CTRL_REG3"""
		self.write(REG.CTRL_REG3, val, 8)
	
	def getCTRL_REG3(self):
		"""Get register CTRL_REG3"""
		return self.read(REG.CTRL_REG3, 8)
	
	# Bits DRDY_H_L
	# Data Ready output signal active high, low 
	# Bits PP_OD
	# Push-pull / Open Drain selection on pin 3 (DRDY) 
	# Bits reserved_0
	# Bits DRDY_EN
	# Data Ready enable 
	#             The DRDY_EN bit enables the DRDY signal on pin 3. Normally inactive, the DRDY output
	#             signal becomes active on new data available: logical OR of the bits STATUS_REGBIT[1]
	#             and STATUS_REGBIT[0] for humidity and temperature, respectively. The DRDY signal returns
	#             inactive after both HUMIDITY_OUT_H and TEMP_OUT_H registers are read. 
	
	# Bits reserved_1
	# Register STATUS_REG
	# 7.6
	#       Status register; the content of this register is updated every one-shot reading, and after
	#       completion of every ODR cycle, regardless of the BDU value in CTRL_REG1. 
	
	
	def setSTATUS_REG(self, val):
		"""Set register STATUS_REG"""
		self.write(REG.STATUS_REG, val, 8)
	
	def getSTATUS_REG(self):
		"""Get register STATUS_REG"""
		return self.read(REG.STATUS_REG, 8)
	
	# Bits reserved_0
	# Bits H_DA
	# Humidity data available. 
	#           H_DA is set to 1 whenever a new humidity sample is available. H_DA is cleared anytime
	#           HUMIDITY_OUT_H (29h) register is read. 
	
	# Bits T_DA
	# Temperature data available. 
	#           T_DA is set to 1 whenever a new temperature sample is available. T_DA is cleared anytime TEMP_OUT_H (2Bh) register is read.
	#           Relative humidity data (LSB) 
	
	# Register HUMIDITY_OUT
	# 7.8
	#       Relative humidity data
	#       Humidity data are expressed as HUMIDITY_OUT_H & HUMIDITY_OUT_L in 2’s complement. Values exceeding the operating humidity range (see Table 3) must be clipped by SW. 
	
	
	def setHUMIDITY_OUT(self, val):
		"""Set register HUMIDITY_OUT"""
		self.write(REG.HUMIDITY_OUT, val, 16)
	
	def getHUMIDITY_OUT(self):
		"""Get register HUMIDITY_OUT"""
		return self.read(REG.HUMIDITY_OUT, 16)
	
	# Bits HUMIDITY_OUT
	# Register TEMP_OUT_L
	# 7.9
	#       Temperature data
	#       Temperature data are expressed as TEMP_OUT_H & TEMP_OUT_L as 2’s complement numbers.
	#       The relative humidity and temperature values must be computed by linear interpolation of current registers with calibration registers, according to Table 19 and scaling as described in Section 8. 
	
	
	def setTEMP_OUT_L(self, val):
		"""Set register TEMP_OUT_L"""
		self.write(REG.TEMP_OUT_L, val, 8)
	
	def getTEMP_OUT_L(self):
		"""Get register TEMP_OUT_L"""
		return self.read(REG.TEMP_OUT_L, 8)
	
	# Bits TEMP_OUT_L
