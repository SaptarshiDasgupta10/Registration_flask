from flask import Flask,render_template,request
import pymysql
conn = pymysql.connect(host="localhost",user = "root",password="",database = "expense-app1")
cursor = conn.cursor()

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login_validation',methods = ['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')
    cursor.execute("""SELECT * FROM `user` WHERE `email` LIKE "{}" AND `password` LIKE "{}" """.format(email,password))
    users = cursor.fetchall()
    if(len(users)>0):
        return render_template('home.html')
    else:
        return render_template('login.html')

@app.route('/add_user',methods = ['POST'])
def add_user():
    name = request.form.get('uname')
    password = request.form.get('upassword')
    email = request.form.get('uemail')
    cursor.execute("""INSERT INTO `user` (`user_id`,`name`,`email`,`password`) VALUES(NULL,'{}','{}','{}')""".format(name,email,password))
    conn.commit()
    return "User Registered Successfully"


if __name__ == "__main__":
    app.run(debug = True)
