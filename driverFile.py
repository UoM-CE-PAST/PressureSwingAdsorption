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
# This is the driver/executor file for the Pressure Swing Adsoprtion program
#
# Reference:
#
# Last Modified:
# Agustinus Rio Sunardi - 04/08/2021
#
# Input Arguments:
# 1. The username
# 2. The experiment name
# 3. The MFC device ID
# 4. The MFM device ID
# 5. The MFC flowrate setpoint
# 6. The sampling time / data polling frequency
# 7. The PSA cycle steps durations
# 8. The number of PSA cycles
# 9. The PSA cycle configuration
#
# Output Arguments:
# 1. The experimental results
# 2. The experimental results saved as a CSV file
#
######################################################################################

from masterFile import masterFile
from savingAsCSV import createFolder
from savingAsCSV import saveCSV
import os
import csv

# The main folder is the folder where all the experimental results are stored
# This folder is named "Experimental Results"
# The program will create this main folder if it does not exist
mainFolder = "Experimental Results"

# The sub folder is the folder where the experimental results of a particular user are stored
subFolder = input("Enter username: ")

# The experiment name is the name of the experiment or experiment ID
experimentName = input("Enter the name of the experiment: ")

pollingData = masterFile()

fileName = experimentName + ".csv"

# The experimental results are saved as a CSV file
# This is saved in the sub folder which is in the main folder
countings = saveCSV(pollingData, os.path.join(mainFolder, subFolder), fileName)