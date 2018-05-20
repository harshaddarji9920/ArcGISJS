mxd = arcpy.mapping
mxd = arcpy.mapping.MapDocument("CURRENT")
lyrlist = arcpy.mapping.ListLayers(mxd)
num = len(lyrlist)
print num
