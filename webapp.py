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
    if "f" not in session:
        session["eq1"]=request.form['eq1']
        session["eq2"]=request.form['eq2']
        session["f"]=0
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    if "c" not in session:
        session["eq3"]=request.form['eq3']
        eq1=session["eq1"]
        eq2=session["eq2"]
        eq3= session["eq3"]
        eq1a="";
        eq2a="";
        eq3a="";
        cor=0;
        if eq1 == "x+2":
            eq1a = "correct!"
            cor=cor+1
        else:
            eq1a = "incorrect."
        if eq2 == "x+2":
            eq2a = "correct!"
            cor=cor+1
        else:
            eq2a = "incorrect."
        if eq3 == "x^2+6x+9":
            eq3a = "correct!"
            cor=cor+1
        else:
            eq3a = "incorrect."
        session["cor"]=cor
        session["eq1"]=eq1a
        session["eq2"]=eq2a
        session["eq3"]=eq3a
        session["c"]=0
    return render_template('page3.html')
    
if __name__=="__main__":
    app.run(debug=False)
