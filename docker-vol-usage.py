#!/usr/bin/env python3

# Docker vSphere Storage Volume Utilisation Script
#
# This script checks the utilisation of Docker Volumes created via vSphere Storage and outputs details in JSON for use with telegraf
#
# Ross A Stewart - July 2019

import subprocess

#
# Variables and Configuration
#

datastore = "datastore1" # vSphere datastore which volumes reside on

#
# Main code
#

# Grab the output of df -P
p1 = subprocess.Popen(['df', '-P'], stdout=subprocess.PIPE, universal_newlines=True)

# Extract lines which reference data store
p2 = subprocess.Popen(['grep', datastore], stdin=p1.stdout, stdout=subprocess.PIPE, universal_newlines=True)

# Close stdout of p1 as this is no longer needed
p1.stdout.close()

json_output = '[\n'
for line in p2.stdout.readlines():
    fields = line.split()
    path = fields[5]
    volumeName = path.split('/')
    volumeName.reverse()
    json_output += '  { \"volume_name\": \"' + volumeName[0] + '\", \"utilisation_percent\": ' + str(fields[4].rstrip('%')) + ' },\n'

# Trim the final two characters from the output as trailing commas are not allowed by the JSON spec
json_output = json_output[:-2]
json_output += '\n]'

p2.stdout.close()

# Close stdout of p2 as this is no longer needed
print (json_output)