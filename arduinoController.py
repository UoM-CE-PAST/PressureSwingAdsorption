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
# This Python code is paired with an Arduino code that is uploaded to the Arduino Uno. 
# The Arduino code is responsible for controlling the valves
#
# Reference:
#
# Last Modified:
# Agustinus Rio Sunardi - 04/08/2021
#
# Input Arguments:
# Cycle duration (list of durations for each process in an Adsorption cycle)
# Number of cycles
# Read data (True or False)
#
# Output Arguments:
# Data from Arduino
#
######################################################################################



import time
import csv

def arduinoController(serialArduino, **kwargs):
    if 'cycleDuration' in kwargs:
        durations_list = kwargs['cycleDuration']
    if 'numCycles' in kwargs:
        num_loops = kwargs['numCycles']      
    if 'readData' in kwargs:
        readData = kwargs['readData']

    # Send the data to the Arduino
    if 'cycleDuration' in kwargs and 'numCycles' in kwargs:
        # Convert the list of durations (for each process in an Adsorption cycle) and number of loops to a comma-separated string
        data_string = ",".join(str(duration) for duration in durations_list)
        data_string += f",{num_loops}"

        # Send the data string to the Arduino
        serialArduino.write(data_string.encode())

        return

    # Read the data coming out from the Arduino
    if 'readData' in kwargs and readData == True:
        with open('data5.csv', 'w', newline='') as csvfile:

            fieldnames = ['Time', 'Valve 1', 'Valve 2', 'Valve 3', 'Valve 4']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader() 
        
            # Read the string coming out from the Arduino
            while readData == True:              
                msgfromArduino=serialArduino.readline()
                msgfromArduino1=msgfromArduino.decode()
                msgfromArduino2=msgfromArduino1.strip()
                msgfromArduino3=msgfromArduino2.split(';')
                msgfromArduino4=list(msgfromArduino3)

                if len(msgfromArduino4) < 4:
                    msgfromArduino4 = ["-", "-", "-", "-"]

                return msgfromArduino4