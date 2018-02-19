import csv
import os
import glob
import options
import time
import file_management as fm
from collections import OrderedDict

#Change File Paths
#READ_CSVPATH = '/var/www/FlaskApp/FlaskApp/static/read.csv'
#WRITE_CSVPATH = '/var/www/FlaskApp/FlaskApp/static/att.csv'
#IMAGEPATH = '/var/www/FlaskApp/FlaskApp/static/Pics/'
READ_CSVPATH = 'read.csv'
WRITE_CSVPATH = 'static/csv/att.csv'
IMAGEPATH = 'static/Pics/'

read_fieldnames=['image_name', 'gender-male','gender-female','gender-unknown', 'score']
new_fieldnames={'gender-unknown':'unknown'}


#Writes a new row of data into csv file
def writeNewRow(data, clothing_type):
    file_exists = os.path.isfile(WRITE_CSVPATH)
    with open(WRITE_CSVPATH, 'a') as csvfile:
        dataWriter = csv.DictWriter(csvfile, fieldnames=fm.retrieveFieldNames(clothing_type), restval=0, lineterminator='\n')
        if not file_exists:
            dataWriter.writeheader()  # file doesn't exist yet, write a header
        dataWriter.writerow(data)

def retrieveImageData(filename, csvpath):
    with open(csvpath) as csvfile:
        my_content = csv.reader(csvfile, delimiter=',')
        for row in my_content:
            if filename == row[0]:
                data = dict()
                for i in range(len(row)):
                    if read_fieldnames[i] in new_fieldnames:
                        data[new_fieldnames[read_fieldnames[i]]] = row[i]
                    else:
                        data[read_fieldnames[i]] = row[i]
                print(data)
                return data
        return None

#Checks if a file path already exists in CSV file
def isFileLabelled(filename, CSVPATH):
    if os.path.isfile(CSVPATH):
        with open(CSVPATH) as csvfile:
            my_content = csv.reader(csvfile, delimiter=',')
            is_labelled = False

            for row in my_content:
                if filename == row[0]:
                    is_labelled = True
                    return True
            if not is_labelled:
                return False
    else:
        return False

#Gets list of image data for images already labelled
def getImagesLabellingList():
    images_data_list = []
    #If CSV File Exists
    if os.path.isfile(READ_CSVPATH):
        for filename in sorted(glob.glob(IMAGEPATH+'*.jpg')): #assuming jpg
             basename = (os.path.basename(filename))
             if not isFileLabelled(basename, WRITE_CSVPATH):
                 print(basename)
                 image_data = retrieveImageData(basename, READ_CSVPATH)
                 if image_data:
                    images_data_list.append(image_data)
    #READ CSV DOES NOT EXIST
    else:
        if os.path.isfile(WRITE_CSVPATH):
            for filename in sorted(glob.glob(IMAGEPATH+'*.jpg')): #assuming jpg
                basename = (os.path.basename(filename))
                if not isFileLabelled(basename, WRITE_CSVPATH):
                    images_data_list.append({'image_name': basename})
        else:
            for filename in sorted(glob.glob(IMAGEPATH+'*.jpg')): #assuming jpg
                images_data_list.append({'image_name': os.path.basename(filename)})
    return images_data_list
