import urllib2
import os
class bcolors:
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   ENDC = '\033[0m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
print " _     _             _             _  __  __           "
print "| |__ | |_ _ __ ___ | |  ___ _ __ (_)/ _|/ _| ___ _ __ "
print "| '_ \| __| '_ ` _ \| | / __| '_ \| | |_| |_ / _ \ '__|"
print "| | | | |_| | | | | | | \__ \ | | | |  _|  _|  __/ |   "
print "|_| |_|\__|_| |_| |_|_| |___/_| |_|_|_| |_|  \___|_|   "
print""
print"Author   :Anlos"
print"Scripter :Anlos"
print""
response = urllib2.urlopen(raw_input(bcolors.OKBLUE + "[+] Enter Http/s Website To sniff HTML Code :- " + bcolors.ENDC))
data = response.read()

# Write data to file


filename = raw_input(bcolors.OKBLUE + "[+] Enter Output File's Name (eg.fb.html or fb.txt) :- " + bcolors.ENDC)

file = open(filename, 'w')
file.write(data)
file.close()
print (bcolors.BOLD+ "[+]File Saved in : HtmlSniffer as" + bcolors.ENDC) ,filename

