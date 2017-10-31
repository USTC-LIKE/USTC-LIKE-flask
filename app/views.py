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
    conn=sqlite3.connect('news.db')
    cur=conn.cursor()
    cur.execute("select news_title,news_brief,news_TitlePic from news")
    values=cur.fetchall()
    print(values)
#    print(values)
    res=[[],[]]
    style=0
    choose=1
    for each in values:
        news_title=each[0]
        news_brief=each[1]
        news_TitlePic=each[2]
        res[choose-1].append([news_title,news_brief,news_TitlePic,style+1])
        style=(style+1)%3
        choose=3-choose
    
    return render_template("news.html",res=res)

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
    name2=name1.split('_',1)[0]+" "+name1.split('_',1)[1]
    name1.replace('_',' ')

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



#!---------------------update-------------------------------------
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif','PNG','JPG','JPEG','GIF'])
app.config['UPLOAD_FOLDER'] = os.getcwd()+"/app/static/save_file"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



def save_db(name,category):
    conn=sqlite3.connect('people.db')
    cur=conn.cursor()
    cur.execute('insert into people (name,category) values(\
                            \''+name+'\',\''+
                            category+'\')')
    cur.close()
    conn.commit()
    conn.close()
    return 1

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        conn=sqlite3.connect('people.db')
        cur=conn.cursor()

        file = request.files['file']       
        family =request.form.get('family')#
        given =request.form.get('given')#
        category =request.form.get('category')#
        homepage =str(request.form.get('homepage'))
        email =str(request.form.get('email'))
        office =str(request.form.get('office'))
        Title1 =str(request.form.get('Title1'))
        Title2 =str(request.form.get('Title2'))
        Title3 =str(request.form.get('Title3'))
        Title4 =str(request.form.get('Title4'))
        Title5 =str(request.form.get('Title5'))
        Content1 =str(request.form.get('Content1'))
        Content2 =str(request.form.get('Content2'))
        Content3 =str(request.form.get('Content3'))
        Content4 =str(request.form.get('Content4'))
        Content5 =str(request.form.get('Content5'))
        name=family+"_"+given;
        cur.execute('select * from people where name=\''+name+'\'')
        values = cur.fetchall()

     

        if len(values)==0:
            cur.execute('insert into people (name,category) values(\
                            \''+name+'\',\''+
                            category+'\')')

        if len(homepage)!=0:
            cur.execute('UPDATE people SET homepage = \''+homepage+'\' WHERE name=\''+name+'\'')

        if len(email)!=0:
            cur.execute('UPDATE people SET email = \''+email+'\' WHERE name=\''+name+'\'')

        if len(office)!=0:
            cur.execute('UPDATE people SET office = \''+office+'\' WHERE name=\''+name+'\'')

        if len(Content1)!=0:
            cur.execute('UPDATE people SET Content1 = \''+Content1+'\',Title1=\''+Title1+'\'\
             WHERE name=\''+name+'\'')

        if len(Content2)!=0:
            cur.execute('UPDATE people SET Content2 = \''+Content2+'\',Title2=\''+Title2+'\'\
             WHERE name=\''+name+'\'')

        if len(Content3)!=0:
            cur.execute('UPDATE people SET Content3 = \''+Content3+'\',Title3=\''+Title3+'\'\
             WHERE name=\''+name+'\'')

        if len(Content4)!=0:
            cur.execute('UPDATE people SET Content4 = \''+Content4+'\',Title4=\''+Title4+'\'\
             WHERE name=\''+name+'\'')

        if len(Content5)!=0:
            cur.execute('UPDATE people SET Content5 = \''+Content5+'\',Title5=\''+Title5+'\'\
             WHERE name=\''+name+'\'')

        if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            filename = file.filename
            #save_db(family+"_"+given,category)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], family+"_"+given+"."+filename.rsplit('.', 1)[1]))
        
        cur.close()
        conn.commit()
        conn.close()

        return family+"_"+given+","+category+"\nThanks!"
        

    return render_template("upload.html")

