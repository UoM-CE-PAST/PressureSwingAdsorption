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
# Function for Keller Pressure Transmitter to poll data
# The required files are keller_protocol.py
# This code was built for Keller X-Line Pressure Transmitter
#
# Reference:
# https://github.com/KELLERAGfuerDruckmesstechnik/keller_protocol_python
#
# Last Modified:
# Agustinus Rio Sunardi - 04/08/2021
#
# Input Arguments:
# Serial port connection
#
# Output Arguments:
# Pressure readings from Keller Pressure Transmitter
#
######################################################################################

def pressureTransmitter(port, baud_rate, address, timeout, echo):

    import keller_protocol.keller_protocol as kp
    import time
    import datetime
    
    class XLine:
        def __init__(self, port, baud_rate, address, timeout, echo=True):
            self.bus = kp.KellerProtocol(port, baud_rate, timeout, echo)
            self.address = address
            self.serial_number = None
            self.f73_channels = {
                "CH0": 0,
                "P1": 1,
                "P2": 2,
                "T": 3,
                "TOB1": 4,
                "TOB2": 5,
                "ConTc": 10,
                "ConRaw": 11,
            }
            self.init_f48()

        def init_f48(self) -> str:
            """Initialise and release"""
            answer = self.bus.f48(self.address)
            # print(f" Init of Device Address: {self.address} with Firmware: {answer}")

        def get_serial(self) -> int:
            """Get Serial Number from X-Line

            :returns Serial Number
            """
            self.serial_number = self.bus.f69(self.address)
            return self.serial_number

        def get_address(self) -> int:
            return self.address

        def set_address(self, new_address: int) -> int:
            """Change the Device address. -> Has to be unique on the RS485 bus

            :param new_address: New address of the Device
            :return: If successful return new_address otherwise old address and throw exception
            """
            self.address = self.bus.f66(self.address, new_address)
            return self.address

        def measure_p1(self) -> float:
            """Get pressure P1

            :return: pressure
            """
            pressure = self.bus.f73(self.address, 1)
            return pressure

    for i in range(10):
        # Example usage:
        # Init transmitter
        transmitter = XLine(
            port, baud_rate, address, timeout, echo
        )
        serial_number = transmitter.get_serial()
        # print(f"Transmitter serial number:{serial_number}")
        while True:
            
            time.sleep(0.1)

            p1 = transmitter.measure_p1()

            return p1