import arcpy

arcpy.env.workspace = arcpy.GetParameterAsText(0)      #this is where the files are to go
input= arcpy.GetParameterAsText(1)                     # this is where the feature class is put
output= arcpy.GetParameterAsText(2)                    # for right now this is where the text file is saved just for testing
User_Class = arcpy.GetParameterAsText(3)               # this is the string into which the user put the Class name

#list for the class in the shape file
Class=[]
# nothing in this list yet, code not done
Fields=[]

# this goes through the field of CLASS_NAME to find all of the class and then put them in the CLass list
with arcpy.da.SearchCursor(input,["CLASS_NAME"]) as Classes:
    for i in Classes:
        if i[0] not in Class:
            Class.append(i[0])
Class.sort()

#this is a text file that is for testing to see if it is outputting the right thing
file_object = open(output,'w')
file_object.write(User_Class)

#this runs through the Class list and matches it to the user input
if User_Class in Class:
    file_object.write("Class verified\n")
    for i in Class:
        file_object.write(i+"\n")