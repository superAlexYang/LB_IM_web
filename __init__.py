from flask import (Flask, render_template, redirect,
                   url_for, request, make_response)
from file_management import getImagesLabellingList, writeNewRow
from options import GROUP_1
from options_race import RACE_Dict
from options_att import ATTRACTIVENESS_dict
import time
import outfit_management as om
import outfit_management_race as omr
import outfit_management_att as oma
import random
app = Flask(__name__)

group_1_count = 0
race_count = 0
attractiveness_count = 0
group_1_page_count = 1
race_page_count = 1
attractiveness_page_count = 1

page_total = 8
group_1_page_percent = (float(group_1_page_count)/page_total)*100
race_page_percent = (float(race_page_count)/page_total)*100
attractiveness_page_percent = (float(attractiveness_page_count)/page_total)*100

imageList = list()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/complete_gender')
def complete_gender():
    random_number = random.randint(10000000, 99999999)
    return render_template('complete_gender.html',random_number=random_number)

@app.route('/complete_race')
def complete_race():
    random_number = random.randint(10000000, 99999999)
    return render_template('complete_race.html',random_number=random_number)

@app.route('/complete_attractiveness')
def complete_attractiveness():
    random_number = random.randint(10000000, 99999999)
    return render_template('complete_attractiveness.html',random_number=random_number)


@app.route('/csv/<path:filename>', methods=['GET', 'POST'])
def download(filename):    
    return send_from_directory(directory='csv', filename=filename)

@app.route('/save_Group_1', methods=['POST'])
def save_Group_1():
    global group_1_count
    group_1_count += 30
    global group_1_page_count
    group_1_page_count += 1
    global group_1_page_percent
    group_1_page_percent = (float(group_1_page_count)/page_total)*100
    if group_1_count==len(imageList):
        group_1_count=0
        group_1_page_count = 1
        group_1_page_percent = (float(group_1_page_count)/page_total)*100
        response = make_response(redirect(url_for('complete_gender')))
        labelledDict = dict(request.form.items()) #request the POST-ed info
        print(labelledDict)
        om.writeNewRow(dict(request.form.items()), 'Group_1')
        return response
    response = make_response(redirect(url_for('group_1')))
    #Saves labels to CSV file
    labelledDict = dict(request.form.items()) #request the POST-ed info
    print(labelledDict)
    om.writeNewRow(dict(request.form.items()), 'Group_1')
    return response

@app.route('/save_RACE', methods=['POST'])
def save_RACE():
    global race_count
    race_count += 30
    global race_page_count
    race_page_count += 1
    global race_page_percent
    race_page_percent = (float(race_page_count)/page_total)*100
    if race_count==len(imageList):
        race_count=0
        race_page_count = 1
        race_page_percent = (float(race_page_count)/page_total)*100
        response = make_response(redirect(url_for('complete_race')))
        labelledDict = dict(request.form.items()) #request the POST-ed info
        print(labelledDict)
        om.writeNewRow(dict(request.form.items()), 'Race')
        return response
    response = make_response(redirect(url_for('RACE')))
    #Saves labels to CSV file
    labelledDict = dict(request.form.items()) #request the POST-ed info
    print(labelledDict)
    omr.writeNewRow(dict(request.form.items()), 'Race')
    
    return response

@app.route('/save_ATTRACTIVENESS', methods=['POST'])
def save_ATTRACTIVENESS():
    global attractiveness_count
    attractiveness_count += 30
    global attractiveness_page_count
    attractiveness_page_count += 1
    global attractiveness_page_percent
    attractiveness_page_percent = (float(attractiveness_page_count)/page_total)*100
    if attractiveness_count==len(imageList):
        attractiveness_count=0
        attractiveness_page_count = 1
        attractiveness_page_percent = (float(attractiveness_page_count)/page_total)*100
        response = make_response(redirect(url_for('complete_attractiveness')))
        labelledDict = dict(request.form.items()) #request the POST-ed info
        print(labelledDict)
        om.writeNewRow(dict(request.form.items()), 'Attractiveness')
        return response
    response = make_response(redirect(url_for('ATTRACTIVENESS')))
    #Saves labels to CSV file
    labelledDict = dict(request.form.items()) #request the POST-ed info
    print(labelledDict)
    oma.writeNewRow(dict(request.form.items()), 'Attractiveness')
    
    return response
#TODO: Write new images into top.csv bottom.csv and shoes.csv as well


