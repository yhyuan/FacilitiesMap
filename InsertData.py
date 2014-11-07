import sys
reload(sys)
sys.setdefaultencoding("latin-1")

import xlrd, arcpy, string, os, zipfile, fileinput, time, math
from datetime import date
start_time = time.time()

ExcelFile = 'input\\Facilities_for_Mapping.xlsx'
wb = xlrd.open_workbook(ExcelFile)
sh = wb.sheet_by_name(u'Facilities')
for rownum in range(1, sh.nrows):
	row = sh.row_values(rownum)
	Location = row[0]
	Address	= row[1]
	Total_Sq_Ft	= str(int(row[2]))
	Lease_Cost = str(int(row[3]))
	Lease_Expiry = row[4]
	Occupants = row[5]
	Num_of_Staff = '0'
	if len(str(row[6])) != 0:
		Num_of_Staff = str(int(row[6]))
	Staff_Cap = '0'
	if len(str(row[7])) != 0:
		Staff_Cap =  str(int(row[7]))
	RSF_per_FTE = '0'
	if len(str(row[8])) != 0:
		RSF_per_FTE = str(int(row[8]))
	Num_of_Fleet = '0'
	if len(str(row[9])) != 0:
		Num_of_Fleet = str(int(row[9]))
	POINT_X	= str(row[10])
	POINT_Y = str(row[11])
	LeasedOwned = ''
	if Lease_Expiry == 'n/a-government owned':
		LeasedOwned = 'Owned'
		Lease_Expiry = ''
		Lease_Expiry1 = ''
		Lease_Expiry2 = ''
	else:
		LeasedOwned = 'Leased'
		Lease_Expiry = ''
		Lease_Expiry1 = ''
		Lease_Expiry2 = ''

	Address = Address.replace('\n', ' ').strip()
	#print Lease_Expiry
	print "Python FacilitiesMapEditor.py Jerry APPEND \"" + POINT_Y + "|" + POINT_X + "|" + Location + "|" + Address  + "|" + Total_Sq_Ft + "|" + Lease_Cost  + "|" + LeasedOwned + "|"+ Lease_Expiry + "|" + Lease_Expiry1  + "|" + Lease_Expiry2   + "|" + ''  + "|" + Num_of_Staff + "|" + Staff_Cap + "|" + RSF_per_FTE + "|" + Num_of_Fleet + "| \""



