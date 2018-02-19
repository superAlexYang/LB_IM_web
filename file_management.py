import csv
import os
import glob
import options
import options_race
import options_att
import time

#Change File Paths to Your Local Paths
Group_1CSV = 'gender.csv'
race_CSV = 'race.csv'
attractiveness_CSV = 'att.csv'
#Retrive header names from DEFAULTS
def retrieveFieldNames(NAME):
    if NAME == 'Group_1':
        OPTS = options.GROUP_1
    elif NAME == 'Race':
        OPTS = options_race.RACE_Dict
    elif NAME == 'Attractiveness':
        OPTS = options_att.ATTRACTIVENESS_dict
    fieldnames = list()
    fieldnames.append('image_name')
    for key in OPTS.keys():
            fieldnames.append(key)
    return fieldnames

#Writes a new row of data into csv file
def writeNewRow(data, NAME):
    if NAME == 'Group_1':
        CSVPATH = Group_1CSV
    elif NAME == 'Race':
        CSVPATH = race_CSV
    elif NAME == 'Attractiveness':
        CSVPATH = attractiveness_CSV
    file_exists = os.path.isfile(CSVPATH)
    with open(CSVPATH, 'a') as csvfile:
        dataWriter = csv.DictWriter(csvfile, fieldnames=retrieveFieldNames(NAME), restval=0, lineterminator='\n')
        if not file_exists:
            dataWriter.writeheader()  # file doesn't exist yet, write a header
        dataWriter.writerow(data)

#Checks if a file path already exists in CSV file
def isFileLabelled(filename, CSVPATH):
    with open(CSVPATH) as csvfile:
        my_content = csv.reader(csvfile, delimiter=',')
        is_labelled = False

        for row in my_content:
            if filename == row[0]:
                is_labelled = True
                return True
        if not is_labelled:
            return False

#Gets list of images to be labelled
def getImagesLabellingList(NAME):
    images_file_list = []
    if NAME == 'Group_1':
        CSVPATH = Group_1CSV
    path = 'static/Pics/'
    #If CSV File Exists
    if os.path.isfile(CSVPATH):
        for filename in sorted(glob.glob(path+'*.jpg')): #assuming jpg
            if not isFileLabelled(filename, CSVPATH):
                images_file_list.append(filename)
    else:
        for filename in sorted(glob.glob(path+'*.jpg')): #assuming jpg
            images_file_list.append(filename)
    return images_file_list