@app.route('/RACE')
def RACE():
    global imageList
    if len(imageList) == 0:
        imageList = om.getImagesLabellingList()
        print(imageList)
    else:
        print("Images Left:", len(imageList)-race_count)

    return render_template('race.html',
        imageDict=imageList[race_count],
        imageDict2=imageList[race_count+1],
        imageDict3=imageList[race_count+2],
        imageDict4=imageList[race_count+3],
        imageDict5=imageList[race_count+4],
        imageDict6=imageList[race_count+5],
        imageDict7=imageList[race_count+6],
        imageDict8=imageList[race_count+7],
        imageDict9=imageList[race_count+8],
        imageDict10=imageList[race_count+9],
        imageDict11=imageList[race_count+10],
        imageDict12=imageList[race_count+11],
        imageDict13=imageList[race_count+12],
        imageDict14=imageList[race_count+13],
        imageDict15=imageList[race_count+14],
        imageDict16=imageList[race_count+15],
        imageDict17=imageList[race_count+16],
        imageDict18=imageList[race_count+17],
        imageDict19=imageList[race_count+18],
        imageDict20=imageList[race_count+19],
        imageDict21=imageList[race_count+20],
        imageDict22=imageList[race_count+21],
        imageDict23=imageList[race_count+22],
        imageDict24=imageList[race_count+23],
        imageDict25=imageList[race_count+24],
        imageDict26=imageList[race_count+25],
        imageDict27=imageList[race_count+26],
        imageDict28=imageList[race_count+27],
        imageDict29=imageList[race_count+28],
        imageDict30=imageList[race_count+29],
        options=RACE_Dict,
        page_number=race_page_count,
        page_tt_number = page_total,
        pg_percent =race_page_percent)

@app.route('/ATTRACTIVENESS')
def ATTRACTIVENESS():
    global imageList
    if len(imageList) == 0:
        imageList = om.getImagesLabellingList()
    else:
        print("Images Left:", len(imageList)-attractiveness_count)

    return render_template('attractiveness.html',
        imageDict=imageList[attractiveness_count],
        imageDict2=imageList[attractiveness_count+1],
        imageDict3=imageList[attractiveness_count+2],
        imageDict4=imageList[attractiveness_count+3],
        imageDict5=imageList[attractiveness_count+4],
        imageDict6=imageList[attractiveness_count+5],
        imageDict7=imageList[attractiveness_count+6],
        imageDict8=imageList[attractiveness_count+7],
        imageDict9=imageList[attractiveness_count+8],
        imageDict10=imageList[attractiveness_count+9],
        imageDict11=imageList[attractiveness_count+10],
        imageDict12=imageList[attractiveness_count+11],
        imageDict13=imageList[attractiveness_count+12],
        imageDict14=imageList[attractiveness_count+13],
        imageDict15=imageList[attractiveness_count+14],
        imageDict16=imageList[attractiveness_count+15],
        imageDict17=imageList[attractiveness_count+16],
        imageDict18=imageList[attractiveness_count+17],
        imageDict19=imageList[attractiveness_count+18],
        imageDict20=imageList[attractiveness_count+19],
        imageDict21=imageList[attractiveness_count+20],
        imageDict22=imageList[attractiveness_count+21],
        imageDict23=imageList[attractiveness_count+22],
        imageDict24=imageList[attractiveness_count+23],
        imageDict25=imageList[attractiveness_count+24],
        imageDict26=imageList[attractiveness_count+25],
        imageDict27=imageList[attractiveness_count+26],
        imageDict28=imageList[attractiveness_count+27],
        imageDict29=imageList[attractiveness_count+28],
        imageDict30=imageList[attractiveness_count+29],
        options=ATTRACTIVENESS_dict,
        page_number=attractiveness_page_count,
        page_tt_number = page_total,
        pg_percent = attractiveness_page_percent)

@app.route('/group_1')
def group_1():
    global imageList
    if len(imageList) == 0:
        imageList = om.getImagesLabellingList()
    else:
        print("Images Left:", len(imageList)-group_1_count)

    return render_template('group_1.html',
        imageDict=imageList[group_1_count],
        imageDict2=imageList[group_1_count+1],
        imageDict3=imageList[group_1_count+2],
        imageDict4=imageList[group_1_count+3],
        imageDict5=imageList[group_1_count+4],
        imageDict6=imageList[group_1_count+5],
        imageDict7=imageList[group_1_count+6],
        imageDict8=imageList[group_1_count+7],
        imageDict9=imageList[group_1_count+8],
        imageDict10=imageList[group_1_count+9],
        imageDict11=imageList[group_1_count+10],
        imageDict12=imageList[group_1_count+11],
        imageDict13=imageList[group_1_count+12],
        imageDict14=imageList[group_1_count+13],
        imageDict15=imageList[group_1_count+14],
        imageDict16=imageList[group_1_count+15],
        imageDict17=imageList[group_1_count+16],
        imageDict18=imageList[group_1_count+17],
        imageDict19=imageList[group_1_count+18],
        imageDict20=imageList[group_1_count+19],
        imageDict21=imageList[group_1_count+20],
        imageDict22=imageList[group_1_count+21],
        imageDict23=imageList[group_1_count+22],
        imageDict24=imageList[group_1_count+23],
        imageDict25=imageList[group_1_count+24],
        imageDict26=imageList[group_1_count+25],
        imageDict27=imageList[group_1_count+26],
        imageDict28=imageList[group_1_count+27],
        imageDict29=imageList[group_1_count+28],
        imageDict30=imageList[group_1_count+29],
        options=GROUP_1,
        page_number=group_1_page_count,
        page_tt_number = page_total,
        pg_percent = group_1_page_percent)
if __name__ == '__main__':
	app.debug = True
	app.run(host = 'localhost', port = 5000)