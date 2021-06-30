from flask import Flask,render_template,request,redirect,url_for
import pymysql

app = Flask(__name__)

conn = pymysql.connect('localhost','root','','student_db')

@app.route("/")
def showData():
    cur = conn.cursor()
    cur.execute("select * from student")
    rows=cur.fetchall()
    return render_template('index.html',datas=rows)#datas=rows โยนขข้อมูลใน rows ไป

@app.route("/student")
def showForm():   
    return render_template('addstudent.html')

@app.route("/insert",methods=['POST'])
def insert():
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        phone = request.form["phone"]
        cur = conn.cursor()
        sql = "insert into student(fname,lname,phone) value(%s,%s,%s)"
        cur.execute(sql,(fname,lname,phone))
        conn.commit()
        return redirect(url_for('showData'))

@app.route("/delete/<string:id_del>",methods=['GET'])
def deleteData(id_del):
    cur = conn.cursor()
    cur.execute("delete from student where id=%s",(id_del))
    conn.commit()
    return redirect(url_for('showData'))

@app.route("/update",methods=['POST'])
def updateData():
     if request.method == "POST":
        id_update = request.form['id']
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        cur = conn.cursor()
        sql = "update student set fname=%s, lname=%s, phone=%s where id=%s "
        cur.execute(sql,(fname,lname,phone,id_update))
        conn.commit()
        return redirect(url_for('showData'))

#---------------------------------------------
#------------------------------------------
    
    

if __name__ == "__main__":
    app.run(debug=True)
    

