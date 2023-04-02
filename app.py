import os
from flask import Flask,render_template,request,redirect,url_for
from flaskext.mysql import MySQL
from werkzeug.utils import secure_filename
app=Flask(__name__)

mysql=MySQL()

app.config["MYSQL_DATABASE_HOST"]='localhost'
app.config["MYSQL_DATABASE_USER"]='root'
app.config["MYSQL_DATABASE_PASSWORD"]=''
app.config["MYSQL_DATABASE_DB"]='e-vaccine'

mysql.init_app(app)



@app.route("/adminlogin",methods=['POST','GET'])
def adminlogin():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        if username=='admin' and password=='admiin':
            return redirect('adminhome')
        else:
            error='invalid'
    else:
        return render_template("adminlogin.html")


@app.route("/hospitallogin",methods=['GET','POST'])
def hospitallogin():
     if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        con=mysql.connect()
        cur=con.cursor()
        cur.execute("SELECT * FROM `addhos` WHERE `username`='"+username+"' AND `password`='"+password+"'")
        data=cur.fetchone()
        if data[1]==username and data[2]==password:
            return redirect (url_for('hospitalhome',id=data[0]))
        else:
            error='invalid'
     return render_template("hospitallogin.html")    

@app.route("/parentlogin",methods=['GET','POST'])
def parentlogin():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        con=mysql.connect()
        cur=con.cursor()
        cur.execute("SELECT * FROM `regi` WHERE `username`='"+username+"' AND `password`='"+password+"'")
        data=cur.fetchone()
        if data[1]==username and data[2]==password:
            return redirect (url_for('parenthome',id=data[0]))
        else:
            error='invalid'
    else:
        return render_template("parentlogin.html")

@app.route("/vaccine")
def vaccine():
    return render_template("vaccine.html")    

@app.route("/parentregister",methods=['GET','POST'])
def parentregister():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        gender=request.form['gender']
        phoneno=request.form['phoneno']
        email=request.form['email']
        con=mysql.connect()
        cur=con.cursor()
        cur.execute ("INSERT INTO `regi`( `username`, `password`, `gender`, `phoneno`, `email`) VALUES (%s,%s,%s,%s,%s)", (username,password,gender,phoneno,email))
        con.commit()
        return redirect('parentlogin')
    else:  
        return render_template("parentregister.html")  

    

@app.route("/parentviewdetail",methods=['POST','GET'])
def parentviewdetail():
    id=request.args.get("id")
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `adddetail` where `poid`= '"+id+"' ")
    data=cur.fetchall()
    return render_template("parentviewdetail.html",hos=data,pid=id)  


@app.route("/hospitalhome")
def hospitalhome():
    hid = request.args.get('id')
    return render_template("hospitalhome.html",hid=hid)   


@app.route("/adminhome")
def adminhome():
    return render_template("adminhome.html")   


@app.route("/parenthome")
def parenthome():
    hid = request.args.get('id')
    return render_template("parenthome.html",hid=hid)


