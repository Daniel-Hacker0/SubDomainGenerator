#Disclaimer:  
# This code is made for education and ethical testing purposes only.  
# Usage of this tool for attacking targets without permission is illegal.
# I assume no liability and am not responsible for any misuse or damage caused by this code.


import argparse
import random
import string
import csv

parser = argparse.ArgumentParser(description="Creates random subdomains for a given domain and tld.")
parser.add_argument('-d', dest='domain', help="Domain")
parser.add_argument('-tld', dest='tld', help="The TLD of the domain")
args = parser.parse_args()

with open('name of .csv goes here','w') as output: #change this to whatever .csv you want to write the domains to.
	columnTitleRow = "ids, url\n"
	output.write(columnTitleRow)
	for n in range(0,100):
		strings = "".join([random.choice(string.ascii_letters + string.digits) for a in range(14)])
		ids = n
		name = strings
		row = str(ids) + "," + name + "." + args.domain + "." + args.tld + "\n"
		output.write(row)
		print(strings + "." + args.domain + "." + args.tld)