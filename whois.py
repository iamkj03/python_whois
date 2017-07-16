#python3 whois.py domain.txt [any file name]

import pythonwhois
import sys
import json

def date_handler(obj):               #handles time error
	if hasattr(obj, 'isoformat'):
		return obj.isoformat()
	else:
		raise TypeError



sente = sys.argv[1]
newfile = sys.argv[2]                #file name of reading and writing files

domain = open(sente, 'r')            #reading file
print("Completed Split")

print("Used whois")
#splitby = domain.readline()
#print(splitby)

result = open(newfile, 'w')          #writing file

for url in range(3): 
	splitby = domain.readline()
	data=pythonwhois.get_whois(splitby)
	dumpfile = json.dumps(data,default=date_handler)
	print(splitby)
	result.write(str(dumpfile))
				     #Using for statement by each url and making json file into
				     #text file
result.close()
domain.close()
				     #closing all the argv
print("Completed!")