@app.route("/parentadddetail",methods=['GET','POST'])
def parentadddetail():
    poid = request.args.get('id')
    if request.method=='POST':
        poid=request.form['poid']
        childname=request.form['childname']
        birthplace=request.form['birthplace']
        dob=request.form['dob']
        childage=request.form['childage']
        weight=request.form['weight']
        parentname=request.form['parentname']
        phoneno=request.form['phoneno']
        email=request.form['email']
        con=mysql.connect()
        cur=con.cursor()
        cur.execute("INSERT INTO `adddetail` (`poid`,`childname`, `birthplace`, `dob`, `childage`,`weight`,`parentname`, `phoneno`,`email`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(poid,childname,birthplace,dob,childage,weight,parentname,phoneno,email))
        con.commit()
        return redirect (url_for('parentviewdetail',id=poid))
    else:
        return render_template("parentadddetail.html",posid=poid)                   

     

@app.route("/adddoctor",methods=['GET','POST'])
def adddoctor():
    hoid = request.args.get('id')
    if request.method=='POST':
        hoid=request.form['hoid']
        name=request.form['name']
        specialization=request.form['specialization']
        degree=request.form['degree']
        experience=request.form['experience']
        joiningdate=request.form['joiningdate']
        gender=request.form['gender']
        phoneno=request.form['phoneno']
        emailid=request.form['emailid']
        con=mysql.connect()
        cur=con.cursor()
        cur.execute("INSERT INTO `adddoc` (`hoid`,`name`,`specialization`,`degree`, `experience`, `joiningdate`,`gender`, `phoneno`, `emailid`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(hoid,name,specialization,degree,experience,joiningdate,gender,phoneno,emailid))
        con.commit()
        return redirect (url_for('hospitalhome',id=hoid))
    else:    
        return render_template("adddoctor.html",hospid=hoid)    

@app.route("/adminaddpolio",methods=['GET','POST'])
def adminaddpolio():
    if request.method=='POST':
        poliodate=request.form['poliodate']
        agelimit=request.form['agelimit']
        poliostatus="enable"
        con=mysql.connect()
        cur=con.cursor()
        cur.execute("INSERT INTO `polio`(`poliodate`, `agelimit`, `poliostatus`) VALUES (%s,%s,%s)",(poliodate,agelimit,poliostatus))
        con.commit()
        return redirect('adminviewpolio')
    else:    
        return render_template("adminaddpolio.html")

@app.route("/adminviewpolio",methods=['GET','POST'])
def adminviewpolio():
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `polio` ")
    data=cur.fetchall()
    return render_template("adminviewpolio.html",polio=data)


@app.route("/parentviewhos",methods=['GET','POST'])
def parentviewhos():
    pid=request.args.get("id")
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `adddoc` ")
    data=cur.fetchall()
    return render_template("parentviewhos.html",polio=data,par=pid)

@app.route("/parentquery",methods=['GET','POST'])
def parentquery():
    pid=request.args.get("pid")
    docid=request.args.get("id")
    if request.method=='POST':
        pid=request.form['pid']
        docid=request.form['docid']
        message=request.form['message']
        desp=request.form['desp']
        status="Not Completed"
        con=mysql.connect()
        cur=con.cursor()
        cur.execute("INSERT INTO `query`(`pid`, `docid`, `message`,`desp`,`status`) VALUES (%s,%s,%s,%s,%s)",(pid,docid,message,desp,status))
        con.commit()
        return redirect(url_for('parentviewquery',id=pid))
    else:    
        return render_template("parentquery.html",parid=pid,doct=docid) 

@app.route("/parentviewquery")
def parentviewquery():
    pid=request.args.get("id")
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `query` where `pid`='"+pid+"' ")
    data=cur.fetchall()
    return render_template("parentviewquery.html",query=data)   

@app.route("/hosviewquery")
def hosviewquery():
    hid=request.args.get("id")
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `query` where `docid`='"+hid+"' ")
    data=cur.fetchall()
    return render_template("hosviewquery.html",query=data,hid=hid)   

@app.route("/hosupdatequery",methods=['GET','POST'])
def hosupdatequery():
    hid=request.args.get("hid")
    id=request.args.get("id")
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `query` where `id`='"+id+"' ")
    data=cur.fetchone()
    if request.method=='POST':
        reply=request.form['reply']
        status=request.form['status']
        con=mysql.connect()
        cur=con.cursor()
        cur.execute("UPDATE `query` SET `reply`='"+reply+"',`status`='"+status+"' WHERE `id`='"+id+"' ")
        con.commit()
        return redirect(url_for('hosviewquery',id=hid))
    else:
        return render_template("hosupdatequery.html",query=data)        


@app.route("/parentviewpolio")
def parentviewpolio():
    pid=request.args.get("id")
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `polio` ")
    data=cur.fetchall()
    return render_template("parentviewpolio.html",polio=data)        


@app.route("/adminviewdoctor",methods=['POST','GET'])
def adminviewdoctor():
    id=request.args.get("id")
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `adddoc`")
    data=cur.fetchall()
    return render_template("adminviewdoctor.html",hos=data)  

@app.route("/viewprofile",methods=['GET','POST'])
def viewprofile():
    hid=request.args.get("id")
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM  `addhos` where `id` = '"+hid+"'")
    data=cur.fetchone()
    return render_template("viewprofile.html",hos=data)     

@app.route("/viewdoctor",methods=['GET','POST'])
def viewdoctor():
    id=request.args.get("id")
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `adddoc` where `hoid`= '"+id+"'")
    data=cur.fetchall()
    return render_template("viewdoctor.html",hos=data)    

@app.route("/adminemail",methods=['POST','GET'])
def adminemail():
    uplid=request.args.get('id')
    conn=mysql.connect()
    cur=conn.cursor()
    cur.execute("SELECT * FROM `adddetail` where `id`='"+uplid+"' ")
    data=cur.fetchone()
    if request.method=='POST':
        emailid=request.form['emailid']
        message=request.form['message']
        
        me = 'projectmail559@gmail.com'
        password = 'feif yjwz pkwu fhjx'
        server = 'smtp.gmail.com:587'
        you = emailid
        
       
        message = EmailMessage()
        message['Subject'] = "Vaccine Remainder"
        message['From'] = me
        message['To'] = you
       
        msg = """
Good Day .

As your children vaccine date is tomorrow go and pls go check the website or 
use the above to search hospital near by your for the vaccine 

http://localhost/vaccine/hospitalview

Regards,

me"""
        server = smtplib.SMTP(server)
        server.ehlo()
        server.starttls()
        server.login(me, password)
        server.sendmail(me, you, msg)
        server.quit()

        return redirect('adminviewvaccine')
    else:
        return render_template("adminemail.html",user=data)
         

@app.route("/viewhospital",methods=['GET','POST'])
def viewhospital():
    id=request.args.get("id")
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `addhos` ")
    data=cur.fetchall()
    return render_template("viewhospital.html",hos=data)     

@app.route("/hospitalview",methods=['GET','POST'])
def hospitalview():
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `addhos` ")
    data=cur.fetchall()
    return render_template("hospitalview.html",hospi=data)     

@app.route("/addhospital",methods=['GET','POST'])
def addhospital():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        hosname=request.form['hosname']
        hosaddress=request.form['hosaddress']
        phoneno=request.form['phoneno']
        email=request.form['email']
        APP_PATH_ROUTE=os.path.dirname(os.path.abspath(__file__))
        target=os.path.join(APP_PATH_ROUTE,'uploads')
        UPLOAD_FOLDER='{}/static/uploads/'.format(APP_PATH_ROUTE)
        con=mysql.connect()
        cur=con.cursor()
        cur.execute("INSERT INTO `addhos` (`username`,`password`,`hosname`, `hosaddress`, `phoneno`, `email`) VALUES (%s,%s,%s,%s,%s,%s)",(username,password,hosname,hosaddress,phoneno,email))
        con.commit()
        return redirect (url_for('hospitallogin'))
    else:    
        return render_template("addhospital.html")


@app.route("/hospitaldelete",methods=['POST','GET'])
def hospitaldelete():
    id=request.args.get("id")
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("DELETE  FROM `addhos` where `id`= '"+id+"' ")
    con.commit()
    return redirect('viewhospital')

@app.route("/hospitalupdate",methods=['POST','GET']) 
def hospitalupdate():  
    id=request.args.get("id")
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `addhos` where `id`= '"+id+"' ")
    data=cur.fetchone()
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        hosname=request.form['hosname']
        hosaddress=request.form['hosaddress']
        phoneno=request.form['phoneno']
        email=request.form['email']
        con=mysql.connect()
        cur=con.cursor()
        cur.execute("UPDATE `addhos` SET `username`='"+username+"',`password`='"+password+"',`hosname`='"+hosname+"',`hosaddress`='"+hosaddress+"',`phoneno`='"+phoneno+"',`email`='"+email+"' WHERE `id`='"+id+"' ")
        con.commit()
        return redirect('viewhospital')
    else:
        return render_template("hospitalupdate.html",hos=data)         

@app.route("/parentadddetailupdate",methods=['GET','POST'])
def parentadddetailupdate():
    id=request.args.get('id')
    pid=request.args.get('pid')
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `adddetail` where `id`= '"+id+"' ")
    data=cur.fetchone()
    if request.method=='POST':
        vaccine1=request.form['vaccine1']
        vaccine2=request.form['vaccine2']
        vaccine3=request.form['vaccine3']
        vaccine4=request.form['vaccine4']
        vaccine5=request.form['vaccine5']
        vaccine6=request.form['vaccine6']
        vaccine7=request.form['vaccine7']
        vaccine8=request.form['vaccine8']
        vaccine9=request.form['vaccine9']
        vaccine10=request.form['vaccine10']
        con=mysql.connect()
        cur=con.cursor()
        cur.execute("UPDATE `adddetail` SET `vaccine1`='"+vaccine1+"',`vaccine2`='"+vaccine2+"',`vaccine3`='"+vaccine3+"',`vaccine4`='"+vaccine4+"',`vaccine5`='"+vaccine5+"',`vaccine6`='"+vaccine6+"',`vaccine7`='"+vaccine7+"',`vaccine8`='"+vaccine8+"',`vaccine9`='"+vaccine9+"',`vaccine10`='"+vaccine10+"' WHERE `id`='"+id+"' ")
        con.commit()
        return redirect(url_for('parentviewdetail',id=pid))
    else:
        return render_template("parentadddetailupdate.html",hos=data)              


@app.route("/adminupdatevaacine",methods=['GET','POST'])
def adminupdatevaacine():
    id=request.args.get('id')
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `adddetail` where `id`= '"+id+"' ")
    data=cur.fetchone()
    if request.method=='POST':
        vaccine1=request.form['vaccine1']
        vaccine2=request.form['vaccine2']
        vaccine3=request.form['vaccine3']
        vaccine4=request.form['vaccine4']
        vaccine5=request.form['vaccine5']
        vaccine6=request.form['vaccine6']
        vaccine7=request.form['vaccine7']
        vaccine8=request.form['vaccine8']
        vaccine9=request.form['vaccine9']
        vaccine10=request.form['vaccine10']
        con=mysql.connect()
        cur=con.cursor()
        cur.execute("UPDATE `adddetail` SET `vaccine1`='"+vaccine1+"',`vaccine2`='"+vaccine2+"',`vaccine3`='"+vaccine3+"',`vaccine4`='"+vaccine4+"',`vaccine5`='"+vaccine5+"',`vaccine6`='"+vaccine6+"',`vaccine7`='"+vaccine7+"',`vaccine8`='"+vaccine8+"',`vaccine9`='"+vaccine9+"',`vaccine10`='"+vaccine10+"' WHERE `id`='"+id+"' ")
        con.commit()
        return redirect('adminparentregisterview')
    else:
        return render_template("adminupdatevaacine.html",hos=data)                        

@app.route("/adminparentchildregisterview",methods=['POST','GET'])
def adminparentchildregisterview():
    id=request.args.get("id")
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `adddetail` ")
    data=cur.fetchall()
    return render_template("adminparentchildregisterview.html",hos=data)
           
@app.route("/adminviewparentchild",methods=['POST','GET'])
def adminviewparentchild():
    id=request.args.get("id")
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `adddetail` where `poid`='"+id+"' ")
    data=cur.fetchall()
    return render_template("adminviewparentchild.html",child=data)

@app.route("/adminparentregisterview",methods=['POST','GET'])
def adminparentregisterview():
    id=request.args.get("id")
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `regi` ")
    data=cur.fetchall()
    return render_template("adminparentregisterview.html",hos=data)   



@app.route("/adminhospitalview",methods=['GET','POST'])
def adminhospitalview():
    id=request.args.get("id")
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `addhos` ")
    data=cur.fetchall()
    return render_template("adminhospitalview.html",hos=data)                 

@app.route("/vaccinenames")
def vaccinenames():
    return render_template("vaccinenames.html") 

    

@app.route("/adminviewvaccine")
def adminviewvaccine():
    con=mysql.connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM `adddetail` ")
    data=cur.fetchall()
    return render_template("adminviewvaccine.html",hos=data) 




if __name__=="__main__":
    app.run(debug=True)        