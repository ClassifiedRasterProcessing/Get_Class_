import arcpy, Frame

arcpy.env.workspace = arcpy.GetParameterAsText(0)      #this is where the files are to go
input1= arcpy.GetParameterAsText(1)                     # this is where the feature class is put
output= arcpy.GetParameterAsText(2)                    # for right now this is where the text file is saved just for testing
User_Field = arcpy.GetParameterAsText(3)               # this is the string into which the user put the Field name
User_Class = arcpy.GetParameterAsText(4)               # this is the string into which the user put the Class name
Cell_Size= arcpy.GetParameterAsText(5)                 # future spot of the input of the cells size of the new feature class
Ratio= arcpy.GetParameterAsText(6)                     # future spot of the input of the Ratio of the new feature class

arcpy.AddMessage(Cell_Size)
arcpy.AddMessage(Ratio)
#list for the class in the shape file
Class_List=[]
# nothing in this list yet, code not done
Fields_List=[]
#this is a text file that is for testing to see if it is outputting the right thing
try:
    file_object = open(output,'w')
except IOError:
    print("Not a raster Shapefile")
else:
    pass






Fields=arcpy.ListFields(input1)
for i in Fields:
    Fields_List.append(i.name)                                   # putting all of the Field in the feature class into the Fields_List
if User_Field in Fields_List:
    file_object.write("Field Verified\n")                        # makes sure user put in the right field that have the class in them
    for i in Fields_List:
        file_object.write(i +"\n")
    with arcpy.da.SearchCursor(input1,[User_Field]) as Classes:   # this goes through the field of User_Field to find all of the class and then put them in the CLass list
        for i in Classes:
            if i[0] not in Class_List:
                Class_List.append(i[0])                          # running through all of the Class and putting them in the Class_List
Class_List.sort()    # just to make the output to look nice


# this runs through the Class list and matches it to the user input
if User_Class in Class_List:
    file_object.write("Class Verified\n")
    for i in Class_List:
        file_object.write(i+"\n")
    file_object.write(Ratio)
    file_object.write(Cell_Size)

xy=Cell_Size.split(" ")
arcpy.AddMessage(xy)
X=xy[0]
Y=xy[1]

Parameters = Frame.classifiedRaster(input1,X,Y,Ratio,User_Class)
Parameters.processRaster(output)