#!--------------------------------------upload news---------------------------------------------------
upload_img_path = os.getcwd()+"\\app\\static\\news_img"



def SaveNews(news_title,news_content,news_brief,news_TitlePic):
    conn=sqlite3.connect('news.db')
    cur=conn.cursor()
    cur.execute("select * from news")
    vals=cur.fetchall()
    num=len(vals)
    cur.execute("insert into news (news_id,news_title,news_content,news_brief,news_TitlePic) values('%s','%s','%s','%s','%s')"
                %(str(num+1),news_title,news_content,news_brief,news_TitlePic) )
    cur.close()
    conn.commit()
    conn.close()
    return 1



def SaveInsertPic(file):
    conn=sqlite3.connect('news.db')
    cur=conn.cursor()
    cur.execute("select * from pic")
    vals=cur.fetchall()
    num=len(vals)
    filename=file.filename
    print(filename)
    name=str(num+1)+"."+filename.rsplit('.', 1)[1]
    #save_db(family+"_"+given,category)
    
    file.save(os.path.join(upload_img_path, name))
    cur.execute("insert into pic (name) values('%s')"%name)
    cur.close()
    conn.commit()
    conn.close()
    return '\n<!--Do not delete this!!!-->\n</div>\n<img style="max-height: 330px;max-width: 860px;" src="../static/news_img/%s"/>\n<div class="job_content">\n<!--Do not delete this!!!-->'%(name)
    #return '\n<!--Do not delete this!!!-->\n<img alt="head" width="860px" height="330px src="../static/news_img/%s"/>\n<!--Do not delete this!!!-->\n'%(name)

def SaveTitlePic(file):
    conn=sqlite3.connect('news.db')
    cur=conn.cursor()
    cur.execute("select * from pic")
    vals=cur.fetchall()
    num=len(vals)
    filename=file.filename
    name=str(num+1)+"."+filename.rsplit('.', 1)[1]
    #save_db(family+"_"+given,category)
    file.save(os.path.join(upload_img_path, name))
    cur.execute("insert into pic (name) values('%s')"%name)
    cur.close()
    conn.commit()
    conn.close()
    return (name)

@app.route('/upload_news',methods=['GET','POST'])
def upload_news():
    if request.method == 'POST':
        print(111)
        print("It is: "+request.form.get('submit'))
        #print(request.form['submit'])
        conn=sqlite3.connect('news.db')
        cur=conn.cursor()
        if(request.form.get('submit')=='Upload'):
            print('Upload')
            title=request.form.get('title')
            brief=request.form.get('brief')
            content=request.form.get('content')
            file = request.files['title_pciture']
            if file and allowed_file(file.filename):
                TitlePic=SaveTitlePic(file)
            else:
                return "ERROR: file is not allowed"

            SaveNews(news_title=title,news_content=content
                    ,news_brief=brief,news_TitlePic=TitlePic)
            return "Uplaoded!"


        elif(request.form.get('submit')=='insert_here'):
            print('insert_here')
            title=request.form.get('title')
            brief=request.form.get('brief')
            content=request.form.get('content')
            print(title)
            print(brief)
            print(content)
            file = request.files['file']
            cmd=""
            if file and allowed_file(file.filename):
                cmd=SaveInsertPic(file)
            NewContent=content+cmd
            return render_template("upload_news.html",title=title,brief=brief,content=NewContent)


    return render_template("upload_news.html")

#!-------------------------------------show news---------------------------------------------------------
@app.route("/news.html/<news_id>")
@app.route("/news/<news_id>")
def show_news(news_id):
    conn=sqlite3.connect('news.db')
    cur=conn.cursor()
    cur.execute("select news_title,news_content from news where news_id=%s"%(news_id))
    values=cur.fetchall()
#    print(values)
    news_title=values[0][0]
    news_content=values[0][1]
    return render_template("single_news.html",
                        news_title=news_title,
                        news_content=news_content)



