######################################################################################
#
# The University of Manchester
# Department of Chemical Engineering
#
# Chemical Engineering Summer Internship
#
# Year:    2023
# Project: Design and Operation of an Experimental Adsorption Rig for Gas Separation
# Python:  Python 3.11
# Author:  Agustinus Rio Sunardi
#
# Purpose:
# Function for Omega Temperature Probe to poll data
# The required files are picosdk.usbtc08 and picosdk.functions
# This code was built for Pico TC-08 USB Thermocouple Data Logger
# However, it has been modified to work with the Omega Temperature Probe and Omega TC-08 USB Thermocouple Data Logger
#
# Reference:
# https://github.com/picotech/picosdk-python-wrappers/blob/master/usbtc08Examples/tc08SingleModeExample.py
#
# Last Modified:
# Agustinus Rio Sunardi - 04/08/2021
#
# Input:
# Serial port connection
#
# Output:
# Temperature readings from Omega Temperature Probe
#
######################################################################################

def temperatureProbe():

    import ctypes
    import numpy as np
    from picosdk.usbtc08 import usbtc08 as tc08
    from picosdk.functions import assert_pico2000_ok
    import datetime

    # Create chandle and status ready for use
    chandle = ctypes.c_int16()
    status = {}

    # open unit
    status["open_unit"] = tc08.usb_tc08_open_unit()
    assert_pico2000_ok(status["open_unit"])
    chandle = status["open_unit"]

    # set mains rejection to 50 Hz
    status["set_mains"] = tc08.usb_tc08_set_mains(chandle,0)
    assert_pico2000_ok(status["set_mains"])

    # set up channel 6
    # therocouples types and int8 equivalent
    # B=66 , E=69 , J=74 , K=75 , N=78 , R=82 , S=83 , T=84 , ' '=32 , X=88 
    typeK = ctypes.c_int8(75)
    status["set_channel"] = tc08.usb_tc08_set_channel(chandle, 6, typeK)
    assert_pico2000_ok(status["set_channel"])

    # set up channel 5
    # therocouples types and int8 equivalent
    # B=66 , E=69 , J=74 , K=75 , N=78 , R=82 , S=83 , T=84 , ' '=32 , X=88 
    typeK = ctypes.c_int8(75)
    status["set_channel"] = tc08.usb_tc08_set_channel(chandle, 5, typeK)
    assert_pico2000_ok(status["set_channel"])

    # set up channel 4
    # therocouples types and int8 equivalent
    # B=66 , E=69 , J=74 , K=75 , N=78 , R=82 , S=83 , T=84 , ' '=32 , X=88 
    typeK = ctypes.c_int8(75)
    status["set_channel"] = tc08.usb_tc08_set_channel(chandle, 4, typeK)
    assert_pico2000_ok(status["set_channel"])

    # set up channel 3
    # therocouples types and int8 equivalent
    # B=66 , E=69 , J=74 , K=75 , N=78 , R=82 , S=83 , T=84 , ' '=32 , X=88 
    typeK = ctypes.c_int8(75)
    status["set_channel"] = tc08.usb_tc08_set_channel(chandle, 3, typeK)
    assert_pico2000_ok(status["set_channel"])

    # set up channel 2
    # therocouples types and int8 equivalent
    # B=66 , E=69 , J=74 , K=75 , N=78 , R=82 , S=83 , T=84 , ' '=32 , X=88 
    typeK = ctypes.c_int8(75)
    status["set_channel"] = tc08.usb_tc08_set_channel(chandle, 2, typeK)
    assert_pico2000_ok(status["set_channel"])

    # set up channel 1
    # therocouples types and int8 equivalent
    # B=66 , E=69 , J=74 , K=75 , N=78 , R=82 , S=83 , T=84 , ' '=32 , X=88 
    typeK = ctypes.c_int8(75)
    status["set_channel"] = tc08.usb_tc08_set_channel(chandle, 1, typeK)
    assert_pico2000_ok(status["set_channel"])

    # get minimum sampling interval in ms
    status["get_minimum_interval_ms"] = tc08.usb_tc08_get_minimum_interval_ms(chandle)
    assert_pico2000_ok(status["get_minimum_interval_ms"])

    # get single temperature reading
    temp = (ctypes.c_float * 9)()
    overflow = ctypes.c_int16(0)
    units = tc08.USBTC08_UNITS["USBTC08_UNITS_CENTIGRADE"]
    status["get_single"] = tc08.usb_tc08_get_single(chandle,ctypes.byref(temp), ctypes.byref(overflow), units)
    assert_pico2000_ok(status["get_single"])

    now = datetime.datetime.now()

    # temperature1 = temperature at the tip of the probe
    # temperature2 = temperature below the tip of the probe
    # temperature3 = temperature below temperature2
    # temperature4 = temperature below temperature3
    # temperature5 = temperature below temperature4
    # temperature6 = temperature below temperature5 and at the base of the probe

    temperature1 = temp[1]
    temperature2 = temp[2]
    temperature3 = temp[3]
    temperature4 = temp[4]
    temperature5 = temp[5]
    temperature6 = temp[6]

    status["close_unit"] = tc08.usb_tc08_close_unit(chandle)
    assert_pico2000_ok(status["close_unit"])

    # return temp
    return temperature1, temperature2, temperature3, temperature4, temperature5, temperature6

