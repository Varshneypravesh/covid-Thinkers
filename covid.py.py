from flask import Flask, render_template , redirect , request , url_for
import flask
import smtplib , os 
import csv
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("sinup.html")

@app.route("/login_page")
def login_page():
       return render_template('login.html')

#@app.route('/success/<name>/<email>')
#def success(name , email):
#       message = "Thanks for registering with covid Thinkers. \
#         we will inform you about opportunities which are added \
#         on our platform."
#       if not email :
#              return "please enter the email"
#       try:
#         PASSWORD = "Luv@8436"
#         sender_email = "rajathakur1502@gmail.com"
#         server = smtplib.SMTP("smtp.gmail.com" , 587)
#         server.starttls()
#         server.login(sender_email , PASSWORD)
#         server.sendmail(sender_email,email , message)
#       except smtplib.SMTPAuthenticationError:
#          return "Authentication error"
#       except smtplib.SMTPException:
#          return "unable to send email."

#      return render_template('welcome.html' , name = name , email = email)

@app.route("/append_csv/<name>/<password>/<email>")
def append_csv(name , password , email):
       file = open('registered.csv' , "a" )
       writer = csv.writer(file)
       writer.writerow((name , password , email))
       file.close()
       return render_template('welcome.html' , name = name , email = email)

@app.route("/login" , methods = ['POST' , 'GET'])
def login():
       if request.method == 'POST':
              name = request.form['name']
              password = request.form['password']
              email = request.form['email']
       else:
              name = request.args.get('name')
              password = request.args.get('password')
              email = request.args.get('email')
       file = open('registered.csv' , 'r')
       reader = csv.reader(file)
       for item in reader:
              if name in item:
                     if name.lower() == item[0].lower() and password == item[1] and email == item[2]:
                              return "Login succesfull!!!"
       return "login failure"
       

@app.route('/sinup',methods = ['POST', 'GET'])
def sinup():
   if request.method == 'POST':
      user = request.form['fn']
      email = request.form['ei']
      password1 = request.form['pw1']
      password2 = request.form['pw2']
      if password1 != password2 or not password1 or not password2:
             return render_template('failure.html')
      return redirect(url_for('append_csv',name = user, password = password1 , email = email))
   else:
      user = request.args.get('fn')
      email = request.args.get('ei')
      password1 = request.args.get('pw1') 
      password2 = request.args.get('pw2')
      if password2 != password1 or not password2 or not password1:
             return render_template('failure.html')
      return redirect(url_for('registration',name = user , password = password1 , email = email))





if __name__ == '__main__':
   app.run(debug = True)