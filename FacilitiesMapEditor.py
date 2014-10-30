#Python FacilitiesMapEditor.py Jerry APPEND "43.841885|-79.0371388|Ajax|230 Westney Road South, 5th Floor Ajax ON L1S7J5|1|11|Leased|10/02/2014|N/A|N/A|0000,1111|1|1|1|1"
#Python FacilitiesMapEditor.py Jerry DELETE 1 
#Python FacilitiesMapEditor.py Jerry UPDATE "3|TOTALSQUAREFEET|1900"
'''
Python FacilitiesMapEditor.py Jerry APPEND 43.841885|-79.0371388|Ajax|230 Westney Road South, 5th Floor Ajax ON L1S7J5|1|1|Leased|10/02/2014|N/A|N/A|0000,1111|1|1|1|1
Python FacilitiesMapEditor.py Jerry APPEND 44.38182656|-79.71349896|Barrie|54 Cedar Pointe Drive, Unit 1201 Barrie ON L4N5R7|1|1|Leased|10/02/2014|N/A|N/A|0000,1111|1|1|1|1
Python FacilitiesMapEditor.py Jerry APPEND 44.1850678|-77.366707|Belleville|345 College St E Belleville ON K8N5S7|1|1|Leased|10/02/2014|N/A|N/A|0000,1111|1|1|1|1
Python FacilitiesMapEditor.py Jerry APPEND 43.3716823|-79.7839681|Burlington|4145 North Service Road, Suite 300 Burlington ON L7L6A3|1|1|Leased|10/02/2014|N/A|N/A|0000,1111|1|1|1|1
Python FacilitiesMapEditor.py Jerry APPEND 45.0186524|-74.7235665|Cornwall|113 Amelia Street, 1st Floor Cornwall ON K6H3P1|1|1|Leased|10/02/2014|N/A|N/A|0000,1111|1|1|1|1
Python FacilitiesMapEditor.py Jerry APPEND 45.2250754|-78.93114893|Dorset|1026 Bellwood Acres Road, Dorset, ON P0A1E0|1|1|Leased|10/02/2014|N/A|N/A|0000,1111|1|1|1|1
Python FacilitiesMapEditor.py Jerry UPDATE 11|LATITUDE|0|LONGITUDE|0|LOCATION|Zero
'''

import arcpy
from time import gmtime, strftime, strptime

OUTPUT_PATH = "\\\\LRCTPTVSUAAP003\\agsShared\\Facilities\\data"
arcpy.env.workspace = OUTPUT_PATH + "\\FacilitiesMap.gdb"
featureName = "\\\\LRCTPTVSUAAP003\\agsShared\\Facilities\\data\\FacilitiesMap.gdb\\Facilities"
USER = arcpy.GetParameterAsText(0)
ACTION = arcpy.GetParameterAsText(1)
featureInsertCursorFields = ("SHAPE@XY", "LOCATION", "ADDRESS", "TOTALSQUAREFEET", "ANNUALCOST", "LEASEDOWNED", "LEASEEXPIRY", "LEASEEXPIRY1", "LEASEEXPIRY2","OCCUPANTS", "NUMBEROFSTAFF", "STAFFCAPACITY", "RSFPERFTE", "NUMBEROFFLEET")
fieldList = list(featureInsertCursorFields)
indexDict = {}
for i in range(len(fieldList)):
	indexDict[fieldList[i]] = i
if ACTION == 'DELETE':
	objectID = arcpy.GetParameterAsText(2)
	try:
		with arcpy.da.UpdateCursor(featureName, featureInsertCursorFields, 'OBJECTID=' + objectID) as cur:
			for row in cur:
				cur.deleteRow ()
	except Exception as e:
		print "\tError: " + featureName + ": " + e.message
elif ACTION == 'APPEND':
	parameters = arcpy.GetParameterAsText(2).split('|');
	LATITUDE = parameters[0]
	LONGITUDE = parameters[1]
	LOCATION = parameters[2]
	ADDRESS = parameters[3]
	TOTALSQUAREFEET = int(parameters[4])
	ANNUALCOST = int(parameters[5])
	LEASEDOWNED = parameters[6]	
	LEASEEXPIRY = parameters[7]
	LEASEEXPIRY1 = parameters[8]
	LEASEEXPIRY2 = parameters[9]
	OCCUPANTS = parameters[10]
	NUMBEROFSTAFF = int(parameters[11])
	STAFFCAPACITY = int(parameters[12])
	RSFPERFTE = int(parameters[13])
	NUMBEROFFLEET  = int(parameters[14])
	try:
		with arcpy.da.InsertCursor(featureName, featureInsertCursorFields) as cur:
			cur.insertRow([(float(LONGITUDE), float(LATITUDE)), LOCATION, ADDRESS, TOTALSQUAREFEET, ANNUALCOST, LEASEDOWNED, LEASEEXPIRY, LEASEEXPIRY1, LEASEEXPIRY2,OCCUPANTS, NUMBEROFSTAFF, STAFFCAPACITY, RSFPERFTE, NUMBEROFFLEET])
	except Exception as e:
		print "\tError: " + featureName + ": " + e.message
elif ACTION == 'UPDATE':
	parameters = arcpy.GetParameterAsText(2).split('|');
	objectID = parameters[0]
	dict = {}
	for i in range(len(parameters)/2):
		dict[parameters[2*i + 1]] = parameters[2*i + 2]
	if (("LATITUDE" in dict) and ("LONGITUDE" in dict)):
		dict["SHAPE@XY"] = (float(dict["LONGITUDE"]), float(dict["LATITUDE"]))
		dict.pop("LONGITUDE", None)
		dict.pop("LATITUDE", None)
	for field in ["TOTALSQUAREFEET", "ANNUALCOST", "NUMBEROFSTAFF", "STAFFCAPACITY", "RSFPERFTE", "NUMBEROFFLEET"]:
		if field in dict:
			dict[field] = int(dict[field])
	try:
		with arcpy.da.UpdateCursor(featureName, featureInsertCursorFields, 'OBJECTID=' + objectID) as cur:
			for row in cur:
				for field in dict:
					row[indexDict[field]] = dict[field]
				cur.updateRow(row) 
	except Exception as e:
		print "\tError: " + featureName + ": " + e.message	
elif ACTION == 'DOWNLOAD':
	print "ACTION"
else:
	print "Error"
	
featureInsertCursorFields = ("SHAPE@XY", "USER", "TIME", "ACTION")
TIME = strftime("%Y-%m-%d %H:%M:%S", gmtime())
try:
	with arcpy.da.InsertCursor("\\\\LRCTPTVSUAAP003\\agsShared\\Facilities\\data\\FacilitiesMap.gdb\\Log", featureInsertCursorFields) as cur:
		cur.insertRow([(0, 0), USER, TIME,  ACTION + ": " + arcpy.GetParameterAsText(2)])
except Exception as e:
	print "\tError: " + featureName + ": " + e.message	