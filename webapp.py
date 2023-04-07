import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set on the server. 
                                     #To run locally, set in env.bat (env.sh on Macs) and include that file in gitignore so the secret key is not made public.

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    session["eq1"]=request.form['eq1']
    session["eq2"]=request.form['eq2']
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    session["eq3"]=request.form['eq3']
    eq1=session["eq1"]
    eq2=session["eq2"]
    eq3= session["eq3"]
    eq1a="";
    eq2a="";
    eq3a="";
    if eq1 == "x+2":
        eq1a = " , which is correct."
    else:
        eq1a = " , which is incorrect"
    if eq2 == "x+2":
        eq2a = " , which is correct."
    else:
        eq2a = " , which is incorrect"
    if eq3 == "x^2+6x+9":
        eq3a = " , which is correct."
    else:
        eq3a = " , which is incorrect"
    return render_template('page3.html', eq1a, eq2a, eq3a)
    
if __name__=="__main__":
    app.run(debug=False)
