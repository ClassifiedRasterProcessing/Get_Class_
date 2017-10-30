import arcpy

rows =arcpy.SearchCursor("E:\College\GIS programming\!Only! Classified Images\SmallLarge_MultiColor_Dots_Random\Class_VECTOR_MultiSize_MultiColor_Dots_Random.shp",fields="FID;Shape;CLASS_NAME;AREA",sort_fields="CLASS_NAME A; AREA D")
for row in rows:
print(row.getValue("CLASS_NAME"))
