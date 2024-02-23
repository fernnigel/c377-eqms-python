# kartik
import re
import os 
dirname = os.path.dirname(__file__) 
filename = os.path.join(dirname, "data\\enquiry.csv" )
enquiries = open(filename, "r")
data = enquiries.readlines()
datalist = []
for line in data:
    line = line.replace("\n"," ")
    res = line.split(",")
    datalist.append(res)
print(datalist)
enquiries.close()