import arcpy, Frame

arcpy.env.workspace = arcpy.GetParameterAsText(0)      #this is where the files are to go
input1= arcpy.GetParameterAsText(1)                     # this is where the feature class is put
output= arcpy.GetParameterAsText(2)                    # for right now this is where the text file is saved just for testing
User_Field = arcpy.GetParameterAsText(3)               # this is the string into which the user put the Field name
User_Class = arcpy.GetParameterAsText(4)               # this is the string into which the user put the Class name
Cell_Size= arcpy.GetParameterAsText(5)                 # future spot of the input of the cells size of the new feature class
Ratio= arcpy.GetParameterAsText(6)                     # future spot of the input of the Ratio of the new feature class
User_Field_Count= arcpy.GetParameterAsText(7)

arcpy.AddMessage(Cell_Size)
arcpy.AddMessage(Ratio)
#list for the class in the shape file
Class_List=[]
# nothing in this list yet, code not done
Fields_List=[]
#this is a text file that is for testing to see if it is outputting the right thing
output1=output
file_object = open(output1,'w')



X_X=int(arcpy.GetRasterProperties_management(input1, "COLUMNCOUNT")[0])

Y_Y=int(arcpy.GetRasterProperties_management(input1, "ROWCOUNT")[0]) 

arcpy.AddMessage(X_X)
arcpy.AddMessage(Y_Y)

x_res = float(arcpy.GetRasterProperties_management(input1, "CELLSIZEX")[0])
y_res = float(arcpy.GetRasterProperties_management(input1, "CELLSIZEY")[0])

arcpy.AddMessage(x_res)
arcpy.AddMessage(y_res)

arcpy.env.cellSize = 20

Fields=arcpy.ListFields(input1)
for i in Fields:
    Fields_List.append(i.name)                                   # putting all of the Field in the feature class into the Fields_List
if User_Field in Fields_List:
    file_object.write("Field Verified\n")                        # makes sure user put in the right field that have the class in them
    for i in Fields_List:
        file_object.write(i +"\n")
    with arcpy.da.SearchCursor(input1,[User_Field]) as Classes: # this goes through the field of User_Field to find all of the class and then put them in the CLass list
        for i in Classes:
            if i[0] not in Class_List:
                Class_List.append(i[0])                           # running through all of the Class and putting them in the Class_List
            for i in Class_List:
                file_object.write(str(i) +"\n")
    del Classes
Class_List.sort()    # just to make the output to look nice

 

# this runs through the Class list and matches it to the user input
if User_Class in Class_List:
    file_object.write("Class Verified\n")
    for i in Class_List:
        file_object.write(i+"\n")
    file_object.write(Ratio)
    file_object.write(Cell_Size)

file_object.close()	
	
xy=Cell_Size.split(" ")
arcpy.AddMessage(xy)
X=xy[0]
Y=xy[1]

Parameters = Frame.classifiedRaster(input1,X,Y,Ratio,User_Class)
arcpy.AddMessage(str(input1) + " " + str(X) + " " + str(Y) + " " + str(Ratio) + " " + str(User_Class))
Parameters.processRaster(output)
