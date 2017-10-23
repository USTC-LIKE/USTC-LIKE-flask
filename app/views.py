from flask import render_template
from flask import Flask,request
import os
from app import app
import sqlite3

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index.html')
@app.route('/index', methods = ['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/people.html")
@app.route("/people")
def people():
    conn=sqlite3.connect('people.db')
    cursor = conn.cursor()
    cursor.execute('select * from people where category == \'PhD\'')
    values= cursor.fetchall()
    
    PhDs=[]
    for stu in values:
        path="./app/static/save_file/"+stu[0]+".jpg"
        if os.path.isfile(path):
            img="../static/people_png/"+stu[0]+".png"
        else:
            img="../static/res/img/people/unknown.jpg"
        homepage="../single_people/"+stu[0]
        PhDs.append([stu[0],homepage,img])

    cursor.execute('select * from people where category == \'graduate\'')
    values= cursor.fetchall()
    
    masters=[]
    for stu in values:
        path="./app/static/save_file/"+stu[0]+".jpg"
        if os.path.isfile(path):
            img="../static/people_png/"+stu[0]+".png"
        else:
            img="../static/res/img/people/unknown.jpg"
        homepage="../single_people/"+stu[0]
        masters.append([stu[0],homepage,img])

    cursor.execute('select * from people where category == \'undergraduate\'')
    values= cursor.fetchall()
    
    undergraduates=[]
    for stu in values:
        path="./app/static/save_file/"+stu[0]+".jpg"
        if os.path.isfile(path):
            img="../static/people_png/"+stu[0]+".png"
        else:
            img="../static/res/img/people/unknown.jpg"
        homepage="../single_people/"+stu[0]
        undergraduates.append([stu[0],homepage,img])


    phdnumber = len(PhDs)
    phdrows = list(range((phdnumber-1)//5+1))
    
    masternumber = len(masters)
    masterrows = list(range((masternumber-1)//5+1))
    
    undergraduatenumber = len(undergraduates)
    undergraduaterows = list(range((undergraduatenumber-1)//5+1))
    

    cursor.close()
    conn.close()

    return render_template("people1.html", PhDs=PhDs,phdnumber=phdnumber,phdrows=phdrows,
                           masters=masters,masternumber=masternumber,masterrows=masterrows, 
                           undergraduates=undergraduates,undergraduatenumber=undergraduatenumber,undergraduaterows=undergraduaterows,)
    
@app.route("/research.html")
@app.route("/research")
def research():
    return render_template("research.html")

@app.route("/projects.html")
@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/news.html")
@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/publications.html")
@app.route("/publications")
def publications():
    conn=sqlite3.connect('LIKE1.db')
    cursor = conn.cursor()

    cursor.execute('select * from PUBLICATION where year == \'2017\'')
    values= cursor.fetchall()
    pubs2017 = values

    cursor.execute('select * from PUBLICATION where year == \'2016\'')
    values= cursor.fetchall()
    pubs2016 = values

    cursor.execute('select * from PUBLICATION where year == \'2015\'')
    values= cursor.fetchall()
    pubs2015 = values

    cursor.execute('select * from PUBLICATION where year == \'2014\'')
    values= cursor.fetchall()
    pubs2014 = values

    cursor.close()
    conn.close()
    return render_template("publications.html",pubs2017=pubs2017,pubs2016=pubs2016,pubs2015=pubs2015,pubs2014=pubs2014)  

@app.route("/information.html")
@app.route("/information")
def information():
    return render_template("information.html", job=1)

@app.route("/information/job1.html")
def job1():
    return render_template("information.html", job=1)
@app.route("/information/job2.html")
def job2():
    return render_template("information.html", job=2)
@app.route("/information/job3.html")
def job3():
    return render_template("information.html", job=3)

@app.route('/hello')
def hello():
    return 'Hello World'



@app.route('/single_people/<name>',methods = ['GET', 'POST'])
def single_people(name):
    conn=sqlite3.connect('people.db')
    cur=conn.cursor()
    cur.execute('select * from people where name=\''+name+'\'')
    values=cur.fetchall()[0]
    print(values)
    category=values[1]
    homepage=values[2]
    email=values[3]
    office=values[4]
    title1=values[5]
    title2=values[6]
    title3=values[7]
    title4=values[8]
    title5=values[9]
    content1=values[10]
    content2=values[11]
    content3=values[12]
    content4=values[13]
    content5=values[14]
    title_content=[]
    if(content1!=None):
        title_content.append([title1,content1])
    if(content2!=None):
        title_content.append([title2,content2])
    if(content3!=None):
        title_content.append([title3,content3])
    if(content4!=None):
        title_content.append([title4,content4])
    if(content5!=None):
        title_content.append([title5,content5])
    name1=name
    print(type(name1))
    name2=name1.split('_',1)[0]+" "+name1.split('_',1)[1]
    name1.replace('_',' ')
    print(name1)

    path="./app/static/save_file/"+name+".jpg"
    if os.path.isfile(path):
        img="../static/save_file/"+name+".jpg"
    else:
        img="../static/res/img/people/unknown.jpg"

    #return name
    return render_template("single_people.html",
                            name=name2,
                            category=category,
                            homepage=homepage,
                            email=email,
                            office=office,
                            title_content=title_content,
                            img=img)