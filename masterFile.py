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
# Code to send user inputs to the respective instruments to begin a PSA experiment
#
# Reference:
#
# Last Modified:
# Agustinus Rio Sunardi - 04/08/2021
#
# Input Arguments:
# Device ID
# Flowrate setpoint
# Sampling time
# Cycle duration
# Number of cycles
# Cycle configuration
#
# Output Arguments:
# Data from Alicat Instruments, Pressure Transmitter, Arduino, and Temperature Probe
#
######################################################################################

def masterFile():

    import time
    import csv
    import serial
    import decimal

    from alicatInstruments import alicatInstruments
    from pressureTransmitter import pressureTransmitter
    from arduinoController import arduinoController
    from temperatureProbe import temperatureProbe

    # Establish serial connection with Alicat Instruments
    serialMF = serial.Serial('COM5', 19200, timeout=0.1)
    serialArduino = serial.Serial('COM4', 9600, timeout=0.1)

    # Get user input for MFC device id
    try:
        MFC_id = input("Enter the MFC device id: ")
    except ValueError:
        print("Invalid input. Please enter a valid device id.")

    # Get user input for MFM device id
    try:
        MFM_id = input("Enter the MFM device id: ")
    except ValueError:
        print("Invalid input. Please enter a valid device id.")

    # Get sampling time for data polling
    try:
        sampling_time = float(input("Enter the sampling time (in seconds): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    if sampling_time < 2:
        sampling_time = 2

    #  Get user input for flowrate setpoint
    try:
        flowrate_setpoint = float(input("Enter the flowrate setpoint (in SLPM): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    MFCSetPoint = alicatInstruments(serialMF, f"AS {flowrate_setpoint}\r")

    # Run the PSA cycle
    # format is Pressurisation Adsorption Blowdown Purge (in seconds)")
    user_input = input("Enter four durations (in seconds) separated by spaces: ")

    # result=[decimal.ConversionSyntax(x)*1000 for x in user_input]
    # print(result)
    test = [float(duration)*1000 for duration in user_input.split()]

    # multiply by 1000 to convert to milliseconds

    try:
        durations_list = [int(duration) for duration in test]
        num_loops = int(input("Enter the number of cycles: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

    cycleConfiguration = input("Enter the cycle configuration (e.g. 1 2 3 4): ")


    total_cycle_time = sum(durations_list) * num_loops / 1000
    print(f"Total cycle time: {total_cycle_time} seconds")

    durations_list.extend(cycleConfiguration)
    #  Send durations and number of loops to Arduino
    arduinoController(serialArduino, cycleDuration = durations_list, numCycles = num_loops)

    with open('dataPolling.csv', 'w', newline='') as csvfile:
        fieldnames = ['Time', 'MFC' , 'MFM', 'Pressure', 'Temperature1', 'Temperature2', 'Temperature3', 'Temperature4', 'Temperature5', 'Temperature6', 'Arduino1', 'Arduino2', 'Arduino3', 'Arduino4']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Read the flowrates from the Alicat devices
        MFC = alicatInstruments(serialMF,f"{MFC_id}\r") # Read the flowrate from the Alicat MFC
        MFM = alicatInstruments(serialMF,f"{MFM_id}\r") # Read the flowrate from the Alicat MFM

        # Read the string coming out of instruments for the duration of the Arduino program
        current_time = time.time()
        start_time = time.time()
        pollingData = []
        while (current_time-start_time) <= total_cycle_time+3 :

            # Read the flowrates from the Alicat devices
            MFC_flowrate = MFC
            MFM_flowrate = MFM
            presTransmitter = pressureTransmitter('COM3', 9600, 253, 0.2, True)
            tempProbe = temperatureProbe()
            arduino=arduinoController(serialArduino, readData = True)

            # Read the pressure from the pressure transmitter
            pressure = presTransmitter

            # Read the temperature from the temperature probe
            temperature = tempProbe

            # SPlit the temperature string into a list of temperatures
            temperature1 = temperature[0]
            temperature2 = temperature[1]
            temperature3 = temperature[2]
            temperature4 = temperature[3]
            temperature5 = temperature[4]
            temperature6 = temperature[5]

            # Arduino reading
            arduino1 = arduino[0]
            arduino2 = arduino[1]
            arduino3 = arduino[2]
            arduino4 = arduino[3]

            # Record the data every second into a csv file
            writer.writerow({'Time': time.strftime("%Y-%B-%d %H:%M:%S"), 'MFC': MFC_flowrate, 'MFM': MFM_flowrate, 'Pressure': pressure, 'Temperature1': temperature[0], 'Temperature2': temperature[1], 'Temperature3': temperature[2], 'Temperature4': temperature[3], 'Temperature5': temperature[4], 'Temperature6': temperature[5], 'Arduino1': arduino[0], 'Arduino2': arduino[1], 'Arduino3': arduino[2], 'Arduino4': arduino[3]})
            
            # Print the data to the console
            print(f"Time: {time.strftime('%Y-%B-%d %H:%M:%S')}, MFC: {MFC_flowrate}, MFM: {MFM_flowrate}, Pressure: {pressure}, Temperature1: {temperature1}, Temperature2: {temperature2}, Temperature3: {temperature3}, Temperature4: {temperature4}, Temperature5: {temperature5}, Temperature6: {temperature6}, Arduino1: {arduino1}, Arduino2: {arduino2}, Arduino3: {arduino3}, Arduino4: {arduino4}")

            current_time = time.time()

            # Append the data to a list
            pollingData.append([time.strftime("%Y-%B-%d %H:%M:%S"), MFC_flowrate, MFM_flowrate, pressure, temperature1, temperature2, temperature3, temperature4, temperature5, temperature6, arduino1, arduino2, arduino3, arduino4])

            # Sleep for X seconds
            # Adjust as necessary
            time.sleep((sampling_time)-2)

    return pollingData