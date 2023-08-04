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
# This file is used to save readings as a CSV file
#
# Reference:
#
# Last Modified:
# Agustinus Rio Sunardi - 04/08/2021
#
# Input Arguments:
# Data polling
# Folder path
# File name
#
# Output Arguments:
# CSV file created in user-specified folder path
#
######################################################################################

import os
import csv
from collections import Counter

def createFolder (folderPath):
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)

def saveCSV (data, folderPath, fileName):
    createFolder(folderPath)
    filePath = os.path.join(folderPath, fileName)

    with open(filePath, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)

        # Write the headings to the CSV file

        headings = ['Date&Time', 'MFM (SLPM)', 'MFC (SLPM)', 'Pressure (bar)', 'Temperature 1 (deg C)', 'Temperature 2 (deg C)', 'Temperature 3 (deg C)', 'Temperature 4 (deg C)', 'Temperature 5 (deg C)', 'Temperature 6 (deg C)', 'Valve 1', 'Valve 2', 'Valve 3', 'Valve 4']

        writer.writerow(headings)

        countings = Counter()

        for row in data:

            # MFMReading is the Second element in each row
            MFMReading = row[1]

            writer.writerow(row)

            # Count the occurrences of each MFMReading
            countings[MFMReading] += 1

    return countings