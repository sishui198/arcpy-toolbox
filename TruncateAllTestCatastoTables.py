# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# TruncateAll.py
# Created on: 2015-03-06 08:44:37.00000
#   (generated by ArcGIS/ModelBuilder)
# Description:
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
#from colorama import init, Fore
#init()

arcpy.env.workspace = r"C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog\ESRI_CATASTO@geodb_exat.sde"

fdlist = arcpy.ListFeatureClasses()

SDE_USER = "ESRI_CATASTO"

PFX = "test_"

#testFdlist = [testfd for testfd in fdlist if testfd.startswith(PFX)]

featuresCATASTO = [SDE_USER+"."+PFX+"bordi_acqua",SDE_USER+"."+PFX+"bordi_particella",SDE_USER+"."+PFX+"bordi_fabbricato",SDE_USER+"."+PFX+"bordi_confine",SDE_USER+"."+PFX+"fiduciali",SDE_USER+"."+PFX+"simboli",SDE_USER+"."+PFX+"linee",SDE_USER+"."+PFX+"testi"]

fdlistCATASTO = [fd for fd in fdlist if fd in featuresCATASTO]

for fd in fdlistCATASTO:
    # Process: Truncate Table
    msg = "* * *\n"+"Truncating feature class {0}.".format(str(fd))
    arcpy.AddMessage(msg)
    # ### TRUNCATE IS DISABLED FOR SAFETY ###
    #arcpy.TruncateTable_management(fd)
    msg = "{0} truncated.".format(str(fd))
    arcpy.AddWarning(msg)

