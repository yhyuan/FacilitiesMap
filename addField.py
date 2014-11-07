import arcpy
featureName = "\\\\LRCTPTVSUAAP003\\agsShared\\Facilities\\data\\FacilitiesMap.gdb\\Facilities"
featrueField = ["LOCATIONNAME", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", ""]
arcpy.AddField_management(featureName, featrueField[0], featrueField[1], featrueField[2], featrueField[3], featrueField[4], featrueField[5], featrueField[6], featrueField[7], featrueField[8])