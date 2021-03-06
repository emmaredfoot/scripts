########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.27.December.2015
########################################################################
# 
# Searches each of the burnup data and finds the keff and associated burnup closest to critical less than 1.00
# Pulls the keff and burnup from the partial table 210 from BURN card
# Run mcnpx_general.burnup first
# Writes a new file with keff and burnup
# New file first column is blank so thorium content can be entered
#
########################################################################
#
#
#
####### 
#
# imports
#
import os
import numpy
from sys import argv
script,mcnpx_output=argv
#
########################################################################
#
#
#
#######
#
# time and content steps
#
content_steps=20 #thorium content from 0.00 to 0.95
time_steps=40 #not time=0
#
#######
#
# open mcnpx output file
#
mcnpx_file=numpy.loadtxt(mcnpx_output)
#
#######
# 
# open the new data file for writing
#
content_burnup_file=open('burnup.content_lower.out','a')
#
#######
#
# search the file
#
for i in range(0,time_steps-1):
    if mcnpx_file[i,4]>1 and (mcnpx_file[i+1,4]<1):
        content_burnup_file.write('\t'+str.format('%.3e'%mcnpx_file[i+1,8])+'\t'+str.format('%.5f'%mcnpx_file[i+1,4])+'\n')
# end i 
#
#######
# 
# close files
#
content_burnup_file.close()
#
########################################################################
#
# EOF
#
########################################################################
