import arcpy

arcpy.env.workspace = arcpy.GetParameterAsText(0)      #this is where the files are to go
input= arcpy.GetParameterAsText(1)                     # this is where the feature class is put
output= arcpy.GetParameterAsText(2)                    # for right now this is where the text file is saved just for testing
User_Field = arcpy.GetParameterAsText(3)               # this is the string into which the user put the Field name
User_Class = arcpy.GetParameterAsText(4)               # this is the string into which the user put the Class name
#list for the class in the shape file
Class_List=[]
# nothing in this list yet, code not done
Fields_List=[]
#this is a text file that is for testing to see if it is outputting the right thing
file_object = open(output,'w')


Fields=arcpy.ListFields(input)
for i in Fields:
    Fields_List.append(i.name)

if User_Field in Fields_List:
    file_object.write("Field Verified\n") #makes sure user put in the right field that have the class in them
    for i in Fields_List:
        file_object.write(i +"\n")
    with arcpy.da.SearchCursor(input,[User_Field]) as Classes:   # this goes through the field of User_Field to find all of the class and then put them in the CLass list
        for i in Classes:
            if i[0] not in Class_List:
                Class_List.append(i[0])
Class_List.sort()


#this runs through the Class list and matches it to the user input
if User_Class in Class_List:
    file_object.write("Class Verified\n")
    for i in Class_List:
        file_object.write(i+"\n")

