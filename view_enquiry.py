# kartik
import re
import os 
dirname = os.path.dirname(__file__) 
filename = os.path.join(dirname, "data\\enquiry.csv" )
enquiries = open(filename, "r")
data = enquiries.readlines()
print(data)
