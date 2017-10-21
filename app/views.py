from flask import render_template
from flask import Flask,request

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
    conn=sqlite3.connect('LIKE1.db')
    cursor = conn.cursor()
    cursor.execute('select * from PEOPLE where kind == \'1\'')
    values= cursor.fetchall()
    print(values)

    leaders = values

    cursor.execute('select * from PEOPLE where kind == \'2\'')
    values= cursor.fetchall()
    print(values)

    students = values
    stunumber = len(values)

    sturows = list(range(stunumber//5+1))
    print(sturows,stunumber)
    cursor.close()
    conn.close()

    return render_template("people1.html",leaders=leaders, students=students,stunumber=stunumber,sturows=sturows)
    
@app.route("/research.html")
@app.route("/research")
def research():
    return render_template("research.html")

@app.route("/projects.html")
@app.route("/projects")
def projects():
    return render_template("projects.html")

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
    return render_template("information.html", job=0)

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

@app.route('/')
@app.route('/page1.html')
def page1():
    user = {'nickname': 'yyl123'}  # fake user

    conn=sqlite3.connect('paper1.db')
    cursor = conn.cursor()
    cursor.execute('select * from paper')
    values= cursor.fetchall()
    cursor.close()
    conn.close()
    #to be continue ...
    
    comments=[]
    for aa in posts:
        cursor.execute('select * from comments where paper_id='+aa[0])
        val1=cursor.fetchall()
        a=""
        for aaa in val1:
            a+=val1[1]+"\n"
        comments.append(a)

    cursor = conn.cursor()
    return render_template("page1.html",
                           title='Home',
                           user=user,
                           posts=values,
                           comments=comments)

@app.route("/add_comments",methods = ['GET', 'POST'])
def add_comments():
    if request.method == "POST":
        new_comments = request.form.get('new_comments')
        i=request.form.get('i')
        conn=sqlite3.connect('paper1.db')
        cursor = conn.cursor()
        cursor.execute('insert into comments (paper_id,content) values (\''+str(i)+'\',\''+new_comments+'\')')
        cursor.close()
        conn.commit()
        conn.close()
    


        return "add"+new_comments+"to paper:"+str(i)
    else:
        return "<h1>add comments Failure !</h1>"

