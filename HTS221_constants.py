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

class REG:
	WHO_AM_I = 15
	AV_CONF = 16
	CTRL_REG1 = 32
	CTRL_REG2 = 33
	CTRL_REG3 = 34
	STATUS_REG = 39
	HUMIDITY_OUT = 41
	TEMP_OUT_L = 42
