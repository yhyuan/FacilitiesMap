import sys
reload(sys)
sys.setdefaultencoding("latin-1")

import xlrd, arcpy, string, os, zipfile, fileinput, time, math
from datetime import date
start_time = time.time()

#ExcelFile = 'input\\Facilities_for_Mapping.xlsx'

INPUT_PATH = "input"
OUTPUT_PATH = "output"
if arcpy.Exists(OUTPUT_PATH + "\\FacilitiesMap.gdb"):
	os.system("rmdir " + OUTPUT_PATH + "\\FacilitiesMap.gdb /s /q")
os.system("del " + OUTPUT_PATH + "\\*FacilitiesMap*.*")
arcpy.CreateFileGDB_management(OUTPUT_PATH, "FacilitiesMap", "9.3")
arcpy.env.workspace = OUTPUT_PATH + "\\FacilitiesMap.gdb"

featureName = "Facilities"
#FieldList = ["LOCATION", "ADDRESS", "TOTAL_SQ_FT", "ANNUALCOST", "LEASEDOWNED", "LEASEEXPIRY", "LEASEEXPIRY1", "LEASEEXPIRY2","OCCUPANTS", "NUM_OF_STAFF", "STAFF_CAP", "RSF_PER_FTE", "NUM_OF_FLEET"]
featureFieldList = [["LOCATION", "TEXT", "", "", "", "", "NON_NULLABLE", "REQUIRED", ""], ["ADDRESS", "TEXT", "", "", "", "", "NON_NULLABLE", "REQUIRED", ""], ["TOTALSQUAREFEET", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", ""], ["ANNUALCOST", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", ""], ["LEASEDOWNED", "TEXT", "", "", "", "", "NON_NULLABLE", "NON_REQUIRED", ""], ["LEASEEXPIRY", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", ""], ["LEASEEXPIRY1", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", ""], ["LEASEEXPIRY2", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", ""], ["OCCUPANTS", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", ""], ["NUMBEROFSTAFF", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", ""], ["STAFFCAPACITY", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", ""], ["RSFPERFTE", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", ""], ["NUMBEROFFLEET", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", ""], ["LOCATIONNAME", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", ""]]
featureInsertCursorFields = tuple(["SHAPE@XY"] + map(lambda x: x[0], featureFieldList))
arcpy.CreateFeatureclass_management(arcpy.env.workspace, featureName, "POINT", "", "DISABLED", "DISABLED", "", "", "0", "0", "0")
# Process: Define Projection
arcpy.DefineProjection_management(featureName, "GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")
# Process: Add Fields	
for featrueField in featureFieldList:
	arcpy.AddField_management(featureName, featrueField[0], featrueField[1], featrueField[2], featrueField[3], featrueField[4], featrueField[5], featrueField[6], featrueField[7], featrueField[8])

featureName = "Log"
featureFieldList = [["USER", "TEXT", "", "", "", "", "NON_NULLABLE", "REQUIRED", ""], ["TIME", "TEXT", "", "", "", "", "NON_NULLABLE", "REQUIRED", ""], ["ACTION", "TEXT", "", "", "", "", "NON_NULLABLE", "REQUIRED", ""]]
featureInsertCursorFields = tuple(["SHAPE@XY"] + map(lambda x: x[0], featureFieldList))
arcpy.CreateFeatureclass_management(arcpy.env.workspace, featureName, "POINT", "", "DISABLED", "DISABLED", "", "", "0", "0", "0")
# Process: Define Projection
arcpy.DefineProjection_management(featureName, "GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")
# Process: Add Fields	
for featrueField in featureFieldList:
	arcpy.AddField_management(featureName, featrueField[0], featrueField[1], featrueField[2], featrueField[3], featrueField[4], featrueField[5], featrueField[6], featrueField[7], featrueField[8])

'''
featureData = []
wb = xlrd.open_workbook(ExcelFile)
sh = wb.sheet_by_name(u'Facilities')
for rownum in range(1, sh.nrows):
	row = sh.row_values(rownum)
	row[1] = row[1].replace('\n', ' ')
	row = [(row[10], row[11])] + row[:10]
	featureData.append(row);
	if rownum > 1:
		break

cntr = 1
try:
	with arcpy.da.InsertCursor(featureName, featureInsertCursorFields) as cur:
		for rowValue in featureData:
			cur.insertRow(rowValue)
			cntr = cntr + 1
except Exception as e:
	print "\tError: " + featureName + ": " + e.message
'''
