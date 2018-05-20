import arcpy,logging, os
from arcpy import env
env.workspace = r"C:\Users\wipro_hmdarji\AppData\Roaming\ESRI\Desktop10.4\ArcCatalog\rtagisdbadmin@gisdb.sde"
featureclass = arcpy.ListFeatureClasses('RTAGISDBADMIN.*')
path = r"D:\GISDB_Counts.txt"
file = open(path, "a")
for fc in featureclass:
    cnt = arcpy.GetCount_management(fc)
    desc = arcpy.Describe(fc)
    gt = desc.shapeType
    print (fc + " , " + str(cnt) + " , "+ gt)
    file.write(time.strftime("%d-%m-%y") + " :, ")
    file.write(fc + " , " + str(cnt) + " , " + gt+'\n')

file.close()
