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
# Function for Alica Mass Flow Controller and Mass Flow Meter
# Alicat Mass Flow Controller can receive commands to set a new setpoint or to poll data
# Alicat Mass Flow Meter can receive commands to poll data
# Both instruments can receive command to set new gas type
# The command to set a new setpoint is '{Instrument ID}S' followed by the setpoint in SLPM
# The command to set a new gas type is '{Instrument ID}G' followed by the gas ID
# The command to poll data is '{Instrument ID}' followed by a carriage return
#
# Reference:
# https://www.alicat.com/using-your-alicat/how-to-issue-serial-commands/
#
# Last Modified:
# Agustinus Rio Sunardi - 04/08/2021
#
# Input Arguments:
# Serial port connection
# Device ID
# Flow rate setpoint
# Gas ID
#
# Output Arguments:
# Flow rate readings from Alicat Mass Flow Controller and Mass Flow Meter
# New setpoint displayed on Alicat Mass Flow Controller panel
# New gas type displayed on Alicat Mass Flow Controller and Mass Flow Meter panel
# 
######################################################################################

def alicatInstruments(ser,command):

    import serial
    import time
    import datetime

    if command[1] == 'S' or command[1] == 'G':
        # Send command to set new setpoint
        ser.write(command.encode())  # Send the command
    else:      
        # Send command to poll data
        ser.write(command.encode())

        response=ser.readline()  # Read the response from the Alicat instrument

        # Convert the response to a vector of floating point values
        # Then just display the 4th value (which is the mass flow rate in SLPM)
        response1 = response.decode()  # Convert bytes to string
        response2 = response1.strip()  # Remove leading and trailing whitespace
        response3 = response2.split(' ')  # Split the string into a list of values
        response4 = list(response3)  # Convert the list of strings to a list of floats
        return response4[4]